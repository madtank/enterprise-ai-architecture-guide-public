# Glossary

**Abstention**
: A deliberate system response that declines to answer or act when evidence, confidence, authorization, or policy is insufficient.

**Action budget**
: A limit on the number, duration, cost, or consequence of actions a tool-using system may take.

**Agent**
: A system that uses a model to choose or sequence actions toward a goal within an environment.

**Agent skill**
: A versioned package of instructions and supporting resources that tells an agent when and how to perform a reusable workflow, including its tools, outputs, validation, and stop conditions.

**Agent extension**
: A skill, plugin, hook, helper, MCP server, tool bundle, agent package, or related component that changes an agent's instructions, capabilities, integrations, or runtime behavior.

**AI gateway**
: A controlled access layer for model services that may provide identity, routing, policy, quotas, logging, and vendor abstraction.

**AI management system**
: Interrelated organizational policies, objectives, processes, roles, and records for responsible development, provision, or use of AI systems.

**AI system inventory**
: The governed record of AI systems, owners, lifecycle state, intended use, risk classification, dependencies, and review status.

**AI system**
: The complete sociotechnical system, including people, workflow, applications, models, data, tools, controls, and operations.

**Attestation**
: An attributable, verifiable statement about an artifact or process, such as which source and build workflow produced a release artifact. An attestation does not by itself prove safety or correctness.

**Archive**
: A controlled retained artifact with defined owner, purpose, access, integrity, retention, review, and final disposition. Archived bytes may contain executable content, but the governed archive state must provide no startup, credential, execution, or production-authority path. An archive is not necessarily deleted, decommissioned, or safe to expose.

**Attack path**
: A modeled sequence from a defined attacker position to a target asset or impact using some combination of vulnerabilities, exposure, network reachability, identities, credentials, permissions, configurations, and trust relationships. Record evidence, confidence, and uncertainty for each material link; treat the path as a hypothesis until the links needed for the claimed traversal are validated. An attack path need not contain a weakness chain.

**Autonomous vulnerability research**
: An authorized, bounded AI-assisted process that generates attack hypotheses and may exercise software in an isolated environment to discover, reproduce, and assess known or unknown weaknesses. Analytical autonomy does not authorize testing external or production targets, disclosure, merge, release, risk acceptance, or changes to active controls.

**Capability profile**
: A stable, provider-neutral contract for the quality, context, modality, tools, data, authority, latency, cost, verification, and fallback required for a class of model or agent work.

**Content-complete**
: A bounded editorial state in which the declared scope is covered, required
  artifacts are usable, validation passes, and no known release-blocking or
  highest-severity content, source, consistency, or accessibility finding
  remains. It does not mean publication-ready, independently approved, or
  operationally effective.

**Code owner**
: A person or team responsible for technical review of defined repository paths or domains. Review routing does not by itself create branch enforcement or full repository accountability.

**Control plane**
: The services that distribute approved configuration, policy, lifecycle state, and routing intent to runtime components. It does not itself make organizational risk-acceptance decisions.

**Corrective action**
: Action that removes or controls a cause of an observed failure or
  nonconformity. It remains open until it is implemented and an effectiveness
  check against defined criteria passes; scheduling the check is not closure.

**Data drift**
: Change in the distribution or properties of input data.

**Data plane**
: The path that handles live user, model, retrieval, tool, and transaction traffic. In this guide, it is also called the runtime plane.

**Decommissioning**
: The controlled technical disablement and removal of a scoped capability, including its routes, identities, integrations, jobs, and infrastructure. It does not by itself prove data deletion, supplier exit, repository archival, or lifecycle closure.

**Development plane**
: The environments and services used to build, train, fine-tune, index, test, evaluate, and package AI artifacts.

**Deployment record**
: The attributable record of what artifact and configuration were deployed, to which environment, under which approval, with which observations and result.

**Evidence pack**
: A concise, reviewable index connecting a change's intent, ownership, decisions, validation, risk, provenance, release, and recovery evidence.

**Execution attempt**
: One bounded try within a root or child execution. Retries and fallbacks have distinct attempt identifiers but consume the original aggregate authority and budget rather than resetting them.

**Execution telemetry**
: Privacy-minimized structured events, traces, metrics, and audit references used to operate and reconstruct an execution. It is not identity, authorization, authoritative workflow state, or proof of a business effect.

**Evaluation**
: Repeatable measurement of an AI system’s quality, safety, security, performance, cost, and business fitness.

