# AI system card

The system card is the durable, reader-oriented description of a deployed AI system. It complements model and data documentation.

The
[fictional procurement-evidence golden thread](../examples/worked-golden-thread.md#2-the-evidence-spine)
shows one synthetic system card joined to its intake, obligation, architecture,
identity, threat, routing, evaluation, release, incident, and retirement
records. It is an illustration, not a completed template for reuse.

## Identity

- **System name and inventory ID:**
- **Version / release:**
- **Lifecycle state:**
- **Business, product, technical, data, and operations owners:**
- **Support and incident contact:**
- **Risk tier and applicable overlays:**
- **Regulatory obligation register version / snapshot digest:** use the
  [regulatory obligation register](regulatory-obligation-register.md);
- **Applicable obligation and applicability-decision IDs:**
- **Obligation decision date / next review:**
- **Transfer, decommissioning, and retirement record ID / state:** use the
  [transfer, decommissioning, and retirement record](transfer-decommissioning-and-retirement.md);
- **Last approved / next review:**

## Intended use

- problem and business outcome;
- intended users and affected people;
- decision, content, or action influenced;
- supported contexts, languages, locations, and scale;
- prohibited and unsupported uses;
- non-AI baseline and fallback.

## Architecture

- architecture and data-flow links;
- predictive, generative, retrieval, agentic, or combined pattern;
- application, orchestration, models, providers, data, tools, and systems of record;
- deployment regions, tenant model, and major trust boundaries;
- maximum autonomy and action consequence;
- human-review points.

## Data

For each dataset or source:

| Name / ID | Purpose | Owner | Population / period | Classification | Version / freshness | Retention / deletion |
|---|---|---|---|---|---|---|
| | | | | | | |

Describe lineage, consent or authority, quality limits, representativeness, exclusions, licensing, and known gaps.

## Models and artifacts

| Artifact | Provider / owner | Immutable revision or limitation | Purpose | Approval | Known limits |
|---|---|---|---|---|---|
| | | | | | |

Include models, prompts, policies, indexes, embeddings, feature definitions, tools, and automated graders.

### Agent and model routes

| Route ID | Task / risk class | Coordinator profile | Worker profile | Verifier | Allowed provider / region / revision | Fallback / escalation | Owner |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Document maximum delegation depth, tool authority, data classes, quality and
critical-case thresholds, latency and spend objectives, route rationale,
observability fields, and last evaluation date. Link the
[model routing and agent dispatch plan](model-routing-and-agent-dispatch-plan.md).

## Evaluation

- evaluation plan and report links;
- baseline and release thresholds;
- representative and critical scenario coverage;
- quality, fairness, safety, security, privacy, reliability, human-factors, and cost results;
- subgroup and slice limitations;
- independent review;
- unresolved findings; residual-risk decision IDs, categories, results,
  current validity and supersession states, named authorities and authority
  bases, exact scopes, conditions, expiries, and invalidation triggers; and
  risks that remain unaccepted or on hold.

## User experience

- AI disclosure;
- source and uncertainty presentation;
- human oversight;
- correction, appeal, opt-out, and escalation;
- accessibility;
- user training and usage policy.

## Security and privacy

- threat model;
- [identity and permission matrix](identity-and-permission-matrix.md),
  including delegation and tool scopes;
- [agent execution and telemetry contract](agent-execution-and-telemetry-contract.md)
  ID, revision, disposition, and operating-evidence period;
- data minimization, encryption, egress, DLP, secrets, and
  privacy-minimized telemetry;
- supply-chain provenance;
- red-team and penetration results;
- retention and forensic-readiness decisions.

## Operations

- service, quality, safety, and cost objectives;
- dashboards and alerts;
- capacity, quotas, budgets, and circuit breakers;
- fallbacks and dependencies;
- rollback, pause, and kill switch;
- incident and recovery procedures;
- sampling and periodic review;
- continuity, successor or no-successor decision, active-work reconciliation,
  asset disposition, readback, residual ownership, and reopen plan.

## Limitations

State plainly:

- conditions where the system should abstain or defer;
- known performance gaps;
- populations or scenarios not validated;
- mutable supplier dependencies;
- explanation and reproducibility limitations;
- residual harms and operational constraints.

## Change history

| Date | Release | Material change | Evaluation / approval | Outcome |
|---|---|---|---|---|
| | | | | |
