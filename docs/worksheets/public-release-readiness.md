# Public-release readiness record

Use this record for one exact external-distribution candidate. It is an
evidence index and decision record, not legal advice, certification, or a
substitute for reviewing the artifact.

Follow the
[public release and external distribution gate](../delivery/public-release-and-external-distribution.md).

## R0–R5 result contract

Use only **Pass / Fail / N/A / Unknown / Stale** in the authoritative result
register below. Every R0–R5 checklist item and every applicable artifact or
review row is a separate control row; do not collapse several outcomes into a
favorable gate summary.

- **Pass** requires present, current, unexpired evidence bound to the exact
  candidate, manifest, distribution boundary, and control row.
- **Fail** means the control was evaluated and its requirement was not met.
- **N/A** requires a documented applicability test, rationale, accountable
  owner, date, and evidence or policy basis showing that the control trigger
  is absent. Missing evidence, ownership, review capacity, or unresolved
  applicability is not N/A.
- **Unknown** means the row was not evaluated or its evidence, owner, scope,
  or conclusion is missing, ambiguous, conflicting, or unbound.
- **Stale** means the evidence or result expired, was invalidated, or no
  longer represents the frozen candidate or distribution boundary.

A blank, omitted, conflicting, expired, or unbound result is **Unknown** or
**Stale**, never an implicit Pass. Any **Fail**, **Unknown**, or **Stale**
result forces the candidate to **Hold** and forbids a publication-ready
status. Checklist boxes are review prompts, not authoritative result state;
do not infer Pass from a checked box or narrative.

R0–R5 is non-authorizing. Only R6 may decide a policy-permitted exception to
a known, evidenced, exception-eligible Fail. R6 cannot relabel, backfill, or
rewrite an R0–R5 result as Pass or publication-ready; the underlying Fail and
Hold disposition remain visible and linked to any conditional decision.

## Release identity

- **Release ID:**
- **Artifact or repository name:**
- **Purpose and expected value:**
- **Audience and locations:**
- **Distribution class:** controlled internal / customer or partner / public /
  open-source or open-data / other
- **Channel, registry, repository, and canonical URL:**
- **Source revision:**
- **Frozen manifest URI and digest:**
- **Candidate artifact digest:**
- **Reachable history and metadata scope:**
- **Release window and expiry, if temporary:**
- **Lifecycle state after release:**
- **Risk tier and material-change triggers:**

## Roles and decisions

| Role | Accountable person or team | Accepted duty | Decision required | Date |
|---|---|---|---|---|
| Content / product owner | | | | |
| Repository / artifact owner | | | | |
| Data / privacy owner | | | | |
| Security / vulnerability owner | | | | |
| Legal / IP / trade-compliance owner | | | | |
| Responsible-AI / risk owner | | | | |
| Distribution operator | | | | |
| Support / incident / takedown owner | | | | |
| Qualified independent approver | | | | |
| Exception authority, if policy permits | | | | |
| Backup or continuity owner | | | | |

## Distribution manifest

List every exposed surface, including repository history, workflow logs,
generated output, examples, downloadable objects, metadata, and third-party
services.

| Artifact or surface | Exact version / digest / history scope | Distribution mode | Classification and rights | Scan / review evidence | Owner |
|---|---|---|---|---|---|
| Source, reachable history, LFS objects, and submodules | | | | | |
| Generated site or documentation | | | | | |
| Workflow history, job summaries, logs, and artifacts | | | | | |
| Release assets and downloadable archives | | | | | |
| Package, image, binary, or installer | | | | | |
| Model, adapter, tokenizer, or configuration | | | | | |
| Dataset, benchmark, feature, embedding, or index | | | | | |
| Prompt, policy, skill, tool, MCP, or schema | | | | | |
| Evaluation, assurance, or security artifact | | | | | |
| Trace, transcript, telemetry, or support example | | | | | |
| Image, audio, video, diagram, or other media | | | | | |
| License, notices, claims, support, and security policy | | | | | |
| Channel, domain, analytics, forms, and embedded services | | | | | |

