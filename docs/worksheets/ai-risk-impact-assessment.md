# AI risk and impact assessment

Use this assessment for systems that move beyond low-risk exploration. Tailor the depth to consequence, exposure, and uncertainty.

## Document control

- **System / use-case ID:**
- **Version and date:**
- **Assessment owner:**
- **Business, product, technical, and data owners:**
- **Assessors and independent reviewers:**
- **Lifecycle state:**
- **Jurisdictions and sector overlays:**
- **Next review date:**

## Purpose and alternatives

- What legitimate purpose and measurable outcome does the system serve?
- What decision, content, or action will it influence?
- What is the current workflow and baseline?
- What non-AI or less autonomous alternatives were considered?
- What uses are explicitly outside scope or prohibited?
- What evidence would cause the enterprise to hold or stop the system?

## System and role

- Does the enterprise develop, provide, deploy, operate, import, distribute, or only use the system?
- What models, data, providers, tools, and systems of record are involved?
- Is behavior predictive, generative, retrieval-based, agentic, multimodal, or combined?
- What is the maximum autonomy and consequence?
- What scale, duration, geography, and population are expected?
- What dependencies and downstream consumers exist?

## Affected stakeholders

For each stakeholder:

| Stakeholder | Benefit | Potential harm or burden | Vulnerability or power imbalance | Participation / evidence |
|---|---|---|---|---|
| | | | | |

Consider users, affected non-users, employees, customers, applicants, patients, children, communities, data subjects, reviewers, and downstream operators.

## Data and rights

- What source, training, validation, evaluation, retrieval, feedback, and telemetry data is used?
- What authority, consent, purpose, classification, residency, retention, and deletion rules apply?
- Could data or derived artifacts reveal sensitive attributes?
- Are there copyright, license, confidentiality, employment, or surveillance concerns?
- How are correction, access, deletion, objection, and opt-out requests handled?
- Can affected people understand and contest an outcome?

## Impact analysis

Assess each credible impact:

| Impact | Affected group | Severity | Likelihood | Scale / duration | Reversibility | Detectability | Existing controls |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Include:

- safety, health, rights, dignity, and freedom;
- fairness, discrimination, accessibility, and exclusion;
- privacy, surveillance, confidentiality, and autonomy;
- financial, employment, education, legal, and service access;
- manipulation, deception, misinformation, and impersonation;
- security, fraud, and abuse;
- workforce and professional-skill effects;
- environmental and societal effects;
- cumulative and interacting impacts.

## Misuse and failure

- How could a malicious user, insider, supplier, or compromised source misuse the system?
- How could the system be wrong, unavailable, stale, unfair, or over-trusted?
- What could prompt injection, poisoning, exfiltration, or excessive agency cause?
- How could scale or repeated low-level errors accumulate?
- Which failures are unacceptable even if rare?

## Controls and treatment

| Risk / impact | Prevent | Detect | Respond / recover | Owner | Evidence | Residual rating |
|---|---|---|---|---|---|---|
| | | | | | | |

Document why the treatment is proportionate and whether it creates new burdens.

## Human oversight and recourse

- What must a person review or approve?
- What information, authority, time, and training do reviewers receive?
- How is automation bias tested?
- How can an affected person correct data or challenge an outcome?
- Who performs independent review?
- What remedy is available?

## Evaluation plan

- representative, edge, subgroup, critical, and adversarial scenarios;
- quality, fairness, safety, security, privacy, reliability, and cost metrics;
- baselines, thresholds, statistical limitations, and zero-tolerance failures;
- human-factors, accessibility, and recourse tests;
- production monitoring and sampling;
- reviewers and independence.

## Classification and obligations

- **Internal risk tier:**
- **Data classification:**
- **Autonomy / consequence class:**
- **Regulatory obligation register version and applicable obligation IDs:**
- **Applicable regulatory or sector classifications and qualified decision:**
- **Open applicability uncertainties and hold conditions:**
- **Prohibition source / decision ID, if any:**
- **Required assurance and approvals:**
- **Inventory and record obligations:**
- **Next legal / regulatory review:**

Do not treat the internal tier as a legal classification.

