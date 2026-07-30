# AI management system

An AI management system turns principles into repeatable organizational practice. It connects leadership, policy, risk and impact assessment, competence, controlled delivery, monitoring, audit, corrective action, and continual improvement.

This chapter is informed by the public description of [ISO/IEC 42001](https://www.iso.org/standard/42001), which specifies an organizational system for establishing, implementing, maintaining, and continually improving responsible AI management. This guide does not claim clause-level conformance or reproduce the licensed standard.

## Management system boundary

Define:

- organizational units and legal entities in scope;
- whether the enterprise develops, provides, deploys, operates, or uses AI;
- covered products, services, processes, regions, and suppliers;
- interfaces with information security, privacy, quality, records, risk, and business continuity systems;
- exclusions and their rationale;
- executive owner and management-review forum.

The boundary must include shadow, embedded, and supplier-provided AI where the enterprise remains accountable for its use.

## Policy hierarchy

Use a coherent hierarchy:

1. **Enterprise AI policy** — purpose, principles, risk appetite, prohibitions, accountability.
2. **Standards** — mandatory outcomes for data, security, evaluation, human oversight, suppliers, and operations.
3. **Architecture patterns** — approved ways to meet recurring requirements.
4. **Procedures and playbooks** — intake, assessment, release, incident, change, exception, and retirement.
5. **Evidence and records** — system inventory, assessments, decisions, evaluations, monitoring, incidents, and improvements.

Policies should be technology-neutral enough to endure but specific enough to produce testable outcomes.

## Objectives and measures

Set objectives for:

- legitimate and valuable use;
- risk and impact assessment coverage;
- inventory completeness and ownership;
- control design and operating effectiveness;
- delivery lead time through approved paths;
- quality, fairness, safety, security, privacy, and reliability;
- incident and corrective-action closure;
- supplier assurance;
- literacy and competence;
- benefits realization and retirement of low-value systems.

Each objective needs an owner, target, measurement method, review cadence, and corrective-action trigger.

## Roles and segregation

Separate, proportionally:

- system development;
- domain validation;
- risk acceptance;
- production deployment;
- independent assurance;
- incident investigation;
- audit.

Small organizations may combine roles, but should document conflicts and introduce peer, management, or external review for consequential decisions.

## Competence and AI literacy

Define competence by role:

- all users: permitted use, data handling, limitations, disclosure, reporting;
- reviewers: domain validation, automation bias, correction, escalation;
- builders: secure design, data, evaluation, operations, documentation;
- platform teams: shared controls, service operation, evidence;
- risk and assurance: classification, testing, impact, control assessment;
- leaders: risk appetite, decision rights, portfolio value, accountability;
- procurement and legal: supplier, IP, privacy, regulatory, exit.

Training completion alone does not demonstrate competence. Use practical exercises and role-specific assessment.

## Documented information

Maintain controlled records for:

- policies, standards, procedures, and approved patterns;
- AI system inventory and ownership;
- risk and impact assessments;
- dated
  [regulatory obligation registers](../worksheets/regulatory-obligation-register.md)
  and source, applicability, deadline, conflict, and exception decisions;
- data, model, supplier, and architecture decisions;
- evaluation plans, results, waivers, and release approvals;
- incidents, complaints, appeals, changes, and corrective actions;
- management review and internal audit;
- retirement and data disposition.

Apply version, integrity, retention, access, privacy, and legal-hold requirements.

## Operational process

The management system should ensure:

- no experiment uses unapproved data or environment;
- no production system lacks an owner and classification;
- control requirements are derived before build;
- evidence is generated during delivery;
- release authority matches risk;
- operating signals feed reassessment;
- material change reopens relevant decisions;
- suppliers and embedded AI remain in scope;
- retirement removes or transfers scoped capability and access, while every
  retained or shared asset keeps an explicit owner, purpose, access rule,
  review date, and final disposition in the
  [transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md).

## Internal audit

Audit both design and operation:

- inventory completeness;
- classification consistency;
- control evidence quality;
- authorization and segregation;
- exception age and remediation;
- monitoring and incident response;
- supplier obligations;
- corrective-action closure;
- policy and practice alignment.

Use risk-based sampling and include deployed-path evidence. A polished document without operating proof is not an effective control.

## Management review

Leadership should review:

- changes in obligations, technology, stakeholders, and enterprise context;
- performance against objectives;
- incidents, complaints, appeals, and audit results;
- top residual risks and exceptions;
- supplier, concentration, capacity, and cost;
- resource, competence, and platform gaps;
- decisions to scale, hold, correct, or retire;
- opportunities for improvement.

Record decisions, owners, funding, and deadlines.

## Nonconformity and corrective action

When a requirement is not met:

1. contain actual or potential impact;
2. preserve evidence and notify required owners;
3. identify systemic and proximate causes;
4. correct the issue and affected records;
5. assess similar systems and shared capabilities;
6. update controls, patterns, tests, and training;
7. verify effectiveness;
8. document residual risk and closure.

Avoid treating every failure as “model hallucination.” Root causes often lie in data, workflow, permissions, evaluation, user experience, or operating incentives.

Use the
[incident, problem, and corrective-action](../operations/incident-problem-and-corrective-action.md)
workflow and
[incident and corrective-action record](../worksheets/incident-and-corrective-action-record.md)
to preserve ownership from containment through effectiveness-based closure.

## Continual improvement

Feed monitoring, incidents, appeals, red-team findings, audit, supplier changes, and delivery friction into:

- evaluation sets;
- control design;
- platform paved roads;
- workforce training;
- policy and risk appetite;
- architecture patterns;
- investment and retirement decisions.