Use one distribution mode per item: public bytes, public metadata or card
only, controlled access, or private and blocked.

## Artifact-specific conditional evidence

Complete the applicable record for every artifact instance. Link a dedicated
model card, dataset card, extension assessment, evaluation report, privacy
assessment, or threat model when it carries the detail. A class marked not
applicable requires a rationale; blank or unknown evidence blocks release.

| Artifact class | Minimum conditional evidence |
|---|---|
| Model, adapter, or tokenizer | Base artifact and digest; tokenizer, configuration, and custom code; training or fine-tune lineage; serialization and safe-load method; integrity, backdoor, memorization, privacy, capability, dual-use, inherited-term, and accountable trade-review results |
| Prompt or policy | ID, digest, role, scope, precedence, variables, defaults, supported model/context/tool assumptions, source rights, injection and conflict or regression results, and confirmation that secrets and deterministic authorization remain outside prompt text |
| Evaluation or assurance artifact | Claim or risk addressed; practice, validation, public, or holdout designation; future-use and contamination decision; inputs and rights; oracle, scorer, grader model and prompt; tools, network, repetitions, uncertainty, gaming risks, and restricted-access alternative |
| Dataset, benchmark, embedding, or index | Source snapshot, owner, rights or consent and purpose; schema, population, collection, transformations, splits, filtering and synthetic method; ACL assumptions; embedding model and chunking recipe; quality, bias, poisoning, reconstruction, membership, linkage, re-identification, correction, and deletion-propagation results |
| Skill, tool, plugin, or MCP package | Full package and digest; source, binary, dependency, install and startup surface; protocol revision and negotiated capabilities; tools, resources, schemas and consequence classes; file, process, network, data, and credential access; OAuth audience/scopes and session handling; dynamic-list changes, sandbox and abuse tests, update, disable, rotation, and revocation path |
| Trace, transcript, or telemetry example | Purpose, real or synthetic source, schema, time range, field classification, exact minimization and transformation methods, linkage and re-identification results, participant and third-party authority, holdout impact, embedded-instruction review, and confirmation that raw hidden reasoning and recoverable sensitive content are excluded |
| Generated text, image, audio, video, or public-interest media | Source and media rights, subject consent, AI disclosure, provenance or content credentials where required, impersonation and fraud review, minors or intimate-content treatment, accessibility, reporting, moderation, and takedown evidence |
| Security research, advisory, proof of concept, or vulnerability evidence | Affected owner and third parties, private report, severity and exploitability, fix or mitigation status, embargo and coordinated-disclosure decision, CVE or advisory path where applicable, and review that live targets, secrets, working bypasses, and unnecessary weaponization detail are excluded |

| Artifact instance | Class | Distribution mode | Pass / fail / N/A | Evidence URI | Owner | N/A rationale or limitation |
|---|---|---|---|---|---|---|
| | | | | | | |

## R0 — Charter

- [ ] Purpose, value, audience, locations, channel, and onward-sharing model
  are explicit.
- [ ] Accountable owners accepted the duties above.
- [ ] The release class and risk tier determine required reviews.
- [ ] Support, security reporting, correction, takedown, and end-of-life
  expectations are defined.
- [ ] A private-to-public repository change includes a current review of
  history, logs, forks, rules, plan features, and platform visibility effects;
  rules disabled by the transition are re-established or replaced and their
  intended review, required-check, bypass, and push behavior is tested before
  the public repository is treated as governed.

**Evidence and open findings:**

## R1 — Frozen distribution unit

- [ ] One manifest enumerates every artifact, dependency, exposed surface,
  history range, metadata object, and channel setting.
- [ ] The source revision and enterprise-built artifacts are immutable or
  identified by digest.
- [ ] Mutable services or aliases record observed identity, limitation,
  change monitor, sentinel, and fallback.
- [ ] The artifact was assembled from the intended source in a clean
  environment.
- [ ] Decision and scan results will be invalidated by a material candidate
  change.

**Manifest and build evidence:**

