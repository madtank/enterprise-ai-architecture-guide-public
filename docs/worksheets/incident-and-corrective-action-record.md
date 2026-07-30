# Incident and corrective-action record

Use this record for material incidents, defects, vulnerabilities,
nonconformities, complaints, and near misses. Restrict sensitive records and
link to them rather than copying protected details into a broadly visible
document.

!!! danger "Do not collapse authority"
    Incident command, service operation, repository custody, change
    implementation, technical approval, release authorization, deployment
    execution, observed-state verification, notification, incident closure,
    and corrective-action closure are distinct duties. One person may hold
    compatible roles only where adopted policy permits it; record each duty
    separately and preserve required independence.

## Identification and ownership

- **Incident / issue ID:**
- **Issue type:**
- **Detected / reported at:**
- **Environment and affected releases:**
- **Severity and rationale:**
- **Incident commander, accepted backup, contact, and authority source:**
- **Technical investigation owner:**
- **Business / product impact owner:**
- **Security / privacy / data / risk / legal owners:**
- **Problem owner:**
- **Corrective-action / control owner and closure authority:**
- **Required independent effectiveness verifier:**
- **Update channel and frequency:**

## Affected-boundary ownership map

Record stable IDs in both tables. A service can depend on several repositories,
and a repository can affect several services. Do not infer ownership from the
person who contributed code, acknowledged an alert, or executed a deployment.
These tables are the canonical affected-entity and ownership scope for this
incident. Later sections reference their stable IDs rather than redefining
owners.

| Service / system ID and affected release | Impact and current operating state | Service owner, on-call, accepted backup, and contact | Restoration-acceptance authority and readback owner | Evidence |
|---|---|---|---|---|
| | | | | |

| Repository / artifact ID and affected revision | Affected service ID and relationship / path | Repository owner, maintainer / triage primary, accepted backup, and contact | Fix / change owner and applicable code owners / reviewers | Handoff state, accepted time, limits, and evidence |
|---|---|---|---|---|
| | | | | |

Use one repository row per service-to-repository edge. A shared repository
therefore appears once for each assessed service, including an attributable
`unaffected` decision where applicable.

## Decision rights and accepted handoffs

Use one row for each material duty and each distinct boundary. A handoff is not
complete until the receiving primary or backup accepts the exact scope, limits,
time, and evidence. Keep the prior holder and escalation active while
acceptance is missing, ambiguous, or expired. This table is the canonical
authority and handoff register; later sections reference its row IDs and
evidence rather than restating role holders.

| Duty / decision and row ID | Scoped service, repository, artifact, or release | Accountable authority, accepted backup, and contact | Executor / verifier and required separation | Authority source, handoff state / time, and evidence |
|---|---|---|---|---|
| Severity and incident command | | | | |
| Containment / shutdown | | | | |
| Service restoration acceptance | | | | |
| Repository repair triage and change ownership | | | | |
| Technical repair acceptance | | | | |
| Merge | | | | |
| Release `go`, `hold`, `abort`, or promotion | | | | |
| Deployment, rollback, or compensation execution | | | | |
| Observed-state readback and reconciliation | | | | |
| Applicability, notification, and communications | | | | |
| Incident closure | | | | |
| Corrective-action criteria and treatment | | | | |
| Corrective-action effectiveness verification | | | | |
| Corrective-action `close` or `keep open` | | | | |

No row creates authority for another row. In particular, incident authority
does not grant ordinary repair, merge, or release approval; repository or code
ownership does not grant service-restoration or incident-closure authority;
and execution does not prove its own result where independent readback is
required.

## Impact

- **Expected behavior:**
- **Observed behavior:**
- **Affected people, tenants, records, actions, or transactions:**
- **Actual and potential harm:**
- **Data and authorization impact:**
- **Availability, quality, cost, regulatory, and contractual impact:**
- **Start, detection, containment, and restoration times:**
- **Safe workaround or recourse:**

## Timeline

| Time | Observation or action | Actor | Evidence / decision |
|---|---|---|---|
| | | | |

Separate confirmed facts, working hypotheses, and unknowns.

## Containment and restoration

- **Containment actions:**
- **Credentials, tools, routes, artifacts, or sources disabled:**
- **Rollback target or fallback:**
- **Forward recovery / compensation:**
- **Actual state readback:**
- **Residual impairment or temporary risk:**
- **Workaround owner and expiry:**

