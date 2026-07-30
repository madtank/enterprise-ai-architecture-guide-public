# Use-case assessment

Copy this template for each proposed AI use case.

## 1. Identity and ownership

- **Use-case name:**
- **Business owner:**
- **Product owner:**
- **Technical owner:**
- **Risk and assurance contacts:**
- **Status:** Idea / Experiment / Build / Production / Retired
- **Review date:**

## 2. Purpose and outcome

- What user or business problem is being solved?
- What decision, content, or action will the system influence?
- Why is AI preferable to a deterministic or non-technical alternative?
- What is the current baseline?
- What measurable outcome defines success?
- What stop metric would make the use case not worth continuing?

## 3. People and impact

- Who uses the system?
- Who is affected but may not use it?
- Could it affect access, employment, education, credit, health, safety, rights, or essential services?
- How will people know AI is involved?
- How can they correct, appeal, or opt out where appropriate?
- What happens if the system is wrong, unavailable, manipulated, or unfair?

## 4. Data

- What inputs, context, outputs, feedback, and telemetry are processed?
- What classifications, owners, permissions, consent, residency, and retention apply?
- Is personal, confidential, regulated, copyrighted, or export-controlled data involved?
- Will any provider retain data or use it to improve models?
- How are deletion and subject-rights requests propagated?
- Which potential legal entities, jurisdictions, source-specific actor roles,
  sectors, markets, and distribution channels must be screened in the
  [regulatory obligation register](regulatory-obligation-register.md)?

## 5. System behavior

- **Pattern:** Predictive / Generative / RAG / Human-approved action / Agent / Other
- What models and providers are proposed?
- What enterprise tools or systems of record can be accessed?
- What actions can the system take?
- What is the maximum autonomy?
- What human oversight is required?
- What fallback exists?

## 6. Initial classification

| Dimension | Assessment | Rationale |
|---|---|---|
| Impact | Low / Moderate / High / Severe | |
| Data sensitivity | Public / Internal / Confidential / Restricted | |
| Autonomy | Inform / Draft / Recommend / Approve / Act | |
| Exposure | Internal / Partner / Customer / Public | |
| Scale | | |
| Reversibility | High / Moderate / Low | |

- **Proposed tier:** 1 / 2 / 3 / 4 (prohibited)
- **Screening state:** Candidate / Hold / Rejected
- **Prohibition source / decision ID, if any:**
- **Novel or uncertain risks:**
- **Required reviewers:**

!!! danger "Tier 4 and prohibitions fail closed"
    If the proposed scope is Tier 4 or a clear legal, regulatory, contractual,
    license, or adopted-policy prohibition applies, only **Hold** or **Reject**
    is permitted. **Hold** allows reassessment only after an authorized change
    to the proposed scope or controlling rule; it does not authorize
    experiment, build, deployment, or release. Risk acceptance, conditions, or
    an exception cannot make the prohibited scope releasable.

## 7. Evidence plan

- Representative and critical evaluation scenarios:
- Quality and harm thresholds:
- Security and privacy tests:
- Human-factors validation:
- Production monitoring:
- Rollback and incident exercise:
- Residual-risk assessment record required / not required and rationale:
- Expected residual-risk categories and named decision authorities / authority
  bases, when required:

## 8. Decision

- **Use-case decision:** Proceed / Proceed with conditions / Hold / Reject
- **Tier 4 / prohibition disposition, if applicable:** Hold for authorized
  scope or controlling-rule change / Reject
- **Named use-case decision authority and authority basis:**
- **Linked residual-risk decision IDs, categories, results, exact scopes,
  conditions, and expiries, if required:**
- **Linked exception decision IDs, separate authorities, scopes, conditions,
  and expiries, if any:**
- **Required supporting inputs and dates; supporting rows are not votes:**
- **Next reassessment trigger or date:**

A **Proceed** or **Proceed with conditions** use-case decision does not itself
accept residual risk or authorize experiment, build, release, deployment,
operation, or publication. When adopted policy requires risk acceptance, link
a current decision for every required category, each from exactly one named
residual-risk decision authority using the
[residual-risk decision contract](../governance/operating-model.md#residual-risk-decision-contract).
Missing, ambiguous, expired, out-of-category, or out-of-scope risk acceptance
forces **Hold**.
