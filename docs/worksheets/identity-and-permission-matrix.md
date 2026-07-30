# Identity and permission matrix

Use this worksheet for one AI system and one defined operating boundary. It
connects approved identity and authorization policy to deployed enforcement
and observed actions. It is an evidence record, not an identity provider,
authorization engine, access-control policy, or substitute for the
organization's IAM standards.

Generate inventories from authoritative configuration where practical, but
require accountable review. A manually completed matrix can be stale; an
automated export can be incomplete or misinterpreted. Unknown or blank
authority blocks a consequential release. Completion demonstrates
documentation, not effective enforcement, legal compliance, standards
conformance, certification, or independent approval.

!!! danger "Models do not receive ambient authority"
    A model name or logical agent label is not automatically an authenticated
    principal. Record the workload, gateway, adapter, or tool identity that
    actually presents a credential. Keep reusable credentials outside model
    context, prompts, memory, tool results, and traces. Tool availability,
    prompt text, MCP annotations, and an `allowed-tools` field do not grant
    resource authority.

## Scope and ownership

- **System name and inventory ID:**
- **Matrix version / state / effective date / expiry:**
- **Release / architecture revision:**
- **Release manifest and artifact digest, when applicable:**
- **Environment(s):**
- **Tenant, organization, account, project, and region boundaries:**
- **Use cases and prohibited uses:**
- **Risk tier, autonomy, and maximum action consequence:**
- **Data classes and affected resource types:**
- **Identity provider(s) and trust domains:**
- **Policy decision and enforcement services:**
- **Authoritative resource-owning services:**
- **Matrix owner and access-review owner:**
- **Source-policy revision and export time:**
- **Observed-state snapshot and evidence URI:**
- **Threat model, data flow, route-grant, and tool-registry URIs:**
- **Agent execution and telemetry contract ID / revision:**
- **Last review / next review / material-change triggers:**

Record separately which requirements come from organization policy, adopted
standards, contracts, law, regulation, or the system's threat model. This
worksheet does not determine their applicability.

Keep these decisions distinct:

- a **principal** is an authenticated human or workload subject; a group,
  role, or capability profile is an entitlement or policy subject and does
  not prove which principal currently holds it;
- a **permission** allows an action on a resource; delegated authority also
  constrains purpose, tenant, data, tools, network, models, time, and budgets;
- human approval, technical authorization, residual-risk acceptance, and
  independent assurance are separate decisions;
- break-glass is a controlled emergency access path, not a policy exception
  or waiver.

Record credential references and classes, never credential values.

## Identity and decision chain

```mermaid
flowchart LR
    Origin["Originating human or client"] --> App["Application workload"]
    App --> Runtime["Orchestrator workload"]
    Runtime --> Policy["Policy and credential broker"]
    Policy --> Child["Bounded child or worker"]
    Policy --> Tool["Tool or connector workload"]
    Approver["Eligible approver"] --> Policy
    Child --> Tool
    Tool --> Resource["Resource-owning service"]
    Resource --> Commit["Final authorization and commit"]
```

The originating identity, executing workloads, approver, and resource owner
remain distinct. A prior gateway, agent, or human decision does not replace
authorization by the service that owns the exact resource and action.

## Identity inventory

Inventory identities that can view data, select a route, invoke a tool,
change authoritative state, administer policy, deploy, approve, support, or
break glass.

| Principal ID | Human / workload kind | Represents / purpose | Assigned groups, roles, profiles | Owner and custodian | Trust domain, tenant, environment | Authentication / federation / applicable human assurance | Credential issuer or source | Privileged / break-glass | Lifecycle, expiry, review | Observed evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

Use explicit kinds such as human, application workload, orchestrator, model
gateway or adapter, child-worker runtime, tool or MCP server, deployment or CI
identity, protected verifier, support identity, administrator, and
break-glass identity.

### Group, role, and profile assignments

Record entitlement containers separately from authenticated principals.

| Group, role, or profile ID | Purpose and permissions | Eligible principal type | Assignment source and rule | Current members / binding evidence | Owner | Expiry / review |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] Every non-human identity has an accountable human or team owner.
- [ ] Group and role membership can be resolved to current accountable people.
- [ ] Shared and personal production credentials are prohibited or explicitly
  identified as release-blocking gaps.
- [ ] Logical agents and model profiles map to the workload identities that
  execute them; the model itself is not treated as a credential holder.
- [ ] Identity proofing and authenticator strength for people match the
  organization's adopted assurance policy.
- [ ] Workload identity is bound to the intended code, runtime, environment,
  and trust domain where the platform supports it.
- [ ] Dormant, orphaned, duplicate, supplier, and emergency identities are
  identified.

## Permission matrix