### Emergency change, when used

- **Emergency change required:** yes / no
- **Incident ID, decision ID, exact action, and target:**
- **Emergency authority and separate executor:**
- **Why ordinary gates cannot meet the required response time:**
- **Before-state evidence and preservation limitation:**
- **Time-bounded identity, scope, expiry, and revocation evidence:**
- **Stop, rollback, forward-recovery, and compensation path:**
- **Observed-state readback owner, result, and evidence:**
- **Unavoidable evidence gaps and residual uncertainty:**
- **Owner and deadline for normal tests, protected review, documentation,
  merge or revert, and corrective action:**
- **Retrospective ordinary release decision ID, release owner, exact candidate,
  and operating envelope, or revert decision:**
- **Final deployment / revert and observed-state readback record:**

Use the
[emergency-change process](../delivery/code-deployment.md#emergency-changes).
Emergency authority is limited to the recorded containment or restoration
action; it does not approve an ordinary fix, merge, general release, or later
promotion.

By the retrospective deadline, any emergency change still present must either
be reverted or packaged as an exact reviewed release candidate and receive the
ordinary release-owner decision, deployment and readback reconciliation, and
operating-envelope record. Merge or completed review alone does not normalize
production state.

### Containment, restoration, and rerelease readback

Record the exact desired and observed state for each applicable checkpoint.
Unknown, stale, mismatched, or ambiguously committed side effects force hold
and reconciliation. Include at least the applicable release manifest,
configuration, route or model, extension, data or migration, identity or
authority, cohort, fallback, and known side-effect state.

| Checkpoint / action | Exact desired state and authority record | Observed state, time, and authoritative source | Match, gap, side effects, and disposition | Readback owner and evidence |
|---|---|---|---|---|
| Containment | | | | |
| Rollback or forward recovery | | | | |
| Service restoration | | | | |
| Fix rerelease / promotion | | | | |

## Evidence

- **Source, build, release, and deployment identifiers:**
- **Model, prompt, policy, data, index, tool, and workflow revisions:**
- **Agent execution and telemetry contract ID / schema / deployed revisions:**
- **Authorization, approval, and side-effect records:**
- **Sanitized logs, traces, screenshots, or samples:**
- **Missing-event, integrity, unknown-outcome, quarantine, and reconciliation
  evidence:**
- **Artifact checksums / signatures / custody:**
- **Redaction, access, retention, and legal-hold treatment:**

## Reproduction and diagnosis

- **Minimal reproducer or statistical replay:**
- **Pre-fix failing test / evaluation:**
- **Immediate technical trigger:**
- **Contributing technical factors:**
- **Process, ownership, human, supplier, or organizational factors:**
- **Why prevention did not block the issue:**
- **Why detection did or did not find it sooner:**
- **Why containment and recovery took the observed time:**
- **Related systems or repositories examined:**

## Fix and verification

- **Affected repository / artifact and decision-rights row IDs:**
- **Accepted repair-handoff evidence IDs:**
- **Fix PR and reviewed commit:**
- **Applicable code owners and required independent reviewers:**
- **Regression, negative, adversarial, and integration checks:**
- **Migration and recovery verification:**
- **Evidence that required checks were not weakened:**
- **Staging or replay result:**
- **Exact fix release decision ID, release owner, conditions, and expiry:**
- **Deployment operator and authoritative deployment record:**
- **Post-fix readback owner, result, time, and evidence:**
- **Service restoration acceptance and residual limits:**

## Notifications and remedy

- **Regulatory obligation register version / snapshot digest:**
- **Applicable or potentially applicable obligation IDs / canonical Event
  IDs:**
- **Occurrence, detection, awareness, confirmation, and materiality-decision
  times:**
- **Incident-instance clock-start fact / time:**
- **Calculated due time, timezone, recipient, and escalation under the
  canonical Event rule:**
- **Required initial and supplemental content:**
- **Supplier, insurer, customer, and downstream notification dependencies:**
- **Qualified applicability and notification decision owner / evidence:**
- **Internal notifications:**
- **Customer or affected-person communication:**
- **Regulatory, contractual, insurer, or supplier notification:**
- **Correction, appeal, refund, transaction repair, or other remedy:**
- **Disclosure restrictions and approval:**

The incident commander records and preserves facts but does not infer legal or
contractual applicability. If the qualified decision is pending, use the
earliest plausible clock for escalation and preserve the hold.

## Corrective and preventive actions

| Action ID and affected service / repository IDs | Type, treatment, due date, and state | Implementation primary / backup and accepted custody | Corrective-action / control owner and closure authority | Predeclared criteria, verifier, evidence, and reopen trigger |
|---|---|---|---|---|
| | corrective / preventive | | | |

Possible actions include tests, evaluation cases, tool restrictions,
authorization, skills, instructions, CI policy, architecture, monitoring,
runbooks, ownership, training, supplier terms, and sibling-system review.

Freeze effectiveness criteria, baseline, scope, observation period, and
required verifier relationship before results are known. A merged fix or
scheduled review is not effectiveness evidence.

## Incident closure

- [ ] Acceptable service is restored.
- [ ] Affected data, transactions, and people are addressed.
- [ ] Required notifications and recourse are complete.
- [ ] Every identified risk is either demonstrably remediated by the released
  permanent fix or, where adopted policy permits retention, links every
  applicable current category-bound decision ID with exact scope, named
  authority and authority basis, result, conditions, validity state, expiry,
  invalidation triggers, and supersession.
- [ ] Every affected service has an accepted restoration readback and named
  restoration authority.
- [ ] Open corrective and preventive actions have identifiers, owners, due
  dates, accepted custody, evidence criteria, independent-verification
  requirements, and closure authority.
- [ ] Inventory, system card, runbooks, tests, skills, and architecture records
  are updated.
- [ ] Evidence is retained and protected under policy.

Incident closure does not close an associated corrective or preventive action.

| Service / system ID | Restored and accepted operating state | Accepting service authority | Linked residual-risk decision IDs, categories, exact scopes, results, conditions, validity states, and expiries | Readback and evidence date |
|---|---|---|---|---|
| | | | | |

- **Incident closure decision ID and time:**
- **Named incident-closure authority:**
- **Authoritative decision:** close / keep open
- **Restoration readback IDs and result:**
- **Open problem, corrective-action, notification, recourse, and residual-risk
  IDs with accepted custody:**

The service-restoration and incident-closure authorities verify linked
residual-risk records; they do not create an embedded acceptance or inherit
the recorded risk authority. A missing, expired, invalidated, out-of-category,
or out-of-scope required decision keeps closure open.
- **Decision evidence and conditions:**

| Supporting role | Name | Approval, advice, or duty acknowledgement | Date and evidence | Conditions / open actions |
|---|---|---|---|---|
| Service / product owner(s) | | | | |
| Repository owner(s), maintainer(s), and fix owner(s) | | | | |
| Security / privacy / risk / legal, if required | | | | |
| Communications / support, if required | | | | |

Supporting rows do not create competing closure decisions. The named incident
authority records the single authoritative decision after required service
restoration, notification, remedy, evidence, and custody conditions are met.

## Corrective-action effectiveness and closure

Complete this section separately for each corrective or preventive action.

- [ ] The action is implemented on the real operating path.
- [ ] The effectiveness method, baseline, scope, observation period, success
  threshold, and verifier relationship were frozen before results were known.
- [ ] The effectiveness check has been completed; it is not merely scheduled.
- [ ] Results and required independent review are linked.
- [ ] Failed, inconclusive, overdue, or regressed actions remain open and are
  revised or escalated.

| Action ID and affected boundaries | Implementation owner / backup and real-path evidence | Frozen baseline, criteria, scope, observation period, verifier, and result | Control-owner `close / keep open` decision, time, and evidence | Reopen triggers |
|---|---|---|---|---|
| | | | | |

| Supporting role | Name | Approval, advice, or duty acknowledgement | Date and evidence | Conditions / follow-up |
|---|---|---|---|---|
| Independent verifier, if required | | | | |
| Affected service and repository owners | | | | |
| Security / risk / legal, if required | | | | |

Only the named corrective-action or control owner records `close` or `keep
open` after the required effectiveness result. Failed, inconclusive, stale,
incomplete-period, overdue, or regressed evidence remains open. Closing one
action does not close sibling actions or the incident.
