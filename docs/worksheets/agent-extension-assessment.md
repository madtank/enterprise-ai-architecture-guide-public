# Agent extension security assessment

Use this worksheet before admitting or updating a skill, plugin, hook, agent
package, MCP server, tool bundle, helper script, or similar extension.

Related control design:
[agent extension supply-chain security](../security/agent-extension-supply-chain.md).

## Identity and ownership

- **Assessment record ID / version / state:** draft / under review /
  decision-bound / superseded / expired
- **Immutable assessment digest and evidence cutoff:**
- **Superseded and superseding assessment record IDs:**
- **Component name and type:**
- **Purpose and intended users:**
- **Canonical source and publisher:**
- **Exact release, commit, and digest where exposed:**
- **Provider-managed mutable-service record, if applicable:**
- **Signer and provenance verification:**
- **License and usage restrictions:**
- **Business, technical, and security owners:**
- **Lifecycle state:** draft / quarantined / pilot / active / deprecated / revoked
- **Pilot or approval scope:**
- **Last review, next review, and expiry:**
- **Revocation authority, replacement, and fallback:**

## Complete package inventory

| Item | Path / identity | Digest / version | Executable or control-bearing | Source / owner | Review result |
|---|---|---|---|---|---|
| Instructions / prompts | | | | | |
| Agents / subagents | | | | | |
| Tools / schemas | | | | | |
| Hooks / startup commands | | | | | |
| Helper scripts / binaries | | | | | |
| MCP servers / manifests | | | | | |
| Packages / containers | | | | | |
| Models / route profiles | | | | | |
| Transitive services | | | | | |

- **Dotfiles, submodules, symlinks, archives, and release assets inspected:**
- **Source-to-binary or source-to-release comparison:**
- **Update and auto-update behavior:**
- **Prior approved version and authority delta:**

## Requested authority

| Authority | Requested scope | Necessary for purpose? | Enterprise-enforced limit | Evidence |
|---|---|---|---|---|
| Filesystem reads | | | | |
| Filesystem writes | | | | |
| Network destinations / protocols | | | | |
| Credentials / token audiences | | | | |
| Data classes / tenants | | | | |
| Shell / subprocess / interpreter | | | | |
| Browser / computer control | | | | |
| Source-control / collaboration writes | | | | |
| Cloud / deployment actions | | | | |
| Models / providers / regions | | | | |
| Tool side effects | | | | |
| Delegation / fan-out / depth | | | | |
| Persistence / background execution | | | | |

The runtime applies the narrower of component-requested and enterprise
authority. Metadata and allowed-tool declarations do not grant authority.

## Static inspection

Record the tool version, rule set, command or workflow, result artifact, and
reviewer for:

| Check | Result | Findings / exceptions | Evidence |
|---|---|---|---|
| Canonicalization and Unicode / bidi review | | | |
| Secret and credential patterns | | | |
| Malware, hidden binary, and unsafe serialization | | | |
| Dependency, vulnerability, and license | | | |
| Semgrep or equivalent code rules | | | |
| CodeQL or equivalent semantic analysis | | | |
| YARA or equivalent content rules | | | |
| Shell and dynamic command construction | | | |
| Hooks, install, build, and auto-execution | | | |
| Network, upload, and exfiltration behavior | | | |
| Manifest-to-content consistency | | | |
| SBOM / AI component inventory | | | |
| Provenance and signature verification | | | |

### Critical veto assertions

Mark each assertion **pass**, **fail**, or **not assessed** and link evidence.

| Required assertion | Result | Evidence |
|---|---|---|
| No credential theft or secret harvesting | | |
| No unapproved external egress or covert payload | | |
| No privilege escalation, persistence, or sandbox escape | | |
| No hidden executable or unexplained binary | | |
| No control, verifier, logging, or approval disabling | | |
| No material behavior that contradicts the declared purpose | | |

A failed or not-assessed assertion blocks approval and results in rejection or
quarantine. It cannot be offset by an aggregate score.

## Contextual and threat review

- **Instruction, code, manifest, and documentation consistency:**
- **Prompt-injection and reviewer-manipulation findings:**
- **Untrusted content to command or tool-argument path:**
- **Private-reader plus public-sink composition risk:**
- **Verifier, registry, update-channel, or evidence tampering path:**
- **Failure, ambiguity, retry, and stop behavior:**
- **Threat-model link and source versions:**
- **Independent human security reviewer:**
- **Advisory model reviewer and protected configuration, if used:**

The model reviewer has no approval or release authority.

## MCP assessment

Complete when MCP is present.

- **Server owner, source, transport, command/image digest, and host:**
- **Negotiated protocol version and approved capability-manifest digest:**
- **Enabled tools, resources/subscriptions, prompts, roots, sampling,
  elicitation, logging, completion, and experimental surfaces:**
- **Per-capability data, direction, consent, authority, output, owner, and
  revocation controls:**
- **Approved tool-list, description, schema, and annotation digest:**
- **Behavior for dynamic capability, resource, prompt, schema, and
  `notifications/tools/list_changed` changes:**
- **Local startup command and human approval:**
- **For `stdio`: host/environment credential source, secret isolation, and
  downstream audience:**
- **For HTTP: protected-resource and authorization-server discovery,
  issuer/endpoints, and RFC 8707 resource/audience:**
- **For HTTP: token scopes, passthrough prevention, exact redirect URI,
  `state`, mandatory PKCE with `S256`, verification of advertised support,
  fail-closed behavior when support is absent, and session binding:**
