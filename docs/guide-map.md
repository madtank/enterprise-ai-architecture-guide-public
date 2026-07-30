# Guide map and coverage review

Use this page to approve the shape of the guide before reviewing individual
chapters. The current navigation groups content by discipline; this map
reorders the same material into the path an enterprise initiative should
follow.

**Review sequence:** set direction → intake and govern → design → admit
dependencies → build → validate → release → operate and correct → transfer or
retire. Ownership, evidence, and decision records apply throughout.

Follow that sequence once in the
[fictional procurement-evidence golden thread](examples/worked-golden-thread.md).
Its synthetic records illustrate traceability; they are not operating
evidence, approval, or a reference implementation.

!!! note "How to read the coverage labels"
    **Direct** means dedicated guidance exists. **Distributed** means the
    requirement exists across several chapters and needs a clearer reader
    path or template. **Organization overlay** means the enterprise must add
    its own legal, regulatory, sector, identity, or policy requirements. A
    label is not a claim of certification, legal sufficiency, or effective
    implementation.

## High-level table of contents

| Guide area | What a reviewer must be able to answer | Start here |
|---|---|---|
| **1. Strategy, value, and adoption** | Why AI, why now, what is the non-AI baseline, who funds it, what value and stop metrics apply, and what risk is unacceptable? | [Strategy and value](executive/strategy-and-value.md), [adoption roadmap](adoption/adoption-roadmap.md), [use-case assessment](worksheets/use-case-assessment.md) |
| **2. Intake, governance, and human impact** | Who is accountable and affected, what is the risk tier, which source-specific obligations apply, what oversight and recourse apply, and who may accept residual risk? | [Operating model](governance/operating-model.md), [AI management system](governance/ai-management-system.md), [responsible AI and human factors](governance/responsible-ai-and-human-factors.md), [risk and impact assessment](worksheets/ai-risk-impact-assessment.md), [regulatory obligation register](worksheets/regulatory-obligation-register.md) |
| **3. System, data, security, and pattern design** | Where are authoritative state, trust and identity boundaries, data rights, human decisions, failure domains, and integration contracts? Which predictive, generative, retrieval, or agentic pattern is justified? | [Reference architecture](architecture/reference-architecture.md), [data architecture](architecture/data-architecture.md), [security architecture](security/security-architecture.md), [identity and permission matrix](worksheets/identity-and-permission-matrix.md), [agent execution and telemetry contract](worksheets/agent-execution-and-telemetry-contract.md), [deployment patterns](architecture/deployment-patterns.md), [agentic AI](architecture/agentic-ai.md), [predictive ML](delivery/predictive-ml.md) |
| **4. Provider, model, data, and extension admission** | Which exact suppliers, deployments, datasets, skills, tools, plugins, hooks, helpers, and MCP servers are approved for this use, authority, region, and operating envelope? | [Third-party risk](governance/third-party-risk.md), [governed model routing](architecture/model-portfolio-and-routing.md), [dated model and provider discovery catalog](architecture/model-and-provider-candidate-catalog.md), [extension supply-chain security](security/agent-extension-supply-chain.md), [platform engineering](platform/platform-engineering.md) |
| **5. AI system delivery and AI-assisted development** | Which lifecycle applies, what authority does AI assistance receive, who owns the repository, and what evidence must every change produce? | [AI system lifecycle](delivery/ai-lifecycle.md), [security-first AI-assisted development lifecycle](delivery/security-first-ai-dlc.md), [skills-first workflow](delivery/skills-first-ai-development.md), [MLOps, LLMOps, and AgentOps](delivery/mlops-llmops-agentops.md) |
| **6. Evaluation, assurance, and control evidence** | Which normal, edge, adversarial, accessibility, safety, security, routing, latency, and cost claims must pass? Which checks are deterministic, advisory, or independently approved? | [Evaluation strategy](delivery/evaluation-strategy.md), [control matrix](governance/control-matrix.md), [control catalog](governance/control-catalog.md), [evaluation plan and report](worksheets/evaluation-plan-and-report.md) |
| **7. Release, deployment, and external publication** | Is approved source bound to the promoted artifact, can deployed state be read back, and are stop, rollback, compensation, and external-release controls credible? | [Code deployment](delivery/code-deployment.md), [public release and external distribution](delivery/public-release-and-external-distribution.md), [production readiness review](worksheets/production-readiness-review.md), [public-release readiness record](worksheets/public-release-readiness.md), and [repository ownership and deployment plan](worksheets/repository-ownership-and-deployment-plan.md) |
| **8. Operations, resilience, incident response, and economics** | Can operators observe the whole system, limit harm, restore service, diagnose root cause, verify corrective action, and manage capacity, cost, and realized value? | [Agent execution and telemetry contract](worksheets/agent-execution-and-telemetry-contract.md), [production operations](operations/production-operations.md), [resilience](operations/resilience.md), [incident and CAPA](operations/incident-problem-and-corrective-action.md), [incident and corrective-action record](worksheets/incident-and-corrective-action-record.md), [FinOps and value](operations/finops-and-value.md) |
| **9. Transfer, decommissioning, and retirement** | How are suppliers exited and data, indexes, models, extensions, credentials, access, infrastructure, records, and persistent copies transferred or retired? | Complete the [transfer, decommissioning, and retirement record](worksheets/transfer-decommissioning-and-retirement.md); it joins the owning lifecycle, data, identity, agent-execution, supplier, repository, public-release, resilience, incident, and obligation records |
| **Evidence throughout: worked thread, worksheets, decisions, glossary, and sources** | Can an auditor reconstruct ownership, intent, applicability, obligations, architecture, threats, tests, exceptions, release, incidents, correction, and retirement from dated evidence? | The [worked golden thread](examples/worked-golden-thread.md), [worksheets](worksheets/system-card.md), [regulatory obligation register](worksheets/regulatory-obligation-register.md), [architecture decision record](worksheets/architecture-decision-record.md), [glossary](glossary.md), [framework alignment](governance/framework-alignment.md), and [authoritative references](references.md) support every stage |

