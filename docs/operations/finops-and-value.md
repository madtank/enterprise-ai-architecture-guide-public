# FinOps, capacity, and value realization

AI economics must connect infrastructure and provider consumption to a successful business outcome. Token volume, GPU hours, and number of users are operational drivers—not value by themselves.

## Unit economics

Choose a unit aligned with the workflow:

- cost per resolved case;
- cost per accepted draft;
- cost per accurate prediction;
- cost per approved transaction;
- cost per research task completed;
- cost per active user with demonstrated benefit.

Include:

- model inference or training;
- embedding, retrieval, reranking, and vector storage;
- orchestration, tools, network, and egress;
- guardrails, evaluation, observability, and retained traces;
- human review, correction, escalation, and support;
- platform engineering, security, assurance, and vendor management;
- idle capacity, commitments, and disaster recovery;
- migration and exit.

## Cost allocation

Attach consumption to:

- business unit and cost center;
- use case and environment;
- application and release;
- model/provider route;
- tenant or customer where permitted;
- successful or failed outcome.

Shared costs need a transparent allocation method. Use showback before chargeback when measurement or ownership is immature.

## Budgets and controls

Layer controls:

- enterprise, domain, product, environment, and workload budgets;
- per-request, per-job, and per-agent-run limits;
- token, step, tool, concurrency, and duration budgets;
- provider quotas and reserved-capacity limits;
- forecast variance and anomaly alerts;
- circuit breakers for runaway retry, loops, or abuse.

Budget exhaustion should produce an explicit safe response. Do not silently drop safety checks, reduce evidence, or route restricted data to an unapproved service.

## Optimization order

Optimize in this order:

1. remove low-value or duplicate calls;
2. reduce context and output while preserving task quality;
3. cache safe, reusable results with correct tenant and freshness boundaries;
4. batch or schedule flexible work;
5. route simple tasks to smaller or cheaper approved models;
6. optimize retrieval, embeddings, and storage;
7. improve accelerator utilization and scaling;
8. consider quantization, distillation, or self-hosting when lifecycle cost supports it.

Every optimization should pass quality, safety, privacy, security, and latency regression thresholds.

## Model routing economics

Routing policy should balance:

- task quality and critical-case performance;
- data handling and region;
- availability and quota;
- latency;
- context and modality;
- unit cost;
- concentration and exit risk.

Record the route and rationale. A router should abstain when no approved model meets the policy.

Evaluate whole-task economics rather than comparing only per-token prices:

```text
total task cost =
  routing + coordination + worker calls + duplicated context
  + tools + synthesis + verification + expected retries and escalation
  + storage, network, guardrails, and committed capacity
```

For parallel work, wall-clock latency may approach routing time plus the
slowest worker plus synthesis and verification, while aggregate token and tool
use still increase. Compare every routed design with a single capable-model
baseline using the same representative and critical-case evaluation set.

Track:

- cost and latency by task class, route, agent role, and accepted outcome;
- false low-tier routing and critical-case escalation recall;
- unnecessary high-tier routing;
- retry, fallback, and verifier invocation;
- savings after coordination and observability overhead;
- quality-adjusted cost per accepted outcome.

Maintain numeric provider prices in a dated, refreshable registry with an
owner, region, SKU, contract, capture date, next review, and material-change
alerts. The
[model and provider candidate catalog](../architecture/model-and-provider-candidate-catalog.md)
page provides a current illustrative candidate snapshot, not a procurement
quote.

## Capacity planning

Plan for:

- steady, peak, burst, and batch demand;
- context and output distributions;
- model-loading and cold-start behavior;
- provider rate and token limits;
- GPU memory, interconnect, storage, and network;
- evaluation, training, and re-indexing peaks;
- failover capacity and quota;
- tenant fairness and priority queues.

For enterprise-operated, capacity-backed serving, track utilization, queue
time, fragmentation, accelerator/CPU/memory allocation, energy where measured,
platform operations, support, and the cost of idle resilience. Normalize those
meters into the same root-execution record used for managed-service usage, then
compare total cost and operating responsibility. Keep a disconnected route's
pre-carved allocation reserved in forecasts and chargeback until authoritative
reconciliation proves the residual headroom reusable.

## Build, buy, or host

Build a total-cost model across:

- implementation and integration;
- data preparation and migration;
- licenses, usage, and committed spend;
- people and on-call skill;
- security, privacy, legal, compliance, and audit;
- reliability and disaster recovery;
- evaluation and change adaptation;
- vendor management;
- portability and exit.

Enterprise-operated serving can be economical at sustained scale, but it
transfers patching, serving, safety, capacity, hardware, and model lifecycle
risk to the enterprise.

## Forecasting

Forecast from business demand, not a flat token-growth assumption:

```text
eligible events
× adoption
× calls per workflow
× average input/output and tool use
× unit prices
+ fixed platform and assurance cost
```

Use ranges for adoption, model mix, prompt size, review rate, and provider pricing. Reforecast when workflow, model, routing, or retention changes.

## Value realization

Measure:

- realized benefit against a defined baseline;
- adoption and completion;
- accepted versus corrected output;
- downstream quality and rework;
- human time shifted, not merely generated;
- risk avoided and new risk introduced;
- total unit cost;
- distribution of benefit and harm.

Set explicit scale, optimize, hold, and stop criteria. Retire systems that do not create sufficient net value even if their model metrics are strong.

## Sustainability

Where material, report training and inference energy, accelerator utilization, workload region, hardware lifecycle, and storage growth. Prefer right-sized models and avoid wasteful repeated computation. Sustainability trade-offs should remain subject to quality, rights, security, and resilience requirements.
