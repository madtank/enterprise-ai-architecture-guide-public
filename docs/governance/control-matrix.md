# Risk tiers and control matrix

Risk tiering should be an organizational policy decision. This example provides a practical starting point, not a legal classification.

Risk tier does not determine whether a legal, regulatory, contractual,
license, or adopted policy obligation applies. Record that separate decision
in the
[regulatory obligation register](../worksheets/regulatory-obligation-register.md).

## Example tiers

| Tier | Description | Examples |
|---|---|---|
| 1 — Assistive | Low-impact and reversible; an informed user remains responsible | brainstorming with approved data, formatting, isolated code suggestions |
| 2 — Operational | Influences internal work or customer content; errors are normally recoverable | knowledge assistant, ticket classification, reviewed draft communication |
| 3 — Consequential | Can materially affect people, money, access, safety, rights, or regulated activity | employment support, financial recommendation, clinical decision support |
| 4 — Prohibited | Prohibited by applicable law or enterprise policy; it may not be developed or deployed | unlawful discrimination, prohibited manipulation, disallowed biometric or surveillance use |

Examples are contextual, not inherently assigned to a tier. A drafting or brainstorming tool may be Tier 3 if it uses highly sensitive data, creates high-consequence content, operates at extreme scale, or affects a consequential workflow.

**Hold / not yet approved** is a decision status, not a risk tier. A use case that the enterprise cannot currently support retains its inherent Tier 1–3 classification and remains on hold until required capability and evidence exist.

## Minimum control outcomes

Legend: **B** baseline, **E** enhanced, **I** independent assurance, **—** not permitted.

| Control outcome | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|:---:|:---:|:---:|:---:|
| Named business and technical owners | B | B | B | — |
| Repository, release, deployment, and incident ownership | B | B | E | — |
| Inventory and system documentation | B | B | B | — |
| Approved data purpose and retention | B | B | E | — |
| Security and privacy review | B | B | E | — |
| Representative task evaluation | B | E | E | — |
| Harm, bias, and accessibility evaluation | As relevant | E | E + I | — |
| Human oversight and recourse | As relevant | B | E | — |
| Output or action traceability | B | E | E | — |
| AI-assisted change evidence and human understanding | B | E | E + I | — |
| Skill, plugin, hook, MCP, and tool admission and revocation | B | E | E + I | — |
| Governed model route, delegation, and total-cost controls | As relevant | E | E + I | — |
| Protected change path and trusted required checks | B | E | E + I | — |
| Staged rollout and rollback | B | E | E | — |
| Continuous quality and drift monitoring | As relevant | B | E | — |
| Adversarial and abuse testing | As relevant | E | E + I | — |
| Supplier and concentration assessment | B | B | E | — |
| Periodic reassessment | Annual and on material change | Semiannual and on material change | Risk-based, at least quarterly and on material change | — |

## Control evidence

A control is not complete because a policy mentions it. Evidence should demonstrate:

- **design:** the control addresses a defined risk;
- **implementation:** the control exists in the deployed path;
- **operation:** it worked over a representative period;
- **exception handling:** failures and waivers are visible and time-bounded;
- **ownership:** a named role reviews the evidence and acts.

Examples include evaluation reports, access decisions, deployment records, approval history, red-team findings, runtime traces, incident tickets, rollback exercises, and user-recourse metrics.

## Risk acceptance

Every exception must identify the unmet requirement, exposure, compensating
controls, accountable exception authority, expiration date, and remediation
owner. Expired exceptions block the affected activity. Escalation alone does
not extend authority; continuation requires a fresh attributable decision.

Risk acceptance applies only to residual risk within the authority granted by
the controlling source and adopted policy. A Tier 4 classification or a clear
legal, regulatory, contractual, license, or adopted-policy prohibition permits
only **Hold** or **Reject** for the prohibited scope. **Hold** allows
reassessment only after an authorized change to the proposed scope or
controlling rule; it does not authorize experiment, build, deployment, or
release. More controls, conditions, an exception, or residual-risk acceptance
cannot make the prohibited scope releasable.

Each accepted risk must link one named, category-bound decision authority and
authority basis, exact scope and evidence, required discipline inputs,
conditions, stop triggers, expiry, invalidation triggers, and supersession.
Supporting inputs are not votes. Unknown, stale, blank, conflicting, or
unbound evidence; unresolved applicability; missing required input; an input
that records a non-waivable or blocking condition; or expired, widened,
superseded, unowned, out-of-category, or ambiguously authorized acceptance is
not exception-eligible and forces **Hold** or **Reject**.
