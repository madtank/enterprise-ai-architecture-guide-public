# Evaluation plan and report

## Document control

- **System and release:**
- **Evaluation owner:**
- **Business and risk owners:**
- **Independent reviewers:**
- **Evaluation environment and dates:**
- **Artifact manifest:**
- **Decision requested:**

## Intended use and claims

List each claim the release must support:

| Claim | Affected workflow / people | Metric | Threshold | Evidence |
|---|---|---|---|---|
| | | | | |

Include explicit non-claims and unsupported contexts.

## Baseline

- current human, rules-based, or previous-release process;
- baseline measurement period and uncertainty;
- comparison method;
- minimum improvement or non-inferiority requirement.

## Test assets

For each set:

| Set | Purpose | Source / owner | Size and slices | Holdout status | Contamination controls |
|---|---|---|---|---|---|
| | | | | | |

Cover representative, edge, subgroup, critical, insufficient-evidence, adversarial, dependency-failure, accessibility, and historical-incident cases.

## Metrics and thresholds

### Task and quality

- correctness, support, relevance, completeness;
- precision, recall, calibration, or ranking;
- retrieval recall and citation validity;
- valid action and verified postcondition;
- abstention and escalation;
- workflow completion and business outcome.

### Impact and human factors

- subgroup quality and fairness;
- harmful or prohibited outcome;
- accessibility;
- reviewer agreement, correction, override, time, and automation bias;
- complaint, appeal, and recourse behavior.

### Security, privacy, and abuse

- prompt-injection success;
- unauthorized retrieval or action;
- sensitive-data leakage;
- poisoning and tool misuse;
- denial-of-wallet and resource abuse.

### Operations and economics

- availability and latency;
- dependency and recovery behavior;
- token, compute, storage, human review, and unit cost.

Record pass, warning, stop, and zero-tolerance thresholds by critical slice.

## Methods

- deterministic assertions;
- expert or domain review;
- affected-user or human-factors study;
- calibrated model-based grading;
- simulation and tool test doubles;
- statistical test and confidence interval;
- red-team and abuse testing;
- shadow, canary, or controlled experiment.

Document evaluator qualification, blinding, inter-rater agreement, grader calibration, and unresolved disagreement.

## Results

| Metric / critical scenario | Baseline | Target | Result and interval | Slice findings | Decision |
|---|---:|---:|---:|---|---|
| | | | | | |

## Failures and analysis

- critical and repeated failure modes;
- root cause by data, model, retrieval, prompt, tool, workflow, human factors, or operations;
- mitigations attempted;
- new regressions or trade-offs;
- limits of the evaluation;
- test-set or evaluator drift concerns.

## Production evaluation

- online signals and sampling design;
- privacy and access controls;
- alert and stop thresholds;
- delayed outcome linkage;
- subgroup and critical-case monitoring;
- evaluator drift checks;
- feedback, complaint, and incident ingestion;
- owner and review cadence.

## Advisory release recommendation

- **Evaluation result:** Pass / Conditional pass / Fail / More evidence
  required
- separate policy-exception decision IDs, named authorities and authority
  bases, exact scopes, conditions, and expiries;
- linked current residual-risk decision IDs for every policy-reserved
  category, including results, exact scopes, named authorities and authority
  bases, conditions, validity states, expiries, invalidation triggers, and
  supersession;
- limitations and unresolved evidence;
- staged rollout and rollback triggers;
- accountable evaluation owner and supporting reviewers;
- next evaluation and material-change triggers.

The evaluation result is decision evidence, not residual-risk acceptance or
release authority. Evaluators and supporting reviewers do not inherit those
authorities, and their rows are not votes. A consuming gate fails closed when
a required exception or category-bound residual-risk decision is missing,
expired, invalidated, out of scope, or outside the named authority.
