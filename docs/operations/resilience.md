# Reliability and resilience

AI systems fail through infrastructure, dependencies, data, model behavior, policy, and human workflow. Reliability engineering must cover the service’s ability to produce an acceptable outcome, not only return an HTTP response.

## Failure domains

Inventory:

- application and orchestration runtime;
- identity, secrets, key management, and policy;
- model provider, endpoint, region, quota, and revision;
- source systems, pipelines, retrieval, feature, vector, and cache stores;
- tools, connectors, queues, and systems of record;
- evaluation, monitoring, and incident systems;
- human review and support capacity;
- vendor control plane and account dependencies.

Record owner, service objective, timeout, retry policy, failure behavior, recovery method, and tested fallback for each critical dependency.

## Service levels

Define:

- availability and successful-task completion;
- latency percentiles by stage;
- quality and critical-failure objectives;
- data, feature, and index freshness;
- action and transaction success;
- human review and appeal timing;
- recovery time objective (RTO);
- recovery point objective (RPO);
- maximum tolerable cost and security exposure.

An AI system can be technically available but semantically failed. Quality stop thresholds should trigger containment just like error-rate thresholds.

## Failure behavior

Choose explicitly:

- retry with idempotency and bounded backoff;
- queue for later processing;
- use a tested model or provider fallback;
- use a deterministic reduced-function path;
- send to a human queue;
- return previously validated data with freshness disclosure;
- abstain or fail closed.

Fallback must preserve data, regional, authorization, and risk policy. A cheaper or available model is not automatically an approved substitute.

## Timeouts, retries, and backpressure

- allocate an end-to-end deadline across components;
- stop issuing new downstream work after caller cancellation and request
  termination of outstanding work;
- cap retries and distinguish transient from permanent failure;
- use idempotency keys for repeated side effects;
- prevent retry storms and agent loops;
- bound queues and define priority and shedding;
- expose overload rather than silently degrading critical controls.

Cancellation intent is not proof that an already-committed provider or tool
request stopped. Track acknowledgements, quarantine late results, retain
claimed reservations, and reconcile authoritative effects through the
[agent execution and telemetry contract](../worksheets/agent-execution-and-telemetry-contract.md).

## High availability and disaster recovery

Decide:

- zonal, regional, provider, or on-premises failure scope;
- active/active, active/passive, or restore strategy;
- data replication and sovereignty constraints;
- model and hardware capacity in the recovery location;
- queue, workflow, approval, and agent-state recovery;
- feature, vector, cache, and index rebuild process;
- dependency and credential bootstrap order;
- consistency and duplicate-transaction handling.

Back up source configuration and reproducible pipelines; a vector index or feature cache may be rebuildable, but recovery time must be tested.

## Model and provider continuity

Prepare for:

- rate-limit and quota exhaustion;
- region or service outage;
- model deprecation or withdrawal;
- mutable alias behavior change;
- safety-policy or acceptable-use change;
- price change;
- account suspension;
- supplier compromise or insolvency.

Maintain a substitution evaluation and migration plan for critical services. Test it against quality and policy requirements rather than assuming API compatibility implies behavioral compatibility.
When a migration becomes an actual transfer or retirement, use the
[transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md)
to bind continuity evidence to successor acceptance, active-work
reconciliation, irreversible sequencing, revocation, readback, and residual
ownership.

## Release safety

Use:

- immutable or fully described release manifests;
- shadow traffic where privacy permits;
- internal, canary, and cohort rollout;
- automated rollback thresholds;
- quality and cost circuit breakers;
- feature flags and kill switches;
- compatibility checks for stateful workflows;
- post-deployment verification of actual versions and routes.

For a mutable provider model, maintain continuous sentinels and an alternate path because ordinary application rollback cannot restore prior model behavior.

Follow the [code deployment and release](../delivery/code-deployment.md)
procedure. Stateful releases need explicit forward recovery and compensation
when returning to an older artifact would not restore valid data or reverse
completed side effects.

## Exercises

Exercise:

- provider and region loss;
- quota exhaustion and cost spike;
- stale or poisoned retrieval;
- identity or secret revocation;
- tool outage during a partial transaction;
- corrupted workflow or memory state;
- model quality regression;
- harmful-output surge;
- telemetry loss;
- human-review backlog;
- index rebuild and data restoration;
- emergency kill switch and communications;
- a deployment that fails between migration and application promotion;
- a rollback that is unsafe because new state has already been written;
- restoration followed by the
  [incident and corrective-action](incident-problem-and-corrective-action.md)
  workflow.

Record whether the system met RTO, RPO, quality, authorization, and evidence requirements.

## Incident severity

Severity should consider:

- actual and potential harm;
- affected people, tenants, records, and transactions;
- data sensitivity and exposure;
- autonomy and irreversibility;
- duration and detectability;
- regulatory, contractual, and public impact;
- propagation to other systems.

A single high-consequence event may outrank a widespread low-quality incident.

## Forensic readiness

Preserve privacy-minimized evidence sufficient to reconstruct:

- initiating identity and intent;
- release, model route, prompts or policies, and relevant data provenance;
- retrieval and tool sequence;
- authorization and approval decisions;
- state transitions, retries, and errors;
- final actions and affected records;
- alerts, operator intervention, and containment.

Define legal hold, access, integrity, and retention before an incident. Avoid creating a new sensitive-data repository merely for debugging.