## R2 — Clean-artifact scrub

### Secrets, private material, and data

- [ ] The exact candidate, reachable history, logs, archives, attachments, and
  metadata passed secret and credential review.
- [ ] No live token, key, cookie, connection string, signing material, or
  recoverable secret remains.
- [ ] Customer, employee, contributor, or other personal and confidential data
  is absent or explicitly authorized for the public purpose.
- [ ] Private prompts, system or developer instructions, raw transcripts,
  hidden reasoning, support cases, and unapproved traces are absent.
- [ ] Internal paths, hostnames, account or tenant identifiers, ticket numbers,
  email addresses, private links, and environment topology are absent or
  approved.
- [ ] Hidden text, Unicode controls, comments, front matter, source maps,
  attachment content, and media metadata were inspected.
- [ ] Training, retrieval, feedback, memory, cache, index, evaluation, and
  telemetry records match the approved data purpose.
- [ ] Drafts, unrelated files, raw research captures, and unapproved
  third-party material are excluded.

### Executable and supply-chain behavior

- [ ] Binaries, serialized objects, macros, notebooks, scripts, hooks,
  installers, and auto-executing examples were inventoried and inspected.
- [ ] Skills, plugins, helpers, tools, MCP servers, startup commands,
  permissions, destinations, and transitive dependencies passed admission.
- [ ] Dynamic download, shell construction, obfuscation, encoded payload,
  upload, background-process, and repository-poisoning risks were assessed.
- [ ] Workflow permissions, triggers, publishing credentials, package names,
  registry namespaces, and mutable dependencies are protected.
- [ ] Vulnerability, malware, dependency, license, provenance, and policy
  findings meet the release thresholds.
- [ ] Appropriate SBOM, AI component or bill-of-materials, model and data
  inventory, checksums, signatures, and provenance evidence are included and
  independently verified.
- [ ] Scan limits and false-negative assumptions are recorded; manual review
  was not replaced by a score.

### Channel and presentation

- [ ] Canonical URLs, redirects, downloads, robots, indexing, analytics,
  cookies, forms, embeds, and domains match the approved channel.
- [ ] Navigation, keyboard use, structure, contrast, alternative text,
  captions, documents, tables, diagrams, and support paths passed the
  applicable accessibility review.
- [ ] Security, privacy, rights, safety, accuracy, and support reporting paths
  are visible and tested.

| Scrub or review | Tool / method and version | Scope | Result | Finding owner / closure | Evidence URI |
|---|---|---|---|---|---|
| Secret and history scan | | | | | |
| Personal / confidential data review | | | | | |
| Hidden content and metadata review | | | | | |
| Malware / binary / serialization review | | | | | |
| Dependency and vulnerability review | | | | | |
| License / provenance review | | | | | |
| Skill / tool / MCP behavior review | | | | | |
| Manual content and artifact review | | | | | |
| Accessibility / visual review | | | | | |

## R3 — Rights and obligations

- [ ] The boundary-specific
  [regulatory obligation register](regulatory-obligation-register.md) is
  current; this section records the exact release-specific delta rather than
  creating a competing source of truth.
- [ ] Applicable jurisdictions, organizational roles, audience locations,
  contracts, supplier terms, policies, and review date are recorded.
- [ ] The publisher has authority to distribute every code, model, dataset,
  media, mark, example, and derivative in the manifest.
- [ ] The owner selected explicit reuse terms or approved
  restricted-distribution terms; automation did not select a license.
- [ ] Required attribution, notices, source offers, copyright, patent, and
  trademark treatment are complete.
- [ ] Model, dataset, benchmark, provider, and API terms permit the intended
  hosting, modification, commercial use, and onward distribution.
- [ ] Personal-data purpose, notice, authority, minimization, access,
  correction, deletion, retention, cross-border, and records duties are
  resolved.
- [ ] Export, sanctions, sector, procurement, accessibility, child-safety,
  content, and disclosure applicability was decided by the accountable owner.
- [ ] AI assistance, provenance, and third-party contributions are disclosed
  as required without implying authorship or rights clearance.
