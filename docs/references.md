# Authoritative references

This bibliography favors official standards bodies, regulators, government cybersecurity agencies, and the owning organizations of open security frameworks. It is a source register for the guide, not an assertion that every source applies to every system.

**Full-register review:** 2026-07-28. Entries with a later source check state it
directly.

## Governance and risk management

- [NIST Artificial Intelligence Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — voluntary, cross-sector AI risk framework, January 2023.
- [NIST AI RMF program and current-status page](https://www.nist.gov/itl/ai-risk-management-framework) — official status, profiles, crosswalks, and revision notices.
- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) — suggested actions for Govern, Map, Measure, and Manage outcomes.
- [NIST AI 600-1, Generative Artificial Intelligence Profile](https://doi.org/10.6028/NIST.AI.600-1) — generative-AI risks and suggested actions, July 2024.
- [ISO/IEC 42001:2023, Artificial intelligence management system](https://www.iso.org/standard/42001) — requirements for establishing, operating, maintaining, and improving an AI management system.
- [ISO/IEC 38507:2022, Governance implications of AI use](https://www.iso.org/standard/56641.html) — guidance for governing bodies and other organizational stakeholders.
- [ISO/IEC 23894:2023, Guidance on AI risk management](https://www.iso.org/standard/77304.html) — integration and implementation of AI-related risk management.
- [ISO/IEC 42005:2025, AI system impact assessment](https://www.iso.org/standard/42005) — lifecycle impact-assessment guidance.
- [OECD AI Principles](https://oecd.ai/en/principles) — intergovernmental principles for trustworthy AI, updated May 2024.
- [Council of Europe Framework Convention on AI, Human Rights, Democracy and the Rule of Law](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence) — treaty framework; obligations depend on signature, ratification, jurisdiction, and implementing measures.
- [Council of Europe HUDERIA](https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems) — non-binding context, stakeholder, human-rights impact, and mitigation methodology.

## Concepts, architecture, lifecycle, data, and quality

- [ISO/IEC 22989:2022, AI concepts and terminology](https://www.iso.org/standard/74296.html) — common AI concepts and terms.
- [ISO/IEC 23053:2022, Framework for AI systems using machine learning](https://www.iso.org/standard/74438.html) — conceptual framework for ML-based AI systems.
- [ISO/IEC 5338:2023, AI system lifecycle processes](https://www.iso.org/standard/81118.html) — AI-specific lifecycle process framework.
- [ISO/IEC 8183:2023, AI data lifecycle framework](https://www.iso.org/standard/83002.html) — stages and actions for data across an AI system lifecycle.
- [ISO/IEC 5259-2:2024, Data-quality measures](https://www.iso.org/standard/81860.html) — data-quality model and measurable characteristics for analytics and ML.
- [ISO/IEC 5259-3:2024, Data-quality management requirements and guidance](https://www.iso.org/standard/81092.html) — management of data quality for analytics and ML.
- [ISO/IEC 5259-5:2025, Data-quality governance framework](https://www.iso.org/standard/84150.html) — governing-body direction and oversight for data quality.
- [ISO/IEC 25059:2023, Quality model for AI systems](https://www.iso.org/standard/80655.html) — AI system quality characteristics; ISO lists a revision in development.
- [NIST SP 800-218A, Secure Software Development Practices for Generative AI and Dual-Use Foundation Models](https://csrc.nist.gov/pubs/sp/800/218/a/final) — AI community profile used with the NIST Secure Software Development Framework.

## AI-assisted development, repository governance, and deployment

- [NIST SP 800-218, Secure Software Development Framework 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) — current final baseline secure-software practices on the check date; version 1.2 remains draft.
- [AWS AI-Driven Development Life Cycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) — vendor-authored AI-centric lifecycle emphasizing AI planning and execution with human validation of critical decisions.
- [AWS Labs AI-DLC Workflows 2.0 at checked commit `9f91454`](https://github.com/awslabs/aidlc-workflows/tree/9f9145442429440ccd93f22e27186aa428007e5a) — vendor-authored GA methodology implementation for multiple harnesses; pin a known-good version, inspect the package, and review generated output.
- [AI-DLC Workflows 2.0 architecture specification at checked commit `9f91454`](https://github.com/awslabs/aidlc-workflows/blob/9f9145442429440ccd93f22e27186aa428007e5a/assets/AI-DLC-Workflows-2.0-Specification.pdf) — included design specification for skills, workflow composition, agents, orchestration, packaging, and Generate–Verify–Learn; neither the implementation nor specification is a formal standard or complete enterprise security baseline.
- [OpenAI agent skills and computer environment](https://openai.com/index/equip-responses-api-computer-environment/) — owning-organization description of tools as executable capability and skills as reusable workflow logic.
- [Agent Skills specification](https://agentskills.io/specification) — owning open-format specification for skill-package metadata and supporting resources, including experimental tool allowlisting.
- [OpenClaw AI-assisted contribution policy](https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md) — project-specific example requiring intent, useful evidence, AI disclosure, human understanding, and its `autoreview` skill when available.
- [OpenClaw agent-transcript skill](https://github.com/openclaw/agent-skills/blob/main/skills/agent-transcript/SKILL.md) — project-specific, best-effort local sanitization with user approval, no raw-log upload, and fail-closed handling of unresolved sensitive material.
- [Knowledge-Based Pull Requests](https://arxiv.org/html/2606.26721) — June 2026 research proposal for human-confirmed knowledge and provenance packages across trust boundaries; early conceptual work, not an established standard.
- [GitHub guidance for reviewing agent-generated pull requests](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/) — vendor guidance on author review, CI weakening, duplication, critical-path review, evidence, and agent-workflow security.
- [GitHub code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) — review routing, syntax, ownership eligibility, and interaction with protected-branch rules.
- [GitHub repository rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) and [available rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets) — concrete branch, review, status-check, signature, and deployment enforcement; feature availability depends on plan and visibility.
- [GitHub deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — environment protection, reviewers, allowed branches or tags, secrets, and deployment controls.
- [GitHub secure use of Actions](https://docs.github.com/en/actions/reference/security/secure-use) — least privilege, pinned dependencies, untrusted input, runners, and workflow security.
- [GitHub dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) — pull-request dependency change review and policy input; availability varies by repository and plan.
- [GitHub artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations) — build provenance and SBOM attestations; provenance supports origin verification but is not a safety determination.
- [GitLab protected branches](https://docs.gitlab.com/user/project/repository/branches/protected/) and [merge-request approvals](https://docs.gitlab.com/user/project/merge_requests/approvals/) — source-control enforcement inputs whose tier, role, inheritance, and overlapping-rule behavior must be verified.
- [GitLab security policy project](https://docs.gitlab.com/user/application_security/policies/security_policy_project/) and [dependency scanning](https://docs.gitlab.com/user/application_security/dependency_scanning/) — protected security-pipeline policy and dependency/CycloneDX evidence inputs; feature availability varies by tier.
- [SLSA 1.2](https://slsa.dev/spec/v1.2/) and [SLSA provenance](https://slsa.dev/spec/v1.2/provenance) — approved supply-chain levels and verifiable artifact origin and build-process information on the check date.
- [CISA Safe Software Deployment](https://www.cisa.gov/sites/default/files/2024-10/safe-software-deployment-how-software-manufacturers-can-ensure-reliability-for-customers-508c.pdf) — manufacturer guidance for safe rollout, testing, monitoring, rollback, and customer reliability.
- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) — primary practitioner guidance for bounded exposure and baseline comparison.
- [NIST SP 800-61r3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — current incident-response revision integrated with CSF 2.0.
- [NIST SP 800-216, Recommendations for Federal Vulnerability Disclosure Guidelines](https://csrc.nist.gov/pubs/sp/800/216/final) — final May 2023 federal guidance for receiving, assessing, managing, and communicating vulnerability reports; adapt it to the organization's own scope and authority.
- [GitHub repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility) and [fork behavior after visibility changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility) — current platform-specific warnings about exposed code, Actions history and logs, forks, and other consequences; verify the exact repository and plan before a visibility change.
- [DORA 2025 State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/) and [errata](https://dora.dev/research/2025/errata/) — official report and corrections on the check date; AI use had positive associations with delivery throughput and product performance but a continuing negative association with delivery stability.

## Cloud model candidates, pricing, and product-specific routing

These primary provider sources feed the
[dated model and provider candidate catalog](architecture/model-and-provider-candidate-catalog.md).
The provider-neutral control design remains in
[governed model routing and agent dispatch](architecture/model-portfolio-and-routing.md).

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing), [model comparison](https://developers.openai.com/api/docs/models/compare), [Reserved Tier](https://openai.com/api-reserved-tier/), and [API data controls](https://developers.openai.com/api/docs/guides/your-data) — owning-provider model, public price, capacity-plan, and data-handling inputs; exact context, processing, cache, regional, and contract terms vary.
- [OpenAI Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) — current role-specific subagent model and reasoning configuration behavior.
- [Microsoft Azure model catalog](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai), [deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types), [data privacy](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy), and [pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/) — distinct Azure deployment, processing-boundary, privacy, and meter inputs.
- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/), [data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html), and [geographic cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html) — Bedrock model, plan, provider-access, and inference-destination inputs.
- [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/), [Harness model configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-models.html), [Harness security considerations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html), and [Intelligent Prompt Routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) — current AWS harness and centrally configured model-routing capabilities, trust assumptions, and limitations.
- [Vertex AI generative AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing), [model lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions), [deployment and endpoint locations](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations), [zero data retention](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention), and [security controls](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-controls) — Google pricing, version status, endpoint geography, feature-specific retention, and security inputs.
- [Google ADK LLM agents](https://adk.dev/agents/llm-agents/), [model routing](https://adk.dev/agents/models/routing/), and [agent routing](https://adk.dev/agents/routing/) — application-controlled role and routing examples; the routing APIs' own pages currently mark them experimental and state their supported language/version.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) — current subagent model selection, tool, permission, skill, and MCP configuration behavior.

## Cybersecurity and privacy foundations

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — enterprise cybersecurity outcomes across Govern, Identify, Protect, Detect, Respond, and Recover.
- [NIST SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — tailorable U.S. Government control catalog; NIST's current minor release was 5.2.0 on the 2026-07-28 source check.
- [NIST SP 800-115, Technical Guide to Information Security Testing and Assessment](https://www.nist.gov/publications/technical-guide-information-security-testing-and-assessment) — September 2008 overview for planning and conducting technical security tests, analyzing findings, and developing mitigation strategies; it is not a complete current testing program; status checked 2026-07-30.
- [NIST SP 800-231, Bug Framework](https://csrc.nist.gov/pubs/sp/800/231/final) — formal language and models for software and hardware weaknesses and vulnerabilities, including weakness chains governed by causation, propagation, and composition rules; checked 2026-07-30.
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — authoritative CISA catalog of vulnerabilities known to be exploited in the wild and a prioritization input; absence is not proof of non-exploitation; checked 2026-07-30.
- [NIST SP 800-88 Rev. 2, Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final) — final September 2025 guidance for an organization-defined media-sanitization program; it supersedes Revision 1 and does not by itself authorize deletion.
- [NIST SP 800-161 Rev. 1 Update 1, Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) — final May 2022 lifecycle C-SCRM guidance with updates through November 2024.
- [NIST SP 800-63-4, Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final) — final July 2025 guidance for identity proofing, authentication, and federation of people interacting with government systems; not a workload-identity or authorization standard.
- [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) and [SP 800-207A, cloud-native access control](https://csrc.nist.gov/pubs/sp/800/207/a/final) — final zero-trust architecture guidance for resource-focused policy and granular user, application, and service identity; not a universal product blueprint.
- [NIST SP 800-205, Attribute Considerations for Access Control Systems](https://csrc.nist.gov/pubs/sp/800/205/final) — final June 2019 guidance for subject, object, operation, and environment attribute semantics, sources, assurance, and lifecycle; it does not require attribute-based access control.
- [NIST SP 800-192, Verification and Test Methods for Access Control Policies/Models](https://csrc.nist.gov/pubs/sp/800/192/final) — final June 2017 access-control policy and model verification guidance; model checks do not prove deployed enforcement.
- [NIST Privacy Framework 1.0](https://www.nist.gov/publications/nist-privacy-framework-tool-improving-privacy-through-enterprise-risk-management) — final voluntary enterprise privacy-risk framework, January 2020. NIST's [version 1.1 project page](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11) still identifies 1.1 as an Initial Public Draft and the final as forthcoming on the 2026-07-28 source check.
- [NIST SP 800-188, De-Identifying Government Datasets](https://www.nist.gov/publications/de-identifying-government-datasets-techniques-and-governance) — final U.S. Government dataset de-identification and disclosure-governance guidance, September 2023; apply its scope limits outside federal datasets.
- [NTIA Dual-Use Foundation Models with Widely Available Model Weights report](https://www.ntia.gov/programs-and-initiatives/artificial-intelligence/open-model-weights-report) — U.S. government policy analysis of open-weight benefits, marginal risks, and evidence uncertainty, July 2024; not release authorization.
- [NIST AI 100-2e2025, Adversarial Machine Learning](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) — taxonomy and terminology for attacks and mitigations, March 2025.
- [NIST SP 1270, Towards a Standard for Identifying and Managing Bias in AI](https://www.nist.gov/artificial-intelligence/ai-fundamental-research-managing-ai-bias) — socio-technical guidance on harmful bias.
- [NISTIR 8312, Four Principles of Explainable Artificial Intelligence](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence) — explanation, meaningfulness, explanation accuracy, and knowledge limits.
- [Joint Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) — NCSC, CISA, NSA, and international-partner guidance across the secure AI lifecycle.
- [ETSI EN 304 223 V2.1.1, Baseline Cyber Security Requirements for AI Models and Systems](https://www.etsi.org/deliver/etsi_en/304200_304299/304223/02.01.01_60/en_304223v020101p.pdf) — published European Standard, December 2025.
- [Deploying AI Systems Securely](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/deploying-ai-systems-securely) — joint government guidance for deployment and operation of externally developed AI systems.
- [AI Data Security](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/ai-data-security) — joint guidance for securing data used to train and operate AI systems.
- [AI and ML Supply Chain Risks and Mitigations](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/artificial-intelligence-and-machine-learning-supply-chain-risks-and-mitigations) — joint government procurement and supply-chain guidance, updated March 2026.

## Generative and agentic AI security

- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) — current LLM and generative-AI application risk list on the check date.
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — agentic-system security risks and mitigations.
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25), [HTTP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), [tools specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools), [security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices), and [client security guidance](https://modelcontextprotocol.io/docs/develop/clients/client-best-practices) — owning-protocol requirements and guidance for capability negotiation, tokens, OAuth, sessions, SSRF, tools and other surfaces, consent, and client enforcement.
- [OWASP practical guide for secure MCP server development](https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/) — community implementation guidance supplementing the protocol sources.
- [Claude Code security](https://code.claude.com/docs/en/security), [sandboxing](https://code.claude.com/docs/en/sandboxing), and [plugin discovery and security](https://code.claude.com/docs/en/discover-plugins) — owning-product permission, sandbox, prompt-injection, MCP trust, plugin execution, marketplace, and managed-restriction behavior.
- [Claude Code Review](https://code.claude.com/docs/en/code-review) and [Claude Code Security](https://www.anthropic.com/news/claude-code-security) — research-preview review capabilities that supplement rather than replace manual review and human approval.
- [MITRE ATLAS](https://atlas.mitre.org/) — living knowledge base of adversary tactics, techniques, mitigations, and case studies for predictive, generative, and agentic AI.
- [Careful Adoption of Agentic AI Services](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services) — joint Five Eyes guidance for identity, privilege, isolation, monitoring, human oversight, and incremental deployment, May 2026.
- [NSA Model Context Protocol Security Design Considerations](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/) — official guidance for MCP-based automation, May 2026.
- [CSA AI Controls Matrix v1.1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) — vendor-neutral cloud-AI control catalog, June 2026.

## Regulation and jurisdictional guidance

- [Regulation (EU) 2024/1689, Artificial Intelligence Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en) — official legal text.
- [Regulation (EU) 2026/1744, Digital Omnibus on AI](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) — official July 2026 amendment to the AI Act; determine current consolidated effect and dates from enacted text.
- [Regulation (EU) 2016/679, General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — official legal text; applicability and role-specific duties require qualified review.
- [European Commission AI Act implementation page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) — official explanatory implementation summary; subordinate to the Official Journal legal text.
- [AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) — Commission update dated 2026-07-27; consult the enacted text and counsel for legal effect.
- [General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) — voluntary tool covering transparency, copyright, and safety and security for relevant GPAI providers.
- [Guidelines for providers and deployers of high-risk AI systems](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems) — Commission classification guidance and current timing; check whether a cited version is draft or final.
- [Article 50 transparency guidance](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) — Commission guidance on AI interaction and generated-content transparency obligations.

## Operations, evaluation, and monitoring

- [NIST AI Resource Center](https://airc.nist.gov/) — official AI RMF implementation and testing, evaluation, verification, and validation resources.
- [NIST AI 800-4, Challenges to the Monitoring of Deployed AI Systems](https://www.nist.gov/news-events/news/2026/03/new-report-challenges-monitoring-deployed-ai-systems) — monitoring categories, barriers, and research gaps, March 2026.
- [ISO/IEC TS 4213:2022, Assessment of ML classification performance](https://www.iso.org/standard/79799.html) — classification-performance methodology; ISO lists a replacement under development.
- [ISO/IEC 24029-2:2023, Robustness assessment using formal methods](https://www.iso.org/standard/79804.html) — methodology for assessing neural-network robustness properties with formal methods.
- [ISO/IEC TR 24027:2021, Bias in AI systems and AI-aided decision making](https://www.iso.org/standard/77607.html) — bias sources, assessment, and treatment across the lifecycle.

## Using this bibliography

- Record the exact publication, edition, retrieval date, and relevant section in each assessment or control mapping.
- Prefer the official legal text over summaries when determining obligations.
- Listing a source here does not mean it applies to a particular organization,
  system, role, jurisdiction, or date.
- Treat drafts, concept notes, news releases, and living web pages according to their stated status.
- Do not reproduce copyrighted standards text. ISO public pages provide descriptions; organizations need licensed access to assess detailed requirements or make conformance claims.
- Recheck time-sensitive sources at least quarterly and whenever a material legal, standards, threat, or supplier change occurs.
