# Enterprise AI control catalog

This catalog translates architecture principles into stable control outcomes. Organizations should tailor applicability, implementation strength, evidence, and frequency by risk tier, jurisdiction, sector, and deployment model.

It is not a substitute for a licensed standard or an applicable legal requirement.

## Control record

For every adopted control, maintain:

- stable identifier and version;
- risk or obligation addressed;
- objective and applicability;
- accountable owner and operator;
- required implementation by risk tier;
- preventive, detective, and responsive mechanisms;
- evidence and test method;
- operating and review frequency;
- automation and monitoring;
- dependencies and inherited controls;
- exception authority, expiry, and compensating controls;
- mappings to adopted frameworks and obligations.

## Governance and accountability

| ID | Control objective | Minimum implementation | Example evidence |
|---|---|---|---|
| GOV-01 | Every AI system has accountable ownership | Name business, product, technical, data, and operations owners before production | Inventory record, role acceptance, support roster |
| GOV-02 | AI systems are completely inventoried | Record purpose, lifecycle, tier, dependencies, regions, owners, and review state | Inventory export, discovery reconciliation |
| GOV-03 | Risk and impact are assessed in context | Assess affected people, data, autonomy, scale, reversibility, misuse, and residual risk | Approved risk and impact assessment |
| GOV-04 | Applicable obligations are identified and maintained | Maintain dated legal, regulatory, contractual, and policy overlays by source-specific actor role | [Regulatory obligation register](../worksheets/regulatory-obligation-register.md), legal review, source and change logs |
| GOV-05 | Decision rights and segregation are proportionate | Separate development, validation, deployment, risk acceptance, and independent assurance as required | RACI, workflow approvals, [identity and permission matrix](../worksheets/identity-and-permission-matrix.md) |
| GOV-06 | Exceptions are explicit, separate, and temporary | Bind the exact unmet internal control and scope to a separate decision ID, one named policy-designated exception authority and adopted-policy basis, a non-waivable screen, compensating controls, monitoring, stop trigger, remediation owner, expiry, invalidation, and supersession; keep category-bound residual-risk and lifecycle or release decisions separate | Exception register, decision evidence, expiry alert, closure proof |
| GOV-07 | Competence and AI literacy match responsibility | Define and assess role-specific knowledge and practical capability | Training and assessment record, exercise result |
| GOV-08 | Leadership reviews effectiveness and improvement | Review outcomes, risks, incidents, audit, suppliers, cost, and corrective action | Management-review minutes and decisions |
| GOV-09 | Production-affecting repositories have accepted ownership and continuity | Name the repository owner, maintainers, code owners, release, deployment, service, incident, and backup responsibilities; review access and succession | Repository register, ownership acceptance, access review, succession exercise |

## Data and knowledge

| ID | Control objective | Minimum implementation | Example evidence |
|---|---|---|---|
| DAT-01 | Data use has authority and a bounded purpose | Approve owners, permitted use, populations, regions, and restrictions | Data contract, purpose approval |
| DAT-02 | Only necessary data is processed | Minimize fields, context, retention, and trace content before provider or model access | Data-flow review, minimization test |
| DAT-03 | Data and derived artifacts are traceable | Record source, transformations, versions, owners, and deployed dependencies | Lineage graph, release manifest |
| DAT-04 | Data quality is defined and monitored | Set requirements for accuracy, completeness, representativeness, freshness, labels, and drift | Data-quality report, alerts, remediation |
| DAT-05 | Source authorization propagates to derived stores | Enforce tenant and resource permissions at retrieval and feature access time | ACL tests, retrieval traces |
| DAT-06 | Correction, retention, and deletion propagate | Update or remove source, cache, index, feature, memory, trace, and feedback assets | Deletion exercise, retention configuration |
| DAT-07 | Poisoning and integrity risks are controlled | Protect ingestion, source trust, change review, anomaly detection, and rollback | Integrity checks, source review, poisoning tests |
| DAT-08 | Rights and licenses are known | Record copyright, license, consent, confidentiality, and downstream-use constraints | Rights register, dataset or model card |

## Security and privacy