- [ ] No unresolved right, prohibition, or applicable duty is being treated as
  permission.

| Frozen register version / snapshot digest | Applicability decision ID / obligation ID | Exact release or channel delta | Artifact-specific treatment | Decision owner | Evidence |
|---|---|---|---|---|---|
| | | | | | |

## R4 — Security, vulnerability, and misuse

- [ ] The threat model covers public recipients, mirrors, dependency
  substitution, package or namespace takeover, unsafe defaults, and misuse.
- [ ] The release contains no live credential, target, authorization bypass,
  detection blind spot, or uncoordinated unremediated vulnerability.
- [ ] Dangerous or dual-use capability and the effort reduction for misuse
  were assessed.
- [ ] Unknown high-consequence capability and safeguards lost after recipient
  control are treated as blockers.
- [ ] Red-team cases, safeguards, holdouts, incident details, and internal
  architecture are disclosed only to the approved depth.
- [ ] Models, adapters, datasets, prompts, tools, and extension defaults have
  bounded permissions and safe examples.
- [ ] Coordinated vulnerability disclosure is complete where required.
- [ ] Security reporting, triage, patch, notification, and supported-version
  expectations are published and owned.
- [ ] The decision records why public bytes are proportionate to metadata-only,
  gated, redacted, hosted, delayed, limited-recipient, or nonpublication
  alternatives.

**Threat, dual-use, and disclosure decision:**

## R5 — Claims, limitations, and usability

- [ ] Each material claim maps to dated evidence for the released revision,
  population, environment, and operating envelope.
- [ ] Measured results are separated from goals, examples, and supplier
  marketing.
- [ ] Security controls are not described as proof that the artifact is safe
  or vulnerability-free.
- [ ] Framework alignment is not described as conformance or certification
  without the applicable assessment.
- [ ] Provenance is not described as proof of authorship, originality, rights,
  safety, or correctness.
- [ ] Known limitations, failure modes, prohibited uses, confidence bounds,
  support status, and version date are visible.
- [ ] AI assistance and generated or manipulated media are disclosed as
  required for the audience.
- [ ] Accessibility and reporting-path defects have been closed or are
  explicitly accepted under policy.

| Public claim or disclosure | Evidence and as-of date | Scope / limitation | Owner | Review trigger |
|---|---|---|---|---|
| | | | | |

## R0–R5 publication-candidate assessment

### R0–R5 result register

Copy one row for every R0–R5 checklist item and every applicable artifact,
conditional-evidence, scrub, rights, threat, claim, and review row. Preserve
the control-row text or a stable local ID so a reviewer can reconcile the
register to the prompts. This register is the sole authoritative R0–R5 result
state.

| Gate / control row | Candidate and boundary binding | Evidence IDs, revisions, and digests | Result: Pass / Fail / N/A / Unknown / Stale | Assessor / owner and date | Freshness, expiry, and invalidation triggers | N/A rationale or finding / action ID |
|---|---|---|---|---|---|---|
| | | | | | | |

Do not summarize a gate as Pass until every prescribed row for that gate is in
the register and is either Pass or justified N/A.

| Gate | Rows reconciled / expected | Pass count | Justified N/A count | Fail / Unknown / Stale / blank count | Gate disposition: Pass / Hold | Open finding IDs and limitations |
|---|---|---|---|---|---|---|
| R0 | | | | | | |
| R1 | | | | | | |
| R2 | | | | | | |
| R3 | | | | | | |
| R4 | | | | | | |
| R5 | | | | | | |

This is a non-authorizing assessment of the exact candidate before the R6
governance decision. Record **publication-ready** only when every prescribed
R0–R5 row is Pass or justified N/A, all evidence is current and bound to the
frozen candidate, all prescribed validation passes, and no
organization-defined release-blocking or highest-severity finding remains.
Any Fail, Unknown, Stale, blank, unjustified N/A, unresolved decision, or
material candidate change forces **Hold**. This assessment cannot approve
publication or substitute for R6.

