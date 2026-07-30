# Repository ownership and deployment plan

Use this worksheet for every repository that can affect a production service,
shared platform, security control, deployment pipeline, model or data artifact,
agent instruction, or enterprise policy.

Use this record with
[code deployment and release](../delivery/code-deployment.md). Route an escaped
issue through the owning
[incident and corrective-action process](../operations/incident-problem-and-corrective-action.md)
and bind the result in its
[incident and corrective-action record](incident-and-corrective-action-record.md).

## Repository identity

- **Organization / repository:**
- **Purpose:**
- **Primary service / system boundary, if one:**
- **Criticality / risk tier:**
- **Data classification:**
- **Lifecycle state:** proposed / active / maintenance / deprecated / archived
- **Transfer, decommissioning, and retirement record ID / state:**
- **Default and release branches:**
- **Downstream services and consumers:**
- **Inventory / catalog record:**

## Service and repository relationship map

Use stable service and repository IDs. One repository can affect several
services, and one service can depend on several repositories. Each related
repository plan should repeat the same service ID so incident and release
records can reconstruct both directions.

| Service / boundary ID | Relationship and affected artifact / path | Service primary, accepted backup, and contact | Release, rollback, incident, and readback route | Inventory and evidence |
|---|---|---|---|---|
| | | | | |

## Accepted ownership

| Responsibility | Primary person or team | Backup | Acceptance date | Review frequency |
|---|---|---|---|---|
| Accountable repository owner | | | | |
| Maintainer / triage | | | | |
| Architecture | | | | |
| Application code | | | | |
| Security and authorization | | | | |
| Data and migrations | | | | |
| Infrastructure and deployment | | | | |
| AI skills / instructions / prompts / evaluations | | | | |
| Change-owner assignment | | | | |
| Release decision | | | | |
| Deployment operation | | | | |
| Observed-state readback | | | | |
| Service / runtime / on-call | | | | |
| Incident command | | | | |
| Incident closure | | | | |
| Security response | | | | |
| Corrective-action effectiveness verification | | | | |
| Corrective-action / control closure | | | | |
| Archival or transfer | | | | |

One person may hold multiple roles for a low-risk repository. Record any
required separation of duties and how absence or departure is handled.
Repository ownership does not grant service-restoration, incident-command,
release, deployment, readback, notification, risk-acceptance, or
corrective-action-closure authority. Record each accepted role even when the
same compatible human holds more than one.

## Access and continuity

- **Organization-owned:** yes / no / not applicable
- **Base repository permission:**
- **Write and maintain access granted through teams:**
- **Direct collaborators and justification:**
- **Administrative roles and necessity:**
- **Deploy keys, source-control integrations, bots, and service identities:**
- **Bypass / break-glass actors:**
- **Access-review owner and last review:**
- **Minimum maintainer coverage:**
- **Succession, transfer, and recovery procedure:**
- **Orphaned-repository detection:**

Use the
[transfer, decommissioning, and retirement record](transfer-decommissioning-and-retirement.md)
when succession, archival, or transfer is executed. This worksheet continues
to own repository-specific access, build, deployment, recovery, and support
facts; the exit record joins them to successor acceptance, external
dependencies, public channels, disposition, and readback.

## Protected paths

Record the actual path owners and enforcement for:

| Path or concern | Owner(s) | Required approval | Enforced by |
|---|---|---|---|
| Path-ownership policy (`CODEOWNERS` or equivalent) | | | |
| Workflow and required-check definitions | | | |
| Infrastructure and deployment | | | |
| Authentication and authorization | | | |
| Security policy and cryptography | | | |
| Database schema and migrations | | | |
| Dependencies and lockfiles | | | |
| Agent instructions and skills | | | |
| Plugins, hooks, MCP manifests, startup commands, and extension registries | | | |
| Prompts, policies, tools, and workflows | | | |
| Model catalog, route policy, prices, and deployment approvals | | | |
| Evaluation assets and thresholds | | | |
| Documentation with legal or compliance effect | | | |

A path-ownership file such as `CODEOWNERS` is review routing. Record the
ruleset, branch protection, policy engine, or external control that makes the
required review enforceable.

## Branch and merge policy

- [ ] Pull requests are required for protected branches.
- [ ] Force pushes and deletion are blocked.
- [ ] Unauthorized direct updates are blocked.
- [ ] Relevant path-owner review is required.
- [ ] Independent human review is required under the adopted policy.
- [ ] Where supported, the most recent reviewable push must be approved by
  someone other than the person who pushed it.