| ID | Control objective | Minimum implementation | Example evidence |
|---|---|---|---|
| SEC-01 | Every request and action has authenticated identity | Carry user, workload, tenant, and delegated identity separately | [Identity and permission matrix](../worksheets/identity-and-permission-matrix.md), identity-flow test, access logs |
| SEC-02 | Authorization is enforced at every resource boundary | Reauthorize retrieval, model use, tools, and system-of-record writes | [Identity and permission matrix](../worksheets/identity-and-permission-matrix.md), negative authorization tests |
| SEC-03 | Workloads and tenants are isolated | Separate environments; constrain network, storage, compute, cache, and memory by risk | Architecture, isolation tests |
| SEC-04 | Secrets and keys remain outside model context | Use workload identity or approved secret management and short-lived credentials | Secret scan, credential inventory |
| SEC-05 | Sensitive content is protected throughout the path | Apply classification, encryption, DLP, redaction, egress, retention, and access controls | DLP tests, key policy, telemetry review |
| SEC-06 | Tool side effects are bounded | Use typed contracts, resource authorization, validation, idempotency, approval, and budgets | Tool specification, replay and abuse tests |
| SEC-07 | AI and software supply chains are trustworthy | Track provenance, licenses, dependencies, integrity, vulnerabilities, and artifact promotion | SBOM/AIBOM, signatures, scan results |
| SEC-08 | AI-specific threats are modeled and tested | Cover injection, poisoning, leakage, excessive agency, evasion, supply chain, and cost abuse | Threat model, red-team report |
| SEC-09 | Vulnerabilities can be reported and remediated | Define disclosure, triage, severity, patch, containment, and customer notification | SECURITY policy, vulnerability records |
| SEC-10 | Agent extensions are admitted as untrusted supply-chain components | Review the full skill, plugin, hook, helper, MCP, tool-schema, startup, binary, and dependency surface; pin versions where exposed and record mutable services; inspect statically and dynamically; approve scope, expiry, and revocation | Extension assessment, authority diff, scan and sandbox results, approved digest or mutable-service record |
| SEC-11 | Agent capability is contained outside model-controlled metadata | Enforce deny-by-default data, filesystem, network, credential, tool, resource, delegation, and side-effect policy; authorize each consequential call | Runtime-policy digest, negative tests, tool decisions, sandbox and egress evidence |

## Delivery and evaluation

| ID | Control objective | Minimum implementation | Example evidence |
|---|---|---|---|
| DEV-01 | Production artifacts are versioned and reproducible | Use immutable revisions where possible and document mutable-service limits | Release manifest, build provenance |
| DEV-02 | Evaluation represents the intended context | Test representative, critical, subgroup, edge, adversarial, and failure cases | Evaluation plan, test-set profile |
| DEV-03 | Releases meet explicit acceptance thresholds | Define baseline, pass/warn/stop thresholds, critical failures, and approver | Evaluation report, approval |
| DEV-04 | Human oversight works in practice | Test actual reviewers for authority, information, time, bias, override, and escalation | Human-factors study, simulation |
| DEV-05 | Changes are classified by impact | Reassess behavioral, data, permission, supplier, autonomy, and obligation changes | Change assessment, regression results |
| DEV-06 | Delivery pipelines protect integrity | Use review, isolated build identities, scanning, evidence gates, and controlled promotion | Pipeline config, attestations |
| DEV-07 | Test assets and automated graders are governed | Protect holdouts, detect contamination, calibrate graders, and track evaluator drift | Dataset card, agreement results |
| DEV-08 | AI-assisted changes preserve accountable intent and evidence | Record the human owner, issue and acceptance criteria, material skills and tools, sanitized decision evidence, exact validation, limitations, and recovery; require human understanding | Change evidence pack, PR, human confirmation |
| DEV-09 | Repository changes use a protected and independently reviewed path | Require PRs, relevant code-owner review, trusted checks, protected policy and workflow files, and separation between change production and approval | Ruleset export, CODEOWNERS, review and check history |
| DEV-10 | Deployments promote an approved and traceable release unit | Make the release manifest and decision tamper-evident; build once and promote by digest for enterprise-built artifacts; record mutable dependencies, sentinels, fallback, and limitations; verify provenance and actual deployed state | Release manifest, verified attestation where applicable, mutable-dependency record, deployment readback |
| DEV-11 | AI generation, verification, and learning are separated and bounded | Isolate construction from protected verification; label deterministic and inferential evidence; cap self-correction; quarantine learning candidates until new-version approval | Workflow manifest, verifier configuration, iteration limits, escalation record, learning-candidate decision |
| DEV-12 | External distribution uses an exact-artifact, fail-closed gate | Freeze and sanitize the outgoing manifest; resolve rights, privacy, security, vulnerability, dual-use, claims, accessibility, and channel duties; require independent approval or an explicitly governed exception; read back the destination; prepare correction and withdrawal | Public-release readiness record, artifact digest, scrub and rights evidence, approval or exception, destination readback, withdrawal exercise |

## Operations and resilience

