# Production operations

AI operations extend ordinary SRE and security operations with quality, data, model, and harm signals.

## Service objectives

Define objectives for:

- availability and end-to-end latency;
- task success and groundedness;
- maximum harmful or invalid action rate;
- data and index freshness;
- escalation and appeal resolution time;
- unit cost and total spend;
- recovery time and rollback readiness.

Quality objectives should be tied to a stable evaluation method and representative production slices.

## Observability

Correlate:

- user or workload identity and tenant;
- use case, release, route, delegation chain, model, prompt, policy, index,
  skill, extension, MCP server, and tool versions;
- retrieval sources and provenance;
- tool requests, authorization decisions, and results;
- latency, tokens or compute, retries, errors, and cost;
- route rationale, worker fan-out, verification, fallback, and escalation;
- guardrail decisions and human interventions;
- privacy-minimized quality and outcome signals.

Do not log sensitive prompts and outputs by default. Apply classification, redaction, encryption, retention, access control, and audit to telemetry.

Complete the
[agent execution and telemetry contract](../worksheets/agent-execution-and-telemetry-contract.md)
to define the canonical root and child identifiers, typed outcomes, required
events, minimization, completeness and integrity checks, alert ownership,
reconciliation, and closure. Route rationale means structured policy reason
codes and evaluated constraints, not hidden reasoning or a model explanation.

Every material alert should create or update an attributable incident, problem,
or corrective action. A dashboard without a response owner and decision path
is observation, not an operating control.

## Failure containment

Use:

- time, token, step, spend, and action budgets;
- rate limits and concurrency limits;
- schema validation and allowlisted tools;
- idempotency and transaction boundaries;
- circuit breakers for providers, tools, and quality thresholds;
- fallback to a safer model, deterministic path, human queue, or graceful refusal;
- versioned rollback for application, prompt, model, policy, index, and tool changes.

## Incident response

AI incident playbooks should cover:

- sensitive-data exposure;
- unauthorized or destructive tool use;
- harmful, discriminatory, or misleading output;
- widespread unsupported claims;
- prompt injection or retrieval poisoning;
- model or vendor compromise;
- malicious or changed skill, plugin, hook, MCP server, tool schema, or route;
- abnormal spend or resource use;
- drift and material quality regression.

Preserve evidence without expanding data exposure. Include product, engineering, security, privacy, risk, legal, communications, and vendor owners according to severity.

Use the
[incident, problem, and corrective-action](incident-problem-and-corrective-action.md)
workflow to join containment and restoration to reproduction, a verified fix,
progressive rerelease, systemic improvement, and effectiveness-based closure.

## Change management

Use progressive delivery and automated regression evaluation. Record every production artifact version. Emergency changes need the same auditability, a time-bounded approval, and retrospective validation.

Follow the [code deployment and release](../delivery/code-deployment.md)
procedure and verify the actual versions, routes, policy, and migration state
after every deployment.

## Retirement

Use the
[transfer, decommissioning, and retirement record](../worksheets/transfer-decommissioning-and-retirement.md)
to freeze scope, stop and reconcile active work, validate continuity or
successor acceptance, remove the retiring boundary's routes, credentials,
indexes, tool permissions, endpoints, jobs, infrastructure, and eligible data,
and read back observed state. Preserve required records and separately
approved shared assets with explicit ownership, access, review, and final
disposition. Retirement does not silently close an incident, CAPA, appeal,
hold, right request, or supplier duty.
