# Third-party AI risk

Most enterprise AI systems depend on external models, hosted services, open-source packages, datasets, connectors, tools, or infrastructure. The enterprise remains accountable for how those dependencies are selected, integrated, authorized, monitored, and retired.

This chapter is vendor-neutral. Contract terms and regulatory duties require review by the appropriate legal, privacy, security, procurement, and risk owners.

## Dependency classes

| Dependency | Examples | Distinctive risks | Minimum evidence |
|---|---|---|---|
| Model API or AI SaaS | hosted inference, copilots, managed assistants | provider data use, silent model changes, regional processing, service concentration, limited observability | service and model identity, data terms, security review, evaluation results, change and incident commitments |
| Self-hosted third-party model | downloaded weights, commercial model package | malicious serialization, weight tampering, hidden behavior, license restrictions, patch ownership | origin, license, checksum or signature, isolated inspection, scan results, model evaluation, approved runtime |
| Open-source software | frameworks, runtimes, libraries, guardrails | dependency compromise, abandoned packages, unsafe defaults, arbitrary code execution | SBOM, provenance, vulnerability and maintenance status, pinned version, build and scan records |
| External dataset | licensed corpus, benchmark, synthetic or public data | unclear rights, poisoning, bias, personal data, deletion constraints, contamination | owner and source, permitted purpose, license, provenance, quality profile, security checks, retention and deletion rules |
| Connector, plugin, tool, or MCP server | search, email, browser, code, database, business action | excessive privilege, prompt injection, tool poisoning, confused deputy, arbitrary output, credential theft | tool contract, owner, scopes, identity flow, input and output validation, threat model, test results, kill path |
| Infrastructure or platform | cloud, accelerator, vector database, feature store | shared responsibility gaps, tenancy failure, residency, outage, capacity, key or weight exposure | architecture and responsibility model, regions, access controls, encryption, resilience evidence, exit plan |

Maintain these dependencies in the AI system inventory as first-class assets. A model name alone is not a sufficient inventory record.

## Risk process

### 1. Establish scope and criticality

For every dependency, record:

- business, technical, data, and supplier owners;
- intended purpose and prohibited uses;
- systems, data classes, users, tenants, and regions in scope;
- whether it can influence people, money, safety, rights, or a system of record;
- access, autonomy, scale, substitutability, and maximum failure impact;
- all downstream services and fourth parties known to be material;
- version, lifecycle status, renewal date, and reassessment triggers.

Apply enhanced review when a dependency has broad data access, action privileges, opaque changes, low substitutability, high concentration, or consequential outcomes.

### 2. Perform due diligence

Ask for evidence proportionate to criticality, not only a completed questionnaire.

#### Organization and service

- What exact entity provides and operates each component?
- Which responsibilities remain with the customer, provider, model producer, and subprocessor?
- What regions and facilities process, store, back up, or support the service?
- What security, privacy, AI governance, and vulnerability-disclosure programs operate in practice?
- What material incidents, enforcement actions, or unsupported lifecycle states affect the proposed use?

#### Data

- What prompts, files, retrieval content, outputs, feedback, and telemetry are retained?
- Are customer data or outputs used for training, evaluation, abuse monitoring, or product improvement?
- Can those uses be disabled contractually and technically?
- How are tenant isolation, encryption, access, residency, deletion, backups, and data-subject requests handled?
- What training and evaluation data provenance, quality, rights, and limitations can be disclosed?

#### Model and system

- Which model, version, safety configuration, context behavior, and service tier will be used?
- What model or system documentation describes intended use, limitations, evaluations, and known failure modes?
- How are weights, build artifacts, prompts, policies, indexes, and release packages protected from tampering?
- How are material model, policy, API, behavior, and deprecation changes communicated?
- What rollback, version pinning, export, or alternate-service options exist?

#### Secure development and supply chain

- Does the provider follow a secure development lifecycle appropriate to AI?
- Are code, model, dataset, build, and deployment dependencies inventoried and traceable?
- Are artifacts signed or otherwise integrity-checked?
- Are downloaded models inspected in an isolated environment and loaded with non-executable or safer formats where practical?
- Are SBOMs, AI bills of materials, provenance records, vulnerability notices, and patch timelines available?

#### Connectors, tools, and agents

- Does each invocation use a named user or workload identity rather than shared credentials?
- Are permissions least-privileged, resource-specific, time-bounded, and revocable?
- Can a model, tool description, retrieved document, memory item, or peer agent change the authorized action?
- Are arguments schema-validated and business invariants rechecked by the system of record?
- Are tool discovery, connector updates, delegation, memory, and inter-agent messages authenticated and audited?
- Can the dependency be isolated, rate-limited, suspended, and removed without disabling unrelated operations?

The [joint secure-AI development guidelines](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development), [AI data-security guidance](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/ai-data-security), [AI/ML supply-chain guidance](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/artificial-intelligence-and-machine-learning-supply-chain-risks-and-mitigations), and [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) provide authoritative inputs for this review.

### 3. Integrate defensively

Do not transfer a supplier assertion directly into trust.

