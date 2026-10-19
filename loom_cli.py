"""Small, dependency-free checks for Loom project conventions."""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


PHASE_DIRS = (
    "01-discovery",
    "02-requirements",
    "03-architecture",
    "04-planning",
    "05-contracts-tests",
    "06-implementation",
    "07-review",
)
TICKET_SECTIONS = (
    "Phase",
    "Question",
    "Why it matters",
    "Evidence",
    "Options / constraints",
    "Owner",
    "Status",
    "Blocked or at risk",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")
REPOSITORY_ROOT = Path(__file__).resolve().parent
LOOM_VERSION = (REPOSITORY_ROOT / "VERSION").read_text(encoding="utf-8").strip()


def check_project(project_root: Path) -> list[str]:
    """Return convention findings without modifying the project."""
    loom_root = project_root / "docs" / "loom"
    if not loom_root.is_dir():
        return ["missing Loom directory: docs/loom"]

    findings = []
    version_file = project_root / ".loom-version"
    if not version_file.is_file():
        findings.append("missing Loom version: .loom-version")
    elif version_file.read_text(encoding="utf-8").strip() != LOOM_VERSION:
        findings.append(
            f"Loom version mismatch: expected {LOOM_VERSION}, found {version_file.read_text(encoding='utf-8').strip()}"
        )
    required_files = [loom_root / "README.md", loom_root / "PROGRESS.md"]
    required_files.extend(
        loom_root / "phases" / phase / filename
        for phase in PHASE_DIRS
        for filename in ("README.md", "PROGRESS.md")
    )
    for path in required_files:
        if path.is_file():
            continue
        relative = path.relative_to(loom_root)
        if relative.name == "PROGRESS.md" and relative.parts[0] == "phases":
            findings.append(f"missing required phase ledger: {'/'.join(relative.parts)}")
        else:
            findings.append(f"missing required artifact: {path.relative_to(project_root)}")

    for document in sorted(loom_root.rglob("*.md")):
        relative_document = document.relative_to(project_root)
        contents = document.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(contents):
            if not (document.parent / target).resolve().is_file():
                findings.append(f"broken markdown link: {relative_document} -> {target}")

    ticket_root = loom_root / "tickets"
    if ticket_root.is_dir():
        for ticket in sorted(ticket_root.glob("LOOM-*.md")):
            contents = ticket.read_text(encoding="utf-8")
            for section in TICKET_SECTIONS:
                if not re.search(rf"^## {re.escape(section)}\s*$", contents, re.MULTILINE):
                    findings.append(
                        f"ticket missing required section: {ticket.relative_to(project_root)} -> {section}"
                    )
    return sorted(findings)


def init_project(project_root: Path) -> list[str]:
    """Install Loom's project scaffold without overwriting existing files."""
    created = []
    loom_root = project_root / "docs" / "loom"
    (loom_root / "tickets").mkdir(parents=True, exist_ok=True)
    project_readme = loom_root / "README.md"
    if not project_readme.exists():
        project_readme.write_text(
            "# Loom Project\n\nSee the phase artifacts and progress ledger below.\n\n"
            + "\n".join(
                f"- [{phase}](phases/{phase}/README.md)" for phase in PHASE_DIRS
            )
            + "\n",
            encoding="utf-8",
        )
        created.append("docs/loom/README.md")
    progress = loom_root / "PROGRESS.md"
    if not progress.exists():
        progress.write_text("# Loom Progress\n\n**Current Focus:** Discovery\n", encoding="utf-8")
        created.append("docs/loom/PROGRESS.md")
    version_file = project_root / ".loom-version"
    if not version_file.exists():
        version_file.write_text(f"{LOOM_VERSION}\n", encoding="utf-8")
        created.append(".loom-version")
    for phase in PHASE_DIRS:
        phase_root = loom_root / "phases" / phase
        phase_root.mkdir(parents=True, exist_ok=True)
        for filename, contents in (
            ("README.md", f"# {phase}\n\nPhase artifact.\n"),
            ("PROGRESS.md", "# Progress\n\nStatus: Pending\n"),
        ):
            path = phase_root / filename
            if not path.exists():
                path.write_text(contents, encoding="utf-8")
                created.append(str(path.relative_to(project_root)))
    for source, destination in (
        (REPOSITORY_ROOT / "loom_cli.py", project_root / "loom_cli.py"),
        (REPOSITORY_ROOT / "bin" / "loom", project_root / "bin" / "loom"),
        (REPOSITORY_ROOT / "templates" / "open-question-ticket.md", project_root / "templates" / "open-question-ticket.md"),
        (REPOSITORY_ROOT / "templates" / "loom-check.yml", project_root / ".github" / "workflows" / "loom-check.yml"),
        (REPOSITORY_ROOT / "templates" / "pull-request-template.md", project_root / ".github" / "PULL_REQUEST_TEMPLATE.md"),
        (REPOSITORY_ROOT / "templates" / "CODEOWNERS", project_root / ".github" / "CODEOWNERS"),
        (REPOSITORY_ROOT / "templates" / "loom-ruleset.json", project_root / ".github" / "loom-ruleset.json"),
    ):
        if not destination.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            created.append(str(destination.relative_to(project_root)))
    return created


def project_plan(mode: str, project_root: Path, project_name: str, repository: str) -> list[str]:
    """Describe project bootstrap actions without changing files or GitHub."""
    actions = [f"inspect {project_root}"]
    if mode == "start" and (project_root / "docs" / "loom").exists():
        actions.append("ERROR: project already contains docs/loom; use adopt")
    else:
        actions.append("create project scaffold")
    actions.extend(
        (
            "install pinned Loom version " + LOOM_VERSION,
            "configure CODEOWNERS and pull-request template",
            "configure Loom check workflow",
            f"prepare ruleset import for {repository}",
            f"create phase branch loom/{project_name}/discovery",
            "open setup pull request",
        )
    )
    return actions


def doctor_findings() -> list[str]:
    """Check the local tools needed for a Loom collaboration."""
    findings = []
    for command in ("git", "gh"):
        if shutil.which(command) is None:
            findings.append(f"missing command: {command}")
    if shutil.which("git") is None:
        return findings
    for key, label in (("user.name", "Git user.name"), ("user.email", "Git user.email")):
        result = subprocess.run(
            ["git", "config", "--global", "--get", key],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0 or not result.stdout.strip():
            findings.append(f"missing Git identity: {label}")
    return findings


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if argv and argv[0] == "project":
        parser = argparse.ArgumentParser(description="Bootstrap a Loom project.")
        parser.add_argument("project", choices=("project",))
        parser.add_argument("mode", choices=("start", "adopt"))
        parser.add_argument("project_root")
        parser.add_argument("--name", default=None)
        parser.add_argument("--repo", default="repository-not-configured")
        parser.add_argument("--apply", action="store_true")
        args = parser.parse_args(argv)
        project_root = Path(args.project_root).resolve()
        project_name = args.name or project_root.name
        actions = project_plan(args.mode, project_root, project_name, args.repo)
        if any(action.startswith("ERROR:") for action in actions):
            for action in actions:
                print(action)
            return 1
        if args.apply:
            for path in init_project(project_root):
                print(f"CREATED: {path}")
            print("NOTE: create the GitHub repository, import the ruleset, and open the setup PR.")
        else:
            for action in actions:
                print(f"PLAN: {action}")
            print("Dry run only. Add --apply to install local project files.")
        return 0

    if argv and argv[0] in ("doctor", "setup"):
        parser = argparse.ArgumentParser(description="Prepare a developer for Loom.")
        parser.add_argument("command", choices=("doctor", "setup"))
        parser.add_argument("--project", default=None)
        parser.add_argument("--apply", action="store_true")
        args = parser.parse_args(argv)
        findings = doctor_findings()
        if findings:
            print("Loom environment needs attention:")
            for finding in findings:
                print(f"- {finding}")
        else:
            print(f"Loom {LOOM_VERSION} environment is ready.")
        print("Next steps:")
        print("- Authenticate GitHub with: gh auth login")
        print("- Read README.md, FRAMEWORK.md, and ORCHESTRATOR.md")
        if args.project:
            project_root = Path(args.project).resolve()
            if args.apply:
                for path in init_project(project_root):
                    print(f"CREATED: {path}")
            else:
                print(f"- Preview project adoption with: bin/loom project adopt {project_root}")
                print("- Add --apply only after reviewing the plan")
        return 1 if findings else 0

    parser = argparse.ArgumentParser(description="Check Loom project conventions.")
    parser.add_argument("command", choices=("check", "init"))
    parser.add_argument("project_root", nargs="?", default=".")
    args = parser.parse_args(argv)
    project_root = Path(args.project_root).resolve()
    if args.command == "init":
        for path in init_project(project_root):
            print(f"CREATED: {path}")
        print("Loom project scaffold ready.")
        return 0
    findings = check_project(project_root)
    if findings:
        for finding in findings:
            print(f"ERROR: {finding}")
        return 1
    print("Loom check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
