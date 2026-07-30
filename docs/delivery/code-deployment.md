# Code deployment and release

Deployment is the controlled promotion of a reviewed, verified release unit
into an environment. For artifacts the enterprise builds, promote the same
immutable artifact rather than rebuilding. For managed or mutable
dependencies, pin a revision where possible and record the observed identity,
limitations, sentinels, and fallback. Deployment is not a branch copy or an
agent declaring that the task is complete.

This chapter provides a canonical deployment contract for application code,
infrastructure as code, database migrations, workflow definitions, agent
instructions, prompts, policies, and other versioned components that can
change production behavior. Extend it with the artifact-specific controls in
[MLOps, LLMOps, and AgentOps](mlops-llmops-agentops.md).

## Required outcomes

A production deployment should make it possible to answer:

- Who owns the repository, service, release decision, deployment, and
  production response?
- Which reviewed source revision produced the artifact?
- Which exact artifact and configuration were deployed?
- Which checks, evaluations, approvals, and exceptions applied?
- What is the expected behavior and approved operating envelope?
- How will a failure be detected, contained, rolled back, or recovered?
- What evidence proves the actual environment reached the intended state?

## Repository ownership is a deployment prerequisite

Every production-affecting repository needs an accepted ownership record. A
`CODEOWNERS` file routes review; it does not by itself establish
accountability, continuity, access control, or branch enforcement.

| Role | Accountability |
|---|---|
| Repository accountable owner | Purpose, lifecycle, governance, maintainer appointment, archival or transfer |
| Maintainers | Triage, repository health, contribution decisions, branch and release hygiene |
| Code owners | Technical review for defined paths or domains |
| Change owner | Intent, scope, evidence, and follow-through for one change |
| Release owner | Go, hold, abort, and promotion decision for one release |
| Deployment operator | Executes or supervises the authorized deployment |
| Observed-state readback owner | Verifies the actual target state and records gaps independently where required |
| Service owner | Production objectives, support, dependency coordination, customer impact, and acceptance of restored operation |
| Incident commander or on-call | Detection, containment, escalation, and restoration coordination under predefined authority |
| Security, privacy, risk, legal, compliance, or other required discipline owner | Required assurance input, constraints, findings, or reserved-category decision under adopted policy; supporting rows are not votes |
| Residual-risk decision authority | One attributable Accept / Accept with conditions / Hold / Reject decision for the exact risk category and scope assigned by adopted policy |
| Exception authority | One separately attributable, policy-permitted exception decision for an exact nonblocking internal-control failure |

The same person may hold several roles for a low-risk repository, but the
decisions must remain explicit. Production-critical repositories should have a
primary and backup maintainer, team-based access where possible, and a
documented succession or transfer path.

The release owner consumes every required current, category-bound
residual-risk and exception decision but does not inherit or repeat those
authorities. Missing, expired, invalidated, out-of-category, out-of-scope, or
ambiguously authorized acceptance forces hold or abort.

Maintain a repository registry containing:

- organization and repository name;
- purpose, criticality, data classification, and lifecycle state;
- owning service or product;
- accountable owner, primary maintainers, and backup;
- code-owner mappings for sensitive paths;
- default and release branches;
- required checks, approvals, and merge policy;
- build and deployment workflows;
- deployment environments and credentials owner;
- support, on-call, and security contact;
- dependencies and downstream consumers;
- archival, transfer, and deletion authority;
- last access and ownership review.

Use the
[repository ownership and deployment plan](../worksheets/repository-ownership-and-deployment-plan.md)
to establish the record.
When archival or transfer is executed, complete the
[transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md)
for repository, release, package, integration, credential, publishing,
security-report, and downstream custody plus observed-state readback.

## Protect the change path

Apply the following outcomes to default and release branches using the
source-control platform's rules, policies, or equivalent external controls:

- require pull requests;
- block force pushes, branch deletion, and unauthorized direct updates;
- require relevant code-owner review;
- require independent human review under the adopted policy;
- where the platform supports it, require approval of the most recent
  reviewable push by someone other than the person who pushed it;