!!! warning "A gate is not an authorization"
    The [public-release gate](delivery/public-release-and-external-distribution.md)
    and [readiness record](worksheets/public-release-readiness.md) now join
    exact-artifact sanitization, rights, security, disclosure, approval,
    readback, and withdrawal evidence. They do not authorize any artifact.
    For each candidate, external distribution remains blocked until
    accountable organization owners apply the gate to the frozen candidate and
    record the required approval or a policy-permitted, scoped, time-bounded
    exception.
    Publication-ready requires an explicit Pass or justified N/A for every
    prescribed R0–R5 row; Fail, Unknown, Stale, blank, or unjustified N/A
    forces Hold. An R6 exception does not rewrite that evidence or turn a held
    candidate into a publication-ready one.

!!! important "Independent assurance"
    Model graders, protected model-based verifiers, and AI-generated reviews
    can supply useful evidence, but they are advisory. The change-producing
    agent, model, or operator cannot independently approve its own material
    change or publication.

## Priority decision queue

| Recommendation | Outline decision | Why |
|---|---|---|
| **Apply before public release** | Use the integrated public-release gate and readiness record for the exact candidate. | The guide-level control gap is closed; artifact-specific authorization, rights, review, and channel decisions remain organization-owned. |
| **Use now** | Complete the reusable identity-and-permission matrix for each system and operating boundary. | The template now connects human and workload identities, resources, actions, delegation, credential lifecycle, break-glass, recertification, final authorization, negative tests, and observed-state reconciliation. |
| **Use now** | Complete the reusable regulatory obligation register for each system and operating boundary. | The template now separates sources, applicability, atomic duties, dates, control implementation, operating evidence, legal exclusions, policy exceptions, conflicts, event clocks, and reassessment without claiming legal sufficiency. |
| **Use now** | Follow the [fictional, non-sensitive worked golden thread](examples/worked-golden-thread.md). | It now connects intake, architecture, threat modeling, routing and extension admission, evaluation, readiness, deployment, incident/CAPA, and retirement evidence without asserting real control operation or approval. |
| **Use now** | Complete the reusable [agent execution and privacy-minimized telemetry contract](worksheets/agent-execution-and-telemetry-contract.md). | It now joins context, memory, durable state, root and child execution, route-grant references, typed tool outcomes, cancellation, ambiguity, event fields, minimization, integrity, retention, alert ownership, reconciliation, closure, and reassessment without treating telemetry as authority or permission to collect. |
| **Use now** | Complete the [transfer, decommissioning, and retirement record](worksheets/transfer-decommissioning-and-retirement.md) for each exit boundary. | The record now joins frozen inventory, continuity, successor acceptance, active-work reconciliation, disposition authority, revocation, supplier and public exit, observed-state readback, residual ownership, closure, and reopen criteria. |
| **Use now** | Review [durable routing and dispatch controls](architecture/model-portfolio-and-routing.md) separately from the [dated managed-cloud provider/model catalog](architecture/model-and-provider-candidate-catalog.md). | Stable, hosting-mode-neutral control design and fast-changing managed-service candidates now have distinct content boundaries and review cadences. |
| **Use now** | Select the applicable [cross-cutting operating path](index.md#cross-cutting-operating-paths). | The three paths now join people and adoption, responsible AI and recourse, predictive ML, FinOps and value, repository ownership and deployment, and incident/CAPA without duplicating their controls. |
| **Defer unless requested** | Cloud-specific and industry-specific implementation profiles. | Keep the core vendor-neutral; add appendices only when a concrete audience and maintenance owner exist. |

## Coverage exceptions to inspect

All major enterprise domains appear in the high-level table. These are the
areas where coverage is fragmented, organization-specific, or not yet backed
by a reusable artifact.

| Concern | Status | Review question |
|---|---|---|
| **Legal, regulatory, sector, records, and intellectual property** | **Direct worksheet + organization overlay** | Does the [regulatory obligation register](worksheets/regulatory-obligation-register.md) bind official sources, source-specific roles, applicability, atomic duties, event deadlines, controls, evidence, conflicts, exclusions, exceptions, and reassessment without implying legal sufficiency? |
| **Identity, authorization, credentials, and tenant isolation** | **Direct worksheet + organization overlay** | Does the [identity and permission matrix](worksheets/identity-and-permission-matrix.md) cover human and workload identities, resources, actions, delegation, non-widening permissions, credential lifecycle, break-glass, recertification, final-action authorization, and observed-state reconciliation? |
| **Privacy and data rights** | **Direct + organization overlay** | Are purpose, minimization, residency, cross-border flow, provider use, access, retention, correction, deletion, and telemetry treatment connected across source data, retrieval, memory, caches, traces, and evaluations? |
| **Agent harness execution and telemetry** | **Direct worksheet + organization overlay** | Does the [agent execution and telemetry contract](worksheets/agent-execution-and-telemetry-contract.md) reconcile one root run across policy, routing, children, tools, costs, authoritative outcomes, and privacy-minimized evidence without treating telemetry as authority or permission to collect? |
| **Public release and external distribution** | **Direct + organization overlay** | Does the exact frozen artifact pass the [fail-closed gate](delivery/public-release-and-external-distribution.md), and are rights and approval recorded for the actual audience and channel? |
| **Transfer and retirement** | **Direct worksheet + organization overlay** | Does the [transfer, decommissioning, and retirement record](worksheets/transfer-decommissioning-and-retirement.md) give every scoped supplier, artifact, copy, identity, credential, route, extension, record, public channel, and recovery dependency an authorized disposition, observed readback, and residual owner? |

## Agent architecture must remain explicit

The high-level outline should not hide the user's coordinator-and-worker
architecture thesis:

- the harness requests a capability profile; a central policy layer selects
  the exact allowlisted deployment and serving boundary, whether managed or
  enterprise-operated, and coordinators or workers cannot select models,
  hosting modes, or invocation paths directly;
- each child grant, context, tool set, data scope, deadline, fan-out, and
  budget is a strict subset of the parent grant and is reconciled to observed
  execution;
- a single capable-model baseline is compared with coordinator/worker variants
  on quality, latency, total task cost, and failure rate before dispatch is
  approved;
- skills define trigger, input, output, tool, stop, and evidence contracts;
  tools return typed results with explicit consequence classes, and MCP
  capability or schema changes and untrusted server results trigger control;
- privacy-minimized root-to-child telemetry identifies component versions,
  authorization, retries, fallbacks, outcomes, cost, and alert owners without
  assuming raw content may be retained;
- provider, model, serving boundary, artifact/runtime, price-plan, policy,
  skill, tool, or MCP changes trigger reassessment, common adapter conformance
  tests, and safe pause, revocation, migration, reconciliation, rollback, and
  retirement.

See [agentic AI architecture](architecture/agentic-ai.md),
[governed model routing and agent dispatch](architecture/model-portfolio-and-routing.md),
the
[dated model and provider candidate catalog](architecture/model-and-provider-candidate-catalog.md),
[model routing and agent dispatch plan](worksheets/model-routing-and-agent-dispatch-plan.md),
[identity and permission matrix](worksheets/identity-and-permission-matrix.md),
the
[agent execution and telemetry contract](worksheets/agent-execution-and-telemetry-contract.md),
[transfer, decommissioning, and retirement record](worksheets/transfer-decommissioning-and-retirement.md),
and [agent extension security](security/agent-extension-supply-chain.md).

## Standards boundary

The guide should integrate established work rather than rename it. The
[framework alignment](governance/framework-alignment.md) and
[authoritative references](references.md) pages own the dated mapping to NIST,
ISO/IEC, OWASP, MITRE ATLAS, SLSA, OpenSSF, cloud-provider architecture, and
applicable jurisdictional or sector sources. The guide does not replace those
sources, legal interpretation, enterprise policy, or an implementation-specific
threat model.

## A compact way to respond

```text
Keep:
Elevate:
Add:
Defer or remove:
Change the order:
```
