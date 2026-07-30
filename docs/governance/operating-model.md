# Governance operating model

The operating model joins central standards with accountable product ownership. A central review board alone cannot safely govern a growing portfolio.

## Decision rights

| Role | Accountable for |
|---|---|
| Business owner | Legitimate purpose, outcome, affected stakeholders, business impact, value, and risk-treatment recommendation |
| Product owner | Workflow, user experience, recourse, adoption, ongoing performance |
| Engineering owner | System design, delivery, testing, reliability, incident response |
| Data owner | Permitted use, quality, access, retention, lineage |
| Model or AI platform owner | Approved capabilities, shared controls, service levels, model inventory |
| Security and privacy | Threats, data protection, access, monitoring, supplier assurance |
| Responsible AI or risk | Classification method, harm evaluation, required risk input, oversight, and portfolio view |
| Legal and compliance | Applicable obligations, disclosures, records, regulated-use constraints |
| Internal audit | Independent assessment of design and operating effectiveness |

One person may hold several roles, but each accountability should remain explicit.

Legal and compliance owners should record source-specific roles,
applicability, atomic duties, deadlines, conflicts, and reassessment in the
[regulatory obligation register](../worksheets/regulatory-obligation-register.md).
That record informs system and release decisions; it does not transfer release
authority to the legal function or turn internal risk tiering into a legal
classification.

## Repository, release, and incident ownership

Every production-affecting repository should have an accepted accountable
owner, primary maintainers, a backup, path-specific code owners, and links to
the service, release, deployment, and incident owners. Repository ownership is
not established by contributor activity or a `CODEOWNERS` file alone.

| Decision | Accountable authority |
|---|---|
| Repository purpose, maintainer appointment, transfer, or archival | Repository owner |
| Change intent, scope, and evidence | Change owner |
| Technical acceptance of owned paths | Code owner and required reviewers |
| Merge | Authorized maintainer after protected checks and review |
| Model-routing plan or exact-deployment admission | One named route or deployment decision authority designated under adopted policy and bound to the exact decision record |
| Agent-extension admission | One named extension-admission authority designated under adopted policy and bound to the exact decision record |
| Release go, hold, or abort | Named release owner |
| Production deployment execution | Deployment operator through a protected environment |
| Residual-risk acceptance for one defined boundary | One named residual-risk decision authority designated under adopted policy for the applicable risk class and bound to the exact decision record |
| Security, privacy, compliance, or other internal-policy exception | One named exception authority separately designated under adopted policy and bound to the exact exception record |
| Incident severity, containment, and restoration coordination | Incident commander under predefined authority |
| Acceptance of restored operating state for each service boundary | Service owner after named observed-state readback |
| Incident closure | Named incident authority after required evidence and service-restoration acceptance |
| Corrective-action effectiveness result | Named independent verifier where adopted policy requires |
| Corrective-action `close` or `keep open` | Control owner after effectiveness evidence |

Authority does not flow between rows. Repository and code owners accept repairs
under repository policy; route, deployment, and extension authorities admit
only their decision-bound dependencies and do not authorize release; release
owners authorize exact releases; deployment operators execute; readback owners
verify observed state; service owners accept restored operation; incident
authorities close incidents; and control owners close corrective actions. One
person may hold compatible roles only where adopted policy permits it and
required independence is preserved. Record many-to-many service and
repository boundaries and accepted handoffs in the
[incident and corrective-action record](../worksheets/incident-and-corrective-action-record.md).

### Residual-risk decision contract

Adopted policy must designate exactly one named residual-risk decision authority
for each residual-risk decision record. Different records may use different
authorities by risk class, tier, consequence, or organizational boundary, but
each record has one attributable decision. Record the policy or delegation
basis, risk category, and scope. The named authority may decide only the
categories explicitly reserved or delegated to it. If policy reserves
different categories to different authorities, create one decision record for each category
and require every applicable record at the consuming gate; do not collapse
them into a cross-category vote. Business, product, engineering, data,
security, privacy, responsible-AI, risk, legal, compliance, affected-domain,
and independent assurance roles provide the inputs that policy requires;
supporting rows are not votes, and a majority cannot create authority.

