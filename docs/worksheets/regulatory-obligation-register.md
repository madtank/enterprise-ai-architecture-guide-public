# Regulatory obligation register

Use this worksheet for one AI system, use case, standalone repository or
artifact, or other defined operating boundary. It connects authoritative
sources and applicability decisions to atomic obligations, implemented
controls, operating evidence, deadlines, and reassessment.

This is a controlled evidence record, not legal advice, a complete catalog of
law, a conformity assessment, a certification, or release authorization.
Qualified legal and compliance owners determine applicability and
interpretation for the relevant entities, activities, roles, jurisdictions,
and dates. Technical, risk, privacy, records, accessibility, intellectual
property, procurement, and business owners supply evidence within their
authority.

!!! danger "Unknown obligations fail closed"
    Do not treat silence, a blank row, an internal risk tier, a voluntary
    framework mapping, a supplier claim, or an AI-generated summary as proof
    that no duty applies. A clear prohibition, missed mandatory date,
    unresolved applicability question, absent accountable owner, or material
    evidence gap blocks the affected activity or release until an authorized
    decision resolves it.

Automation may find candidate sources, extract citations, detect changes, and
join evidence. It must not make a binding applicability decision, invent an
exception, waive a person's rights, or silently translate a source-specific
actor role into an enterprise role.

## Completion standard

For every potentially applicable source:

1. preserve an exact official source, status, version or consolidation, cited
   provision, and retrieval date;
2. record the legal entities, territories, source-specific actor roles,
   system characteristics, people, data, activity, and dates tested for
   applicability;
3. split applicable text into atomic obligations or prohibitions;
4. map each obligation to an accountable owner, implementation, decision
   point, evidence, timing, and operating test;
5. record gaps, lawful exclusions or derogations, and organizational
   exceptions separately;
6. reconcile the register to the exact system, release, supplier, and deployed
   state before a consequential decision; and
7. monitor official sources and material system changes, then invalidate
   affected decisions when their premises change.

Completion demonstrates a reviewable mapping. It does not prove that a control
is effective, that every source was found, or that the system complies.

## Document control

| Field | Value |
|---|---|
| Boundary / system / use-case / artifact / inventory ID | |
| System, artifact, and release version | |
| Operating boundary ID | |
| Accountable business and product owners | |
| Legal and compliance owner | |
| Privacy, records, IP, accessibility, security, and risk owners | |
| Register owner and custodian | |
| Record version and lifecycle state | Draft / Under review / Approved for stated boundary / Superseded |
| Effective date and review cutoff | |
| Source retrieval cutoff | |
| Next scheduled review | |
| Protected record location and access class | |
| Approved sanitized derivative, if any | |
| Linked system or artifact record, impact assessment, data flows, identity matrix, supplier records, and release manifest | |

Store privileged legal analysis, personal data, confidential contracts,
regulator communications, and protected incident material in approved
restricted systems. Link to a minimal evidence reference here; do not copy
sensitive contents into a broadly visible register.

## Operating boundary

### Entities, activities, and exposure

| Dimension | Exact in-scope value | Explicitly out of scope | Evidence / owner |
|---|---|---|---|
| Legal entities and business units | | | |
| Product, service, and intended purpose | | | |
| AI system and component boundary | | | |
| Development, provision, deployment, operation, use, import, distribution, or resale activities | | | |
| Users, customers, workers, affected non-users, and vulnerable groups | | | |
| Establishment, development, hosting, processing, support, sales, and use locations | | | |
| Audience, market, and external distribution channels | | | |
| Data subjects, data classes, sources, transfers, retention, and deletion paths | | | |
| Autonomy, decision, content, and action consequences | | | |
| Scale, duration, frequency, and materiality | | | |
| Sector, product-safety, professional, public-sector, or critical-service context | | | |
| Suppliers, models, datasets, tools, subprocessors, agents, and downstream integrators | | | |

Do not infer territorial scope only from the hosting region. Establishment,
market placement, offered service, affected people, monitoring, remote access,
support, onward distribution, and data transfers can each require analysis.