- **Assessment ID:**
- **Source revision:**
- **Frozen manifest ID and digest:**
- **Candidate artifact digest:**
- **Audience, channel, and distribution class:**
- **Assessor and assessment date:**
- **Source-currency date:**
- **Validation and advisory-review evidence:**
- **Open P0 / P1 or organization-defined blocking findings:**
- **Content state:** content-incomplete / content-complete
- **R0–R5 candidate disposition:** publication-ready public-review candidate /
  Hold
- **Status rationale and limitations:**

Content-incomplete always implies Hold. Content-complete does not override a
Fail, Unknown, Stale, blank, unjustified N/A, open blocker, or invalidated
candidate.

## R6 — Findings, decision, and exceptions

R6 is append-only governance over the preserved R0–R5 results. It does not
repair missing evidence or edit, relabel, backfill, or treat any R0–R5 result
as Pass or publication-ready.

**Outcome mapping:** ordinary **Go** requires a decision-bound R0–R5
disposition of **publication-ready public-review candidate**, every prescribed
row to be Pass or justified N/A, every R6 requirement satisfied, current
required owners and approvals, every required current category-bound
residual-risk decision, and no exception. **Conditional go under governed
exception** requires a current policy-permitted exception to either a known,
evidenced, exception-eligible R0–R5 Fail or an R6-only governance requirement.
It preserves every underlying Fail and Hold disposition, and a conditional
decision must not be recorded as ordinary Go. Any other Hold candidate,
missing or expired exception, missing required residual-risk decision, or
non-exception-eligible result requires Hold or Reject.

Unknown, Stale, blank, unjustified N/A, a missing required owner or unaccepted
required duty, missing decision authority, missing distribution rights, an
unresolved applicable obligation or required treatment, a clear legal,
regulatory, contractual, license, or adopted-policy prohibition, any live or
recoverable secret, credential, cookie, connection string, private key, or
signing material, a prohibited record, incomplete required coordinated
disclosure, an open organization-defined release blocker or highest-severity
finding, unknown high-consequence capability, or a missing publication or
withdrawal path is not exception-eligible and forces Hold or Reject.

- [ ] Every residual-risk decision required for the frozen candidate is
  current and links its decision ID, category, result, exact scope, named
  authority and authority basis, conditions, validity state, expiry,
  invalidation triggers, and supersession.

| Finding / unmet control | Severity | Exposure and scope | Treatment / compensating control | Owner | Due / expiry | Closure evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] No non-exception-eligible, organization-defined release-blocking, or
  highest-severity finding remains open.
- [ ] No known live credential, prohibited record, or missing right to
  distribute is waived.
- [ ] Each permitted exception is scoped to the exact artifact, audience,
  channel, duration, owner, controls, stop conditions, and expiry; cites the
  adopted-policy provision, R0–R5 control row or R6-only requirement, finding,
  evidence cutoff, and named human exception authority; and has an
  attributable record URI and digest.
- [ ] The required independent-approval or governed-exception record binds the
  manifest, digest, claims, terms, channel, audience, and release window.
- [ ] The independent approver did not produce the material change, or the
  record clearly identifies a policy-permitted non-independent exception and
  its human governance authority.
- [ ] The change-producing agent, model, or automated operator did not accept
  an exception.
- [ ] AI review is recorded as advisory rather than independent approval.

### R6 publication decision

- **Decision ID and timestamp:**
- **Named publication-decision authority and authority basis:**
- **Decision:** go / conditional go under governed exception / hold / reject
- **Decision-bound R0–R5 assessment ID and disposition:**
- **Manifest ID, source revision, and artifact digest:**
- **Audience, channel, distribution class, claims, terms, and release window:**
- **Linked residual-risk decision IDs:** categories, results, exact scopes,
  named authorities and authority bases, conditions, validity states, expiries,
  invalidation triggers, and supersession
- **Finding and condition IDs:**
- **Separate exception decision IDs:** exact scopes, named exception
  authorities and authority bases, controls, stop conditions, and expiries
