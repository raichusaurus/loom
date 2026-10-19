import tempfile
import unittest
from pathlib import Path

from loom_cli import check_project, init_project


class LoomCliTests(unittest.TestCase):
    def test_valid_project_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_project(root)
            self.assertEqual(check_project(root), [])

    def test_missing_phase_artifact_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_project(root)
            (root / "docs/loom/phases/03-architecture/PROGRESS.md").unlink()
            findings = check_project(root)
            self.assertIn(
                "missing required phase ledger: phases/03-architecture/PROGRESS.md",
                findings,
            )

    def test_invalid_question_ticket_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_project(root)
            (root / "docs/loom/tickets/LOOM-001-open-question.md").write_text(
                "# Open question\n\n## Question\nDecide this.\n"
            )
            findings = check_project(root)
            self.assertIn(
                "ticket missing required section: docs/loom/tickets/LOOM-001-open-question.md -> Owner",
                findings,
            )

    def test_init_creates_project_scaffold_without_overwriting_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("existing project\n")

            created = init_project(root)

            self.assertIn("docs/loom/PROGRESS.md", created)
            self.assertEqual((root / ".loom-version").read_text(), "0.1.0\n")
            self.assertEqual((root / "README.md").read_text(), "existing project\n")
            self.assertEqual(check_project(root), [])

    def _write_project(self, root):
        loom = root / "docs/loom"
        (root / ".loom-version").write_text("0.1.0\n")
        (loom / "tickets").mkdir(parents=True)
        (loom / "README.md").write_text("[discovery](phases/01-discovery/README.md)\n")
        (loom / "PROGRESS.md").write_text("Status: in progress\n")
        for phase in (
            "01-discovery", "02-requirements", "03-architecture",
            "04-planning", "05-contracts-tests", "06-implementation", "07-review",
        ):
            phase_dir = loom / "phases" / phase
            phase_dir.mkdir(parents=True)
            (phase_dir / "README.md").write_text("Complete.\n")
            (phase_dir / "PROGRESS.md").write_text("Status: complete\n")


if __name__ == "__main__":
    unittest.main()
