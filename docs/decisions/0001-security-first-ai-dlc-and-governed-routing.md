# ADR 0001: Security-first AI-DLC and governed model routing

- **Status:** proposed; requires repository-owner and qualified independent
  security review
- **Date:** 2026-07-27
- **Accountable decision owner:** `@madtank`
- **Required reviewer disciplines:** enterprise architecture, security,
  platform engineering, and delivery governance; accepted reviewers are not
  yet assigned
- **Decision scope:** AI-assisted development, agent extensions, model
  portfolio, multi-agent routing, verification, release, and operations

## Context

Enterprise teams increasingly use coding agents, skills, tools, plugins, hooks,
MCP servers, cloud model catalogs, and multi-agent harnesses. Treating any one
of those as the development lifecycle creates gaps:

- instructions and extensions can carry executable supply-chain risk;
- an AI-authored review is not independent verification;
- model and worker selection can bypass data, region, authority, or cost policy;
- a cheap worker can increase total cost through coordination and retries;
- feedback can poison shared skills or policy if promoted automatically;
- a provider methodology can be mistaken for an enterprise standard.

The AWS Labs v2 repository describes AI-DLC Workflows 2.0 as a GA,
multi-harness methodology implementation, and its architecture specification
provides a useful skills-based Generate–Verify–Learn design. Neither is a
formal standard or a complete enterprise control baseline. Cloud harnesses can
configure different models for agents or invocations, but this capability does
not authorize arbitrary worker self-selection.

## Decision

Adopt three connected architectural outcomes:

1. Use the
   [security-first AI-assisted development lifecycle](../delivery/security-first-ai-dlc.md)
   as the
   organization-level lifecycle overlay. It defines mandatory G0–G6 gates for
   component admission, composition, controlled generation, independent
   verification, release, controlled learning, and operations/revocation.
2. Treat skills, plugins, hooks, MCP servers, helper code, and dynamic tool
   metadata as untrusted extension supply chain. Admit exact versions or
   approved mutable-service records through the
   [agent-extension security pipeline](../security/agent-extension-supply-chain.md)
   and enforce authority outside the model.
3. Use
   [stable capability profiles and central policy](../architecture/model-portfolio-and-routing.md)
   to resolve coordinator, worker, verifier, fallback, and escalation routes.
   Maintain a small dated
   [model and provider candidate catalog](../architecture/model-and-provider-candidate-catalog.md);
   approve exact supplier-operated, jointly managed, or enterprise-operated
   deployments only after task, security, data, serving-boundary, latency,
   reliability, capacity, and total-cost evidence. Enforce that decision
   through one exclusive final model-invocation policy enforcement point: a
   provider-egress gateway for a managed service, or a serving-admission
   gateway, scheduler, or runtime PEP for enterprise operation. Bind the grant
   and PEP check to the serving-boundary ID/revision/digest and authenticated
   freshness-bounded observed state. For enterprise operation, separate the
   PEP's invocation-admission identity from the decision-bound runtime identity
   that reads approved artifacts and uses approved accelerators. Its durable
   single-use `committed-to-invoke` lease transition orders live revocation
   against model invocation, and parallel child work is reserved from one
   root-execution budget. Permit disconnected invocation only with exact
   PEP/device holder binding, non-overlapping pre-reserved allocation,
   rollback-resistant local state, bounded revocation exposure, and
   reconciliation-before-refresh; otherwise mark it unsupported.

Generate, Verify, Learn, merge, and deploy remain distinct decisions even when
one product interface supports all of them. A component or model can narrow
enterprise authority but cannot broaden it.

## Consequences

### Benefits

- reusable skills and tools remain central to developer productivity;
- artifacts and evidence make AI-assisted pull requests inspectable without
  publishing unsafe raw sessions;
- deterministic controls and independent human gates prevent self-certification;
- a frontier coordinator can delegate economical work without bypassing
  provider, data, region, tool, or spend policy;
- component revocation, model replacement, and incident reconstruction become
  explicit platform capabilities;
- managed-service and enterprise-operated routes use one policy contract
  without pretending their credential, artifact, runtime, capacity, and
  operating duties are identical;
- disconnected serving can remain fail-closed against cloning and snapshot
  rollback, at the cost of platform-specific holder binding, protected local
  state, offline allocation, and delayed block-effect semantics;
- vendor methods can be adopted without inheriting their unstated security
  assumptions.

### Costs and trade-offs

- component admission, evaluation, and route telemetry require platform and
  security investment;
- a small model portfolio may delay access to new models;
- independent verification and human review add latency;
- sandboxing and central routing can reduce local flexibility;
- prices and lifecycle dates require continuous refresh;
- multi-agent dispatch may not outperform one capable model and must earn its
  added complexity through measurements.
- enterprise-operated serving transfers model/runtime integrity, patching,
  safety, capacity, hardware, reliability, physical security, and lifecycle
  duties to the organization.

## Rejected alternatives

### Allow each agent or worker to choose any available model

Rejected because it cannot reliably preserve provider, region, data, preview,
tool, budget, and approval constraints. Central policy resolves logical
profiles to exact deployments.

### Trust marketplace screening or an allowed-tools field

Rejected because discovery metadata is not an authorization boundary and
extensions may bundle scripts, hooks, servers, binaries, or mutable behavior.

### Use only static string matching for skill security

Rejected because attacks can emerge from code, instructions, dependencies,
repository context, or tool composition. Static analysis remains mandatory but
is combined with contextual review, threat modeling, sandbox execution,
runtime enforcement, and revocation.

### Publish complete agent transcripts as proof of thought

Rejected as a default because raw transcripts can expose secrets, private
paths, injected content, unrelated work, or hidden instructions. Use a concise,
human-confirmed evidence package and publish a sanitized trace only when safe,
useful, and approved.

### Treat AI-DLC v2 as a fixed external standard

Rejected because it is a flexible vendor design specification. This guide uses
its skills and Generate–Verify–Learn concepts as input under a separately
owned enterprise control overlay.

## Validation and review

Before this ADR becomes accepted:

- documentation validation and strict site build pass;
- security and platform owners verify product-specific claims and current
  sources;
- an independent qualified human reviews the security, governance, and
  deployment control changes;
- the repository owner accepts the architecture and limitations;
- any organizational adoption runs a low-consequence pilot and records
  accepted outcomes, defect escape, reviewer load, control bypass, recovery,
  latency, and total cost.

This ADR does not authorize public publication, model procurement, production
deployment, repository merge, or access changes.