- dismiss or refresh stale approvals after material changes;
- require conversation resolution;
- require uniquely named test, security, build, policy, and documentation
  checks from their expected trusted source;
- use an up-to-date branch requirement or merge queue for high-change
  repositories;
- restrict bypass to named break-glass roles and review every use.

Protect path-ownership policy, workflow definitions, deployment and
infrastructure code, authorization logic, security policy, database
migrations, dependency locks, agent instructions and skills, plugin and MCP
manifests, hooks, startup commands, extension and model registries, route
policy, evaluation assets, and required-check configuration. A change to the
method of verification is a control change, not ordinary application code.

On GitHub, `CODEOWNERS` can route review, rulesets or branch protection can
enforce branch and review rules, merge queues can serialize integration, and
environments can gate deployment. Other platforms should implement equivalent
outcomes. Verify feature availability and actual configuration instead of
inferring enforcement from checked-in files.

On GitHub, also use dependency review for dependency-changing pull requests,
pin third-party workflow actions to reviewed full commit identifiers, isolate
untrusted fork workflows from privileged credentials, and verify artifact
provenance against the expected repository, source, workflow, builder, signer,
and policy. Provenance supports origin verification; it is not a safety or
correctness determination.

On GitLab, use protected branches, Code Owners and required approvals,
protected variables and runners, pipeline-execution or security policies, and
fork-pipeline isolation to achieve the same outcomes. Where risk requires it,
set direct push or merge roles to no one, prevent authors or committers from
self-approving, prevent approval-rule override, and require the protected
security pipeline. Capture dependency scanning and CycloneDX evidence where
applicable. GitLab tier, role, inherited rule, and overlapping protection
semantics vary; verify effective behavior with a negative test.

At the environment boundary:

- keep production credentials in the protected production environment;
- restrict deployable branches or release tags;
- prevent a change author from approving their own production deployment;
- prohibit routine administrator bypass;
- serialize incompatible deployments;
- use short-lived workload identity rather than long-lived shared secrets.

Feature behavior and availability vary by source-control plan and deployment
platform. Record the actual enforcement mechanism and test it; do not infer
protection from the presence of configuration files.

## Canonical repository command contract

Each repository should expose a small set of documented, automation-friendly
commands. The implementation may use `make`, task runners, package scripts, or
platform APIs, but the outcomes should remain stable.

```text
bootstrap    Prepare an isolated development or validation environment.
check        Run fast formatting, lint, type, policy, and local-link checks.
test         Run the relevant unit and integration tests.
verify       Run all merge-blocking checks without mutating their policy.
build        Produce the immutable release candidate from an approved source revision.
evidence     Emit the evidence manifest for the source and artifact.
deploy       Deploy an approved digest to one named environment.
smoke        Verify the actual deployed version, route, and critical behavior.
promote      Expand an already deployed and verified artifact to the next stage.
rollback     Restore a named known-good target or invoke documented forward recovery.
```

Commands should:

- be non-interactive in CI;
- fail with a non-zero status;
- print the source revision, artifact digest, target environment, and release
  identifier where relevant;
- avoid printing secrets or sensitive content;
- write machine-readable results in addition to concise human output;
- use the same implementation locally and in automation where practical.

The repository `README`, contributor instructions, or agent map should point
to the canonical commands. An agent should discover the contract rather than
inventing a deployment procedure.

## Release unit and manifest

Define the release as a compatible set of artifacts rather than only a
container image or commit:

- source and infrastructure revision;
- application, package, image, or binary digest when the enterprise builds or
  can pin it;
- database and state migration revision;
- model, adapter, or provider route;
- prompt, policy, guardrail, and feature-flag revision;
- data, feature, knowledge, embedding, and index revision;
- tool schemas, connectors, workflow, and agent topology;
- environment configuration;
- evaluation suite and threshold version;
- SBOM, AI bill of materials, and provenance attestations where applicable;
- known-good rollback and forward-recovery targets.

Store the approved release manifest and decision record as immutable or
tamper-evident. Record mutable external aliases as limitations, read back
their observed identity, monitor them continuously, and define reassessment
and fallback.

## Deployment procedure

### Step 0: Assign the release