Record explicit allows. Unlisted access should fail closed under the adopted
policy. If a row represents a role or group, link its membership and
eligibility rule. A wildcard requires an accountable rationale, a bounded
scope, and representative negative-test evidence.

| Principal / role | Acting for | Resource and owner | Action and consequence | Purpose / use case | Tenant, environment, data class | Conditions and approval | Decision and enforcement point | Credential audience, scope, lifetime, binding | Delegation rule | Expiry / review | Policy and test evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

For each row:

- identify the exact resource or bounded resource set, not only a broad
  service name;
- distinguish read, propose, approve, execute, administer, delegate, export,
  and delete;
- classify the action as read-only, reversible, compensatable, material,
  irreversible, or safety- or rights-critical;
- bind purpose, tenant, environment, data class, region, time, and transaction
  conditions where relevant;
- record the deterministic decision and enforcement points;
- identify any human approval and whether a parameter change invalidates it;
- make delegation deny-by-default and narrower than the delegator's current
  authority;
- link both configured-policy evidence and a representative allowed and denied
  test.

## Authorization checkpoints

Complete every checkpoint that exists in the system. A check at one layer is
not inherited automatically by later layers.

| Checkpoint | Subject and delegated identity | Resource / action | Decision owner | Enforcement point | Context evaluated | Fail-closed behavior | Decision evidence |
|---|---|---|---|---|---|---|---|
| Use-case entry | | | | | | | |
| Data retrieval / context assembly | | | | | | | |
| Model, provider, region, or route selection | | | | | | | |
| Child-agent or worker dispatch | | | | | | | |
| Tool discovery and invocation | | | | | | | |
| External communication or publication | | | | | | | |
| System-of-record validation and commit | | | | | | | |
| Policy, identity, or credential administration | | | | | | | |

- [ ] The resource-owning service reauthorizes the exact action immediately
  before a consequential commit.
- [ ] Authentication, tool discovery, model selection, consent, and prior
  approval are not treated as final resource authorization.
- [ ] Unavailable, stale, conflicting, or unverifiable authorization state
  fails closed or enters a separately approved degraded mode.
- [ ] Authorization decisions cannot be replaced or widened by model output,
  retrieved content, tool descriptions, or tool results.

### Authorization attributes

Record every subject, resource, action, and environment attribute used in a
material decision.

| Attribute and class | Meaning and allowed values | Authoritative source and owner | Integrity, freshness, availability | Mapping / transformation | Failure behavior | Test evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] Tenant, role, group, purpose, data class, device or workload posture,
  risk, region, and resource attributes have unambiguous semantics.
- [ ] Stale, unavailable, conflicting, untrusted, or unmapped attributes do
  not default to broader access.
- [ ] Federated and provider-specific attributes map to the enterprise policy
  without collisions or unintended privilege.

## Delegation and child-authority attenuation

Complete one row for every coordinator-to-worker, agent-to-agent, or
on-behalf-of delegation class. Link the
[model routing and agent dispatch plan](model-routing-and-agent-dispatch-plan.md)
when a route grant carries the decision.

| Parent grant / principal | Child workload | Bounded task and output | Allowed data, resources, tools, routes, actions | Explicitly prohibited authority | Depth, fan-out, time, retry, spend limits | Audience, presenter, nonce, expiry, revocation state | Subset proof / policy result | Observed use and reconciliation |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

- [ ] The child uses its own authenticated workload identity; its granted
  permissions and constraints are a strict subset of the originating and
  parent authority across tenant, environment, purpose, data, resource,
  action, tool, network, route, time, and aggregate budget.
- [ ] Human approval and separation-of-duties requirements are inherited or
  made stricter; delegation cannot remove them.
- [ ] A coordinator, worker, skill, prompt, or tool cannot mint, broaden,
  renew, or approve its own authority.
- [ ] Fallback, retry, parallel dispatch, and escalation cannot bypass the
  parent grant or aggregate root-execution limits.
- [ ] The grant is short-lived, tamper-evident, audience-restricted,
  sender-presenter bound where required, replay-resistant, and revocable.
- [ ] The final model-invocation policy enforcement point or tool broker
  validates current policy and revocation state; applications, models, workers,
  and skills lack direct managed-provider credentials, enterprise
  invocation-admission and serving-runtime identities, or target-system
  credentials.
- [ ] Observed child execution is reconciled to the issued grant, and a
  widened or unrecognized path alerts and stops safely.

Express the implementation invariant in enforceable policy:
`effective child = requested child ∩ parent grant ∩ current enterprise policy`.

## Credentials, tokens, and sessions

| Credential / token class | Holder | Issuer / broker | Audience and scope | Storage and model visibility | Lifetime / renewal | Rotation and revocation | Session / transaction binding | Owner and evidence |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

