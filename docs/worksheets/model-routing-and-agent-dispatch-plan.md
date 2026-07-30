# Model routing and agent dispatch plan

Complete one copy per product and production environment. Candidate examples
dated 2026-07-27 are discovery inputs, not blanket approvals.

Related architecture:
[governed model routing and agent dispatch](../architecture/model-portfolio-and-routing.md).
Refresh candidates and product-specific claims from the
[dated model and provider candidate catalog](../architecture/model-and-provider-candidate-catalog.md).

## Decision metadata

| Field | Value |
|---|---|
| Routing-plan record ID / version | |
| Record state | draft / under review / decision-bound / superseded / expired |
| Immutable plan digest and evidence cutoff | |
| Named route-decision authority and source of authority / adopted policy | |
| Record owner and accepted backup | |
| Product / service and environment | |
| Exact tenant, task, data, tool, region/site, serving, and authority boundary | |
| Business and product owner | |
| Engineering and platform owner | |
| Security / privacy and model-risk owner | |
| FinOps / procurement owner | |
| Supported tenants and permitted data classes | |
| Required inference geographies | |
| Availability and latency objectives | |
| Monthly budget and maximum cost per run | |
| Evaluation artifact and policy version | |
| Routing-policy version and catalog revision | |
| Agent execution and telemetry contract ID / revision | |
| Decision effective time and expiry | |
| Material-change, evidence-freshness, and invalidation triggers | |
| Supersedes and superseded-by decision IDs | |
| Opened, target approval, and mandatory review dates | |

## Role profiles

| Profile | Task and risk class | Minimum capability | Maximum authority | Quality and critical threshold | Latency objective | Cost ceiling | Verifier | Owner |
|---|---|---|---|---|---|---|---|---|
| Frontier coordinator | | | | | | | | |
| Balanced worker | | | | | | | | |
| Economical worker | | | | | | | | |
| Protected verifier | | | | | | | | |

A model-based protected verifier may advise, reject, or escalate. It does not
satisfy independent human assurance and cannot approve a material change or
residual risk.

## Candidate discovery shortlist

Start from the dated discovery table in
[the model and provider candidate catalog](../architecture/model-and-provider-candidate-catalog.md),
then refresh the exact service, region, processing plan, context band,
currency, contract, and date. Do not duplicate a stale public price table in
the completed worksheet. That catalog is a managed-cloud discovery snapshot,
not the universe of allowed deployment patterns. An enterprise-operated
candidate must instead link its controlled artifact inventory, provenance,
license, runtime, capacity, support, and lifecycle evidence.

| Role | Candidate source / service | Exact candidate | Cost-record ID and capture date | Evaluation disposition |
|---|---|---|---|---|
| | | | | |

The cost record must label its unit and every applicable meter, including
input, cache read, cache write or population, output, request, modality, tools,
grounding, guardrails, storage, network, committed or idle capacity,
accelerator/CPU/memory, energy or facility allocation where measured, license,
platform operations, patching, and support. Azure-hosted deployments use Azure
meters rather than OpenAI direct rates. A token-only estimate is invalid for a
capacity-backed enterprise-operated route.

## Serving boundary records