### Source-specific actor and responsibility map

Use each source's own defined roles. Similar labels such as provider,
developer, producer, deployer, operator, user, importer, distributor,
processor, controller, employer, publisher, or platform may carry different
meanings across sources.

| Source ID | Legal entity | Source-defined role | Triggering activity | Upstream / downstream party | Assigned enterprise owner | Contract or handoff evidence | Open role question |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

- [ ] Every source-defined role has been tested against actual conduct, not
  only the contract label or supplier's description.
- [ ] One entity holding multiple roles has each role and obligation recorded.
- [ ] Shared, transferred, and retained responsibilities are explicit.
- [ ] The map covers material downstream reuse and changed intended purpose.

## Authoritative source inventory

Record official legal text and regulator material separately from standards,
frameworks, contracts, licenses, and internal policy. A guidance page can help
interpret or monitor a requirement, but it does not replace the controlling
text.

| Source ID | Type and legal force | Issuing authority / jurisdiction | Official title and URL | Exact version, consolidation, section, or contract revision | Status and date type | Source owner | Retrieved at | Next source check | Change alert / archive evidence |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Record publication, enactment, entry-into-force, amendment, repeal, and source
status here. Store application, transition, renewal, reporting, and
event-triggered clocks in the canonical event ledger and reference its Event
IDs from applicability and obligation records.

Use types such as:

- law, regulation, binding order, permit, license, or regulator decision;
- contract, data-processing agreement, procurement term, supplier term, or
  open-source/content license;
- adopted organizational policy or mandatory control baseline;
- normative standard or conformity specification, including the law,
  regulation, order, permit, contract, or policy that gives it effect when
  applicable;
- voluntary framework, guidance, or code; and
- draft, proposal, consultation, or other non-binding horizon-scanning input.

- [ ] Official text is preferred over search results, summaries, news,
  marketing, or generated answers.
- [ ] Amendments, corrections, implementing acts, regulator decisions,
  applicable local law, and authoritative guidance are linked where needed.
- [ ] Entry into force, application, transition, reporting, renewal, and
  repeal dates are not collapsed into one “effective” date.
- [ ] Licensed standards are cited without reproducing restricted text; a
  qualified owner has access to the applicable edition before making a claim,
  and the record identifies whether law, regulation, order, permit, contract,
  or policy gives the standard legal or organizational effect.
- [ ] Drafts and voluntary materials are visibly separated from binding
  requirements unless law, regulation, order, permit, contract, or adopted
  policy gives them effect.

## Applicability determinations

Create one row per provision or coherent scope decision. Use `Applies now`,
`Applies on event or date`, `Conditionally applies`, `Does not apply`,
`Uncertain — hold`, or `Superseded`. `Does not apply` requires affirmative
rationale and evidence. Use `Uncertain — hold` when material facts or
qualified interpretation are missing.

| Decision ID | Source / provision | Territory and entity trigger | Role and activity trigger | System, data, people, scale, or sector trigger | Exclusion, threshold, or dependency tested | Applicability state | Application Event ID(s) | Reasoning and evidence | Qualified decision owner / reviewer | Decision date | Next decision review |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

Validate at least:

- the exact system definition, intended purpose, modification, integration,
  and placement or use context;
- source-defined provider, deployer, operator, importer, distributor,
  controller, processor, employer, or other roles;
- affected people, protected characteristics, children or vulnerable people,
  workers, consumers, and public-service recipients;
- personal, biometric, health, financial, employment, education, location,
  communications, confidential, copyrighted, or export-controlled data;
- consequential decisions, human review, profiling, surveillance, safety
  functions, essential services, public-interest content, and synthetic media;
- cross-border, remote access, supplier, subprocessor, onward-transfer, and
  downstream distribution facts; and
- thresholds, exemptions, exclusions, transition provisions, and dates in the
  controlling source.

## Atomic obligation register

Do not map an entire regulation, contract, or standard to one generic control.
Create a stable obligation ID for each independently testable prohibition,
precondition, duty, right, outcome, disclosure, record, deadline, or event
response.