- [ ] Prefer short-lived, just-in-time, workload, or on-behalf-of credentials
  over reusable bearer secrets.
- [ ] Secrets are injected by the host or broker and never copied into
  prompts, model-visible environment variables, memory, tool output, or
  privacy-minimized traces.
- [ ] OAuth or federation tokens are validated for issuer, audience, client,
  subject, tenant, scope, expiry, and resource; token passthrough and
  confused-deputy flows are denied.
- [ ] Session identifiers are unpredictable, protected, bound to the
  authenticated context, and never used as authorization by themselves.
- [ ] Credential caches, refresh paths, delegated sessions, and failure
  recovery preserve the original scope and tenant.
- [ ] Revocation and rotation propagate within a defined objective, and
  affected runs, releases, and actions can be identified.

For local process-based extensions, record the host identity, start command,
environment source, filesystem and network boundary, and secret injection.
Do not apply an HTTP authorization flow to a local transport merely because
another extension uses OAuth.

## Human approval and separation of duties

| Action class | Eligible approver | Ineligible / conflicting roles | Parameters bound to approval | Approval lifetime and invalidation | Final resource authorization | Evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] Consequential approvals bind the exact action, target, material
  parameters, consequence, requester, tenant, and expiry.
- [ ] Changed parameters, stale state, expired approval, or a different target
  triggers a new decision.
- [ ] The change-producing agent or model cannot approve its own change.
- [ ] Production policy, identity, credential, and access changes use
  risk-proportionate separation between request, approval, execution, and
  review.
- [ ] Approval eligibility is enforced rather than inferred from a chat
  message or model interpretation.
- [ ] The action result and authoritative transaction ID are read back and
  attributed to the requester, approver, and executor.

## Privileged and break-glass access

| Capability | Eligible identity | Normal path | Emergency trigger | Maximum duration | Monitoring and notification | Retrospective review / revoke test | Owner |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

- [ ] Standing privilege is minimized and separate administration identities
  are used where required.
- [ ] Break-glass access has a defined emergency purpose, strong
  authentication, narrow scope, short expiry, visible alert, and named
  incident owner.
- [ ] Emergency access does not silently disable tenant, logging, retention,
  or legal restrictions.
- [ ] Every use receives timely retrospective review, credential rotation or
  revocation where indicated, and corrective action for misuse or control
  failure.
- [ ] Recovery from an unavailable identity or policy service is exercised
  without creating an unmonitored permanent bypass.

## Tenant, data, and network boundaries

| Boundary | Identity / attribute source | Isolation and authorization rule | Shared components | Cross-boundary exception | Negative test and observed evidence | Owner |
|---|---|---|---|---|---|---|
| Tenant / organization | | | | | | |
| Environment / account / project | | | | | | |
| Region / residency zone | | | | | | |
| Data class / purpose | | | | | | |
| Retrieval, memory, cache, index, and trace | | | | | | |
| Tool, network destination, and system of record | | | | | | |

- [ ] Tenant and resource attributes come from trusted context rather than
  model-generated text.
- [ ] Shared caches, indexes, memory, filesystems, queues, evaluation stores,
  and telemetry preserve tenant and purpose isolation.
- [ ] Network reachability is not treated as permission.
- [ ] Support, evaluation, debugging, and supplier access follow the same
  identity, purpose, minimization, and review controls.

## Lifecycle and recertification

| Trigger / cadence | Identities and permissions in scope | Authoritative source | Reviewer | Required action | Completion evidence |
|---|---|---|---|---|---|
| Join / create | | | | | |
| Role, purpose, tenant, or risk change | | | | | |
| Departure / disable | | | | | |
| Credential, supplier, tool, route, or policy change | | | | | |
| Periodic access recertification | | | | | |
| Dormancy, orphaning, expiry, or incident | | | | | |
| Transfer, decommissioning, or retirement | | | | | |

Verify that disablement removes group membership, grants, sessions, cached
tokens, workload bindings, deploy or signing access, provider routes, tool
access, and emergency privilege. Preserve only the access evidence required
by the adopted records and privacy policy.

Project the final identity state and enforcement-point readback into the
[transfer, decommissioning, and retirement record](transfer-decommissioning-and-retirement.md).
That record owns the exit sequence and closure; this matrix remains
authoritative for who or what may hold each permission.

## Verification and abuse cases