- **OIDC nonce handling, when ID tokens are used:**
- **Session-ID generation and authorization separation:**
- **SSRF, redirect, DNS, metadata, and internal-network protection:**
- **Host-held credentials and secret isolation:**
- **Per-call user, workload, tenant, purpose, resource, and parameter authorization:**
- **Per-capability consent and authorization:**
- **Output schema, size, classification, content/control separation, and rendering validation:**
- **Cross-server data-flow policy:**
- **Immediate disablement and token-revocation test:**

## Isolated dynamic execution

| Scenario | Expected behavior | Observed behavior | Pass / fail | Evidence |
|---|---|---|---|---|
| Normal task with synthetic data | | | | |
| Canary secret present | no read or egress | | | |
| Unapproved file request | deny and log | | | |
| Unapproved network request | deny and log | | | |
| Injected instruction in input or tool result | treat as data | | | |
| Malformed or oversized output | reject safely | | | |
| Permission denied / missing sandbox | fail closed | | | |
| Retry, timeout, process, and cost limits | stop within bounds | | | |
| Dynamic tool or schema change | quarantine | | | |
| Revocation during execution | stop safely | | | |

- **Sandbox image and policy digest:**
- **Synthetic data and canary design:**
- **Allowed network and filesystem policy:**
- **Process, syscall, file, network, and tool observation artifact:**
- **Time, CPU/GPU, memory, file, output, token, call, and spend limits:**
- **Declared-to-observed behavior delta:**

## Findings

| ID | Severity | Finding / abuse path | Evidence and confidence | Mitigation | Residual exposure after mitigation and required decision category | Owner / due date |
|---|---|---|---|---|---|---|
| | | | | | | |

## Final admission decision

- **Decision ID and timestamp:**
- **Named extension-admission authority and authority basis:**
- **Decision:** approve / hold / reject
- **Decision-bound assessment record ID, version, and digest:**
- **Decision-bound package / manifest identity, release, commit, signer, and
  immutable digest; or mutable-service identity, configuration, observed
  revision, interface / capability hashes, sentinels, exception, and
  fallback:**
- **Exact system, use case, environment, tenant, region, user / workload, data,
  repository, runtime, harness / model, capability / tool, destination,
  side-effect, and delegation boundary:**
- **Authorized lifecycle state, only when approved:** pilot / active
- **Evidence-index IDs, revisions, digests, cutoff, freshness, and integrity
  reference:**
- **Conditions and finding IDs, owners, monitoring, stop triggers, and
  expiries:**
- **Linked current residual-risk decision IDs for every policy-reserved
  category:** category, result, exact scope, named authority and authority
  basis, conditions, validity state, expiry, invalidation triggers, and
  supersession
- **Separate policy-exception decision IDs:** exact scope, named exception
  authority and authority basis, result, controls, stop conditions, and expiry
- **Runtime-policy digest and authoritative registry record URI / digest:**
- **Effective time, decision expiry, and next review:**
- **Material-change, reassessment, and invalidation triggers:**
- **Superseded and superseding record IDs:**
- **Revocation, containment, replacement, and fallback action:**
- **Runtime enforcement and observed-state readback owners:**

Conditions do not create a fourth decision. An **Approve** decision may carry
only enforceable, monitored, unexpired conditions and authorizes only the
recorded `pilot` or `active` lifecycle scope. **Hold** and **Reject**
authorize no execution. A completed assessment, favorable scan, lifecycle
label, marketplace listing, prior-version approval, or supporting-role
consensus is not admission.

The extension-admission authority consumes every required current
category-bound residual-risk and exception record but does not inherit or
repeat those authorities. Missing, expired, invalidated, out-of-category, or
out-of-scope required decisions force **Hold** or **Reject**. This worksheet
creates no embedded residual-risk acceptance and does not authorize release.

| Role | Named principal and authority / duty | Required approval, advice, or duty acknowledgement | Time and attributable evidence | Conflict, condition, or exception IDs and expiry |
|---|---|---|---|---|
| Extension-admission authority; record the authoritative approve / hold / reject decision | | | | |
| Assessment or change producer; no self-approval authority | | | | |
| Component owner | | | | |
| Platform / runtime owner | | | | |
| Security reviewer | | | | |
| Data / privacy owner, if applicable | | | | |
| Repository / release owner | | | | |
| Qualified independent approver, when policy requires | | | | |

Supporting rows are not votes, and their completion does not infer approval.
A blank, stale, missing, ambiguous, or negative required approval, or an
unresolved conflict with controlling policy, forces **Hold** until resolved by
the owner of that reserved decision right or a separately authorized,
policy-permitted exception. Critical veto findings cannot be excepted. The
extension-admission authority cannot waive a prohibition, missing required
approval, or another authority's reserved decision right. AI-generated review
remains advisory.

A material change to a bound package, revision, digest, signer, dependency,
manifest, capability or schema, authority, scope, runtime policy, or evidence;
a mutable-service observation outside its approved envelope; a failed sentinel
or veto assertion; expiry; loss of ownership; or loss of enforcement
invalidates admission. Deny new execution and contain or revoke existing
exposure as recorded until a new attributable superseding decision is issued.
Preserve the prior decision-bound record; do not edit it to manufacture
continued approval.

## Continuous assurance

- [ ] runtime verifies the approved digest and policy;
- [ ] observed files, processes, network, tools, data, routes, and cost are reconciled;
- [ ] dependency, maintainer, signer, marketplace, model, tool, and schema changes alert;
- [ ] review expires automatically;
- [ ] revoked components are denied across all runtimes;
- [ ] credentials can be rotated and affected releases identified;
- [ ] fallback and component removal have been exercised;
- [ ] incidents feed versioned rules and regression tests through separate approval.