Before execution:

1. name the release owner and deployment operator;
2. link the issue, specification, change record, PR, and approved source
   revision;
3. classify behavioral, security, data, operational, and compliance impact;
4. identify the service and incident owners;
5. select the required approval and deployment depth.

**Output:** owned release record with risk tier and decision rights.

### Step 1: Establish readiness criteria

Define:

- expected behavior and baseline;
- required tests and evaluations;
- technical, semantic-quality, safety, security, cost, and business health
  thresholds;
- stop, hold, promote, and rollback conditions;
- migration compatibility and data-loss limits;
- monitoring queries and dashboards;
- observation period at each stage.

Do this before seeing favorable production signals. Emergency containment may
precede the complete record, but the decision and retrospective work remain
mandatory.

**Output:** approved release and recovery plan.

### Step 2: Verify the reviewed source

Confirm:

- required reviewers approved the current head revision;
- required checks ran against that revision and current base;
- no test, coverage, workflow, policy, or protection was weakened without
  explicit approval;
- every exception links a separate decision ID, exact unmet internal control
  and scope, result, named policy-designated exception authority and
  adopted-policy authority basis, non-waivable screen, compensating controls,
  monitoring, stop trigger, remediation owner, expiry, invalidation triggers,
  and supersession; any required category-bound residual-risk decision remains
  separate, and exception authority grants no release or deployment authority;
- the source tag or commit is immutable or otherwise protected.

For a defect, require a reproducer or regression check that demonstrates the
pre-change failure when practical.

**Output:** merge and build authorization tied to a source revision.

### Step 3: Build once in a trusted environment

For components the enterprise builds, use a controlled builder with a minimal
identity. Resolve and record inputs, pin dependencies, scan sources and
dependencies, and produce:

- immutable artifact digest;
- SBOM and relevant AI component inventory;
- build provenance or attestation;
- vulnerability, malware, license, and policy results;
- release manifest.

Do not rebuild a nominally equivalent enterprise-built artifact separately for
staging and production. For managed models, hosted APIs, data sources, or
other components the enterprise cannot build or pin, record the approved
identifier or alias, observed revision when available, supplier evidence,
sentinel results, limitation, fallback, and change-monitoring trigger.

**Output:** release candidate and evidence bound to immutable identifiers where
available.

### Step 3A: Verify provenance, integrity, and rights

Before promotion, independently verify:

- the attestation subject matches the candidate artifact and digest;
- the repository, source revision, builder, workflow, signer, and identity are
  expected and trusted;
- signatures and transparency or verification records satisfy policy;
- the manifest describes the complete intended release unit;
- vulnerability, malware, dependency, license, source, and policy findings
  meet the approved thresholds;
- mutable or unverifiable components have explicit limitations, monitoring,
  fallback, and risk decisions.

Attestation generation is not attestation verification. Provenance supports
origin and process claims; it does not prove functional safety, line-level
authorship, originality, copyright ownership, or license clearance.

**Output:** verified provenance and policy decision bound to the release
candidate.

If any artifact will leave the established enterprise access boundary, also
apply the
[public release and external distribution](public-release-and-external-distribution.md)
gate to the exact outgoing bundle. Deployment rights and provenance evidence
do not by themselves clear public data, intellectual property, vulnerability,
dual-use, claims, or support obligations.

### Step 4: Verify compatibility and recovery

Check:

- application, API, schema, workflow, and state compatibility;
- expand-contract or other backward-compatible migration sequence;
- whether older instances can coexist during rollout;
- whether rollback would corrupt, discard, or misinterpret new state;
- compensation for completed external side effects;
- known-good configuration, data restore point, and artifact availability;
- actual authority and command required to stop or roll back.

Exercise recovery before a consequential release. “Redeploy the old version”
is not a complete rollback plan for stateful behavior.

**Output:** tested rollback, forward-recovery, or compensation record.

### Step 5: Deploy the exact release candidate to staging

Use the deployment identity and protected environment to deploy the approved
digest or recorded managed-component revision. Apply environment-specific
configuration without rebuilding enterprise-built artifacts. Then read back:

