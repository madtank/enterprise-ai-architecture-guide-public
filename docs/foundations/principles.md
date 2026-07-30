# Architecture principles

These principles are defaults. Deviations are allowed when documented with evidence and an accountable approver.

## 1. Begin with the decision or workflow

Define who acts, what changes, and how success is measured before selecting a model. Prefer deterministic software when it meets the need.

## 2. Match control strength to impact

Risk depends on the use context, not only the model. Data sensitivity, affected people, decision consequence, scale, reversibility, and autonomy determine the control tier.

## 3. Keep humans meaningfully accountable

Human review must have sufficient time, context, authority, and skill to change an outcome. A decorative approval button is not meaningful oversight.

## 4. Separate systems of engagement from systems of record

AI may propose, summarize, classify, or orchestrate. Authoritative state changes should pass through explicit business services with validation, authorization, audit, and idempotency.

## 5. Treat model output as untrusted input

Validate structure, permissions, policy, provenance, and business invariants before using output in downstream actions. Never grant authority merely because a model requested it.

## 6. Minimize and govern context

Retrieve only data required for the task. Enforce access at retrieval time, carry provenance, prevent cross-tenant leakage, and define retention for prompts, context, and outputs.

## 7. Evaluate the whole system

Model benchmarks are insufficient. Test retrieval, prompts, tools, workflow, guardrails, latency, cost, usability, and human behavior using representative scenarios.

## 8. Design for change

Models, prompts, indexes, policies, tools, and data all change. Version them independently, record lineage, use staged rollout, and define rollback compatibility.

## 9. Make the safe path the easy path

Provide reusable identity, model access, policy enforcement, evaluation, observability, and audit capabilities. Teams should not rebuild baseline controls.

## 10. Preserve exit options

Use stable internal contracts around models and vendors. Track data portability, model substitution, service limits, regional availability, and concentration risk.