| Test | Expected decision and safe behavior | Environment / fixture | Result | Evidence | Finding owner / due date |
|---|---|---|---|---|---|
| Valid least-privilege request | | | | | |
| Unauthenticated or unknown principal | | | | | |
| Wrong tenant, environment, resource, or data class | | | | | |
| Expired, wrong-audience, altered, or replayed credential / grant | | | | | |
| Child requests wider data, tool, route, action, or budget | | | | | |
| Direct provider, tool, or system-of-record bypass | | | | | |
| Prompt or tool output attempts to change authority | | | | | |
| Approval target or parameters change after approval | | | | | |
| Policy, identity, or revocation service is stale or unavailable | | | | | |
| Credential rotation, revocation, and active-session termination | | | | | |
| Cross-tenant cache, memory, index, trace, or retry path | | | | | |
| Break-glass invocation and recovery | | | | | |
| Joiner, mover, leaver, and orphaned workload | | | | | |
| Audit-event loss, tampering, or identity ambiguity | | | | | |

Use test doubles and non-production fixtures for destructive or external
actions. A successful allowed request does not prove that denied paths are
enforced.

## Observed-state reconciliation and privacy-minimized evidence

This table is the identity and authorization projection. The
[agent execution and telemetry contract](agent-execution-and-telemetry-contract.md)
owns the common root-execution event schema, typed outcome states, completeness
rules, cancellation and ambiguity behavior, and closure criteria.

| Evidence stream | Required fields | Sensitive fields excluded or transformed | Access / retention | Reconciliation or alert | Owner |
|---|---|---|---|---|---|
| Authentication and federation | | | | | |
| Policy decision and enforcement | | | | | |
| Delegation / route grant | | | | | |
| Tool proposal, approval, execution, and result | | | | | |
| Resource commit and postcondition | | | | | |
| Privileged and break-glass use | | | | | |
| Identity / permission configuration change | | | | | |

Evidence should distinguish proposal, policy decision, human approval,
execution, authoritative result, and denial. Carry privacy-minimized identity,
tenant, purpose, resource, action, policy revision, delegation, decision,
credential class, time, and correlation identifiers. Exclude credentials,
session secrets, hidden reasoning, and unnecessary raw prompts or outputs.

- [ ] Approved policy, deployed configuration, identity-provider state, and
  observed runtime use are reconciled on a defined cadence.
- [ ] Unknown principals, grants, sessions, group members, capabilities,
  direct paths, or privileged uses alert an accountable owner.
- [ ] Audit access and retention are themselves authorized, minimized, and
  monitored.
- [ ] Evidence supports incident reconstruction without turning telemetry into
  a new sensitive-content store.

## Findings, exceptions, and decision

**Disposition:** ready for stated scope / conditional / hold / revoke

**Decision scope, conditions, and next review:**

| Finding / unmet control | Severity | Exposed identities, tenants, resources, or actions | Treatment / compensating control | Owner | Due / expiry | Closure evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] No organization-defined release-blocking identity, authorization,
  credential, tenant-isolation, or bypass finding remains open.
- [ ] Every exception names the unmet outcome, exact scope, rationale,
  compensating controls, monitoring, owner, expiry, and remediation.
- [ ] An exception decision is explicitly labeled and records its governance
  authority separately from any qualified independent approval.
- [ ] An exception cannot create authority that the accepting role does not
  hold or override a clear legal prohibition.
- [ ] Material changes invalidate affected rows, tests, approvals, and
  exceptions.

| Role | Name | Decision | Date | Conditions / next review |
|---|---|---|---|---|
| System / product owner | | | | |
| Identity and access owner | | | | |
| Resource / data owner | | | | |
| Platform / security owner | | | | |
| Operations owner | | | | |
| Risk / privacy / legal owner, when required | | | | |
| Qualified independent approver, when required | | | | |
| Governance exception authority, if policy permits | | | | |

## Source boundary

**Source check:** 2026-07-28.

This worksheet adapts identity and authorization inputs from
[NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final),
whose current minor release was 5.2.0 on the check date;
[NIST SP 800-63-4](https://csrc.nist.gov/pubs/sp/800/63/4/final);
[NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final);
[NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final);
[NIST SP 800-205](https://csrc.nist.gov/pubs/sp/800/205/final);
[NIST SP 800-192](https://csrc.nist.gov/pubs/sp/800/192/final);
the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization);
and the joint
[Careful Adoption of Agentic AI Services](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services)
guidance.

SP 800-53 is a tailorable U.S. Government control catalog, not a universal
baseline. SP 800-63-4 addresses identity proofing, authentication, and
federation for people interacting with government systems; it does not define
workload identity or this system's authorization policy. SP 800-207 and
800-207A provide zero-trust architecture guidance, including application and
service identity in cloud-native environments. SP 800-205 provides attribute
considerations rather than requiring attribute-based access control, and SP
800-192 provides policy-model verification and testing methods rather than
proof that deployed enforcement uses the tested policy. MCP authorization is
optional and HTTP-specific; its requirements apply only to applicable
transports and protocol roles. The organization must select its own control
baseline, assurance levels, policy language, decision rights, and enforcement
mechanisms.