| Obligation ID | Source / exact provision | Binding force and obligation type | Applies to entity / role / activity | Trigger and scope | Required outcome or prohibited result | Canonical Event ID(s) | Accountable interpretation owner | Approved interpretation / decision link |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Useful obligation types include:

- prohibition or restricted use;
- registration, authorization, assessment, or other precondition;
- governance, competence, human oversight, or separation of duties;
- risk, impact, quality, safety, security, privacy, or accessibility outcome;
- technical documentation, instructions, logging, records, or retention;
- transparency, disclosure, labeling, provenance, notice, or consent;
- individual or customer access, correction, objection, appeal, deletion,
  portability, support, or remedy;
- supplier, contract, audit, cooperation, or downstream flow-down;
- incident, complaint, authority, affected-party, or public reporting; and
- monitoring, reassessment, correction, withdrawal, transfer, or retirement.

Paraphrase for the operating team but retain the exact citation. A paraphrase
must not weaken a condition, exception, definition, deadline, or protected
right in the controlling source.

## Control, evidence, and effectiveness mapping

One implementation may support several obligations, and one obligation may
require several controls. Preserve both relationships; do not infer compliance
from a single policy statement or control ID.

| Obligation ID | Control / implementation ID | Enforcement or decision point | Implementation and control owner | Implementation state | Test ID and result | Evidence ID(s) | Gap / remediation owner and date | Obligation disposition |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Use implementation states such as `Planned`, `Partial`, `Implemented`,
`Operating`, and `Retired`. Use obligation dispositions such as `Open`,
`Hold`, `Conditionally ready`, `Ready for stated decision`, and `Superseded`.
These are workflow states, not compliance claims.

### Evidence register

| Evidence ID | Obligation / control IDs | Design / implementation / operating / decision evidence | Exact artifact, revision, period, and digest | Method, result, coverage, and limitations | Evidence owner | Verifier and independence | Access, retention, and legal-hold treatment | Evidence state / expiry |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Use evidence states such as `Absent`, `Pending`, `Current — pass`, `Current —
fail / hold`, `Stale / hold`, `Unavailable / hold`, and `Superseded`. A
passing artifact has meaning only for its stated scope, revision, method,
period, and limitations.

Use evidence that distinguishes:

1. **design:** the implementation could satisfy the mapped outcome in the
   actual architecture;
2. **implementation:** it exists on every in-scope path and resists bypass;
3. **operation:** it worked over a representative period, including failures,
   overrides, complaints, and exceptions; and
4. **decision:** an authorized owner reviewed the evidence for the exact
   obligation, system state, and date.

Evidence references should identify the system, release or configuration,
control, source obligation, time period, owner, integrity protection, access
class, retention, and verification result. Minimize prompts, outputs,
identifiers, and personal data; a legal record requirement does not authorize
unbounded collection.

## Coverage challenge

Mark each domain `Screened — no candidate source`, `Candidate source found`,
`Applicable obligations mapped`, or `Uncertain — hold`. These prompts are not
a universal list of laws.