!!! danger "Tier 4 and prohibitions fail closed"
    If the assessed scope is Tier 4 or a clear legal, regulatory, contractual,
    license, or adopted-policy prohibition applies, only **Hold** or **Reject**
    is permitted. **Hold** allows reassessment only after an authorized change
    to the proposed scope or controlling rule; it does not authorize
    experiment, build, deployment, or release. Risk acceptance, conditions, or
    an exception cannot make the prohibited scope releasable.

## Residual-risk decision

Use the
[residual-risk decision contract](../governance/operating-model.md#residual-risk-decision-contract).
Exactly one named residual-risk decision authority records each decision.
Required discipline inputs support that decision; supporting rows are not
votes, and a majority cannot create authority. The named authority may decide
only the risk categories that adopted policy explicitly reserves or delegates
to it. If the assessment crosses categories reserved to different
authorities, repeat this decision block for each category and require every
applicable record; do not combine them into a cross-category vote. Use
**Accept**, **Accept with conditions**, **Hold**, or **Reject**. This decision
retains only the decision-bound residual risk; it does not authorize an
experiment, build, release, deployment, operation, or publication.

- **Decision ID, version, and timestamp:**
- **Decision:** Accept / Accept with conditions / Hold / Reject
- **Risk category and reserved authority boundary:**
- **Decision-bound system, use case, purpose, revision, environment,
  population, exposure, and validity window:**
- **Risk statement, cause, consequence, and affected people:**
- **Residual likelihood, impact, and rating after treatment:**
- **Evidence cutoff, required input IDs, freshness, and material
  uncertainties:**
- **Named residual-risk decision authority and authority basis:** policy or
  delegation, applicable risk class / tier, scope, and validity
- **Tier 4 / prohibition disposition, if applicable:** Hold for authorized
  scope or controlling-rule change / Reject
- **Conditions, compensating controls, monitoring, and stop triggers:**
- **Remediation owner, due date, and closure evidence:**
- **Separate exception decision IDs, authorities, policy bases, scopes, and
  expiries, if any:**
- **Decision expiry and reassessment / invalidation triggers:**
- **Attributable decision-evidence URI and digest:**
- **Superseded and superseding decision IDs:**

| Required input role | Named principal | Input / finding and record ID | Blocking, nonblocking, or resolved | Time, freshness, and attributable evidence |
|---|---|---|---|---|
| Business / product | | | | |
| Engineering / data | | | | |
| Security / privacy | | | | |
| Responsible AI / risk | | | | |
| Legal / compliance, when required | | | | |
| Affected-domain or independent assurance, when required | | | | |

Missing, ambiguous, out-of-category, or expired authority; missing, stale, or
out-of-scope required input; or an unresolved non-waivable, blocking, or
conflicting required input forces **Hold** or **Reject**. The change-producing
AI or automation cannot accept risk. A policy-permitted exception is recorded
separately and does not create residual-risk or release authority. Preserve a
superseded decision and link the replacement; do not edit a decision-bound record to manufacture current acceptance.

## Assessment disposition

This roll-up reports whether the assessment package may be presented to the
named next lifecycle gate. It neither accepts an unlinked residual risk nor
authorizes that gate.

- **Assessment disposition ID, version, and timestamp:**
- **Required residual-risk decision set:** decision IDs, categories, exact
  scopes, results, validity states, expiries, and supersession states
- **Required exception decision set, if any:** decision IDs, exact scopes,
  results, authorities, expiries, and validity states
- **Assessment disposition:** Proceed / Proceed with conditions / Hold / Reject
- **Conditions, unresolved uncertainties, and stop triggers:**
- **Named next lifecycle gate and accountable gate owner:**
- **Disposition evidence URI and digest:**
- **Next review or reassessment trigger:**

**Proceed** authorizes only presentation of the current assessment package to
the named next gate. Any missing, invalidated, expired, superseded, held, or
rejected required decision forces the assessment disposition to **Hold** or
**Reject**. The gate owner makes the separate lifecycle decision.

## Stakeholder summary

Explain in plain language:

- what the system does;
- who may benefit or be harmed;
- the principal limitations;
- how people receive disclosure, correction, and recourse;
- who is accountable.