**Exploitability validation**
: A controlled, evidence-producing determination of whether a vulnerability candidate represents a security-property violation that is reachable and reproducible under stated attacker prerequisites and deployment conditions. The result is verified, rejected, or inconclusive and remains bound to the tested artifact and environment. Impact, severity, and business materiality are recorded separately.

**Forward recovery**
: Restoration by applying a new corrective change or compatible migration instead of returning to a previous artifact version.

**Feature store**
: A governed service for defining, producing, and serving reusable machine-learning features consistently across training and inference.

**Foundation model**
: A broadly trained model that can be adapted to multiple downstream tasks.

**Guardrail**
: A preventive or detective control applied to input, retrieved context, generated output, or action.

**Grounding**
: Supplying authoritative or task-relevant evidence to constrain or support an output.

**Governance-approved**
: A decision state in which the authorized owners and required qualified
  independent approver, or a policy-permitted human exception authority, have
  accepted one exact decision-bound candidate with recorded scope, conditions,
  and expiry where applicable. It is not proof of correctness or completion
  of publication readback.

**Independent assurance**
: Assessment performed with sufficient organizational and decision-making independence from the people who developed or operate the system.

**Inconclusive vulnerability validation**
: A protected validation attempt that lacks sufficient or consistent evidence to verify or reject a vulnerability candidate for the tested boundary. The candidate remains open, dependent decisions remain on Hold, and the attempt cannot be treated as approval or proof of absence.

**Inferential verification**
: An advisory judgment produced through reasoning, such as model-based review. It can identify concerns but does not replace deterministic evidence or an authorized human decision.

**Incident**
: An event that causes or threatens unacceptable service, security, safety, data, business, legal, or stakeholder impact and requires coordinated containment or restoration.

**Lineage**
: The traceable relationship between source data, transformations, artifacts, releases, and outcomes.

**Management plane**
: The services that observe, support, audit, meter, and operate AI systems, including telemetry, incident response, capacity, and cost management.

**Material change**
: A change that can alter intended purpose, affected people, risk, obligations, behavior, data handling, permissions, quality, or the approved operating envelope.

**Model registry**
: A controlled record of model artifacts, versions, lineage, evaluation, lifecycle state, and related evidence. A registry records approvals; authorized people and processes make them.

**Model portfolio**
: The small governed set of exact model deployments and logical capability profiles approved or being evaluated for defined enterprise uses.

**Model router**
: A service or policy that selects among approved models or endpoints based on task, quality, risk, data, region, availability, latency, or cost.

**Human-in-the-loop**
: A pattern in which a person must review or approve an outcome before it takes effect.

**Human-on-the-loop**
: A pattern in which a person supervises operation and can intervene without approving every action.

**Model card**
: Structured documentation of a model’s purpose, provenance, evaluation, limitations, and conditions of use.

**Model drift**
: Degradation or change in model behavior due to shifts in data, environment, users, or dependencies.

**Provenance**
: Evidence about the origin, custody, transformation, and authenticity of an artifact or datum.

**Publication-ready**
: A non-authorizing candidate state in which a content-complete, immutable
  distribution unit is bound to its manifest and digest and has passed the
  applicable R0–R5 public-release checks: every prescribed row has an explicit
  Pass or justified N/A result backed by current evidence, with no Fail,
  Unknown, Stale, blank, unresolved release-blocking, or highest-severity
  finding. It means safe and polished enough to present for exact-artifact
  governance review; it does not permit publication, satisfy R6 approval, or
  establish organizational reliance. An R6 exception preserves the
  underlying R0–R5 result and cannot make a held candidate publication-ready.

**Public withdrawal**
: A publisher-controlled action to deprecate, restrict, correct, or remove an externally distributed artifact where authorized. It cannot guarantee deletion of forks, downloads, caches, registries, mirrors, or recipient copies.

**Prompt injection**
: Instructions embedded in user or retrieved content that attempt to alter system behavior or misuse its authority.

**Protected verifier**
: A verifier whose identity, configuration, tests, and evidence path are protected from the change-producing agent. A model-based protected verifier is advisory and does not by itself provide independent assurance or authorize a material change.

**Problem**
: The underlying or systemic cause, or set of contributing conditions, behind one or more incidents, defects, nonconformities, or near misses.

**Release manifest**
: The immutable or tamper-evident record binding all compatible code, infrastructure, data, model, prompt, policy, index, tool, workflow, configuration, evaluation, and recovery revisions in a release.

**Rejected vulnerability candidate**
: A vulnerability candidate for which protected validation produced sufficient negative evidence for the exact tested artifact, environment, threat model, and prerequisites. Rejection is not proof of global absence; a material boundary or assumption change invalidates the result and returns the issue to candidate review.