| Domain | Screening questions | Status | Source / decision IDs | Owner / next action |
|---|---|---|---|---|
| AI-specific rules | Definitions, actor roles, prohibited practices, high-impact or high-risk classification, general-purpose models, transparency, documentation, monitoring, incident, and registration duties? | | | |
| Privacy and data protection | Purpose and authority, sensitive data, automated decisions, profiling, biometrics, surveillance, notices, rights, impact assessments, minimization, retention, deletion, transfers, and subprocessors? | | | |
| Equality, civil rights, and fairness | Discrimination, protected groups, accommodations, testing, notices, adverse decisions, review, and remedy? | | | |
| Consumer, competition, and communications | Deception, unfair practices, endorsements, advertising, public-interest content, marketing claims, impersonation, recording, or communications rules? | | | |
| Employment and workforce | Hiring, management, monitoring, consultation, notice, collective rights, workplace safety, or professional accountability? | | | |
| Accessibility and inclusion | Digital service, communications, document, product, procurement, and reasonable-accommodation duties? | | | |
| Safety, product, and critical services | Product safety, medical or other regulated product, machinery, essential service, critical infrastructure, operational resilience, or sector approval? | | | |
| Cybersecurity and incident reporting | Security baseline, vulnerability handling, material incident, authority, customer, affected-person, insurer, or contractual reporting windows? | | | |
| Data, content, and intellectual property | Copyright, database, patent, trade secret, trademark, publicity, confidentiality, training or input rights, output use, attribution, provenance, and takedown? | | | |
| Children and vulnerable people | Age assurance, parental authority, design, profiling, content, exploitation, safety, support, reporting, and heightened-rights duties? | | | |
| Records and evidence | Decision, model, data, consent, notice, approval, complaint, incident, audit, retention, deletion, legal hold, privilege, and regulator-access duties? | | | |
| Procurement, supplier, and contract | Public procurement, regulated outsourcing, audit, data use, subprocessor, change, service, incident, IP, evidence, flow-down, and exit terms? | | | |
| Trade, export, sanctions, and restricted parties | Model, weights, software, cryptography, technical data, destination, end-user, end-use, support, publication, and reporting restrictions? | | | |
| Environment and resource use | Energy, water, emissions, reporting, efficiency, siting, hardware, or supply-chain obligations? | | | |
| External distribution | License, privacy, security disclosure, claims, accessibility, terms, support, vulnerability, dual-use, export, sanctions, correction, withdrawal, and persistent-copy duties? | | | |

## Canonical date and event clock ledger

This is the authoritative clock ledger for the register. Source publication
or entry-into-force status remains in the source inventory; applicability
decisions, atomic obligations, rights, notices, and incident records reference
stable Event IDs here rather than maintaining independent deadline copies.

| Event ID | Source / obligation | Date type and timezone | Trigger / calculation rule | Required preparation or deliverable | Dependency | Accountable owner | Alert lead time | Status / evidence |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

- [ ] Dates come from the current controlling text or authoritative decision,
  not a remembered timeline.
- [ ] Staggered, role-specific, transitional, renewal, periodic, and
  event-triggered dates remain separate.
- [ ] The owner has alerts early enough to change design, contracts, data,
  training, documentation, or market availability.
- [ ] Missed or uncertain mandatory dates create a hold and escalation, not an
  automatically accepted exception.

## Rights, notices, and regulatory events

| Request or event | Source / obligation IDs | Canonical Event ID(s) / threshold | Recipient plus initial / supplemental content | Intake, identity validation, human decision, and appeal | Systems, suppliers, backups, and downstream propagation | Evidence, owner, and tested date |
|---|---|---|---|---|---|---|
| Access, correction, objection, deletion, portability, opt-out, contest, or remedy | | | | | | |
| Complaint or affected-person report | | | | | | |
| Security, privacy, safety, or AI incident | | | | | | |
| Regulator, court, auditor, or law-enforcement request | | | | | | |
| Mandatory disclosure, registration, certification, or renewal | | | | | | |
| Product correction, recall, withdrawal, suspension, or public notice | | | | | | |

Exercise each material path without exposing unnecessary personal,
confidential, privileged, security-sensitive, or regulator-restricted
material.

## Supplier and downstream obligations

| Obligation ID | Upstream / downstream party and source-defined role | Responsibility retained by enterprise | Required term, instruction, evidence, or flow-down | Monitoring / change notice | Failure, suspension, exit, and records path | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] Contract language matches actual technical behavior and actor roles.
- [ ] Supplier evidence scope, service, period, exclusions, and assessor are
  known; a badge or generic certification is not substituted for the duty.
- [ ] Mutable models, policies, regions, subprocessors, data uses, and terms
  have change detection and a reassessment owner.
- [ ] Exit preserves required evidence while removing obsolete data,
  credentials, permissions, routes, and integrations.
- [ ] Downstream instructions and restrictions survive export, embedding,
  API use, fine-tuning, agent delegation, and external distribution where
  required.

