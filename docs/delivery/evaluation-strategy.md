# Evaluation strategy

Evaluation is the evidence that an AI system is fit for a particular purpose. It is a portfolio of tests, not one score.

## Evaluation layers

| Layer | Measures |
|---|---|
| Component | model behavior, retrieval relevance, classifier performance, guardrail accuracy |
| Integration | prompts, context, tools, schemas, authorization, state transitions |
| Scenario | end-to-end task success, harms, edge cases, misuse, human interaction |
| Production | business outcome, feedback, drift, incidents, cost, latency |

## Build the test set

Include:

- representative tasks weighted by real demand;
- high-impact cases even if rare;
- ambiguous and insufficient-information cases;
- known historical failures and user complaints;
- adversarial and abuse cases;
- multilingual, accessibility, and subgroup cases where relevant;
- dependency failure and stale-data conditions.

Protect test data from unintended training or prompt tuning. Maintain a sequestered holdout for release decisions.

## Metrics

Choose metrics based on the task:

- task completion and factual support;
- precision, recall, calibration, and abstention;
- retrieval recall, ranking quality, and citation correctness;
- harmful-output and policy-violation rates;
- action validity, authorization, and recovery;
- human correction, override, and escalation;
- latency, availability, token or compute use, and cost;
- business outcome and unintended downstream effects.

Aggregate scores can hide severe failures. Define slice-level and critical-case thresholds.

Where behavior is nondeterministic, run enough independent trials to estimate
the occurrence rate and uncertainty rather than accepting one favorable
sample. Combine outcome grading with trajectory and side-effect checks for
tool-using agents.

## Router and delegation evaluation

Treat routing and delegation as separately evaluated components. Test:

- task, risk, data, and authority classification;
- provider, region, model, preview, data, and tool allowlist enforcement;
- false low-tier and unnecessary high-tier routing;
- escalation recall for ambiguous and high-consequence cases;
- information loss, injection propagation, and instruction drift across
  handoffs;
- worker quality against a single capable-model baseline;
- verifier separation, authority limits, and seeded-defect detection;
- parallelism, retry, loop, cancellation, timeout, and budget behavior;
- safe abstention when no approved route satisfies policy;
- route stability across prompt, model, provider, price, and policy changes.

Measure both route accuracy and end-to-end outcome. A cheaper route must not
ship when it fails a critical quality, safety, authorization, privacy, or human
oversight threshold. Use offline and shadow evaluation before enabling a new
route, then progressive exposure with stop and rollback triggers.

## Release criteria

Each release should have:

- a named baseline;
- pass, warning, and stop thresholds;
- zero-tolerance critical failures where appropriate;
- reviewer agreement rules for subjective grading;
- documented statistical confidence or sample limitations;
- linked current residual-risk decision IDs for every policy-reserved
  category, including exact scope, named authority and authority basis,
  result, conditions, validity state, expiry, invalidation triggers, and
  supersession;
- a rollback trigger tied to production monitoring.

Evaluation produces decision evidence; it does not accept residual risk or
authorize release. Evaluation reviewers and owners are supporting inputs, not
votes. The release gate verifies the separate current category-bound decision
set.

## Model-based graders

Model graders can scale evaluation but are not ground truth. Calibrate them against qualified human review, measure disagreement and bias, pin their versions, protect them from prompt injection in evaluated content, and retain human review for consequential judgments.

## Online evaluation

Production evaluation should combine automated signals, structured user feedback, targeted sampling, outcome data, and incident analysis. Content review must follow privacy, employment, and data-minimization rules.

## Incident-derived regression

Every material defect, harmful outcome, complaint, control bypass, and near
miss should be assessed for inclusion in a protected regression suite. For a
fix:

1. reproduce the affected behavior or define a representative statistical
   replay;
2. demonstrate that the check fails on the affected revision;
3. verify that it passes on the proposed revision;
4. test related boundary, negative, adversarial, and subgroup cases;
5. preserve the case without leaking sensitive incident data;
6. monitor the relevant production signal after progressive rerelease.

Use the
[incident and corrective-action record](../worksheets/incident-and-corrective-action-record.md)
to connect the issue, fix, evaluation evidence, release, and effectiveness
check.