- running artifact and configuration versions;
- database and workflow migration state;
- model, prompt, policy, index, and tool routes;
- identity and authorization policy;
- health and critical-path behavior.

Run smoke, integration, security, and representative behavioral evaluations
against the deployed system.

**Output:** staging deployment record and observed-state verification.

### Step 6: Make the production go, hold, or abort decision

The release owner reviews:

- staging and pre-production results;
- open findings and exceptions;
- production capacity, dependency, support, and change-window readiness;
- communication and incident readiness;
- recovery evidence;
- authorization from required business, technical, security, risk, or legal
  owners.

The deployment operator cannot convert missing approval into approval.

Record the decision in the
[production readiness review](../worksheets/production-readiness-review.md) or
an equivalent controlled record. Bind its decision ID and time to the reviewed
source, release manifest and digest, exact target and rollout stage, release
window, conditions and expiry, required owners, deployment operator,
observed-state readback owner, rollback or compensation path, and every
accepted exception. A material change invalidates authorization for further
deployment or promotion and requires a new or superseding decision record.

**Output:** attributable, exact-release production decision with conditions,
expiry, and execution and readback owners.

### Step 7: Start with bounded exposure

Choose the narrowest viable stage:

- dark or disabled deployment;
- shadow traffic where privacy and correctness permit;
- internal users;
- a canary instance, tenant, region, or cohort;
- a small percentage of traffic;
- blue-green environment with controlled switch.

Use feature flags, rate and action budgets, circuit breakers, and kill
switches to limit blast radius. Avoid canaries that exclude the only
high-consequence paths.

**Output:** production canary record with release and cohort identity.

### Step 8: Observe and compare

Compare the canary to its baseline across:

- errors, latency, saturation, retries, and dependency health;
- task success, groundedness, critical failure, and abstention;
- authorization, harmful action, safety, and privacy signals;
- data, feature, and index freshness;
- business outcome and user-support signals;
- spend, tokens, compute, and external-service usage;
- migration integrity and state consistency.

Automated thresholds should pause or roll back obvious failure. A person
reviews ambiguous or high-consequence quality signals. Missing telemetry is a
failed gate, not evidence of health.

**Output:** promote, hold, abort, or rollback decision with supporting
observations.

### Step 9: Promote progressively

Expand exposure in defined increments, repeating observed-state verification
and health comparison. Do not change the artifact during promotion. A required
fix becomes a new reviewed release candidate.

**Output:** complete promotion timeline and final production state.

### Step 10: Close the release

Record:

- actual deployed manifest and environment readback;
- approval, start, promotion, stop, and completion times;
- health and evaluation results;
- incidents, deviations, manual interventions, and exceptions;
- rollback-target validity;
- monitoring and review owner;
- user, support, or regulatory communication;
- follow-up actions with owners and due dates.

Close temporary access, credentials, flags, change windows, and exceptions
that are no longer required.

**Output:** complete deployment record connected to the decision-bound
production readiness review and observed production evidence.

## Prevention, detection, and response

| Failure mode | Prevent | Detect | Respond | Primary owner |
|---|---|---|---|---|
| Wrong or unowned change | linked intent, change owner, code owners | PR and policy checks | reject or reassign | repository owner |
| Broken build or regression | canonical tests, small changes, protected CI | trusted required checks | block merge | change owner |
| Weakened controls | protect workflows and policy, independent review | diff and ruleset checks | hard stop and investigate | security or platform owner |
| Dependency compromise | pinning, approved sources, least privilege | SCA, provenance, malware and integrity checks | quarantine and rebuild | supply-chain owner |
| Wrong release unit deployed | build once where applicable, immutable manifest, environment restriction | deployed-state and mutable-dependency readback | stop and restore a compatible known-good state | deployment operator |
| Migration incompatibility | expand-contract design, rehearsal, backup | staging and canary validation | roll forward, compensate, or restore | data and service owner |
| Quality or safety regression | representative evaluations, bounded canary | online quality and harm thresholds | pause, fallback, kill, or roll back | product and risk owner |
| Authorization failure | typed services, negative tests, scoped identities | access-denial and anomaly monitoring | revoke, contain, investigate | security owner |
| Silent provider or model change | pinned revisions where possible, alternate route | sentinel evaluations and change monitoring | reroute, constrain, or suspend | AI platform owner |
| Deployment automation failure | idempotency, serialization, timeouts | workflow and environment telemetry | halt and use tested manual recovery | platform owner |
| Unclear recovery | exercised runbook and named authority | readiness review and game day | escalate and fail closed | service owner |

