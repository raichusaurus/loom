# Architecture Template

**Project Name:** [Your Project Name]  
**Date:** [Date]  
**Based on Requirements:** [Link to Requirements document]

---

## System Overview

[High-level description of what the system does and how]

---

## Technology Stack

| Layer | Technology | Justification |
|-------|-----------|--------------|
| **Frontend** | [e.g., React, Vue, Angular] | [Why this choice?] |
| **Backend** | [e.g., Node.js, Python, Java] | [Why this choice?] |
| **Database** | [e.g., PostgreSQL, MongoDB] | [Why this choice?] |
| **Cache** | [e.g., Redis, Memcached] | [Why this choice or N/A?] |
| **Message Queue** | [e.g., RabbitMQ, Kafka] | [Why this choice or N/A?] |
| **Infrastructure** | [e.g., AWS, GCP, Kubernetes] | [Why this choice?] |
| **Deployment** | [e.g., Docker, CI/CD tool] | [Why this choice?] |

### Justification
[Why this tech stack fits the requirements, constraints, and team skills]

---

## System Architecture Diagram

```
[ASCII diagram or description of major components]

Example:
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTP/REST
       ▼
┌─────────────────┐
│  API Gateway    │
└──────┬──────────┘
       │
   ┌───┴────┬──────────┬─────────┐
   ▼        ▼          ▼         ▼
[Service][Service][Service][Service]
   │        │          │         │
   └────────┴──────────┴─────────┘
            │
            ▼
      [Database]
```

---

## Components & Responsibilities

### Component 1: [Name]
- **Purpose:** [What it does]
- **Responsibility:** [Specific tasks]
- **Technology:** [Tech used]
- **Interfaces:** [What it exposes/consumes]

### Component 2: [Name]
- **Purpose:** [...]
- **Responsibility:** [...]
- **Technology:** [...]
- **Interfaces:** [...]

---

## Data Model

### Core Entities

#### Entity 1: [Name]
```
{
  id: UUID (primary key)
  field1: [type]
  field2: [type]
  ...
  created_at: timestamp
  updated_at: timestamp
}
```

**Relationships:** [How it relates to other entities]

#### Entity 2: [Name]
[...]

### Database Schema
[Link to schema diagram or description]

### Data Flow Diagram
```
[Show how data flows through the system]
```

---

## Integration Points

### External API: [System Name]
- **Endpoint:** [URL]
- **Purpose:** [What data/functionality]
- **Authentication:** [How authenticated]
- **Data Format:** [JSON, XML, etc.]
- **Error Handling:** [Retry strategy, fallbacks]

---

## Scalability Strategy

### Horizontal Scaling
[How services/instances scale]
- Load balancing: [approach]
- Database replication: [approach]
- Cache distribution: [approach]

### Vertical Scaling
[When/if we scale instances up]
- CPU/Memory limits: [...]
- Monitoring triggers: [...]

### Data Scaling
- Sharding strategy: [if applicable]
- Archive strategy: [how old data is handled]
- Backup strategy: [frequency and retention]

---

## Reliability & Resilience

### High Availability
[How we prevent single points of failure]
- Redundancy: [components duplicated]
- Failover: [automatic recovery approach]
- Health checks: [monitoring strategy]

### Disaster Recovery
- RTO (Recovery Time Objective): [target time to recover]
- RPO (Recovery Point Objective): [acceptable data loss]
- Backup location: [where backups are stored]
- Recovery procedure: [steps to recover]

### Error Handling
[How we handle failures gracefully]
- Service timeouts: [timeout values]
- Retry logic: [exponential backoff, etc.]
- Circuit breakers: [when to fail fast]
- Graceful degradation: [what happens when parts fail]

---

## Security Design

### Authentication
[Who can use the system]
- Mechanism: [OAuth2, JWT, session-based, etc.]
- Identity provider: [if external]
- MFA: [if required]

### Authorization
[What users can do]
- Role-based access control: [roles defined]
- Resource-level permissions: [how enforced]

### Data Protection
- Encryption in transit: [TLS/SSL]
- Encryption at rest: [AES-256, etc.]
- PII handling: [masking, redaction strategies]

### Network Security
- Firewall rules: [what's allowed]
- VPC/Network segmentation: [isolation]
- DDoS protection: [if applicable]

---

## Deployment Strategy

### Environments
- **Development:** [where developers work]
- **Staging:** [pre-production testing]
- **Production:** [live system]

### Deployment Process
1. [Step 1: e.g., Build Docker image]
2. [Step 2: e.g., Push to registry]
3. [Step 3: e.g., Deploy to staging]
4. [Step 4: e.g., Run smoke tests]
5. [Step 5: e.g., Deploy to production]

### Rollback Strategy
[How to quickly revert if issues arise]

---

## Monitoring & Observability

### Metrics
- Application metrics: [request rate, latency, errors]
- Infrastructure metrics: [CPU, memory, disk]
- Business metrics: [users, transactions, revenue]

### Logging
- Log level: [DEBUG, INFO, WARN, ERROR]
- Log destination: [centralized log service]
- Log retention: [how long kept]

### Alerting
| Alert | Threshold | Action |
|-------|-----------|--------|
| High error rate | > 5% | Page on-call engineer |
| High latency | > 1s p95 | Investigate performance |
| Low disk space | < 20% available | Alert ops team |

---

## Known Limitations & Trade-offs

[What we're NOT doing and why]

### Limitation 1
- **Issue:** [What we're not handling perfectly]
- **Reason:** [Why this trade-off makes sense]
- **Future:** [Plan to address this]

---

## Approval

- [ ] Technology stack is approved
- [ ] Architecture diagram is understood by team
- [ ] Components and responsibilities are clear
- [ ] Data model makes sense
- [ ] Scalability approach is feasible
- [ ] Security approach meets requirements
- [ ] Deployment strategy is clear
- [ ] Team is ready to proceed to Contracts & Tests / CI/CD

**Approved By:** _________________ **Date:** _________

---

## Notes

[Additional context, open questions, future improvements]