## Concurrent sources and conflicts

`Use the strictest rule` is not a sufficient conflict method. Requirements can
apply to different entities or activities, protect different interests, have
different legal priority, or be impossible to satisfy simultaneously.

| Conflict ID | Source and obligation IDs | Overlap, conflict, or ambiguity | Hierarchy, territory, role, contract, and rights analysis | Technical / operational resolution | Interim hold or containment | Qualified decision owner / date | Reassessment trigger |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

- [ ] A mapping never narrows a stricter applicable outcome without an
  authorized source-based decision.
- [ ] Contract or policy does not claim to waive a non-waivable duty or right.
- [ ] The architecture supports per-entity, region, role, user, data, and
  channel treatment where one global behavior is insufficient.
- [ ] Unresolved conflict blocks the affected path and has a named escalation.

## Source-based exclusions and derogations

A source-based exclusion, exemption, alternative, or derogation exists only
when the controlling source provides it and a qualified owner confirms the
facts and conditions.

| Record ID | Source / exact provision | Applicability decision / obligation IDs | Exclusion, exemption, alternative, or derogation | Triggering facts and conditions | Qualified rationale and evidence | Decision owner / date | Recheck and invalidation trigger |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

The record becomes invalid when a threshold, entity, role, territory, purpose,
system fact, date, or other relied-on condition changes.

## Organizational exceptions and residual risk

An organizational policy exception or residual-risk acceptance is an internal
governance decision. It cannot waive law, regulator authority, contract
rights, or affected-person rights. A control failure does not become lawful
because it is labeled an exception.

Each residual-risk decision names exactly one authority for a risk category
that adopted policy reserves or delegates to that authority. If different
categories have different reserved authorities, record separate decisions and
require all of them at the consuming gate. Required discipline rows are
inputs, not votes. Exception authority does not confer residual-risk or
release authority.

| Exception ID | Obligation / control ID | Policy authority and exact scope | Unmet internal outcome | Prohibition, missing-right, mandatory-duty, and applicability check | Compensating controls, monitoring, and stop conditions | Exception authority | Linked residual-risk decision IDs, categories, exact scopes, named authorities and bases, results, expiries, and invalidation states | Effective / expiry | Remediation owner / date / status |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

- [ ] The exception authority and every linked residual-risk decision
  authority each hold the required category-bound authority and are separate
  from the requester where policy requires.
- [ ] Every linked residual-risk decision is current, attributable,
  category-bound, exact-scope-bound, unexpired, and not invalidated or
  superseded.
- [ ] Prohibitions, absent rights, missed mandatory duties, and unresolved
  applicability are not bypassed through an exception or risk acceptance.
- [ ] Expiry automatically reopens the obligation and blocks the affected
  activity unless renewed through an authorized review.

## Change monitoring and reassessment

Reassess on both source change and factual change.

| Trigger | Monitoring source / system | Detection owner | Affected decision / obligation IDs | Immediate containment | Reassessment SLA | Last test / evidence |
|---|---|---|---|---|---|---|
| Official amendment, repeal, correction, implementing measure, court or regulator decision, guidance, or deadline change | | | | | | |
| Legal entity, market, territory, audience, source-defined role, or distribution-channel change | | | | | | |
| Purpose, user, affected population, consequence, scale, autonomy, or human-review change | | | | | | |
| Model, data, prompt, route, tool, agent, supplier, subprocessor, region, retention, or contract change | | | | | | |
| Incident, complaint, rights request, enforcement action, audit finding, control failure, or missed deadline | | | | | | |
| New evidence that invalidates a classification, exclusion, assurance claim, or accepted interpretation | | | | | | |

Maintain a change log:

| Date | Source or factual change | Decisions and obligations invalidated | Interim action | Owner | New approval / evidence |
|---|---|---|---|---|---|
| | | | | | |

## Decision and release handoff

### Reconciliation

- [ ] The system boundary, legal entities, roles, jurisdictions, users,
  affected people, data flows, suppliers, channels, and exact release match
  this register.