Prevention is strongest when it makes an unsafe state difficult to create.
Detection must open an owned action or block a gate. Response must restore
acceptable service without destroying the evidence needed for diagnosis.

## Rollback, forward recovery, and compensation

Use rollback when a known-good prior state can be restored safely within the
required time. Prefer forward recovery when:

- a schema or data transformation is irreversible;
- newer clients or state are incompatible with the prior version;
- an external side effect has already occurred;
- a security fix must remain in place;
- provider behavior cannot be restored by deploying old application code.

Compensation is a business operation that counteracts a completed side effect,
such as reversing a transaction or invalidating an issued authorization. It
must be typed, authorized, idempotent where possible, observable, and tested.

Rollback contains impact; it does not by itself complete root-cause analysis,
data correction, customer remedy, or preventive action. Continue through the
[incident, problem, and corrective-action process](../operations/incident-problem-and-corrective-action.md).

## Emergency changes

Emergency access is for containment or restoration, not convenience.

1. Declare the incident and authorized emergency owner.
2. Record the reason normal gates cannot meet the required response time.
3. Minimize scope and preserve before-change evidence.
4. Use a time-bounded break-glass identity.
5. Retain an independent approval where feasible; never let an agent authorize
   its own emergency action.
6. Verify the actual production result.
7. Revoke emergency access promptly.
8. Within a defined retrospective window, either revert the emergency change
   or package the surviving state as an exact reviewed release candidate and
   obtain the ordinary release-owner `go`, `hold`, or `abort` decision,
   deployment reconciliation, observed-state readback, and operating-envelope
   record.
9. Complete normal tests, protected review, documentation, and corrective
   actions within that window.

An emergency change that remains unreviewed becomes an undocumented
production fork.
Merge or completed review alone does not normalize a surviving emergency
production state.
Emergency incident authority does not automatically grant repository repair,
merge, general release, promotion, or self-readback authority. Bind the service
owner, repository and change owners, release owner, operator, readback owner,
incident-closure authority, and corrective-action owner through the
[incident and corrective-action record](../worksheets/incident-and-corrective-action-record.md).

## AI-assisted deployment controls

AI assistance does not lower the deployment standard.

- Keep agents on isolated branches and away from production credentials.
- Treat issue text, PR descriptions, retrieved documents, tool output, and
  external skills as untrusted inputs.
- Record the accountable initiator, material skills and tools, and sanitized
  evidence without retaining hidden reasoning.
- Do not allow the change-producing agent to approve, merge, or deploy its own
  work.
- Use a deterministic, policy-scoped executor for privileged actions.
- Require an independent person who understands the change.
- Treat skipped tests, deleted checks, reduced thresholds, changed triggers,
  broader permissions, or new bypass paths as blockers until explicitly
  justified and approved.
- Bind verification and deployment evidence to immutable revisions.
- Treat AI-assistance labels, attestations, and transcripts as limited
  provenance signals; separately review source, dependencies, originality,
  license obligations, and the actual changed behavior.

See the
[skills-first AI-assisted change workflow](skills-first-ai-development.md) for
the complete change workflow.

## Deployment measures

Measure outcomes rather than deployment volume:

- lead time from approved intent to verified production;
- deployment frequency for accepted changes;
- change failure, rollback, and forward-recovery rates;
- time to detect, contain, restore, and fully remediate;
- percentage of releases with verified deployed-state readback;
- rollback exercise success and recovery time;
- escaped defect and incident recurrence;
- emergency-change frequency and retrospective completion;
- owner and backup coverage;
- exception age;
- human review time and deployment toil;
- cost per accepted, stable release.

A faster pipeline that increases unowned failures or hides recovery debt is
not an improvement.