- [ ] Stale approvals are dismissed or refreshed.
- [ ] Review conversations must be resolved.
- [ ] Required checks have unique names and trusted sources.
- [ ] Branches must be current or use a serialized integration mechanism such
  as a merge queue.
- [ ] Required approval count is risk appropriate.
- [ ] Bypass is named, limited, logged, and retrospectively reviewed.
- [ ] AI-generated review does not replace required human approval.

## Canonical repository commands

| Outcome | Command / workflow | Owner | Expected artifact |
|---|---|---|---|
| Bootstrap | | | |
| Fast check | | | |
| Test | | | |
| Full verify | | | |
| Build | | | |
| Evidence manifest | | | |
| Deploy staging | | | |
| Smoke test | | | |
| Deploy / promote production | | | |
| Rollback / recover | | | |

## Build and artifact policy

- **Trusted builder and identity:**
- **Source revision format:**
- **Artifact repository:**
- **Enterprise-built artifact identifier / digest:**
- **Managed or mutable component identity and limitation:**
- **Dependency and source pinning:**
- **SBOM / AI component inventory, as applicable:**
- **Provenance or attestation and verification policy:**
- **Vulnerability, malware, license, and policy checks:**
- **Retention and deletion:**
- **Build-once promotion enforced by:**
- **Mutable-component sentinels, fallback, and reassessment trigger:**

## Deployment environments

| Environment | Purpose | Allowed refs | Deployment identity | Approver(s) | Credentials owner |
|---|---|---|---|---|---|
| Development | | | | | |
| Evaluation / test | | | | | |
| Staging | | | | | |
| Production | | | | | |

- **Self-review prevented by:**
- **Administrator bypass prevented or controlled by:**
- **Deployment serialization / concurrency:**
- **Production change windows:**
- **Break-glass path:**

## Release and deployment plan

- **Release unit and manifest fields:**
- **Staging verification:**
- **Progressive rollout stages:**
- **Health and comparison baseline:**
- **Automatic stop / rollback thresholds:**
- **Human hold / abort authority:**
- **Feature flag / kill switch:**
- **Actual deployed-state readback:**
- **Observation period and owner:**
- **Release closeout evidence:**

## Recovery

- **Known-good artifact and configuration:**
- **Rollback command and authority:**
- **Schema / state compatibility:**
- **Data backup and restore point:**
- **Forward-recovery procedure:**
- **External-side-effect compensation:**
- **Fallback service or manual path:**
- **Last rollback / restore exercise:**
- **Measured recovery time and data loss:**

## Incident and support ownership

- **Repository incident triage primary, accepted backup, and contact:**
- **Service / system relationship-map IDs and service-owner routes:**
- **Incident commander and incident-closure authority defaults:**
- **Fix / change owner assignment and applicable code-owner route:**
- **Release owner, deployment operator, and observed-state readback defaults:**
- **Emergency-change authority, executor, expiry / revocation, retrospective
  route, and surviving-state release / revert normalization:**
- **Security and privacy escalation:**
- **Supplier escalation:**
- **Customer / stakeholder communication:**
- **Private vulnerability route:**
- **Issue tracker and severity policy:**
- **Corrective-action tracker, control owner, independent-verifier rule, and
  closure authority:**

Record durable defaults and handoff triggers here. The instance-specific
[incident and corrective-action record](incident-and-corrective-action-record.md)
owns the actual affected boundaries, current role holders, accepted handoffs,
decisions, and evidence.

| Duty or decision | Default primary, accepted backup, and contact | Authority source and enforced separation | Handoff trigger, recipient, acceptance evidence, and escalation | Review frequency |
|---|---|---|---|---|
| Repository issue and repair triage | | | | |
| Service impact and restoration acceptance | | | | |
| Incident command and containment | | | | |
| Emergency production change | | | | |
| Technical repair acceptance | | | | |
| Merge | | | | |
| Release `go`, `hold`, `abort`, and promotion | | | | |
| Deployment, rollback, and compensation execution | | | | |
| Observed-state readback and reconciliation | | | | |
| Applicability, notification, and communications | | | | |
| Incident closure | | | | |
| Corrective-action effectiveness verification | | | | |
| Corrective-action `close` or `keep open` | | | | |

An alert acknowledgement or repository handoff does not transfer authority.
Keep the prior holder and escalation active until the recipient accepts the
exact scope, limits, time, and evidence. The repository owner cannot declare a
service restored or an incident closed merely because a repair was merged.

## Review and sign-off

| Role | Name | Decision | Date | Conditions / next review |
|---|---|---|---|---|
| Repository owner | | | | |
| Technical maintainer | | | | |
| Service / operations owner | | | | |
| Security / platform owner | | | | |
| Business / product owner, if required | | | | |