Do not use `managed` or `self-hosted` as a complete boundary. Create one
immutable record per exact serving path using the axes in
[deployment patterns](../architecture/deployment-patterns.md#model-deployment-choices).

| Serving boundary ID / revision / digest | Operating responsibility | Deployment location / region or site | Tenancy, connectivity, and data path | Artifact control; exact model and runtime/configuration identity | Exact invocation target; final invocation PEP and owner | Exclusive invocation, artifact, control, and egress identities | Authenticated observed-state measurement, freshness, and normalized meter sources |
|---|---|---|---|---|---|---|---|
| | supplier-operated / jointly managed / enterprise-operated | | | | | | |

For enterprise-operated serving, bind the model or weights digest, provenance
and license, adapters/quantization, serving image, runtime/configuration and
safety-policy digests, patch/vulnerability state, cluster, namespace, node
pool, accelerator or device class, separate invocation-admission and
serving-runtime identities, and an authenticated deployment/load measurement
source with maximum age. Runtime self-report alone is insufficient. For a
managed service, bind the provider service, account/project, endpoint, region,
processing plan, data configuration, exposed or monitored mutable-service
identity, available provider readback, and any exact-revision limitation.

The final PEP must be the sole path to the target. A disconnected PEP requires
a separately approved, signed, bounded-validity policy package bound to the
boundary ID/revision/digest, one PEP/device/workload proof key, and measured
runtime. Record its monotonic version, pre-reserved non-overlapping use/time/
token/cost/resource allocation, maximum validity within the approved offline
revocation-exposure objective, rollback-resistant local package/epoch/consume/
lease/clock state, refresh and reconciliation path, and independently
verifiable disablement method. Clone, snapshot restore, state corruption,
expiry, exhaustion, missed refresh, or uncertain measurement, clock, or block
state fails closed. Do not refresh or reuse the allocation before
reconciliation.

## Exact deployment approvals

An application may use a deployment only when its lifecycle state is
**route-eligible** and its linked, current admission decision is **Approve**.
A lifecycle label alone grants no authority.

| Deployment ID | Lifecycle state | Serving boundary ID / revision / digest | Exact model/artifact, runtime/configuration, serving-TCB identities, and measurement policy | Invocation target / region or site | Data / retention | Processing or capacity plan / tools | Evaluation and conformance artifacts | Operating owner; not decision authority | Approval expiry / next review |
|---|---|---|---|---|---|---|---|---|---|
| | candidate | | | | | | | | |

States:

- **candidate** — proposed for evaluation; not runnable without a current
  **Approve** decision bounded to the exact evaluation scope;
- **route-eligible** — selectable only inside a current **Approve** decision;
- **deprecated** — retained only inside the recorded migration envelope;
- **blocked** — invocation denied.

Attach current evidence for training use, abuse monitoring, retention, deletion,
residency, cross-boundary processing, feature-specific zero retention,
identity, private networking, encryption, audit, tools, model-invocation and
other egress, safety configuration, artifact/runtime integrity, patch state,
price or capacity allocation, quota, lifecycle, emergency disablement, and
observed-state readback.

Each deployment state that permits evaluation or routing must be backed by one
attributable admission decision. A routing-plan decision and a deployment
admission may name different authorities, but each decision has exactly one
named authority designated under adopted policy.

| Deployment approval ID / revision and deployment ID | Named admission decision authority and basis | Decision: approve / hold / reject | Authorized state and exact scope | Decision-bound evidence IDs, revisions, and digests | Effective time / expiry | Conditions / exception IDs | Invalidation and block triggers | Supersedes / superseded by |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

**Approve** permits only the recorded `candidate` evaluation or
`route-eligible` routing scope while the decision remains current. Evaluation
approval must be limited to its recorded environment, data, tools, authority,
and expiry; it is not production approval. **Hold** authorizes no new or
widened route under this record. **Reject** does not admit the proposed
deployment or scope. A prior record may remain usable only if it is separately
current and was not invalidated, blocked, or superseded.

## Central routing rules

| Rule ID | Request predicate | Hard exclusions | Eligible deployment IDs | Ranking objective | Fallback / escalation | Failure behavior | Owner |
|---|---|---|---|---|---|---|---|
| | | | | | | deny | |

For each rule:

- identify required user, workload, tenant, environment, task, risk, modality,
  tool, and data labels;
- identify prohibited serving boundaries, operating responsibilities,
  locations, connectivity modes, providers, models, artifacts/runtimes,
  previews, aliases, regions/sites, retention modes, tools, and processing or
  capacity plans;
- link the evaluation proving each deployment can perform the task;
- define whether ranking optimizes measured quality, latency, availability,
  concentration, expected cost, or an approved combination;
- define safe behavior when every eligible deployment is unavailable;
- record and reproduce the selected and rejected constraints.

### Policy checklist

- [ ] No route is eligible unless an exact deployment is `route-eligible`
      under a current **Approve** decision.
- [ ] Applications and agents cannot submit arbitrary provider identifiers.
- [ ] Managed routers and enterprise-operated runtimes cannot escape the
      decision-bound `route-eligible` set or serving boundary.
- [ ] Preview models are sandbox-only unless an explicit exception exists.
- [ ] The decision is short-lived and bound to identity, tenant, task, and data.
- [ ] The decision is emitted as a versioned, tamper-evident route grant.
- [ ] Only the policy service can mint a grant; every child grant references
      its parent and narrows authority and budgets.
- [ ] The log records policy version, route rationale, and rejected candidates.
- [ ] An emergency policy change can block a deployment without an application release.

### Route-grant contract

- **Schema identifier and version:**
- **Envelope format, canonicalization, and signature algorithm:**
- **Approved issuer, signing key / key set, and rotation owner:**
- **Exact adapter audiences, presenting workload identities, and mTLS / DPoP /
  key-confirmation holder binding:**
- **Maximum lifetime, clock skew, and replay treatment:**
- **Atomic shared consume store, grant-ID retention, and outage behavior:**
- **Serving-boundary ID, revision, digest and axes; exact
  artifact/runtime/configuration, invocation target, final invocation PEP,
  required measurement policy, and observed-state source:**
- **Exclusive managed-provider credential or enterprise-operated
  invocation-admission identity; separate decision-bound serving-runtime,
  artifact-registry administration, control-plane, update, tool, telemetry,
  and outbound-egress identities; direct-call denial evidence:**
- **For enterprise operation, authenticated deployment/load measurement source,
  trust root, bound artifact/runtime/infrastructure fields, maximum age,
  unavailable behavior, and proof that runtime self-report cannot satisfy the
  check:**
- **Deployment approval ID, catalog revision, revocation epoch, authoritative
  live-check owner, epoch scope/increment rule, final-invocation
  `issued` to `committed-to-invoke` lease transition, block-effective
  acknowledgement, in-flight quarantine, and fail-closed outage behavior:**
  - Treat the catalog revision as decision provenance.
  - Define a monotonically increasing revocation epoch for each deployment
    approval.
  - Record how every connected managed or local final PEP acknowledges a new
    epoch or is independently verified drained or disabled, and how every
    outstanding disconnected package and lease is acknowledged, independently
    disabled, or expired or exhausted before a block is declared effective.
- **Disconnected-policy package, signer, monotonic version, exact
  boundary/deployment/epoch, PEP-device-workload proof key, measured runtime,
  pre-reserved non-overlapping allocation, maximum validity and approved
  revocation-exposure objective, rollback-resistant local
  package/epoch/consume/lease/clock state, clone/snapshot-restore invalidation,
  reconciliation-before-refresh rule, independently verifiable local/physical
  disablement, and fail-closed behavior, if applicable:**
- **Primary and each fallback target's deployment ID, approval ID, deployment
  record revision, serving-boundary revision/digest, and revocation epoch:**
- **Root-execution budget ledger, atomic sibling reservations, settlement,
  unresolved-result holds, and outage behavior:**
- **Reservation binding to grant, parent grant and decision, canonical root,
  signed allocation, state, expiry, and digest:**
- **Per-attempt limits, total execution allocations, root deadline, and how
  retries and fallbacks consume rather than reset those totals:**
- **Idempotency key, downstream durable enforcement or proven retry safety,
  ambiguous-result reconciliation, and permitted retry semantics:**
- **Required subject, tenant, environment, task, data, route, authority,
  budget, verifier, fallback, and telemetry fields:**
- **Parent-to-child attenuation rule:**
- **Identity and permission matrix URI:**
- **Agent execution and telemetry contract URI / schema:**
- **Unavailable-deployment and replacement-grant behavior:**
- **Grant and decision-log retention:**
- **Sensitive handling, transmission, redaction, and fields explicitly
  prohibited from the grant:**

## Agent dispatch design

| Parent profile | Child profile | Task boundary and output schema | Allowed tools / data | Max fan-out | Max depth | Max retries | Timeout | Cost cap | Verifier |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| Coordinator | Economical worker | | | | | | | | |
| Coordinator | Balanced worker | | | | | | | | |

- **Decomposition method:**
- **Maximum tasks per run:**
- **Context supplied and intentionally withheld:**
- **Duplicate-work prevention:**
- **Cancellation behavior:**
- **Result integration and verification:**
- **Human authorization points:**

### Harness acceptance

- [ ] Parent and children use independently configured logical profiles.
- [ ] Every adapter validates the same enterprise route-grant contract before
      model access.
- [ ] Expired, altered, untrusted-signer, wrong-audience, wrong-tenant, and
      wrong-workload grants fail closed.
- [ ] The adapter proves the grant's holder binding; a copied grant presented
      by another workload or key fails closed.
- [ ] Horizontally scaled adapters atomically consume grant uses and reject
      concurrent replay.
- [ ] Consume-store unavailability fails closed before model or tool access.
- [ ] Applications, workers, skills, and unapproved workloads have neither
      managed-provider credentials nor enterprise invocation-admission or
      serving-runtime identities, and have no direct provider, internal
      endpoint, DNS, loopback, IPC, socket, embedded-library, weights-path, or
      accelerator-runtime access.
- [ ] Final model-invocation enforcement transactionally checks the selected
      serving-boundary ID/revision/digest, target, artifact/runtime identity,
      authenticated freshness-bounded deployment/load measurement, deployment
      approval, and epoch while changing a single-use lease from
      `issued` to `committed-to-invoke`; only then may it send, queue, or
      execute.
- [ ] Supplier/jointly managed paths enforce provider credentials and egress;
      enterprise-operated paths enforce the serving identity plus network,
      process, filesystem, and runtime admission.
- [ ] A direct or embedded path that cannot enforce the grant is unsupported.
- [ ] The durable lease transition orders races: a block committed first
      denies the attempt, while an invocation committed first is treated as in
      flight and quarantined or cancelled under policy.
- [ ] A block stops new leases, has an acknowledged effective state across
      every managed or local PEP, and drains or disables a PEP that misses the
      epoch.
- [ ] An enterprise-operated PEP rejects a missing, stale, tampered, or
      runtime-only self-reported deployment/load measurement.
- [ ] A disconnected package is bound to one PEP/device proof key and measured
      runtime, has a monotonic version and non-overlapping pre-reserved
      allocation, and updates rollback-resistant local
      package/epoch/consume/lease/clock state.
- [ ] Clone, snapshot restore, local-state corruption, expiry, exhaustion,
      missed refresh, or uncertain measurement, clock, or block state fails
      closed; refresh waits for authoritative allocation reconciliation.
- [ ] Every primary and fallback target carries its own serving boundary,
      boundary revision/digest, deployment approval, deployment record revision,
      and revocation epoch.
- [ ] Central restrictions propagate to every child.
- [ ] A child cannot change serving boundary, operating responsibility,
      location, connectivity, provider, model/artifact, runtime/configuration,
      region/site, data class, or tool scope.
- [ ] A child grant references its parent and cannot widen authority or budgets.
- [ ] Fan-out, depth, concurrency, tokens, retries, time, and cost have hard
      per-grant limits and atomically reserved aggregate root-execution limits.
- [ ] Concurrent siblings cannot oversubscribe the root budget; ambiguous
      results retain their reservations until authoritative reconciliation.
- [ ] A reservation mismatched to its grant, parent, root, signed allocation,
      state, expiry, or digest fails closed.
- [ ] Expiry releases only an unclaimed reservation; claimed work retains its
      upper bound until terminal state and delayed usage settlement.
- [ ] Primary, retry, and fallback attempts share total allocations and the
      root deadline; none can reset a per-execution total.
- [ ] Cancellation terminates or accounts for outstanding work.
- [ ] Decision ID, exact route, serving-boundary ID/revision/digest,
      model/artifact, runtime/configuration, authenticated measurement reference
      and freshness result, final PEP, location, region/site, processing or
      capacity plan, normalized meter source, usage, total allocated cost,
      latency, tools, verification, fallback, and outcome are logged and
      reconciled without raw grants, credentials, internal addresses, weights
      paths, prompts, or results.
- [ ] A protected verifier can reject a result before integration.
- [ ] Escalation is explicit, bounded, and observable.
- [ ] Ambiguous-result retries require tested downstream idempotency or proven
      retry safety; otherwise execution stops for reconciliation.
- [ ] Failure cannot silently fall back to an unapproved deployment.

### Cross-harness conformance evidence

Record **pass**, **fail**, or **unsupported** for every adapter and attach the
evidence. Do not combine independent cases into one result.

| Test case | Codex | Claude Code | Google ADK | Amazon Bedrock AgentCore | Application-specific adapter | Evidence |
|---|---|---|---|---|---|---|
| Valid grant and expected telemetry | | | | | | |
| Expired grant | | | | | | |
| Altered grant or untrusted signer | | | | | | |
| Copied grant presented by the wrong holder or key | | | | | | |
| Concurrent replay to separate adapter instances | | | | | | |
| Consume or replay store unavailable | | | | | | |
| Approval, epoch, or single-use invocation-lease service unavailable — no invocation | | | | | | |
| Block commits before the invocation lease reaches `committed-to-invoke` — no managed or local invocation | | | | | | |
| Connected managed or local PEP misses epoch acknowledgement — require independently verified drain/disable; an administrative flag cannot make the block effective | | | | | | |
| Invocation lease commits before the block — treat as in flight and cancel or quarantine | | | | | | |
| Direct managed-provider credential or egress bypass | | | | | | |
| Direct enterprise invocation-admission identity, serving-runtime identity, internal endpoint, DNS, loopback, IPC, socket, library, weights, or accelerator-runtime bypass | | | | | | |
| Cloud-mode grant replayed at a local PEP, local-mode grant at a cloud PEP, or boundary revision/digest mismatch | | | | | | |
| Serving boundary, artifact/runtime/configuration, quantization, safety policy, infrastructure location, or target changed after minting | | | | | | |
| Enterprise deployment/load measurement missing, stale, tampered, or only self-reported by its serving runtime | | | | | | |
| Disconnected policy package expired, exhausted, stale, wrong-epoch, measurement-failed, clock-uncertain, or locally corrupt | | | | | | |
| Disconnected package or VM/device snapshot copied, cloned, or rolled back | | | | | | |
| Disconnected package has wrong holder/runtime, a non-monotonic version, overlapping allocation, or un-reconciled predecessor | | | | | | |
| Disconnected PEP marked disabled without acknowledgement, independently verified local/physical disablement, or expiry/exhaustion of every package and lease | | | | | | |
| Primary target changed or revoked after minting | | | | | | |
| Fallback target changed or revoked after minting | | | | | | |
| Wrong tenant | | | | | | |
| Wrong workload | | | | | | |
| Wrong adapter audience | | | | | | |
| Provider or model override | | | | | | |
| Tool, data, or authority expansion | | | | | | |
| Initial attempt exceeds a per-attempt token, output, or timeout cap while remaining below the total allocation | | | | | | |
| Fan-out, depth, concurrency, or retry expansion | | | | | | |
| Concurrent siblings exceed root budget | | | | | | |
| Reservation binding mismatch | | | | | | |
| Unclaimed reservation expires | | | | | | |
| Claimed reservation expires while work remains in flight | | | | | | |
| Usage or billing settles after the provider result | | | | | | |
| Aggregate budget ledger unavailable | | | | | | |
| Provider or tool outcome remains permanently unknown | | | | | | |
| Retry exceeds remaining total allocation | | | | | | |
| Fallback exceeds remaining total allocation | | | | | | |
| Attempt exceeds the root deadline | | | | | | |
| Approved deployment unavailable or fallback requested | | | | | | |
| Unapproved cross-boundary or on-premises-to-cloud fallback / data transfer | | | | | | |
| Cross-boundary migration enabled before target evaluation, conformance, cost, rollback, and readback evidence | | | | | | |
| Source route, identity, process, or artifact remains usable after cutover | | | | | | |
| Observed telemetry omits serving-boundary revision/digest, exact artifact/runtime, authenticated measurement/freshness, final PEP, or meter source | | | | | | |
| Capacity-backed route supplies token-only cost | | | | | | |
| Ambiguous result without proven retry safety | | | | | | |
| Observed route or telemetry mismatch | | | | | | |

Mark unsupported constraints as a failed conformance result, not as silently
ignored fields. Attach the shared fixture, adapter mapping, negative-test
output, and expected-versus-observed execution record.

## Cost plan

Use exact prices or allocated resource costs for the serving boundary, model
and runtime revision, region/site, processing or capacity plan, context band,
currency, and capture date. State the authoritative meter and allocation rule.

```text
call cost =
  uncached input × input rate
  + cache-read input × cache-read rate
  + cache-write input × cache-write rate
  + output × output rate
  + request or modality charges
  + tools, grounding, guardrails, storage, and network
  + allocated accelerator, CPU, memory, energy, facility, license,
    platform-operation, patching, and idle-resilience cost

run cost =
  routing + coordinator + workers + synthesis + verification
  + expected retries, fallback, and escalation
```

| Call class | Deployment ID | Calls / run | Retry rate | Input / call | Cache read / call | Cache write / call | Output / call | Resource time / allocation | Cost / meter record ID | Auxiliary / call | Expected cost / run |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| Coordinator | | | | | | | | | | | |
| Economical worker | | | | | | | | | | | |
| Balanced worker | | | | | | | | | | | |
| Verifier / escalation | | | | | | | | | | | |

Calculate expected and worst-case calls, tokens or resource time, cost per run,
runs per month, committed and idle capacity, platform/on-call allocation,
monthly cost, and savings against a single capable-model baseline. Replace
illustrative assumptions with observed traces.

## Escalation and failure

| Observable condition | From profile | To profile or human gate | Maximum attempts | Additional budget | Final behavior |
|---|---|---|---:|---:|---|
| Invalid schema | | | | | |
| Required evidence missing | | | | | |
| Test or policy check fails | | | | | |
| Tool or serving-boundary failure | | | | | |
| Conflicting worker results | | | | | |
| Consequential action requested | | Human approval | 0 | 0 | stop |

Do not use self-reported confidence as the only escalation signal.

## Evaluation plan

| Suite | Profile | Data class | Quality threshold | Critical-case threshold | Tool success | p95 latency | Max cost / accepted task | Current result | Artifact |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| | Frontier coordinator | | | | | | | | |
| | Balanced worker | | | | | | | | |
| | Economical worker | | | | | | | | |
| | Protected verifier | | | | | | | | |

Include representative, ambiguous, long-context, structured-output, tool-use,
injection, prohibited-data, tool-denial, partial-failure, seeded bad-worker,
cancellation, timeout, retry, escalation, latency, concurrency, and cost cases.

Compare:

1. one capable-model baseline;
2. coordinator plus balanced workers;
3. coordinator plus economical workers;
4. mixed workers with verifier and escalation.

A cheaper route fails if it misses any critical safety, authorization,
human-oversight, or quality threshold.

## Rollout and rollback

| Stage | Traffic / data scope | Entry evidence | Success | Rollback trigger | Owner |
|---|---|---|---|---|---|
| Offline evaluation | synthetic or approved corpus | | | | |
| Shadow | production-shaped; no user-visible result | | | | |
| Canary | limited tenants and tasks | | | | |
| Limited production | approved classes | | | | |
| General production | approved scope | | | | |

Rollback:

1. block the affected deployment in central policy;
2. cancel outstanding child work where safe;
3. use only a previously approved fallback or fail closed;
4. preserve route, tool, cost, verification, and output evidence;
5. notify owners and open the incident or defect record;
6. require new evaluation and approval before re-enabling.

## Final routing-plan decision

- **Decision ID and timestamp:**
- **Named route-decision authority and authority basis:**
- **Decision:** approve / hold / reject
- **Decision-bound plan ID, version, and digest:**
- **Exact approved deployment approval IDs, revisions, and revocation epochs,
  including fallbacks:**
- **Serving-boundary IDs, revisions and digests; operating responsibility,
  location, tenancy, connectivity, artifact/runtime and serving-TCB identities,
  measurement policies, invocation targets, final PEPs, and cross-boundary
  fallback or migration scope:**
- **Product, service, environment, tenant, task, data, tool, region/site, and
  authority scope:**
- **Routing-policy and catalog revisions:**
- **Evaluation, conformance, price, security, privacy, and other required
  evidence IDs, revisions, digests, and evidence cutoff:**
- **Conditions, finding and exception IDs, monitoring, and stop triggers:**
- **Effective time and expiry:**
- **Material-change, reassessment, and invalidation triggers:**
- **Supersedes and superseded-by decision IDs:**
- **Attributable decision-evidence URI and digest:**
- **Authoritative registry location, enforcement owner, and readback owner:**

| Role | Named principal and authority / duty | Required approval, advice, or duty acknowledgement | Time and attributable evidence | Conflict, condition, or exception IDs and expiry |
|---|---|---|---|---|
| Route-decision authority; record the authoritative approve / hold / reject decision | | | | |
| Plan or change producer; no self-approval authority | | | | |
| Business / product owner | | | | |
| Engineering / platform owner | | | | |
| Security / privacy and model-risk owner | | | | |
| FinOps / procurement owner | | | | |
| Model governance owner | | | | |
| Qualified independent approver, when policy requires | | | | |

Supporting rows are not votes, and their completion does not infer approval.
A blank, stale, missing, or negative required approval, or an unresolved
conflict with controlling policy, forces **Hold** until resolved by the owner
of that reserved decision right or a separately authorized, policy-permitted
exception. The route-decision authority cannot waive a prohibition, missing
required approval, or another authority's reserved decision right.
AI-generated review remains advisory.

An **Approve** decision may carry only enforceable, monitored, unexpired
conditions. **Hold** and **Reject** authorize no new route grant under this
decision. Expiry, invalidation, blocking, or supersession stops new grants
under the affected record. Apply the recorded revocation-epoch, cancellation,
quarantine, and fallback controls to in-flight work. Preserve the prior record
and link a new superseding decision; do not edit a decision-bound record to
manufacture continued approval.
