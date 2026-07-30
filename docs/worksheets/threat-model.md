# AI threat model

## Scope and owners

- **System / release:**
- **Threat-model owner and participants:**
- **Business and security owners:**
- **Risk tier, data class, exposure, and autonomy:**
- **Architecture and data-flow links:**
- **Assumptions and excluded systems:**
- **Last review / material-change triggers:**

## Assets

| Asset | Security property | Owner | Impact if compromised |
|---|---|---|---|
| Prompts and policies | confidentiality / integrity | | |
| Training and evaluation data | confidentiality / integrity / availability | | |
| Retrieval sources and indexes | authorization / integrity / freshness | | |
| Models and weights | confidentiality / integrity / availability | | |
| Identities and credentials | confidentiality / authorization | | |
| Tools and systems of record | integrity / authorization / availability | | |
| Workflow state and memory | confidentiality / integrity / isolation | | |
| Traces and approvals | integrity / non-repudiation / privacy | | |

## Actors and capabilities

- ordinary and malicious users;
- affected people and external content publishers;
- insiders, operators, and privileged administrators;
- tenants and partner systems;
- model, data, tool, and infrastructure suppliers;
- compromised model, tool, package, dataset, or document;
- autonomous or misdirected agents.

For each, state access, knowledge, resources, and credible goals.

## Trust boundaries

Document identity, authorization, data classification, encryption, validation, logging, and failure behavior at:

- user to application;
- application to runtime;
- runtime to model;
- runtime to retrieval and memory;
- runtime to tool broker;
- tool to system of record;
- agent to agent;
- build pipeline to registry;
- registry or control plane to runtime;
- runtime to telemetry;
- tenant, environment, region, and supplier boundaries.

## Abuse cases

| ID | Threat / abuse path | Preconditions | Impact | Existing controls | Detection | Residual risk |
|---|---|---|---|---|---|---|
| T-01 | | | | | | |

Include:

- direct and indirect prompt injection;
- jailbreak and policy evasion;
- training, RAG, memory, evaluation, and tool poisoning;
- sensitive-data or prompt exfiltration;
- cross-tenant access and confused deputy;
- excessive agency and approval bypass;
- insecure output rendering or code execution;
- malicious or over-privileged tools;
- malicious skill requests shell access and exfiltrates credentials after
  workspace trust;
- plugin bundles a malicious hook, helper binary, or local MCP startup command;
- admitted MCP server later changes tool names, descriptions, schemas, or
  annotations, or enables unapproved resources, prompts, sampling, elicitation,
  roots, or logging;
- token passthrough or confused-deputy OAuth grants cross-tenant access;
- indirect injection composes private-data read access with an exfiltration
  tool;
- agent weakens its security skill, verifier, evaluation, or CI and then
  self-certifies;
- poisoned correction is promoted into a shared skill, policy, guardrail, or
  knowledge library;
- mutable CI dependency or untrusted fork pipeline obtains privileged
  credentials;
- SSRF and uncontrolled egress;
- model extraction, inversion, membership inference, or evasion;
- supply-chain compromise;
- denial of service, denial of wallet, and runaway loops;
- trace tampering and repudiation.

Use current [MITRE ATLAS](https://atlas.mitre.org/), [NIST adversarial ML](https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations), and [OWASP GenAI](https://genai.owasp.org/) resources as completeness checks.

## Control design

For each significant threat, identify:

- preventive, detective, and responsive controls;
- deterministic enforcement point;
- owner and operating frequency;
- evidence and test;
- control failure behavior;
- compensating controls and exception expiry.

## Security tests

- [ ] identity, tenant, and per-resource authorization;
- [ ] prompt injection and poisoned retrieval;
- [ ] secret, personal-data, and restricted-data exfiltration;
- [ ] tool schema, approval, replay, and idempotency;
- [ ] code, markup, URL, file, and command output handling;
- [ ] egress, redirect, DNS, metadata, and internal-address controls;
- [ ] model, dataset, package, and artifact integrity;
- [ ] load, quota, retry, loop, and cost abuse;
- [ ] credential revocation, pause, kill switch, and recovery;
- [ ] forensic reconstruction.

## Decision

- open critical and high findings;
- linked residual-risk decision IDs, categories, exact scopes, named
  authorities and authority bases, results, conditions, validity states,
  expiries, invalidation triggers, and supersession states;
- conditions for release;
- next red-team or reassessment date;
- changes added to regression evaluation.

The threat model identifies and treats risk; it does not accept residual risk
or authorize release. Each consuming gate verifies the required current,
category-bound decision records without creating an embedded acceptance or
inferring authority from supporting reviewers.
