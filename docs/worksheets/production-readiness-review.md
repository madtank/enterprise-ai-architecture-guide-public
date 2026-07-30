# Production readiness review

Use this as an evidence index and attributable decision record for one exact
production release candidate and target boundary. Follow the
[code deployment and release](../delivery/code-deployment.md) path. Use the
decision evidence index below to record the result for each applicable rubric
outcome; the checkbox sections are review prompts, not a second status record.
A **go** requires every gate to be **pass**, justified **not applicable**, or
**exception approved**. A known nonblocking failure may transition to
**exception approved** only through a linked, scoped, policy-permitted,
unexpired decision with compensating controls and stop conditions. A **fail**,
**unknown**, **stale**, or blank result always forces **hold** or **abort**;
missing, unknown, or stale required evidence cannot be converted into an
exception.

`Exception approved` is valid only for a known, evidenced,
policy-permitted, nonblocking internal-control failure with a current
attributable exception record. It cannot waive or replace a Tier 4
classification; a clear legal, regulatory, contractual, license, or
adopted-policy prohibition; missing operating or distribution rights; an unmet
mandatory duty, precondition, or deadline; uncertain applicability; a missing
required owner, discipline decision, approval, or independence; unknown,
stale, or blank evidence; or expired, widened, unowned, out-of-category, or
ambiguous authority. A source-based exclusion, exemption, or derogation must
come from the controlling source and link its current
[regulatory-obligation decision](regulatory-obligation-register.md#source-based-exclusions-and-derogations).
Any such non-waivable condition forces **hold** or **abort**.

!!! danger "Fail closed"
    Hold or abort when the candidate, target, decision authority, required
    evidence, rollback or compensation path, deployment identity, or
    observed-state readback owner is missing or ambiguous. A completed
    checklist, successful workflow, AI review, or prior approval for another
    revision does not authorize deployment.

## Record control and exact decision boundary

| Field | Value |
|---|---|
| Readiness record ID / version | |
| Record state | draft / under review / decision-bound / superseded / expired |
| AI system / inventory ID and system-card version | |
| Release ID and change / request ID | |
| Intended purpose, risk tier, users, affected people, and prohibited uses | |
| Reviewed source and infrastructure revisions | |
| Immutable or tamper-evident release manifest URI, version, and digest | |
| Enterprise-built artifact IDs and digests | |
| Managed or mutable component observed identities, observation time, limitations, sentinels, and fallback | |
| Configuration, migration, data / index, and prompt / policy revisions; route-plan decision ID / version / digest; exact deployment approval IDs / revisions / revocation epochs; extension-admission decision ID / version / digest; execution-telemetry revision | |
| Exact target environments, tenants, regions, cohorts, and rollout stage | |
| Current deployed state and maximum requested production exposure | |
| Planned release / change window and decision expiry | |
| Last known-good manifest / digest; rollback and forward-recovery record IDs and executor authority | |
| Schema, migration, and state compatibility; compensation and ambiguous-side-effect reconciliation | |
| Last recovery exercise date / result, measured RTO / RPO, and known limits | |
| Staging deployment record, observed-state readback, and test evidence | |
| Current evaluation, impact, threat, obligation, identity, route, extension, execution-telemetry, supplier, and incident / CAPA record IDs | |
| Protected deployment identity, workflow, environment, and enforcement evidence | |
| Evidence cutoff, freshness limits, and reassessment triggers | |
| Record owner and accepted backup; evidence location, classification, access, retention, and integrity control | |
| Superseded and superseding readiness record IDs | |

The decision applies only to the boundary above. A material change to a
decision-bound identity or boundary, or a mutable-component observation that
breaches its approved identity or behavior envelope, sentinel, limitation, or
reassessment trigger, invalidates authorization. Preserve routine observations
as append-only operating evidence. For existing exposure, follow the recorded
hold, containment, rollback, or recovery rule; further deployment or promotion
requires a new or superseding record when the approved checkpoint sequence or
maximum envelope no longer applies. Store restricted evidence in its governed
system and link it by stable ID and digest; do not copy credentials, protected
personal data, or confidential incident material into this worksheet.

## Decision evidence index

Link governed evidence rather than pasting sensitive content. Use **pass**,
**fail**, **not applicable**, **exception approved**, **unknown**, or **stale**
for each row and explain every not-applicable or exception-approved result. A
pass means the evidence applies to the exact candidate and target, is within
its validity window, and was produced and verified with the independence
required by adopted policy.

| Evidence gate | Authoritative record IDs, revisions, digests, and candidate / target binding | Status, assessor, verification date, and independence | Freshness, expiry, and invalidation triggers | Findings, limitations, and evidence location |
|---|---|---|---|---|
| Ownership, inventory, purpose, and obligation applicability | | | | |
| Architecture, data, identity, and tenant boundary | | | | |
| Evaluation, human impact, routing, and total cost | | | | |
| Threat, privacy, extension / MCP, and supply-chain assurance | | | | |
| Reliability, capacity, telemetry, incident, and support readiness | | | | |
| Build, provenance, manifest, artifact, and trusted checks | | | | |
| Staging, recovery, compensation, and observed-state rehearsal | | | | |
| Findings, residual risk, exceptions, and required approvals | | | | |

## Minimum outcome rubric

Use the following prompts to test completeness and applicability. Record their
authoritative results, evidence, limitations, and any not-applicable rationale
in the decision evidence index rather than inferring status from a checked or
unchecked box.

## Ownership and scope

- [ ] Business, product, technical, data, and assurance owners are named.
- [ ] Production-affecting repositories have accepted owners, primary
  maintainers, backups, code owners, and an access-review cadence.
- [ ] Change, release, deployment, service, and incident decision rights are
  named.
- [ ] Intended purpose, users, affected people, and prohibited uses are documented.
- [ ] Risk tier and material-change triggers are approved.
- [ ] The AI system is present in the enterprise inventory.
- [ ] The
  [regulatory obligation register](regulatory-obligation-register.md)
  matches the exact entities, source-specific roles, jurisdictions, system,
  release, data, suppliers, dates, and channels; no unresolved
  release-blocking prohibition, unlawful waiver, uncertain applicability,
  missed deadline, expired evidence, or expired exception remains. Every
  permitted conditional decision or time-bounded exception is linked with its
  scope, authority, controls, owner, and expiry.

## Architecture and data

- [ ] Current data-flow and trust-boundary diagrams are linked.
- [ ] Authoritative sources and systems of record are identified.
- [ ] The
  [identity and permission matrix](identity-and-permission-matrix.md) binds
  approved human and workload identities, tenant isolation, delegation,
  credentials, tools, final-action authorization, and negative-test evidence.
- [ ] The current
  [agent execution and telemetry contract](agent-execution-and-telemetry-contract.md)
  binds root and child identity, separate execution and effect states, typed
  tool outcomes, cancellation, ambiguity, event completeness, minimization,
  retention, alert ownership, reconciliation, and closure to the exact
  release.
- [ ] Data purpose, minimization, residency, retention, and deletion are approved.
- [ ] Model, prompt, data, index, policy, and tool lineage is recorded.

## Quality, safety, and human factors

- [ ] Evaluation set represents normal, edge, critical, and adversarial scenarios.
- [ ] Release thresholds pass against the approved baseline.
- [ ] Unsupported, harmful, biased, and inaccessible behavior is tested as relevant.
- [ ] Human oversight has been tested with actual reviewers.
- [ ] Disclosure, correction, appeal, refusal, and fallback behavior is validated.
- [ ] Open findings have an owner, due date, and residual-risk decision.
- [ ] Router and delegation evaluation covers false low-tier routing,
  unnecessary high-tier routing, handoff loss, verifier effectiveness, and
  critical-case escalation.
- [ ] Every coordinator, worker, verifier, fallback, and escalation route meets
  its applicable release thresholds.

## Security and privacy

- [ ] Threat model and abuse analysis are current.
- [ ] Prompt injection, data exfiltration, poisoning, and tool abuse are tested.
- [ ] Secrets and credentials use workload identity or approved secret management.
- [ ] Provider terms, data use, retention, region, and incident duties are approved.
- [ ] Telemetry is minimized before collection, protected, retained,
  access-controlled, and tested for prohibited-field rejection,
  cross-tenant access, deletion, restored backups, and restricted-sample
  separation.
- [ ] Agent instructions, skills, CI, deployment, ownership, and policy files
  are protected and independently reviewed.
- [ ] Skills, plugins, hooks, helpers, MCP servers, startup commands, and
  negotiated capabilities and dynamic schemas match approved digests/versions
  or explicit monitored mutable-service records and passed admission.
- [ ] Agent and model selection cannot bypass provider, region, revision, data,
  tool, credential, or authority allowlists.
- [ ] Downstream agents cannot acquire greater authority than the originating
  identity delegated.
- [ ] MCP authentication prevents token passthrough and confused-deputy access;
  tool-list changes, SSRF, sessions, output, and cross-server flows are controlled.

## Reliability and operations

- [ ] Service and quality objectives are defined.
- [ ] Capacity, quotas, rate limits, cost limits, and action budgets are configured.
- [ ] Dependency failures, timeouts, retries, and circuit breakers are tested.
- [ ] Dashboards and alerts cover outcome, quality, safety, security, reliability, and cost.
- [ ] Support, escalation, incident, and communications owners are ready.
- [ ] Rollback or safe fallback has been exercised.
- [ ] Traces record route ID, delegation chain, actual model revision,
  structured policy reason codes, latency, usage, total cost, validation,
  escalation, and authoritative outcome references without hidden reasoning.
- [ ] Event loss, duplication, reordering, tampering, collector outage,
  cancellation before and after send, late results, unknown writes,
  reconciliation, and incomplete execution closure are tested.
- [ ] Step, token, spend, concurrency, retry, and delegation-depth limits are tested.
- [ ] Route abstention, provider failure, fallback, stronger-model escalation,
  human escalation, component revocation, and credential rotation are exercised.
- [ ] Model, price, region, policy, extension, MCP schema, and lifecycle changes
  trigger reassessment and regression evaluation.

## Release and approval

- [ ] The record-control fields bind this review to one exact release candidate,
  target boundary, rollout stage, and decision window.
- [ ] Required trusted checks passed against the reviewed source revision.
- [ ] Enterprise-built artifacts were built once and are identified by
  immutable digests.
- [ ] Managed or mutable dependencies identify the observed revision,
  limitation, sentinels, fallback, and reassessment trigger.
- [ ] The immutable or tamper-evident release manifest is approved.
- [ ] Applicable source/build provenance, SBOM, scans, signatures, and
  attestations are linked and independently verified against artifact,
  repository, builder, workflow, signer, and policy.
- [ ] Release uses an approved staged rollout.
- [ ] Enterprise-built production artifacts are pinned by immutable digest;
  managed or mutable components satisfy the recorded identity, observation,
  limitation, sentinel, fallback, and reassessment controls.
- [ ] `Go`, `hold`, `abort`, `promote`, and `rollback` metrics and automatic
  stop conditions are configured.
- [ ] Deployment uses a protected identity and environment, prevents
  self-approval, and restricts bypass.
- [ ] The named rollback target, forward recovery, and compensation are
  compatible with state and migrations.
- [ ] Every residual risk that policy requires the organization to accept has
  one current, decision-bound **Accept** or **Accept with conditions** record
  from exactly one named residual-risk decision authority for that category.
  Every policy-reserved category is covered, and required discipline inputs
  are current and are not treated as votes.
- [ ] Required decisions are attributable and current. The change-producing
  agent, model, or artifact cannot approve or accept an exception. A deployment
  operator may also hold a compatible human approval role only where adopted
  policy explicitly permits it and required independence is preserved; missing
  approval remains missing.
- [ ] A named owner will read back actual deployed revisions, routes, policy,
  migration state, and critical behavior.
- [ ] When any artifact crosses the established access boundary, a separate
  [public-release readiness record](public-release-readiness.md) captures
  accountable-owner approval, or a named governance authority's
  policy-permitted exception, for the exact sanitized distribution unit,
  channel, and withdrawal path.
- [ ] Next review date and continuous monitoring owner are recorded.

## Findings, exceptions, and expiry

| ID, type, and status | Scope, unmet outcome, and release effect | Treatment, compensating controls, and stop trigger | Decision authority, owner, due date, and expiry | Closure criteria and evidence |
|---|---|---|---|---|
| | | | | |

- [ ] No organization-defined release-blocking or highest-severity finding
  remains open.
- [ ] Every accepted residual risk and policy-permitted exception names the
  exact candidate, target, exposure, rationale, authority, compensating
  controls, monitoring, stop condition, owner, and expiry.
- [ ] An expired, widened, unowned, or ambiguously authorized condition fails
  closed; the change-producing agent or model did not accept the exception.

## Final production decision

- **Decision ID and timestamp:**
- **Named decision authority / release owner:**
- **Decision:** go / hold / abort
- **Decision-bound source revision, manifest ID, and digest:**
- **Immediately authorized target, next rollout stage, cohort / exposure, and
  release window:**
- **Maximum bounded rollout envelope:** environment, region, tenant / cohort,
  traffic percentage, route, and time limit
- **Progression rule:** automatic only when named thresholds pass / fresh
  attributable decision required at each checkpoint
- **Condition, finding, and exception IDs governing execution or promotion:**
- **Automatic stop, human hold, rollback, forward-recovery, and compensation
  thresholds:**
- **Accepted residual-risk decision IDs, exact scopes, named authorities,
  authority bases, owners, conditions, and expiries:**
- **Separate policy-exception decision IDs, exact scopes, named authorities,
  authority bases, conditions, and expiries:**
- **Signed or attributable decision-evidence URI and digest:**
- **Decision expiry and material-change / reassessment triggers:**
- **Protected deployment workflow and deployment operator:**
- **Observed-state readback owner and authoritative deployment-record
  location:**
- **Next promotion checkpoint, review, or closeout date:**

A `go` with conditions is available only for policy-permitted nonblocking
findings with enforceable controls, monitoring, stop conditions, owners, and
unexpired deadlines. It cannot replace missing approval or waive a release
blocker. Emergency containment or restoration uses the separately authorized
incident and emergency-change path; it does not create production-release
approval. The maximum bounded rollout envelope is not executable authority
beyond the immediately authorized stage unless the selected progression rule
permits automatic progression and its named thresholds pass, or a fresh
attributable checkpoint decision is recorded.

| Role | Named principal and authority / duty | Approval, advice, or duty acknowledgement | Time and attributable evidence | Condition / exception IDs and expiry |
|---|---|---|---|---|
| Release owner | | | | |
| Change producer; no self-approval authority | | | | |
| Trusted evidence verifier; record independence | | | | |
| Deployment operator; execute only the decision-bound candidate | | | | |
| Service owner; production objectives, support, and impact | | | | |
| Observed-state readback owner; independently verify target state | | | | |
| Residual-risk record verifier; verify each linked decision ID, category, exact scope, authority basis, result, validity, expiry, and supersession; create no acceptance here | | | | |
| Business / product owner | | | | |
| Technical owner | | | | |
| Data owner | | | | |
| Security / privacy owner | | | | |
| Risk / responsible-AI owner | | | | |
| Legal / compliance owner, if required | | | | |
| Incident / on-call owner; accept containment and restoration duty | | | | |
| Qualified independent approver, when policy requires; provide required independent approval / assurance | | | | |
| Exception authority, if used | | | | |

Duty acknowledgement is not automatically approval. Keep release decision,
deployment execution, observed-state verification, service ownership, and
independent assurance distinct even when policy permits one person to hold
more than one compatible role. The release owner's authoritative decision is
not inferred from a vote or majority of the supporting rows. The release owner
does not inherit residual-risk or exception authority, and either of those
decisions remains an input rather than authorization to release. Missing,
ambiguous, expired, out-of-category, or out-of-scope residual-risk acceptance
forces **hold** or **abort**.

## Promotion, readback, and closeout

Preserve the decision-bound snapshot and append or link execution evidence;
do not overwrite it with observed facts. Link the authoritative deployment
record rather than rewriting observations to match this decision. Each
promotion is a governed checkpoint within the bounded rollout envelope; a step
outside that envelope needs a superseding readiness decision.

Use **proceed**, **promote**, **hold**, **abort**, or **rollback** for the
execution action at each checkpoint.

| Production checkpoint | Decision-bound target and manifest | Expected state and thresholds | Observed state / result | Execution action | Owner, time, and evidence |
|---|---|---|---|---|---|
| Initial production exposure | | | | | |
| Intermediate promotion(s) | | | | | |
| Maximum bounded-envelope checkpoint | | | | | |

For every applicable checkpoint, reconcile at least:

| Readback boundary | Approved desired revision / state | Observed revision / state and time | Match / gap | Disposition, owner, and evidence |
|---|---|---|---|---|
| Enterprise-built artifact and configuration | | | | |
| Schema, workflow, migration, data, and index state | | | | |
| Model, prompt, policy, route, and provider deployment | | | | |
| Skill, helper, plugin, MCP capability, tool schema, and startup state | | | | |
| Identity, authorization, credential, tenant, and egress policy | | | | |
| Cohort, region, exposure, feature flags, budgets, and kill switches | | | | |
| Telemetry, alerts, incident path, support, and critical behavior | | | | |

Missing, stale, ambiguous, or mismatched observed state stops promotion and
requires hold, rollback, forward recovery, or reconciliation under the named
authority. Do not edit the approved state after deployment to manufacture a
match.

- **Authoritative deployment record ID / location:**
- **Actual deployed manifest, artifact, mutable-component observations, and
  target readback:**
- **Actual deployment start, promotion, stop / rollback, and completion
  times:**
- **Deployment execution state:** not started / executing / stopped / rolled
  back / forward recovered / completed
- **Observed exposure after execution:** environment, region, tenant / cohort,
  traffic percentage, route, and time window
- **Readiness authorization state:** active / consumed / invalidated / expired /
  superseded
- **Release closeout state:** open / watch open / ordinary closed /
  closed with owned residual / reopened
- **Incidents, deviations, manual interventions, and follow-up actions:**
- **Rollback-target validity and temporary-access / exception closure:**
- **Release closeout owner, decision, time, and next operating review:**

The readiness decision authorizes only the recorded deployment envelope. It
does not prove that the target reached that state; closeout requires
independent observed-state evidence and reconciliation to the decision-bound
manifest.
