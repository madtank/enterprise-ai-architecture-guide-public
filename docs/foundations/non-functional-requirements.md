# Non-functional requirements

Non-functional requirements define the operating envelope of an AI system. They should be measurable, testable, owned, and connected to release and stop decisions.

## Requirement model

For each requirement, record:

- scenario and affected stakeholder;
- metric and measurement method;
- target, minimum, and stop threshold;
- scope and important slices;
- owner and evidence source;
- test environment and production signal;
- behavior when the requirement cannot be met;
- review and material-change triggers.

## Quality and fitness

Define task-specific requirements for:

- correctness, factual support, relevance, and completeness;
- calibration, confidence, and abstention;
- retrieval recall, ranking, freshness, and citation validity;
- fairness across relevant groups;
- consistency and reproducibility expectations;
- action validity and postcondition verification;
- explainability for users, reviewers, and auditors;
- graceful behavior with ambiguous or insufficient evidence.

Probabilistic quality should be expressed statistically, with sample size and uncertainty.

## Safety and human impact

- unacceptable outcomes and critical-failure rate;
- human review authority, time, information, and workload;
- correction, appeal, escalation, and opt-out timing;
- accessibility and language coverage;
- foreseeable misuse and abuse resistance;
- maximum autonomous consequence and cumulative loss;
- safe state after interruption, uncertainty, or policy conflict.

## Security and privacy

- supported identity assurance and delegation;
- least privilege, tenant isolation, and authorization latency;
- approved data classes, regions, and providers;
- data minimization, retention, deletion, and trace-redaction objectives;
- encryption, key ownership, secret handling, and egress restrictions;
- vulnerability response and credential-revocation time;
- audit completeness and forensic evidence availability.

## Reliability and resilience

- availability and successful-task completion;
- latency percentiles by workflow stage;
- recovery time objective and recovery point objective;
- provider, region, network, model, tool, and data dependency behavior;
- queue depth, backpressure, retry, and timeout limits;
- capacity headroom and quota-exhaustion behavior;
- rollback time by artifact type;
- index, feature, cache, and state rebuild objectives;
- consistency and duplication behavior under retry.

Quality can fail while infrastructure remains available. Define both technical and semantic service objectives.

## Performance and scale

- concurrent users, requests, jobs, or agents;
- input, context, output, and artifact size;
- batch completion window;
- tokens, compute, memory, storage, network, and accelerator needs;
- cold-start and model-loading limits;
- scaling rate and regional capacity;
- noisy-neighbor and tenant fairness.

Test representative peaks and degraded dependencies, not only average throughput.

## Cost and sustainability

- cost per successful task or business outcome;
- monthly budget, forecast variance, and anomaly threshold;
- maximum per-request and per-agent-run spend;
- cost allocation granularity;
- accelerator utilization and idle-capacity targets;
- energy or carbon reporting requirements where relevant;
- retention and storage-growth limits.

Cost controls should fail safely and should not route sensitive workloads to unapproved cheaper services.

## Operability

- observable versions, lineage, and decision points;
- dashboard and alert coverage;
- support hours, severity, and escalation;
- runbook completeness and exercise frequency;
- change lead time and rollback readiness;
- sampling and review capacity;
- inventory and evidence freshness.

## Portability and interoperability

- replaceable model, vector, feature, workflow, and tool contracts;
- export formats for data, prompts, evaluations, logs, and state;
- acceptable vendor-specific dependency;
- migration time and data-egress constraints;
- model or provider substitution quality threshold;
- protocol and schema version compatibility.

Portability requirements should be driven by credible exit scenarios, not abstract purity.

## Compliance and records

- required system, decision, consent, approval, and incident records;
- retention and legal-hold behavior;
- disclosure and content-marking behavior;
- data-subject or affected-person request handling;
- jurisdiction and sector overlays;
- evidence integrity, access, and production time.

Time-sensitive legal requirements should live in maintained overlays with an owner and reviewed-as-of date.
