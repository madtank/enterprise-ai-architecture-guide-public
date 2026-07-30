# Framework alignment

This guide uses authoritative standards, regulatory sources, and security guidance as inputs. It does not replace legal advice, a licensed standard, a conformity assessment, or an organization's own risk decisions.

**Source register checked:** 2026-07-28

## How to interpret the sources

| Source type | Meaning for this guide |
|---|---|
| Law or regulation | Binding only when its scope, jurisdiction, actor role, and application date cover the organization or system. Legal counsel should confirm applicability. |
| Normative standard | Contains requirements or specifications in the published standard. Conformance cannot be inferred from this guide. ISO standards generally require access to the licensed full text. |
| Guidance standard or technical report | Provides structured guidance without necessarily defining certifiable requirements. |
| Government framework or guidance | Authoritative and usually voluntary unless adopted through law, regulation, contract, or organizational policy. |
| Community framework or threat knowledge base | Practical, frequently updated input for controls and tests. It is not law and should be version-pinned when used as assurance evidence. |

Use `aligned with` only when a documented mapping exists. Use `conforms to`, `complies with`, or `certified to` only when the applicable requirements and assessment basis have been established by qualified owners.

## Dated source register

| Source | Status on check date | Primary use in this guide |
|---|---|---|
| [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) | Voluntary framework, January 2023; NIST states that version 1.0 is being revised | Common risk vocabulary and the Govern, Map, Measure, and Manage outcomes |
| [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) | Voluntary implementation suggestions based on AI RMF 1.0 | Candidate actions and evidence practices; not a universal checklist |
| [NIST Generative AI Profile, AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) | Final, July 2024 | Risks and actions specific to generative AI |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Tailorable U.S. Government control catalog; current minor release 5.2.0 on the check date | Security and privacy control selection, implementation, and assurance inputs; not an automatic baseline |
| [NIST SP 800-63-4](https://csrc.nist.gov/pubs/sp/800/63/4/final) | Final, July 2025; scoped to identity proofing, authentication, and federation of people interacting with government systems | Human digital-identity assurance inputs; not workload identity or system authorization policy |
| [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) and [SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final) | Final, August 2020 and September 2023 | Resource-focused zero-trust architecture and granular application or service identity in cloud-native environments |
| [NIST Privacy Framework 1.0](https://www.nist.gov/publications/nist-privacy-framework-tool-improving-privacy-through-enterprise-risk-management) | Final voluntary framework, January 2020; version 1.1 remained an Initial Public Draft on the check date | Enterprise privacy-risk outcomes; not a legal determination |
| [EU General Data Protection Regulation, Regulation 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Binding EU regulation that has applied since May 2018 when its fact-specific scope is met | Source-specific controller, processor, data-subject, processing, rights, security, transfer, and accountability duties; AI or framework alignment does not establish compliance |
| [NIST SP 800-188](https://www.nist.gov/publications/de-identifying-government-datasets-techniques-and-governance) | Final, September 2023; scoped to U.S. Government datasets | De-identification technique selection, disclosure review, and governance inputs |
| [NTIA open-model-weights report](https://www.ntia.gov/programs-and-initiatives/artificial-intelligence/open-model-weights-report) | U.S. government policy report, July 2024 | Benefits, marginal risks, uncertainty, monitoring, and release alternatives for widely available model weights; not release authority |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | Published international management-system standard | Organization-wide AI policy, objectives, operation, assurance, and continual improvement |
| [ISO/IEC 38507:2022](https://www.iso.org/standard/56641.html) | Published international guidance standard | Governing-body oversight of effective, efficient, and acceptable AI use |
| [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) | Published international guidance standard | Integration of AI risk management into organizational activities |
| [ISO/IEC 42005:2025](https://www.iso.org/standard/42005) | Published international guidance standard | AI system impact assessment across the lifecycle |
| [ISO/IEC 5338:2023](https://www.iso.org/standard/81118.html) | Published international standard | AI-specific system lifecycle processes |
| [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) | Final, July 2024; used with SP 800-218 | Secure development practices for generative AI and foundation-model systems |
| [NIST SP 800-216](https://csrc.nist.gov/pubs/sp/800/216/final) | Final, May 2023; federal vulnerability-disclosure guidance | Receiving, assessing, managing, and communicating vulnerability reports; organizations must adapt it to their own scope |
| [AWS AI-DLC Workflows 2.0 at checked commit `9f91454`](https://github.com/awslabs/aidlc-workflows/tree/9f9145442429440ccd93f22e27186aa428007e5a) | Vendor-authored GA methodology implementation and included design specification; not a formal standard or complete enterprise security baseline | Multi-harness skills, stages, agents, gates, and Generate–Verify–Learn design input under an enterprise control overlay |
| [ETSI EN 304 223 V2.1.1](https://www.etsi.org/deliver/etsi_en/304200_304299/304223/02.01.01_60/en_304223v020101p.pdf) | Published European Standard, December 2025 | Baseline cybersecurity requirements across the AI lifecycle |
| [Joint guidelines for secure AI system development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) | Government guidance, version 1.0, November 2023 | Secure design, development, deployment, operation, and maintenance |
| [NIST adversarial machine learning taxonomy, AI 100-2e2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) | Final, March 2025, with a published planning note | Threat terminology for predictive and generative AI |
| [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) | Community security guidance, 2025 edition | LLM and generative-AI application threat scenarios |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Community security guidance, published December 2025 | Agent goal, tool, identity, memory, communication, and cascading-failure threats |
| [MITRE ATLAS](https://atlas.mitre.org/) | Living threat knowledge base | Threat modeling, adversary techniques, mitigations, and red-team scenarios |
| [CSA AI Controls Matrix v1.1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) | Vendor-neutral community control catalog, June 2026 | Detailed cloud-AI control objectives and implementation crosswalks |
| [EU Artificial Intelligence Act, Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en), as amended by [Regulation 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) | Binding EU regulation subject to scope, role, and staggered application dates; EUR-Lex records the July 2026 amending regulation as in force | Jurisdiction-specific provider, deployer, model, system, and transparency obligations |
| [EU General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) | Voluntary compliance tool, published July 2025 | Transparency, copyright, and safety and security practices for covered GPAI providers |
| [OECD AI Principles](https://oecd.ai/en/principles) | Intergovernmental principles, updated May 2024 | Human-centered values, transparency, robustness, accountability, and interoperability |
| [Council of Europe HUDERIA](https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems) | Non-binding impact-assessment guidance; methodology approved in 2025 and COBRA model in 2026 | Context analysis, stakeholder engagement, human-rights impact, mitigation, and review |

## Practical crosswalk

This is an implementation map, not a clause-level standards crosswalk.

| Guide area | Principal source inputs | Expected organizational evidence |
|---|---|---|
| [Scope and vocabulary](../foundations/scope-and-vocabulary.md) | NIST AI RMF, OECD AI Principles, ISO/IEC 22989 public description | Approved vocabulary, system boundary, actor roles, intended context |
| [Governance operating model](operating-model.md) | NIST Govern, ISO/IEC 42001, ISO/IEC 38507 | Policy set, inventory, decision rights, competence records, management review |
| [Regulatory obligation register](../worksheets/regulatory-obligation-register.md) | NIST AI RMF Govern 1.1 and Map 1.1, NIST Privacy Framework, exact applicable legal and regulator sources | Dated source inventory, role and applicability decisions, atomic obligations, deadlines, control and evidence links, conflicts, exclusions, exceptions, and reassessment |
| [Risk tiers and controls](control-matrix.md) | NIST AI RMF, ISO/IEC 23894, CSA AICM | Risk method, current and target control profile, separate exceptions, and current category-bound residual-risk decision records |
| [Use-case assessment](../worksheets/use-case-assessment.md) | NIST Map, ISO/IEC 42005, HUDERIA | Context and impact assessment, affected stakeholders, mitigation plan, review triggers |
| [Reference architecture](../architecture/reference-architecture.md) | NIST CSF 2.0, ETSI EN 304 223, joint secure-development guidance | Data-flow and trust-boundary diagrams, control placement, threat model |
| [Security architecture](../security/security-architecture.md) and [identity and permission matrix](../worksheets/identity-and-permission-matrix.md) | NIST SP 800-53 Rev. 5 release 5.2.0, NIST SP 800-63-4, NIST SP 800-207 and 800-207A, NIST SP 800-205 and 800-192, MCP authorization specification, joint agentic-AI guidance | Human and workload identity inventory, resource permissions and attributes, authorization checkpoints, strict delegation attenuation, credential lifecycle, break-glass, policy-model and deployed negative tests, and observed-state reconciliation |
| [Deployment patterns](../architecture/deployment-patterns.md) | NIST GenAI Profile, OWASP, MITRE ATLAS, joint agentic-AI guidance | Pattern-specific security requirements, abuse cases, containment and red-team tests |
| [AI system lifecycle](../delivery/ai-lifecycle.md) | ISO/IEC 5338, NIST SP 800-218A | Lifecycle plan, artifact lineage, approvals, reproducible releases, retirement evidence |
| [Transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md) | NIST AI RMF 1.0 Govern 1.7 and Manage 2.4 plus the voluntary Playbook, NIST SP 800-53 Rev. 5 release 5.2.0, NIST SP 800-88 Rev. 2, NIST SP 800-161 Rev. 1 Update 1, ISO/IEC 5338 public scope | Exact exit boundary, orthogonal states, frozen inventory, continuity and successor acceptance, active-work reconciliation, approved disposition and irreversible sequence, access and supplier removal, authoritative readback, residual ownership, closure, and reopen evidence |
| [Security-first AI-assisted development lifecycle](../delivery/security-first-ai-dlc.md) | NIST SP 800-218 and 800-218A, AWS AI-DLC 2.0 design specification, SLSA | Component admission, workflow manifest, isolated generation, protected verification, controlled learning, release and revocation evidence |
| [Skills-first AI-assisted change workflow](../delivery/skills-first-ai-development.md) | [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), [Agent Skills specification](https://agentskills.io/specification), [DORA 2025](https://dora.dev/research/2025/dora-report/) | Approved skill registry and lifecycle, pinned bundles, external-skill approval, scoped identities and tools, PR evidence, independent review |
| [Agent extension supply-chain security](../security/agent-extension-supply-chain.md) | MCP specification and security guidance, OWASP agentic guidance, MITRE ATLAS, SLSA | Component digest, authority diff, static and contextual findings, sandbox observation, MCP policy, runtime reconciliation, revocation |
| [Agent execution and privacy-minimized telemetry contract](../worksheets/agent-execution-and-telemetry-contract.md) | NIST AI RMF Measure and Manage, NIST SP 800-53 Rev. 5 release 5.2.0 Audit and Accountability and related families, NIST Privacy Framework 1.0, OWASP agentic guidance, owning MCP specifications where applicable | Canonical root and child execution identity, separate authority and effect states, typed outcomes, cancellation and ambiguity treatment, minimized event schema, integrity and completeness, alert ownership, reconciliation, closure, and conformance evidence |
| [Repository ownership and deployment](../delivery/code-deployment.md) | [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), GitHub CODEOWNERS/rulesets/environments, [SLSA 1.2](https://slsa.dev/spec/v1.2/), [CISA Safe Software Deployment](https://www.cisa.gov/sites/default/files/2024-10/safe-software-deployment-how-software-manufacturers-can-ensure-reliability-for-customers-508c.pdf) | Accepted ownership, protected-branch evidence, trusted checks, artifact digest and provenance, deployment approval, deployed-state readback, tested recovery |
| [Public release and external distribution](../delivery/public-release-and-external-distribution.md) | NIST SP 800-218 and 800-218A, NIST AI 600-1, NIST Privacy Framework 1.0, NIST SP 800-188 and 800-216, NTIA 2024 open-model-weights report, SLSA, source-control visibility guidance | Exact distribution manifest, clean-artifact scrub, rights and security decisions, baseline independent approval or separately labeled policy-permitted governance exception, destination readback, support and withdrawal evidence |
| [Evaluation strategy](../delivery/evaluation-strategy.md) | NIST Measure, ISO/IEC 25059 public description, NIST GenAI Profile | Evaluation plan, representative test sets, thresholds, results, limitations, waivers |
| [Production operations](../operations/production-operations.md) | NIST Manage, secure-deployment guidance, NIST AI 800-4 monitoring report | Service objectives, monitoring coverage, incident records, rollback and recovery exercises |
| [Incident, problem, and corrective action](../operations/incident-problem-and-corrective-action.md) | [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) for cybersecurity incidents, NIST Manage, CISA Safe Software Deployment, ISO/IEC 42001 continual improvement | Incident and impact record, containment and restoration evidence, cause analysis, owned corrective actions, effectiveness checks, authorized closure |
| [Third-party risk](third-party-risk.md) | NIST SP 800-218A, joint supply-chain and data-security guidance | Dependency inventory, supplier evidence, contracts, AIBOM or equivalent, exit tests |

## Applying the alignment

1. Determine the organization's roles, jurisdictions, contractual duties, and adopted policies.
2. Complete the
   [regulatory obligation register](../worksheets/regulatory-obligation-register.md)
   so binding duties, contracts, adopted policy, voluntary targets, and
   non-binding horizon-scanning inputs remain distinct.
3. Select a risk profile based on the use case, affected people, data, autonomy, exposure, and reversibility.
4. Map each selected outcome to a named control owner, implementation, evidence, test, and review cadence.
5. Record gaps as remediation items. Use a time-bounded risk acceptance only
   when the controlling source and adopted policy permit it; never use one to
   override a prohibition, create an absent right, excuse a missed mandatory
   duty, or resolve uncertain applicability.
6. Reassess when the intended purpose, model, data, tools, supplier, autonomy, deployment region, or applicable rule changes.

Where sources overlap, the legal and compliance owner resolves obligations; the risk owner resolves risk treatment; and the architecture owner documents how the chosen controls operate together. A mapping should never reduce a stricter applicable requirement.

## Currency and conformance warnings

- **NIST AI RMF:** NIST says AI RMF 1.0 is being revised. Pin mappings to version 1.0 until a successor is assessed, and record the migration decision when it is published.
- **EU requirements:** use the
  [official AI Act text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en),
  the [July 2026 amending regulation](https://eur-lex.europa.eu/eli/reg/2026/1744/oj),
  and the [Commission's current implementation page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
  rather than copying a permanent timeline into policy. Confirm the current
  consolidated effect and application dates with qualified counsel.
- **Living security sources:** OWASP, MITRE ATLAS, CSA AICM, and government cybersecurity guidance change as threats evolve. Record the version or retrieval date in each threat model and assurance report.
- **ISO claims:** public ISO pages describe purpose and scope but do not reproduce all requirements. Do not claim ISO conformance, certification readiness, or clause coverage without the licensed standard and a qualified assessment.
- **Legal interpretation:** classification under this guide is an internal risk decision. It does not determine whether a system is legally prohibited, high-risk, or otherwise regulated.

Review this page's source register at least quarterly and after a material
regulatory, standards, threat, or supplier change. Review each system's
[regulatory obligation register](../worksheets/regulatory-obligation-register.md)
on its adopted legal cadence and event deadlines; the guide-level source check
does not satisfy a system-specific duty.
