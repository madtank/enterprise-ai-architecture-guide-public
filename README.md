# Enterprise AI Architecture Guide

An opinionated, vendor-neutral guide for designing, governing, delivering, and operating AI systems in an enterprise.

The guide is intended for:

- enterprise and solution architects;
- AI, data, security, and platform leaders;
- engineering and product teams shipping AI capabilities;
- risk, legal, privacy, compliance, and audit partners.

It covers predictive machine learning, generative AI, retrieval, and agentic systems. The emphasis is on production systems: business ownership, risk-tiered controls, reusable platform capabilities, measurable quality, human impact, security, resilience, economics, and safe operations.

## Start here

Use steps 1–2 to orient. Apply the later gates only when their system,
repository, dependency, release, incident, or exit boundary is in scope; they
are not a universal linear checklist.

1. Review the [guide map and coverage checklist](docs/guide-map.md) to confirm
   the high-level scope and remaining decisions.
2. Choose an applicable
   [cross-cutting operating path](docs/index.md#cross-cutting-operating-paths)
   or [detailed role path](docs/index.md#detailed-role-paths) on the guide
   home.
3. Use the [reference architecture](docs/architecture/reference-architecture.md) and [data architecture](docs/architecture/data-architecture.md) to establish shared boundaries.
4. Complete the [use-case assessment](docs/worksheets/use-case-assessment.md)
   for every proposal. Escalate to the
   [AI risk and impact assessment](docs/worksheets/ai-risk-impact-assessment.md)
   before build or production, or sooner when screening identifies material
   people, data, autonomy, or regulatory risk.
5. Record source-specific applicability, duties, deadlines, controls, and
   evidence in the
   [regulatory obligation register](docs/worksheets/regulatory-obligation-register.md).
6. Tailor controls using the [control matrix](docs/governance/control-matrix.md) and [framework alignment](docs/governance/framework-alignment.md).
7. Follow the [AI system lifecycle](docs/delivery/ai-lifecycle.md) and capture
   consequential choices in an
   [architecture decision record](docs/worksheets/architecture-decision-record.md).
8. Trace those decisions end to end in the
   [fictional procurement-evidence golden thread](docs/examples/worked-golden-thread.md).
9. For AI-assisted engineering changes, apply the
   [security-first AI-assisted development lifecycle](docs/delivery/security-first-ai-dlc.md)
   and execute the
   [skills-first AI-assisted change workflow](docs/delivery/skills-first-ai-development.md).
10. Before ordinary use, admit applicable skills, plugins, hooks, and MCP
   servers through
   [agent extension supply-chain security](docs/security/agent-extension-supply-chain.md).
11. Before routing production work, approve exact serving-boundary deployments
   and multi-agent dispatch with
   [governed model routing and agent dispatch](docs/architecture/model-portfolio-and-routing.md);
   refresh discovery inputs from the separate
   [dated model and provider candidate catalog](docs/architecture/model-and-provider-candidate-catalog.md).
12. Bind human, workload, agent-runtime, tool, credential, tenant, and
    delegated authority with the
    [identity and permission matrix](docs/worksheets/identity-and-permission-matrix.md).
13. Define root-to-child state, typed outcomes, cancellation, reconciliation,
    and privacy-minimized operating evidence with the
    [agent execution and telemetry contract](docs/worksheets/agent-execution-and-telemetry-contract.md).
14. Verify release evidence with the
   [production readiness review](docs/worksheets/production-readiness-review.md).
15. Before any artifact leaves an established access boundary, apply the
   [public release and external distribution](docs/delivery/public-release-and-external-distribution.md)
   gate to the exact candidate.
16. Use the canonical
   [code deployment](docs/delivery/code-deployment.md) and
   [incident-to-corrective-action](docs/operations/incident-problem-and-corrective-action.md)
   paths.
17. Before transferring, decommissioning, archiving, withdrawing, or retiring
    a system or material dependency, complete the
    [transfer, decommissioning, and retirement record](docs/worksheets/transfer-decommissioning-and-retirement.md).

## Local preview

Python 3.11 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python scripts/check_requirements_lock.py
python -m pip install --require-hashes --only-binary=:all: -r requirements.txt
python scripts/check_docs.py
mkdocs serve
```

Then open `http://127.0.0.1:8000`.

Repository validation, publication, and rollback are documented in
[DEPLOYMENT.md](DEPLOYMENT.md). No public site deployment is currently
configured.

`requirements.in` declares the reviewed direct dependency;
`requirements.txt` is the generated, hash-locked transitive closure. Pull
request validation reproduces that lock with the repository-pinned resolver
before installing it.

## Repository policies

- [Publication and provenance](PUBLICATION.md)
- [Security reporting](SECURITY.md)
- [Support and corrections](SUPPORT.md)
- [Contributing](CONTRIBUTING.md)
- [Ownership](OWNERSHIP.md)
- [Validation, protection, and release](DEPLOYMENT.md)

## Coverage

This first comprehensive edition includes:

- executive strategy, portfolio value, adoption, and risk appetite;
- multi-plane enterprise reference, data, security, platform, and resilience architecture;
- predictive ML, generative AI, RAG, and agentic AI patterns;
- AI management, responsible AI, third-party risk, and standards alignment;
- MLOps, LLMOps, AgentOps, evaluation, production operations, and FinOps;
- security-first AI-assisted development lifecycle, skills-first AI-assisted
  change workflow, PR evidence,
  agent-extension and MCP supply-chain security, repository governance, code
  deployment, exact-artifact public-release controls, incident repair, and
  corrective action;
- durable central policy routing, coordinator-worker dispatch, performance
  evaluation, and total-cost controls, plus a separate dated model and provider
  candidate catalog;
- reusable assessments, obligation, identity, execution-telemetry, and
  transfer/retirement records, system cards, threat models, evaluation
  reports, and readiness worksheets;
- a fictional, non-sensitive worked golden thread connecting intake,
  architecture, routing, extensions, evaluation, deployment, incident/CAPA,
  and retirement evidence;
- a dated bibliography of authoritative primary sources.

It deliberately separates:

- durable principles from fast-changing product choices;
- enterprise platform capabilities from use-case implementations;
- mandatory control outcomes from example implementation patterns.

## Status, provenance, and limitations

This guide was developed with AI assistance after initiation by the repository
owner. This repository is a source-only public reference artifact; its
availability does not by itself indicate independent approval, organizational
adoption, certification, or fitness for a particular system. The
[publication and provenance record](PUBLICATION.md) defines the public source
boundary, AI-assistance disclosure, validation, exclusions, and generated-site
limitations. See [SUPPORT.md](SUPPORT.md) for the current support boundary.

The guide is a design and control reference. It is not a certification, legal
advice, security assurance, deployment approval, or permission to publish.
Accountable owners must determine applicability, tailor controls, verify
operation, and approve each consequential system and release. AI review is
advisory and does not provide independent approval.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review and contribution model.
See [OWNERSHIP.md](OWNERSHIP.md) for repository accountability, merge
authority, and continuity.

The original repository content is available under the
[MIT License](LICENSE). Third-party dependencies and any generated
distribution artifacts remain subject to their own applicable terms. A
generated site is not part of this source distribution. See
[third-party notices and distribution boundaries](THIRD_PARTY_NOTICES.md).
