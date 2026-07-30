# AI supplier and component assessment

Use for model providers, AI SaaS, managed platforms, open-weight models, datasets, tools, connectors, evaluation services, and material transitive dependencies.

## Identity and scope

- **Supplier / component:**
- **Service and proposed use:**
- **Business and technical owners:**
- **Risk tier and data classes:**
- **Regions and affected jurisdictions:**
- **Assessment date / renewal date:**
- **Alternatives and exit owner:**

## Operating responsibility

Document who owns:

- infrastructure and patching;
- model and artifact updates;
- data quality and provenance;
- access and tenant isolation;
- evaluation and safety controls;
- monitoring and incident response;
- backups, resilience, and recovery;
- regulatory and affected-person obligations.

## Data

- What input, output, metadata, feedback, support, and telemetry does the supplier receive?
- Is data retained, for how long, and where?
- Is data used for training, improvement, abuse monitoring, or human review?
- What opt-out is contractual rather than dashboard-only?
- Which subprocessors and cross-border transfers apply?
- How are deletion, correction, export, and legal hold handled?
- What isolation and encryption apply?
- Can the enterprise obtain evidence of deletion?

## Model and service change

- Is an immutable model revision available?
- Can aliases change without customer action?
- What notice applies to versions, behavior, pricing, policy, region, and deprecation?
- Are release notes and evaluation evidence available?
- Can updates be tested before production?
- What fallback or rollback exists?
- Can safety behavior or acceptable-use policy interrupt a critical workflow?

## Security and privacy assurance

- independent reports and certifications;
- vulnerability disclosure and response;
- penetration and red-team coverage;
- identity, SSO, workload identity, and least privilege;
- tenant isolation and privileged support access;
- private connectivity and egress;
- encryption and key options;
- logging and customer-visible audit;
- secure development and supply-chain provenance;
- breach notice, cooperation, and forensic evidence.

## Quality and responsible AI

- intended and prohibited uses;
- model/system documentation;
- evaluation methods, populations, and limitations;
- bias, safety, misuse, privacy, and robustness testing;
- accessibility and human oversight;
- provider/deployer responsibility split;
- complaint and abuse reporting;
- content provenance or marking where relevant.

## Legal, IP, and compliance

- linked
  [regulatory obligation register](regulatory-obligation-register.md)
  source, applicability, and obligation IDs;
- data-processing and confidentiality terms;
- ownership and permitted use of input and output;
- training-data and model provenance representations;
- open-source and model license obligations;
- IP indemnity and exclusions;
- sector and jurisdiction support;
- audit and regulator cooperation;
- records and transparency obligations;
- export, sanctions, and location restrictions;
- insurance and liability limits.

Supplier answers and contract terms inform the enterprise register; they do
not establish the enterprise's source-specific actor role, legal
applicability, or control effectiveness.

## Reliability and economics

- service objectives and support;
- regional and provider architecture;
- capacity, quotas, and priority;
- continuity and disaster recovery evidence;
- unit pricing and price-change rights;
- committed spend and overage;
- cost and usage export;
- financial viability and concentration.

## Open-source and open-weight components

- origin, maintainer, governance, and release process;
- checksum or signature;
- model, dataset, code, and adapter licenses;
- serialization and loader safety;
- scanning and known vulnerabilities;
- community dependency and abandonment risk;
- internal owner for patching, serving, evaluation, and support.

## Exit and portability

- data, prompt, evaluation, logs, state, and configuration export;
- model or provider substitution;
- deletion and account closure;
- migration time, egress cost, and contract assistance;
- tested continuity during transition;
- dependencies that cannot be ported.

For an approved exit, project these findings into the
[transfer, decommissioning, and retirement record](transfer-decommissioning-and-retirement.md)
and require successor acceptance, disposition authority, supplier and
customer-side readback, residual ownership, and reopen criteria.

## Decision

| Finding / risk | Treatment or contract term | Owner | Evidence | Due / expiry |
|---|---|---|---|---|
| | | | | |

- **Decision:** Approve / Approve with conditions / Hold / Reject
- **Named supplier-admission decision authority and authority basis:**
- **Approved uses, data, regions, and scale:**
- **Conditions and linked exception decision IDs, separate authorities,
  scopes, and expiries:**
- **Linked residual-risk decision IDs, categories, results, exact scopes,
  named authorities and authority bases, conditions, expiries, invalidation
  triggers, and supersession states:**
- **Monitoring and renewal triggers:**

Supplier admission, policy exceptions, and residual-risk acceptance are
separate decisions. The supplier-admission authority consumes every required,
current, category-bound risk decision but does not inherit or repeat its
authority. Missing, expired, invalidated, out-of-category, or out-of-scope
acceptance forces **Hold** or **Reject**.
