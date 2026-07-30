# AI-assisted change evidence

Use this worksheet as a concise reviewer brief and evidence index. Delete
sections that are genuinely not applicable; do not fill them with generated
boilerplate. Link large artifacts rather than pasting raw logs.

## Change identity

- **Change / issue ID:**
- **Repository and target branch:**
- **Base commit:**
- **Reviewed head commit:**
- **Change owner:**
- **Repository owner:**
- **Required code owners / reviewers:**
- **Release and deployment owner, if applicable:**
- **Risk tier / change classification:**

## Intent

- **Problem and affected user or operation:**
- **Expected outcome:**
- **Acceptance criteria:**
- **Scope:**
- **Non-goals:**
- **Constraints and unchanged behavior:**
- **Open questions and decision owner:**

## Approach and decisions

- **Implementation summary:**
- **Affected components and interfaces:**
- **Architecture decision or design link:**
- **Alternatives considered and rejected:**
- **Data, authorization, dependency, migration, or compatibility impact:**

## AI assistance

- **AI-assisted:** yes / no
- **Accountable human initiator:**
- **Agent / harness:**
- **Model and provider, if policy requires disclosure:**
- **Approved skill selected and immutable version or digest, or why no
  approved skill matched:**
- **Registry lifecycle state and applicability at execution:**
- **Conflicts, precedence decision, or no-match fallback:**
- **External skill installation or update approval and evidence, if applicable:**
- **Plugin / marketplace source and immutable package digest:**
- **Included hooks, scripts, startup commands, binaries, MCP servers, and
  transitive dependencies:**
- **MCP server identity, transport or start command, approved tool-list/schema
  digest, and authentication audience/scopes:**
- **Material tools and permission classes:**
- **Execution isolation:**
- **Allowed network destinations:**
- **Runtime-policy and sandbox-policy digests:**
- **Run or session IDs:**
- **Sanitized decision trace or transcript:** not retained / private link /
  approved PR attachment
- **Redaction and publication approval:**

Do not include hidden reasoning, system or developer instructions, raw tool
output, credentials, cookies, private paths, unrelated tasks, or unnecessary
personal and confidential data.

## Verification

| Check | Exact command or workflow | Result | Evidence URI | Source / artifact revision |
|---|---|---|---|---|
| Reproducer or pre-change failure | | | | |
| Format / lint / type | | | | |
| Unit tests | | | | |
| Integration / contract tests | | | | |
| Migration / compatibility | | | | |
| Security / secret / dependency / license | | | | |
| Behavioral / safety / adversarial evaluation | | | | |
| Performance / cost | | | | |
| Visual or interactive review | | | | |

Classify each material check as deterministic executable, statistical or
behavioral, inferential advisory, or human judgment.

### Defect evidence

- **Did the regression check fail on the affected revision?**
- **Does it pass on the proposed revision?**
- **Which related paths and boundary cases were tested?**

### Verification independence

- **Who or what produced the change?**
- **Who or what reran the trusted checks?**
- **Verifier identity and protected configuration:**
- **Deterministic versus inferential verification classification:**
- **Iteration, token, time, retry, and spend limits:**
- **Halting or escalation result:**
- **Independent human reviewer:**
- **Were CI, policy, tests, thresholds, ownership, or workflow triggers
  changed?**
- **If yes, who independently approved the control change?**

## Risk and limitations

- **Security and privacy impact:**
- **Reliability and operational impact:**
- **Affected people and responsible-AI impact:**
- **Supply-chain and licensing impact:**
- **Known limitations:**
- **Unresolved findings:**
- **Separate policy-exception decision ID:**
- **Named policy-designated exception authority and adopted policy or
  delegation basis:**
- **Exact unmet internal control, decision-bound scope, result, exposure, and
  rationale:**
- **Non-waivable screen:** clear legal, regulatory, contractual, license, or
  adopted-policy prohibition; missing rights or mandatory duty; uncertain
  applicability; missing required owner, discipline decision, approval,
  independence, or evidence; or Tier 4 scope. Any present item forces **Hold**
  or **Reject** and is not exception-eligible.
- **Compensating controls, monitoring, stop trigger, remediation owner, due
  date, expiry, invalidation triggers, and supersession:**
- **Linked current category-bound residual-risk decision IDs, recorded
  separately when policy requires risk acceptance:**
- **Authority separation confirmed:** the exception decision accepts no
  residual risk and authorizes no merge, release, deployment, publication, or
  operation
- **Learning candidate proposed:** yes / no
- **Learning candidate origin, sanitization, poisoning/regression result, and
  promotion or rejection record:**

## Release and recovery

- **Release manifest / artifact digest:**
- **Deployment required:** yes / no
- **Rollout stages and cohorts:**
- **Go, hold, abort, and rollback thresholds:**
- **Rollback target:**
- **Forward recovery or compensation:**
- **Dashboards and alerts:**
- **Observation owner and period:**
- **Communication or recourse required:**

## Human confirmation

The accountable contributor confirms:

- [ ] I reviewed the proposed change rather than forwarding agent output
  unread.
- [ ] I understand and can explain the intent, implementation, risks, and
  evidence.
- [ ] I verified that the evidence corresponds to the reviewed revision.
- [ ] I disclosed known failures, uncertainty, and limitations.
- [ ] I did not expose prohibited or sensitive session information.
- [ ] I will respond to review and post-release issues or arrange an explicit
  handoff.

| Name | Role | Decision | Date | Conditions |
|---|---|---|---|---|
| Change owner | | | | |
| Code owner / reviewer | | | | |
| Security / risk, if required | | | | |
| Release owner, if applicable | | | | |