| ID | Control objective | Minimum implementation | Example evidence |
|---|---|---|---|
| OPS-01 | Outcome and technical behavior are observable | Correlate root and child execution, release, model route, authority, data, tool, authoritative outcome, quality, security, reliability, and total-cost signals without assuming raw content collection is permitted | [Agent execution and telemetry contract](../worksheets/agent-execution-and-telemetry-contract.md), completeness reconciliation, dashboards, minimized trace samples |
| OPS-02 | Production operates within defined objectives | Set service, quality, safety, freshness, cost, RTO, and RPO thresholds | SLO record, error and quality budgets |
| OPS-03 | Failure is contained | Enforce time, token, step, spend, action, retry, and concurrency budgets plus circuit breakers | Runtime policy, fault-injection results |
| OPS-04 | Fallback and recovery are safe | Test fallback, rollback, compensation, index rebuild, and provider or region failure | Exercise report, recovery timing |
| OPS-05 | AI incidents are detected and managed | Define severity, containment, evidence, notification, correction, and learning | Incident plan and records |
| OPS-06 | Cost is attributable and bounded | Allocate usage, forecast, alert anomalies, and enforce budgets without bypassing safety | Cost dashboard, budget tests |
| OPS-07 | Material change triggers reassessment | Monitor provider, model, data, behavior, tools, policy, region, and legal changes | Change alerts, reassessment log |
| OPS-08 | Transfer and retirement remove scoped capability and intentionally disposition retained exposure | Reconcile active work; transfer or remove scoped routes, jobs, credentials, permissions, indexes, data, suppliers, repositories, and dependencies under approved retention, hold, shared-asset, continuity, and successor decisions; read back actual state | [Transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md), successor acceptance, revocation and disposition proof, residual register |
| OPS-09 | Releases use bounded exposure and verified promotion decisions | Use staged rollout, baseline comparison, automatic stop conditions, named go/hold/abort authority, and post-deployment readback | Canary record, health comparison, promotion decisions |
| OPS-10 | Issues produce verified fixes and systemic improvement | Join incident containment, reproduction, independent fix verification, progressive rerelease, corrective action, and effectiveness testing | Incident record, pre/post regression evidence, corrective-action closure |
| OPS-11 | Dynamic agent components can be detected, suspended, and revoked | Reconcile deployed skills, tools, schemas, MCP servers, models, routes, permissions, and prices with approved state; alert on change and exercise kill, rotate, fallback, and recovery | Inventory diff, change alert, revocation and credential-rotation exercise, fallback result |

## People and responsible use

| ID | Control objective | Minimum implementation | Example evidence |
|---|---|---|---|
| HUM-01 | People understand AI involvement and limits | Provide role-appropriate disclosure, provenance, uncertainty, and accountability | UX test, disclosure copy |
| HUM-02 | Affected people can correct and contest | Provide accessible correction, appeal, independent review, and remedy | Recourse exercise, resolution metrics |
| HUM-03 | Harm and fairness are evaluated contextually | Define affected groups, harms, fairness rationale, metrics, and mitigations | Impact assessment, slice results |
| HUM-04 | Services remain accessible and inclusive | Test interaction, output, language, assistive technology, and support | Accessibility report |
| HUM-05 | Automation bias and workload are controlled | Measure reviewer reliance, correction, fatigue, incentives, and capacity | User study, review-queue metrics |

## Supplier and concentration

| ID | Control objective | Minimum implementation | Example evidence |
|---|---|---|---|
| SUP-01 | Suppliers and components receive risk-based due diligence | Review data, security, quality, IP, change, operations, and role allocation | Supplier assessment, approval |
| SUP-02 | Contracts support the required control outcomes | Bind data use, incident, change, evidence, service, IP, regulatory, and exit terms | Executed terms, deviation approval |
| SUP-03 | External change is detected and validated | Monitor model, policy, API, price, subprocessor, region, and lifecycle changes | Notices, regression evaluation |
| SUP-04 | Concentration and exit are managed | Inventory correlated dependencies and test alternate or degraded paths | Concentration report, exit exercise |

## Testing control effectiveness

Test three levels:

1. **Design effectiveness:** Would the control address the stated risk in the actual architecture?
2. **Implementation effectiveness:** Is it present on every relevant production path and resistant to bypass?
3. **Operating effectiveness:** Did it work over the review period, including exceptions and failures?

Automated evidence should carry system, release, control, time, and integrity metadata. Failed evidence should open an owned action or block the relevant decision.

## Tailoring

- Tier 1 normally uses baseline controls with evidence generated by paved-road services.
- Tier 2 adds domain evaluation, stronger operating monitoring, and enhanced security or human-impact treatment.
- Tier 3 requires deeper impact and threat assessment, enhanced controls, independent assurance where appropriate, and more frequent review.
- Tier 4 is prohibited and cannot be made releasable by checking more controls.

Document every tailoring decision. A control may be not applicable only when the architecture makes the risk absent and the rationale is reviewed.