**Remediation validation**
: Protected post-fix verification that the original reproduction no longer succeeds, required behavior remains intact, material bypasses or newly introduced weaknesses were assessed, and the evidence is bound to the corrected artifact or control revision. If promotion is required, bind that revision into a release candidate separately. Remediation validation does not establish deployed-state remediation, corrective-action effectiveness, incident closure, or corrective-action closure.

**Residual risk**
: Risk remaining after controls and treatment have been applied.

**Retirement**
: An accountable lifecycle decision ending ordinary operation or support for a defined system or capability and assigning its exit disposition and duties. The decision is not exit closure: applicable continuity, disposition, observed-state readback, watch, retained-duty, and residual-ownership gates must still pass. It does not automatically close incidents, CAPAs, records, contracts, or public copies.

**Repository owner**
: The accountable person or team for a repository's purpose, lifecycle, governance, maintainer appointments, continuity, and transfer or archival decisions.

**Root execution**
: One canonical, bounded end-to-end run to which every execution-scoped child, attempt, route, tool call, approval, transaction, reservation, event, and alert is causally linked. Platform events and multi-run incidents use their own affected-scope records rather than a fabricated root.

**Route grant**
: A short-lived, tamper-evident authorization artifact issued by the central routing policy service for one bounded route decision naming an exact primary deployment and any exact preauthorized fallbacks. It is not a credential for arbitrary reuse or the complete execution record.

**Risk acceptance**
: An attributable decision by exactly one named, category-bound authority designated under adopted policy to retain a defined residual risk for an exact scope and validity window. Required discipline inputs are not votes; a cross-category exposure needs every decision that policy reserves to a different authority. Acceptance cannot waive a prohibition or authorize a lifecycle transition, release, deployment, operation, or publication.

**Retrieval-augmented generation (RAG)**
: A pattern that retrieves external information and supplies it as context to a generative model.

**Session memory**
: Temporary information retained across interactions within a bounded user session.

**Serving boundary**
: The immutable, revisioned and digested decision-bound description of one model-serving path, including operating responsibility, deployment location, tenancy, connectivity, data path, artifact control, exact model and runtime identity, invocation target, final policy enforcement point, and observed state and meter. A label such as "managed," "cloud," "on-premises," or "self-hosted" is not sufficient by itself.

**Serving trusted computing base (TCB)**
: The minimum protected components and identities whose correct operation is required to admit and execute an approved model invocation. For enterprise-operated serving, the final invocation-admission PEP and the least-privileged serving runtime are separate principals, and exact-state enforcement requires an authenticated, freshness-bounded measurement from a protected source rather than runtime self-report alone.

**System of record**
: The authoritative service or repository for a defined business entity or transaction.

**Threat modeling**
: Structured, scope-bound analysis of assets and security objectives, data flows, trust boundaries, attacker capabilities and goals, abuse cases, assumptions, threats, and required controls. A threat model informs testing and risk decisions; it is not automatic approval.

**Tool**
: A capability exposed to an AI runtime through a defined, authorized contract.

**Transfer**
: A defined change in accountability, custody, operation, support, or asset scope that is complete only when a named successor accepts it and both sides reconcile authoritative records. It does not by itself establish legal title or data-transfer authority.

**Vector store**
: A service that stores and searches vector representations, often used for semantic retrieval. It does not replace source authorization or governance.

**Verified vulnerability**
: A vulnerability candidate for which reproducible or equivalent deterministic evidence demonstrates that a defined security property can be violated under stated conditions. Inferential or model judgment alone cannot assign this state; deterministic evidence produced through a protected execution path may support it. Verified does not mean independently assured, determine business acceptance, or authorize disclosure or production testing.

**Vulnerability candidate**
: A scanner, reviewer, agent, or analyst finding that indicates a potential security weakness but is not yet supported by reproducible or equivalent deterministic evidence of a security-property violation under stated conditions.

**Vulnerability correlation**
: Relating findings because they share a component, dependency, asset, cause, or risk context. Correlation neither orders the findings nor proves reachability, exploitability, material impact, or a weakness chain.

**Weakness chain**
: A causal sequence of two or more implementation weaknesses in which a consequence of one propagates as a cause or enabling condition of the next and the sequence ultimately enables a security failure. Each link and the composed sequence require reproducible or equivalent deterministic evidence. This guide prefers *weakness chain*; *software vulnerability chain* is treated as an informal synonym when every link is within software.

**Workflow state**
: Durable, authoritative progress and result data for a multi-step process, distinct from conversational context or model memory.
