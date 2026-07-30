# AI system lifecycle

AI delivery adds probabilistic behavior and data dependencies to ordinary software delivery. It should extend—not bypass—secure development and change management.

This page governs the AI product or system and its operating envelope from
discovery through retirement. It is the lifecycle backbone, not the workflow
for one repository change.

## Choose the delivery path

| Task | Primary guidance | Required record or evidence |
|---|---|---|
| Discover, design, build, validate, operate, or retire an AI product or system | This AI system lifecycle | [Use-case assessment](../worksheets/use-case-assessment.md) for every proposal; [risk and impact assessment](../worksheets/ai-risk-impact-assessment.md), [ADR](../worksheets/architecture-decision-record.md), [system card](../worksheets/system-card.md), [evaluation report](../worksheets/evaluation-plan-and-report.md), [production readiness review](../worksheets/production-readiness-review.md), and [transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md), as applicable |
| Produce an AI-assisted repository or infrastructure change | [Security-first AI-assisted development lifecycle](security-first-ai-dlc.md) as the control overlay, executed through the [skills-first AI-assisted change workflow](skills-first-ai-development.md) | [AI-assisted change evidence](../worksheets/ai-assisted-change-evidence.md), repository tests, review evidence, and an ADR or threat model when required |
| Admit or update a skill, plugin, hook, helper, or MCP server | [Agent extension supply-chain security](../security/agent-extension-supply-chain.md) before ordinary use | [Agent extension security assessment](../worksheets/agent-extension-assessment.md), immutable component record, one attributable approve / hold / reject decision bound to the exact package, scope, evidence, conditions, expiry, and revocation path |
| Approve a model deployment, service plan, route, or agent dispatch pattern | Apply [governed model routing and agent dispatch](../architecture/model-portfolio-and-routing.md) before the application or harness can select it; use the [dated candidate catalog](../architecture/model-and-provider-candidate-catalog.md) only as discovery input | [Model routing and agent dispatch plan](../worksheets/model-routing-and-agent-dispatch-plan.md), one attributable approve / hold / reject decision for the exact plan or deployment-record revisions, evaluation, price, scope, expiry, and route-grant conformance evidence |
| Decide whether a defined residual risk may be retained | Apply the [residual-risk decision contract](../governance/operating-model.md#residual-risk-decision-contract); keep required discipline inputs, exception authority, and the owning lifecycle gate distinct | [AI risk and impact assessment](../worksheets/ai-risk-impact-assessment.md), one category-bound, attributable Accept / Accept with conditions / Hold / Reject decision for each policy-reserved category, bound to the exact risk, system boundary, evidence, conditions, expiry, and invalidation triggers |
| Promote an approved release to an environment | [Code deployment and release](code-deployment.md) | Release manifest, trusted-build evidence, readiness decision, deployed-state readback, observation, and rollback record |
| Distribute a repository, site, model, data, prompt, extension, evaluation, media, or security artifact beyond an established access boundary | [Public release and external distribution](public-release-and-external-distribution.md) in addition to the applicable build and deployment path | [Public-release readiness record](../worksheets/public-release-readiness.md), exact sanitized distribution manifest, rights and security decisions, approval, destination readback, and withdrawal plan |
| Respond to an escaped defect, control failure, incident, or recurring problem | [Incident, problem, and corrective action](../operations/incident-problem-and-corrective-action.md) | [Incident and corrective-action record](../worksheets/incident-and-corrective-action-record.md), containment, root cause, corrective action, and effectiveness evidence |

The paths compose rather than compete:

- the **AI system lifecycle** governs the product and operating envelope;
- the **security-first AI-assisted development lifecycle** overlays every
  material AI-assisted engineering change;
- the **skills-first AI-assisted change workflow** organizes how that change
  is produced and evidenced;
- extension admission and model-route approval are prerequisite side gates
  whenever those dependencies change;
- deployment promotes the approved release;
- external distribution is a separate side gate for the exact outgoing
  artifact and does not replace deployment or coordinated vulnerability
  disclosure; and
- incident and corrective action feed escaped failures back into requirements,
  tests, controls, and lifecycle decisions.

The
[fictional procurement-evidence golden thread](../examples/worked-golden-thread.md)
shows the composed paths with stable synthetic record IDs. It illustrates how
evidence joins; it does not approve the example or replace any record.

## Discover

- name the outcome, owner, users, and non-AI alternative;
- map affected stakeholders and foreseeable misuse;
- define success, harm, cost, and stop metrics;
- classify initial impact, autonomy, data, and exposure;
- establish whether experimentation is permitted.

## Design

- model the end-to-end workflow and trust boundaries;
- choose the least autonomous viable pattern;
- identify authoritative sources and systems of record;
- define identity, authorization, data, and retention paths;
- create an evaluation plan before tuning;
- document fallback, escalation, and recourse.

## Build

- version code, prompts, models, datasets, indexes, policies, and tools;
- use isolated environments and synthetic or minimized data where possible;
- enforce model access through approved gateways;
- capture lineage and reproducible build metadata;
- automate unit, integration, security, and evaluation suites.

## Validate

- evaluate representative normal, edge, adversarial, and abstention cases;
- compare against a baseline, including the current human or deterministic process;
- test authorization and tenant boundaries end to end;
- exercise degraded dependencies, quotas, timeouts, and provider failure;
- verify human review with actual reviewers;
- obtain one category-bound, attributable decision from the named
  residual-risk authority for each acceptance required by policy, record
  required discipline inputs as inputs rather than votes, and keep any policy
  exception as a separate decision.

## Release

- name the repository, change, release, deployment, service, and incident
  owners;
- bind the approved source, code, infrastructure, model, data, prompt, policy,
  index, tool, workflow, configuration, evaluation, and recovery revisions in
  a release manifest;
- build enterprise-produced artifacts once in a trusted environment and
  promote the exact verified digest; record managed or mutable dependencies,
  sentinels, limitations, and fallback;
- use shadow, internal, canary, or limited-cohort rollout;
- pin immutable production revisions where the service supports them; otherwise record the mutable alias and limitation, monitor behavioral drift, and maintain a tested fallback;
- configure thresholds, alerts, rate limits, action budgets, and circuit breakers;
- confirm support, incident, rollback, and communications ownership;
- read back the actual deployed revisions, routes, policy, and migration state;
- record go, hold, abort, promotion, and rollback decisions plus the approved
  operating envelope.

## Operate and improve

- monitor business outcome, quality, safety, security, reliability, and cost;
- sample outcomes using privacy-preserving review;
- investigate distribution and behavior shifts;
- feed incidents, feedback, and appeals into evaluation sets;
- route material failures through the
  [incident, problem, and corrective-action](../operations/incident-problem-and-corrective-action.md)
  loop and verify preventive actions;
- reassess material changes;
- disposition unused versions, data, access, and infrastructure through the
  [transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md),
  preserving required records and separately approved shared dependencies.

## Artifact lineage

Separate request-level traceability from release-level provenance.

At an appropriate privacy level, a production event should identify:

- use case, release, tenant, and execution identifier;
- application and orchestration revision;
- model provider, route, and immutable revision when exposed;
- prompt, policy, index, tool, and workflow revisions needed to investigate behavior;
- authorization, approval, and consequential action results.

The release record should connect the deployed manifest to:

- source and build provenance;
- data, model, prompt, policy, index, tool, and evaluation versions;
- evaluation results, limitations, exceptions, and approval;
- rollback or forward-recovery targets.

Exact model revisions may be unavailable for mutable provider services, and retaining content may violate privacy or data-minimization requirements. Document those limitations and preserve the minimum metadata needed for accountability.