- **Attributable decision-evidence URI and digest:**
- **Material-change, stop, withdrawal, and reassessment triggers:**

**Conditions, release window, and next review:**

The named publication-decision authority's decision is not inferred from a
vote or majority of the supporting-role rows. Those rows record required
discipline approval, advice, or accepted duty. Missing required input forces
Hold. The publication-decision authority consumes the required current
category-bound residual-risk and exception decisions but does not inherit,
repeat, or widen those authorities. Missing, expired, invalidated,
out-of-category, or out-of-scope required decisions force Hold or Reject.

| Role | Name | Decision | Date | Conditions |
|---|---|---|---|---|
| Content / product owner | | | | |
| Repository / artifact owner | | | | |
| Data / privacy owner | | | | |
| Security / vulnerability owner | | | | |
| Legal / IP / trade compliance | | | | |
| Responsible-AI / risk owner | | | | |
| Qualified independent approver | | | | |
| Exception authority, if used | | | | |
| Distribution operator | | | | |

## R7 — Publication and readback

- **Protected publication workflow / operator:**
- **Minimum-permission identity and environment:**
- **Decision-bound artifact and digest:**
- **Last known-good or withdrawal target:**
- **Stop, rollback, correction, and communication commands or runbook:**
- **Publication start / completion time:**

| Public-state check | Expected | Observed | Result | Evidence | Owner |
|---|---|---|---|---|---|
| Repository / URL / registry identity | | | | | |
| Version, digest, provenance, and history | | | | | |
| Visibility and channel permissions | | | | | |
| License, notices, claims, and limitations | | | | | |
| Navigation, downloads, and representative content | | | | | |
| Security, privacy, rights, safety, and support contacts | | | | | |
| Accessibility and visual behavior | | | | | |
| Rollback / withdrawal / revocation path | | | | | |

R7 is satisfied only when every prescribed public-state check has an explicit
**Pass** backed by current evidence matching the R6 decision-bound artifact,
manifest, channel, terms, and audience. **Fail**, **Unknown**, **Stale**,
blank, or any identity, digest, permission, claim, terms, or support-path
mismatch means publication is not verified. Stop further promotion
immediately and record **correct**, **restrict**, or **withdraw** below.
Workflow completion is not a readback result.

## R8 — Monitoring, takedown, and retirement

R8 **continue** requires a current, unexpired R6 Go or governed-exception
decision, all decision conditions satisfied, no stop trigger, and passing R7
readback. Expiry, invalidation, a stop trigger, or failed or incomplete
readback forbids Continue. R8 cannot extend or relabel R6, cure a failed
readback, or authorize materially changed public bytes. A material correction
returns to the earliest affected gate and requires a new R6 decision before
publication.

- **Operational decision ID and timestamp:**
- **Named operational-disposition authority and authority basis:**
- **Operational disposition:** continue / correct / restrict / withdraw /
  retire
- **Decision-bound published version, digest, channel, and observed state:**
- **Incident, condition, and exception IDs with expiries:**
- **Attributable operational-decision evidence URI and digest:**
- **Monitoring owner and dashboards / queries:**
- **Report intake and severity path:**
- **Source, dependency, rights, claim, misuse, mirror, and domain triggers:**
- **Correction and public-notice owner:**
- **Takedown authority and channels:**
- **Credential, signing, package, domain, and namespace recovery owner:**
- **Known fork, cache, archive, registry, and mirror limitations:**
- **Next review date:**
- **Transfer, deprecation, and end-of-life record:** link the
  [transfer, decommissioning, and retirement record](transfer-decommissioning-and-retirement.md);

- [ ] A withdrawal exercise demonstrated the publisher-controlled path.
- [ ] The plan records that rollback cannot guarantee deletion of recipient
  copies, forks, caches, archives, registries, or mirrors.
- [ ] An incident links to restricted evidence, affected channels, revocation,
  notification, corrective action, and effectiveness testing.
- [ ] Unsupported versions and successor or no-successor decisions will be
  communicated.