- [ ] Every identified candidate source has a reviewed applicability decision;
  coverage-domain screening and any discovery uncertainty are recorded
  separately; every applicable obligation has an owner and implementation
  path.
- [ ] Prohibitions and preconditions pass before lower-priority controls.
- [ ] Required notices, instructions, registrations, assessments, contracts,
  records, training, human oversight, tests, and event paths are ready.
- [ ] Design, implementation, and operating evidence is current for the
  consequence and lifecycle stage.
- [ ] No uncertain applicability, missed deadline, unapproved exclusion,
  expired exception, unresolved conflict, or material control gap remains on
  the affected path.
- [ ] Register changes are propagated to the system card, impact assessment,
  threat model, data records, supplier records, evaluation plan, readiness
  review, runbooks, incident plan, and
  [transfer, decommissioning, and retirement record](transfer-decommissioning-and-retirement.md).

### Register decision

- **Decision:** Ready for the stated boundary / Ready with conditions /
  Hold / Reject
- **Exact system, release, entities, roles, territories, activities, and
  channels covered:**
- **Material assumptions and uncertainties:**
- **Conditions and stop triggers:**
- **Open remediation and due dates:**
- **Next review and source-monitoring cadence:**

This decision closes only the register review. Production release, external
distribution, residual-risk acceptance, and independent approval remain
separate decisions under the applicable
[production readiness](production-readiness-review.md) and
[public-release](public-release-readiness.md) gates.

### Sign-off

| Role | Name / team | Decision and scope | Date | Evidence / conditions |
|---|---|---|---|---|
| Legal and compliance applicability owner | | | | |
| Privacy / data protection owner, when applicable | | | | |
| Records / information governance owner, when applicable | | | | |
| IP / licensing / trade owner, when applicable | | | | |
| Accessibility / civil-rights / responsible-AI owner, when applicable | | | | |
| Security / incident owner, when applicable | | | | |
| Business / product / system owner | | | | |
| Residual-risk record verifier, when a permitted risk remains; acknowledge linked category-bound decision IDs only and create no embedded acceptance | | | | |
| Qualified independent reviewer, when required | | | | |
| Organizational exception authority, if policy permits | | | | |

## Source boundary

**Source check:** 2026-07-28.

- [NIST AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
  calls for AI-related legal and regulatory requirements to be understood,
  managed, and documented in Govern 1.1 and for context-specific laws and
  expectations to be documented in Map 1.1. The framework is voluntary and is
  being revised; it does not determine applicability or compliance.
- The [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/)
  supplies voluntary candidate actions. NIST states that it is not a universal
  checklist or ordered implementation method.
- [NIST Privacy Framework 1.0](https://www.nist.gov/publications/nist-privacy-framework-tool-improving-privacy-through-enterprise-risk-management)
  is a voluntary privacy-risk framework, not a legal test. On the check date,
  NIST still described version 1.1 as an Initial Public Draft.
- [Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
  has applied since 2018-05-25 when its fact-specific scope is met and
  illustrates a concurrent privacy and data-protection overlay. Actor roles,
  Member-State overlays, amendments, and regulator guidance require current
  review; satisfying an AI-specific obligation does not establish that a
  privacy obligation is satisfied.
- [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en)
  is an example of binding, role- and date-specific AI regulation when its
  scope applies. It was amended by
  [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj),
  which EUR-Lex records as in force. Use the current official text and the
  [European Commission implementation page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
  for change monitoring, then obtain qualified advice; a Commission summary
  does not replace the enacted text.
- The
  [Council of Europe Framework Convention on AI](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence)
  illustrates why treaty signature, ratification, territorial scope, and
  implementing measures must be recorded separately.

Each organization must add the exact applicable national, subnational,
sector, safety, privacy, civil-rights, employment, consumer, accessibility,
cybersecurity, records, IP, trade, procurement, contract, and regulator
sources for its operating boundary. Recheck official sources after material
change and on the adopted legal-review cadence; a quarterly guide-level source
check is not a substitute for a shorter statutory or event deadline.
