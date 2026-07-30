# Deployment patterns

Choose the simplest pattern that satisfies the outcome and risk constraints. More autonomy creates more failure paths and should require stronger evidence.

## Pattern selection

| Pattern | Best fit | Primary risks | Default controls |
|---|---|---|---|
| Predictive service | Classification, forecasting, scoring | drift, bias, unstable features | feature lineage, threshold tests, drift monitoring |
| Prompted generation | Drafting, transformation, summarization | unsupported claims, data disclosure | output evaluation, disclosure, safe context |
| Retrieval-augmented generation | Answers grounded in enterprise knowledge | stale or unauthorized retrieval, weak citations | entitlement-aware retrieval, provenance, freshness tests |
| Human-approved action | AI prepares a consequential transaction | automation bias, incomplete review | explicit approval, change preview, durable audit |
| Bounded agent | Multi-step work using approved tools | runaway loops, tool abuse, goal misinterpretation | action budget, tool allowlist, checkpoints, kill switch |
| Autonomous operation | High-volume, reversible, well-observed actions | cascading impact, silent failure | strict scope, simulation, circuit breakers, continuous oversight |

## Retrieval-augmented generation

Use RAG when answers must reflect current or proprietary knowledge. Do not use it as a substitute for source governance.

Required design choices:

- authoritative source ownership and update cadence;
- document-level and passage-level permissions;
- deletion propagation and index refresh objectives;
- query and result filtering by tenant, purpose, and identity;
- provenance carried from retrieval into the response;
- evaluation of retrieval separately from generation;
- behavior for insufficient, conflicting, or stale evidence.

## Tool-using assistants and agents

Treat every tool invocation as an API transaction initiated by an untrusted planner.

The safe default is:

1. the model proposes a typed action;
2. deterministic code validates schema and policy;
3. the tool service authorizes the caller and resource;
4. consequential changes show a preview or require approval;
5. the owning service validates invariants and executes;
6. the runtime records the result and updates state;
7. budgets, timeouts, and circuit breakers limit continuation.

Avoid broad tools such as unrestricted shell, database, browser, or email access. Expose narrow operations with semantic names and bounded parameters.

## Model deployment choices

Classify an option across four axes:

- **operating responsibility:** supplier-operated, jointly managed, or enterprise-operated;
- **tenancy:** shared, logically isolated, dedicated, or physically isolated;
- **deployment location:** supplier cloud, enterprise cloud, data center, edge, or device;
- **artifact control:** closed service, exportable adapter, or enterprise-controlled weights.

Evaluate each option across:

- quality on representative tasks;
- security and privacy terms;
- data use and retention;
- region and residency;
- throughput, latency, and availability;
- model and API version stability;
- observability and abuse controls;
- unit economics at expected demand;
- exit cost and substitutability;
- internal operational capability.

Enterprise operation can increase control but also transfers patching, scaling, model security, safety, capacity, and reliability obligations to the enterprise. A “managed” label does not remove the need to document the actual shared-responsibility boundary.

### Exclusive governed model access

A routing decision is not an enforcement boundary if an application, harness,
worker, or skill can invoke either a managed provider or an
enterprise-operated model path directly. Record one decision-bound
`serving_boundary_id`, revision, and digest for the operating responsibility,
location, tenancy, connectivity, artifact control, exact target, serving TCB,
and final model-invocation policy enforcement point (PEP).

In governed environments:

- for supplier-operated or jointly managed services, only the approved gateway
  or adapter holds provider credentials and provider-bound egress;
- for enterprise-operated serving, only the approved serving gateway,
  scheduler, or runtime PEP holds invocation-admission authority; a separate
  decision-bound serving-runtime identity holds only the approved artifact-read
  and accelerator access;
- workload identity, network, process, filesystem, and runtime policy deny
  every direct or alternate invocation path;
- the final invocation PEP transactionally compares the selected target's
  current approval and revocation state, boundary revision/digest, and an
  authenticated freshness-bounded deployment/load measurement and changes a
  single-use invocation lease to `committed-to-invoke`; only then does it send,
  queue, or execute the request;
- approval, revocation, lease, or required disconnected-policy freshness
  unavailability fails closed rather than using a stale grant, cached model
  process, local weights, provider default, or ambient credential;
- an emergency block stops new leases, advances the affected approval's
  revocation epoch, and becomes effective only after every connected managed
  or local PEP acknowledges the epoch or is independently verified drained or
  disabled and every outstanding disconnected package and lease is
  acknowledged, independently disabled, or expired or exhausted; work already
  committed is cancelled where supported and its results quarantined; and
- a shared root-execution budget ledger atomically reserves fan-out,
  concurrency, token, retry, time, and cost headroom across all parallel
  children before dispatch.

Test each approved path. A direct managed-provider attempt must lack credentials
and egress. A direct invocation-admission PEP, serving-runtime identity,
internal endpoint, loopback, socket, embedded-library, weights, or
accelerator-runtime attempt must lack identity and access. A stale, tampered,
missing, or runtime-only self-reported deployment/load measurement must fail
closed. A grant
minted before a deployment block but not yet `committed-to-invoke` must be
rejected; an earlier committed attempt is treated as in flight. Concurrent
child requests must not reserve more aggregate authority or budget than the
originating execution received. The durable `committed-to-invoke` lease
transition is the race boundary: a block committed first denies the attempt,
while an invocation committed first is in flight and subject to cancellation
and result quarantine.

Switching operating responsibility, location, connectivity, artifact identity,
runtime/configuration, or final PEP is a material change, not an invisible
fallback. A disconnected boundary needs a signed, bounded-validity package
bound to one PEP/device key and measured runtime, a pre-reserved non-overlapping
allocation, rollback-resistant local consume/lease/epoch state, and validity no
longer than its approved revocation-exposure objective. Clone, snapshot restore,
state corruption, expiry, exhaustion, missed refresh, or block uncertainty
fails closed. A block remains pending until the package is acknowledged,
independently disabled, or expired or exhausted.
See the
[portable route-grant contract](model-portfolio-and-routing.md#portable-route-grant-contract)
for the required identifiers, live checks, and conformance cases.

This chapter selects the runtime and responsibility pattern. It does not
replace the promotion procedure. Use
[code deployment and release](../delivery/code-deployment.md) to assign
repository and release ownership, build and attest the release unit, deploy
through protected environments, verify actual state, and recover from failure.
