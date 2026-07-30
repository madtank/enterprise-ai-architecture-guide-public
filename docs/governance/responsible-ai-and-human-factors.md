# Responsible AI and human factors

Responsible AI concerns the effects of a system on people, organizations, and society. It must be designed into the workflow, data, evaluation, governance, and recourse—not added as an output filter.

The [OECD AI Principles](https://oecd.ai/en/principles) provide a widely used values baseline covering inclusive growth, human rights and democratic values, transparency, robustness, security and safety, and accountability.

## Impact assessment

Assess intended and unintended effects across:

- directly affected individuals and groups;
- users and human reviewers;
- people represented in training, retrieval, or evaluation data;
- employees and contractors whose work changes;
- non-users affected by downstream decisions;
- customers, communities, and the environment.

Consider severity, likelihood, scale, duration, reversibility, detectability, cumulative effects, and distribution. Low average harm can hide severe impact on a smaller group.

## Stakeholder participation

For consequential systems:

- identify affected groups early;
- involve domain, accessibility, frontline, and lived-experience expertise;
- test whether disclosures, explanations, and recourse are understandable;
- document disagreement and uncertainty;
- protect participants and sensitive feedback;
- report how input changed the design.

Consultation is not approval, and one representative cannot speak for every affected person.

## Fairness

Define fairness in the decision context:

- which groups and intersections matter;
- which benefits, errors, and burdens are distributed;
- whether historical labels encode unequal treatment;
- which metric reflects the harm;
- what trade-offs exist between metrics;
- what threshold or mitigation is acceptable;
- how performance will be monitored after deployment.

Technical parity metrics are evidence, not the entire fairness decision. Evaluate the surrounding eligibility, review, correction, and appeal process.

## Transparency and disclosure

People should receive information appropriate to their role:

- that AI is involved;
- the system’s purpose and limits;
- what data or sources inform the outcome;
- whether content is generated or manipulated;
- what a recommendation, score, or confidence means;
- how to correct data, challenge an outcome, or reach a person;
- who remains accountable.

Do not disclose system prompts, security controls, personal data, or proprietary details in ways that create new risk. Transparency should enable informed action.

## Explainability

Different audiences need different explanations:

| Audience | Need |
|---|---|
| Affected person | understandable reason, consequence, correction and recourse |
| Frontline reviewer | evidence, uncertainty, relevant policy, next action |
| Engineer | features, retrieval, versions, trace, error mode |
| Risk and audit | design rationale, evaluation, controls, approvals, operating evidence |
| Executive | outcome, material exposure, trends, decisions required |

For predictive systems, distinguish local decision explanation from global model behavior. For generative and agentic systems, provenance and action trace may be more useful than a post-hoc narrative of internal reasoning.

## Meaningful human oversight

Human oversight is meaningful only if the reviewer:

- has authority to change or stop the outcome;
- sees the relevant source evidence and uncertainty;
- has sufficient time and manageable volume;
- understands system limits and common failure modes;
- is not penalized for appropriate override;
- can escalate ambiguity;
- receives feedback on outcomes;
- is monitored for automation bias and fatigue.

Measure correction, override, escalation, review time, disagreement, backlog, and outcome—not merely that a button was clicked.

## Contestability and recourse

Define:

- who may challenge an outcome;
- how they learn that a challenge is possible;
- response and resolution time;
- who performs independent review;
- access to relevant evidence;
- correction of source and derived data;
- downstream propagation of correction;
- remedy when reversal is impossible;
- monitoring for repeated or disparate complaints.

Recourse should not require technical knowledge or access unavailable to the affected person.

## Accessibility and inclusion

Test:

- keyboard, screen-reader, contrast, and alternative-format support;
- language and literacy range;
- speech, hearing, vision, cognitive, and motor needs;
- timeout and interaction burden;
- error recovery and human assistance;
- whether generated content preserves accessibility metadata;
- performance differences across accents, dialects, devices, and environments.

An AI feature should not make an otherwise accessible service unusable.

## Automation bias and behavior

Test with realistic users:

- whether confident wording causes overreliance;
- whether uncertainty and citations improve decisions;
- whether reviewers verify selectively or not at all;
- whether targets or incentives suppress override;
- whether frequent false alerts create fatigue;
- whether users disclose more sensitive data conversationally;
- whether the system changes professional judgment or skill over time.

Use workflow design, training, sampling, and accountability to address human-system risk.

## Synthetic media

For generated or manipulated image, audio, video, and public-interest text, define:

- consent and permitted subjects;
- provenance and content credentials where appropriate;
- visible disclosure or labeling;
- impersonation and fraud defenses;
- special treatment of minors and intimate content;
- moderation, reporting, and takedown;
- retention and forensic evidence.

Jurisdictional transparency obligations should be maintained in the dated
[regulatory obligation register](../worksheets/regulatory-obligation-register.md).

## Evidence

The assurance record should include:

- impact assessment and affected stakeholders;
- stakeholder-participation summary;
- fairness choices and slice results;
- explanation and disclosure tests;
- accessibility results;
- human-oversight simulation;
- contestability and correction exercise;
- open harms and mitigations plus linked residual-risk decision IDs,
  categories, results, exact scopes, named authorities and authority bases,
  conditions, validity states, expiries, invalidation triggers, and
  supersession;
- production complaints, overrides, appeals, and outcomes.