Use **Accept**, **Accept with conditions**, **Hold**, or **Reject**. Missing,
ambiguous, out-of-category, or expired decision authority; missing, stale, or
out-of-scope required input; or an unresolved non-waivable, blocking, or
conflicting required input forces **Hold** or **Reject**. The change-producing
AI or automation cannot accept risk. A human who also holds another role may
decide only when policy explicitly designates that authority and preserves
required independence.

Bind the decision to:

- the risk statement, cause, consequence, affected people, and residual
  likelihood and impact;
- the exact system, use case, purpose, revision, environment, population,
  exposure, evidence cutoff, and validity window;
- required discipline inputs, unresolved uncertainties, conditions,
  compensating controls, monitoring, stop triggers, remediation owner, expiry,
  reassessment triggers, and attributable evidence; and
- any separate exception decision, its authority, policy basis, scope,
  conditions, and expiry.

Risk acceptance retains only the defined residual risk within the recorded
authority and window. It cannot waive a clear legal, regulatory, contractual,
license, or adopted-policy prohibition; cure missing rights or a mandatory
duty; or make a Tier 4 scope releasable. An exception is a separate decision
and does not confer residual-risk or release authority. Acceptance does not authorize experiment, build, release, deployment, operation, or publication:
the owner of the applicable lifecycle gate must make that separate decision
using the current risk record as evidence.

A material change, breached condition or stop trigger, expired decision,
changed controlling obligation, or evidence outside the recorded envelope
invalidates the decision and forces the affected activity to hold, contain, or
follow its separately authorized rollback or recovery path. Preserve the old
record and link a superseding decision rather than editing accepted history.

Prefer team-based repository access and at least two organization owners for
continuity. Minimize administrative and bypass authority, review direct
collaborators and deployment identities periodically, and document how
ownership is transferred when a maintainer or team departs.

## Federated governance

### Central team

- defines taxonomy, minimum controls, and evidence standards;
- operates or approves shared platform capabilities;
- maintains the inventory and portfolio risk view;
- reviews high-risk or novel uses;
- publishes reusable tests and patterns;
- monitors aggregate incidents, vendors, cost, and concentration.

### Domain and product teams

- own the use case and business process;
- perform classification and produce evidence;
- validate data authority and stakeholder impact;
- operate the system within approved boundaries;
- report material changes and incidents;
- retire the use case and dispose of data appropriately.

## Lifecycle gates

| Gate | Decision | Minimum evidence |
|---|---|---|
| Intake | Is exploration legitimate and worthwhile? | owner, purpose, affected users, initial classification |
| Experiment | May representative data and models be used? | data approval, isolated environment, experiment limits |
| Build | Is the architecture acceptable? | threat model, data flows, ADRs, evaluation plan |
| Release | May the exact candidate enter production within current decision-bound risk records and readiness evidence? | evaluation results, current category-bound residual-risk and exception decisions, readiness review, release approval, rollback |
| Operate | Does the system remain within its envelope? | monitoring, incidents, drift, changes, periodic review |
| Retire | Can service and retained assets be transferred, decommissioned, or retained safely? | [transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md), successor or no-successor decision, dependency and active-work reconciliation, records and data disposition, user communication, observed-state readback |

Use the [repository ownership and deployment plan](../worksheets/repository-ownership-and-deployment-plan.md)
to record accepted duties, the
[code deployment and release](../delivery/code-deployment.md) procedure for
promotion, and the
[incident, problem, and corrective-action](../operations/incident-problem-and-corrective-action.md)
process when outcomes leave the approved envelope.

## Material change triggers

Reassessment is required when any of the following changes:

- intended purpose or affected population;
- risk tier, autonomy, or user exposure;
- model provider, model or artifact revision, mutable alias behavior, or material capability;
- training, fine-tuning, retrieval, or grounding data;
- tools, permissions, or systems of record;
- regions, retention, or data-sharing terms;
- quality or harm thresholds;
- a significant incident, complaint, or legal obligation.

A change may use a pre-approved low-risk path only when its scope is bounded, tested behavioral and operational impact is within the approved envelope, regression evidence passes, and rollback is available. File size, semantic-version label, or a description such as “minor prompt change” does not by itself make a change low risk.