- route access through approved identity, network, policy, and logging controls;
- minimize data before it crosses an organizational boundary;
- isolate and inspect imported models, packages, datasets, and tool responses;
- pin versions where possible and detect unapproved changes;
- treat model and tool output as untrusted input;
- authorize each tool action against the initiating identity, purpose, resource, and current policy;
- limit steps, time, tokens, spend, data volume, and actions;
- test tenant boundaries, prompt injection, poisoned retrieval, malformed tool output, dependency failure, and rollback;
- preserve a deterministic, human, or alternate-provider fallback where the business impact requires it.

For agentic services, apply the [joint Careful Adoption of Agentic AI Services guidance](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services). For MCP-based integrations, also assess the [NSA MCP security design considerations](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/).

For an imported skill, plugin, hook, helper, or MCP server, complete the
[agent extension security assessment](../worksheets/agent-extension-assessment.md).
Review the complete package, dynamic update behavior, tool schema and
description, requested authority, token audience, cross-server data flow, and
revocation path. Supplier curation or marketplace screening is not enterprise
admission.

## Contract outcomes

Contracts should make the shared-responsibility model testable. Address, as applicable:

Map supplier and downstream duties to the system's
[regulatory obligation register](../worksheets/regulatory-obligation-register.md).
A supplier term, questionnaire, or assurance report is an input; it does not
decide enterprise applicability or prove that the customer-side control
operates.

| Outcome | Contract considerations |
|---|---|
| Permitted use | approved purpose, users, data classes, regions, prohibited secondary use |
| Data control | ownership, training and improvement restrictions, retention, deletion, backups, export, data-subject support |
| Security | baseline controls, encryption, isolation, access, secure development, testing, vulnerability disclosure and remediation |
| Transparency | model and service identity, material limitations, subprocessors, locations, provenance and assurance evidence |
| Change control | advance notice for model, API, safety-policy, data-use, subprocessor, region, price, and deprecation changes |
| Incidents | definition, notification time, investigation cooperation, evidence access, containment, communications and lessons learned |
| Assurance | audit rights, independent reports, penetration or red-team summaries, remediation tracking, right to request evidence |
| Service continuity | availability and support objectives, quotas, capacity, recovery, backups, force-majeure handling |
| Portability and exit | export formats, transition assistance, deletion attestation, credential revocation, continued access during transition |
| Intellectual property | rights to inputs and outputs, training-data and component licensing, infringement allocation, open-source obligations |
| Regulatory cooperation | records, assessments, authority requests, notices, and role-specific support required by applicable law |

Do not accept a certification badge as complete evidence. Confirm its scope, covered service, assessor, period, exclusions, and relationship to the proposed architecture.

## Continuous assurance

Monitor both the dependency and its use:

- provider advisories, vulnerability notices, incidents, legal or ownership changes;
- service, model, policy, API, price, region, and subprocessor changes;
- quality, safety, security, drift, latency, availability, and cost against agreed thresholds;
- new privileges, data paths, tools, agents, or downstream dependencies;
- expiring licenses, attestations, exceptions, and end-of-support dates;
- concentration and correlated-failure exposure across the portfolio.

Material change should trigger regression evaluation and, where relevant, a new security, privacy, impact, legal, and architecture review. Record the production versions actually used; a provider's current marketing name is not adequate evidence.

## Continuity and exit

An exit plan is a tested architecture capability, not a procurement sentence.
Execute an actual exit through the
[transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md)
so supplier evidence, successor acceptance, data and credential disposition,
active work, billing, public or repository state, and observed readback share
one accountable boundary.

1. Identify an alternate model, service, deterministic workflow, or manual process for critical functions.
2. Maintain portable copies of organization-owned prompts, policies, schemas, evaluation sets, configuration, and approved source data.
3. Define export formats for fine-tuning assets, indexes, logs, feedback, and evidence where the organization has rights to them.
4. Run the same release evaluation against the alternate path and document unacceptable behavioral differences.
5. Exercise failover, provider suspension, credential revocation, routing changes, and degraded operation.
6. On exit, remove integrations and permissions, rotate secrets, stop data flows and jobs, obtain deletion evidence, and update inventories and downstream owners.
7. Preserve records required for audit, incident response, legal hold, or regulatory duties without retaining unnecessary sensitive content.

The [joint guidance for deploying AI systems securely](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/deploying-ai-systems-securely) recommends validating externally developed systems, protecting model artifacts, enforcing access controls, monitoring behavior, and preparing recovery. Use those outcomes as acceptance tests rather than relying on supplier promises.

## Decision record

The approval record should state:

- dependency and approved version or service scope;
- risk tier and criticality;
- evidence reviewed and evidence unavailable;
- required controls and contract conditions;
- residual-risk decision IDs, categories, results, exact supplier and use
  scopes, named category-bound authorities and authority bases, conditions,
  expiries, invalidation triggers, and supersession states;
- separate policy-exception decision IDs, authorities, scopes, conditions, and
  expiries;
- monitoring owner and reassessment date;
- continuity path and last exit-test result;
- conditions that automatically suspend approval.

The supplier-approval authority consumes the required current residual-risk
and exception records; it does not inherit or recreate their authority.
Supporting discipline inputs are not votes. Missing, stale, expired,
invalidated, out-of-category, out-of-scope, or ambiguously authorized
acceptance forces hold or rejection.
