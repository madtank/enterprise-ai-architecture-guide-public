#!/usr/bin/env python3
"""Validate tracked Markdown links and MkDocs navigation without network access."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
NAV_RE = re.compile(r"^\s*-\s+[^:]+:\s+([^\s#]+\.md)\s*$")
HTTPS_RE = re.compile(r"https://", re.IGNORECASE)
EXTERNAL_SCHEMES = {"data", "http", "https", "mailto", "tel"}
REFERENCE_SOURCE_MANIFEST = Path("scripts/reference_source_files.txt")
# Public reader guidance is source-controlled here. Agent instructions,
# pull-request templates, and revision-bound operational evidence are excluded.
ROOT_PUBLIC_GUIDANCE = frozenset(
    {
        "CONTRIBUTING.md",
        "DEPLOYMENT.md",
        "OWNERSHIP.md",
        "README.md",
        "SECURITY.md",
        "SUPPORT.md",
    }
)
FAIL_CLOSED_POLICY_INVARIANTS = {
    Path("docs/governance/control-matrix.md"): (
        "## Risk acceptance",
        "only **Hold** or **Reject**",
        "cannot make the prohibited scope releasable",
    ),
    Path("docs/worksheets/use-case-assessment.md"): (
        '!!! danger "Tier 4 and prohibitions fail closed"',
        "only **Hold** or **Reject**",
        "cannot make the prohibited scope releasable",
        "**Tier 4 / prohibition disposition, if applicable:**",
    ),
    Path("docs/worksheets/ai-risk-impact-assessment.md"): (
        '!!! danger "Tier 4 and prohibitions fail closed"',
        "only **Hold** or **Reject**",
        "cannot make the prohibited scope releasable",
        "**Tier 4 / prohibition disposition, if applicable:**",
    ),
}
RESIDUAL_RISK_AUTHORITY_INVARIANTS = {
    Path("docs/governance/operating-model.md"): (
        "exactly one named residual-risk decision authority",
        "one decision record for each category",
        "supporting rows are not votes",
        "out-of-category",
        "missing, stale, or",
        "out-of-scope required input",
        "An exception is a separate decision",
        "It cannot waive a clear legal, regulatory, contractual,",
        "cure missing rights or a mandatory",
        "make a Tier 4 scope releasable",
        "unresolved non-waivable, blocking, or",
        "does not authorize experiment, build, release, deployment, operation, or",
    ),
    Path("docs/governance/control-matrix.md"): (
        "Expired exceptions block the affected activity",
        "Supporting inputs are not votes",
        "not exception-eligible and forces **Hold** or",
    ),
    Path("docs/worksheets/ai-risk-impact-assessment.md"): (
        "## Residual-risk decision",
        "**Risk category and reserved authority boundary:**",
        "**Named residual-risk decision authority and authority basis:**",
        "supporting rows are not",
        "out-of-category",
        "missing, stale, or",
        "out-of-scope required input",
        "does not authorize an",
        "do not edit a decision-bound record",
        "## Assessment disposition",
        "Any missing, invalidated, expired, superseded, held, or",
    ),
    Path("docs/worksheets/use-case-assessment.md"): (
        "**Use-case decision:** Proceed / Proceed with conditions / Hold / Reject",
        "current decision for every required category",
        "does not itself",
        "out-of-category",
    ),
    Path("docs/worksheets/production-readiness-review.md"): (
        "`Exception approved` is valid only",
        "clear legal, regulatory, contractual, license, or",
        "missing operating or distribution rights",
        "mandatory duty, precondition, or deadline",
        "uncertain applicability",
        "missing\nrequired owner, discipline decision, approval, or independence",
        "expired, widened, unowned, out-of-category, or",
        "Any such non-waivable condition forces **hold** or **abort**",
        "exactly one named residual-risk decision authority for that category",
        "Every policy-reserved category is covered",
        "required discipline inputs\n  are current and are not treated as votes",
        "does not inherit residual-risk or exception authority",
        "Residual-risk record verifier; verify each linked decision ID",
        "create no acceptance here",
    ),
    Path("docs/worksheets/regulatory-obligation-register.md"): (
        "Linked residual-risk decision IDs, categories, exact scopes",
        "every linked residual-risk decision",
        "category-bound",
        "Exception authority does not confer residual-risk or",
        "create no embedded acceptance",
    ),
    Path("docs/worksheets/vendor-assessment.md"): (
        "**Linked residual-risk decision IDs, categories, results, exact scopes,",
        "does not inherit or repeat its",
        "out-of-category",
    ),
    Path("docs/governance/third-party-risk.md"): (
        "residual-risk decision IDs, categories, results, exact supplier and use",
        "does not inherit or recreate their authority",
        "Supporting discipline inputs are not votes",
    ),
    Path("docs/delivery/code-deployment.md"): (
        "| Residual-risk decision authority |",
        "| Exception authority |",
        "does not inherit or repeat those",
        "every exception links a separate decision ID",
        "named policy-designated exception authority and",
        "exception authority grants no release or deployment authority",
    ),
    Path("docs/delivery/evaluation-strategy.md"): (
        "linked current residual-risk decision IDs for every policy-reserved",
        "does not accept residual risk or",
        "supporting inputs, not",
    ),
    Path("docs/operations/incident-problem-and-corrective-action.md"): (
        "one named, category-bound residual-risk decision authority",
        "Every retained risk",
        "current category-bound decision IDs",
        "every identified risk demonstrably remediated by the released permanent fix",
        "covered by every applicable",
        "none inherits or",
        "Supporting discipline rows are not votes",
    ),
    Path("docs/worksheets/incident-and-corrective-action-record.md"): (
        "Every identified risk is either demonstrably remediated by the released",
        "or, where adopted policy permits retention, links every",
        "Linked residual-risk decision IDs, categories, exact scopes, results",
        "do not create an embedded acceptance or inherit",
    ),
    Path("docs/security/agent-extension-supply-chain.md"): (
        "current category-bound residual-risk decisions where policy requires acceptance",
        "does not inherit or repeat their authority",
        "supporting inputs, not votes",
        "admission itself does not accept residual",
    ),
    Path("docs/security/security-architecture.md"): (
        "linked category-bound residual-risk decision IDs",
        "validity states,",
    ),
    Path("docs/delivery/security-first-ai-dlc.md"): (
        "one current category-bound decision for every policy-reserved category",
        "supporting rows are not votes",
        "separate decision ID and one named policy-designated exception authority",
        "exception authority does not inherit residual-risk, merge, release,",
    ),
    Path("docs/architecture/model-portfolio-and-routing.md"): (
        "retaining residual risk requires one",
        "current category-bound decision for every policy-reserved category",
        "supporting rows are not votes",
    ),
    Path("docs/delivery/public-release-and-external-distribution.md"): (
        "named exception authority and adopted-policy authority basis",
        "does not inherit residual-risk or publication",
        "a missing decision is not exception-eligible",
    ),
    Path("docs/worksheets/agent-extension-assessment.md"): (
        "Linked current residual-risk decision IDs for every policy-reserved",
        "Separate policy-exception decision IDs",
        "creates no embedded residual-risk acceptance",
        "does not authorize release",
    ),
    Path("docs/worksheets/evaluation-plan-and-report.md"): (
        "## Advisory release recommendation",
        "linked current residual-risk decision IDs for every policy-reserved",
        "not residual-risk acceptance or",
        "their rows are not votes",
    ),
    Path("docs/worksheets/agent-execution-and-telemetry-contract.md"): (
        "current category-bound residual-risk decision IDs",
        "separately named loss or",
        "Neither authority inherits the other",
        "residual-unknown-pending-governance",
        "recovery owner may contain or compensate but cannot accept risk",
        "links to every required current category-bound residual-risk decision",
        "For every retained risk, link every applicable current category-bound",
        "administrative-closure authority to stop",
        "does not accept residual risk, approve an",
    ),
    Path("docs/worksheets/transfer-decommissioning-and-retirement.md"): (
        "for every retained risk, every applicable current category-bound",
        "named exit or\n  administrative-closure authority",
        "accepts no\nresidual risk and grants no exception",
        "authorities do not inherit one another",
    ),
    Path("docs/architecture/reference-architecture.md"): (
        "one named,\ncategory-bound residual-risk decision authority",
        "Review processes supply required discipline inputs, not votes",
        "a registry does not approve an artifact",
    ),
    Path("docs/worksheets/ai-assisted-change-evidence.md"): (
        "**Separate policy-exception decision ID:**",
        "**Named policy-designated exception authority and adopted policy or",
        "**Non-waivable screen:**",
        "clear legal, regulatory, contractual, license, or",
        "missing rights or mandatory duty",
        "uncertain\n  applicability",
        "missing required owner, discipline decision, approval,\n  independence, or evidence",
        "or Tier 4 scope",
        "Any present item forces **Hold**",
        "**Linked current category-bound residual-risk decision IDs, recorded",
        "the exception decision accepts no",
    ),
    Path("docs/governance/control-catalog.md"): (
        "Exceptions are explicit, separate, and temporary",
        "one named policy-designated exception authority and adopted-policy basis",
        "keep category-bound residual-risk and lifecycle or release decisions separate",
    ),
    Path("docs/worksheets/public-release-readiness.md"): (
        "every required current category-bound",
        "Every residual-risk decision required for the frozen candidate",
        "**Linked residual-risk decision IDs:**",
        "does not inherit,",
        "out-of-category",
    ),
    Path("docs/worksheets/system-card.md"): (
        "residual-risk decision IDs, categories, results,",
        "current validity and supersession states",
    ),
    Path("docs/worksheets/threat-model.md"): (
        "linked residual-risk decision IDs, categories, exact scopes",
        "does not accept residual risk",
        "without creating an embedded acceptance",
    ),
    Path("docs/examples/worked-golden-thread.md"): (
        "entries are required inputs, not votes",
        "invalidated `RIA-PEA-001` is not consumable",
        "historical acceptance cannot authorize a corrected candidate",
        "advisory recommendation, and links to separate exception and residual-risk",
        "has no exception, residual-risk, or release authority",
        "Advisory `Pass` evaluation result",
    ),
}
RESIDUAL_RISK_AUTHORITY_FORBIDDEN = {
    Path("docs/governance/operating-model.md"): (
        "Is residual risk acceptable for production?",
    ),
    Path("docs/worksheets/regulatory-obligation-register.md"): (
        "| Residual-risk acceptor |",
        "| Residual-risk acceptor,",
    ),
    Path("docs/worksheets/vendor-assessment.md"): (
        "**Residual-risk acceptor:**",
    ),
    Path("docs/governance/third-party-risk.md"): (
        "residual risks, compensating controls, and accountable acceptor;",
    ),
    Path("docs/delivery/code-deployment.md"): (
        "| Security or risk owner | Required assurance, exceptions, and residual-risk decisions |",
        "exceptions identify exposure, compensating control, owner, and expiry",
    ),
    Path("docs/worksheets/production-readiness-review.md"): (
        "| Residual-risk decision authority; accept only the exact decision-bound risk |",
    ),
    Path("docs/worksheets/threat-model.md"): (
        "residual risks and accountable acceptors;",
    ),
    Path("docs/delivery/evaluation-strategy.md"): (
        "an approver for residual risk",
    ),
    Path("docs/operations/incident-problem-and-corrective-action.md"): (
        "| Accept residual product risk |",
        "which risks are temporarily accepted",
        "permanent fix released or an explicit time-bounded risk decision",
    ),
    Path("docs/worksheets/incident-and-corrective-action-record.md"): (
        "The permanent fix is released or residual risk is explicitly accepted.",
        "| Residual risk, condition, and expiry |",
        "The permanent fix is released or every residual risk",
    ),
    Path("docs/security/agent-extension-supply-chain.md"): (
        "bounded value, understood residual risk",
        "acceptable residual risk, named owner",
    ),
    Path("docs/security/security-architecture.md"): (
        "unresolved findings and risk acceptances;",
    ),
    Path("docs/delivery/security-first-ai-dlc.md"): (
        "Named qualified owner records the decision and conditions",
        "stop conditions, and exception owner;",
        "An exception identifies the unmet outcome, exposure, compensating controls,",
    ),
    Path("docs/architecture/model-portfolio-and-routing.md"): (
        "and residual-risk approval.",
    ),
    Path("docs/delivery/public-release-and-external-distribution.md"): (
        "accountable acceptor, remediation owner",
    ),
    Path("docs/worksheets/agent-extension-assessment.md"): (
        "Conditions, finding and policy-permitted exception IDs",
    ),
    Path("docs/worksheets/evaluation-plan-and-report.md"): (
        "## Release recommendation",
        "**Decision:** Pass / Conditional pass / Fail / More evidence required",
        "threshold exceptions and expiry;",
        "residual risk and limitations;",
        "accountable approvers;",
    ),
    Path("docs/worksheets/agent-execution-and-telemetry-contract.md"): (
        "authorized residual-risk or loss decision",
        "authorized-residual-unknown",
        "qualified decision authority",
        "risk-acceptance or loss record",
    ),
    Path("docs/worksheets/transfer-decommissioning-and-retirement.md"): (
        "policy basis, qualified authority, decision ID",
        "linked risk, loss, incident, contract, legal, privacy, or records decision",
    ),
    Path("docs/architecture/reference-architecture.md"): (
        "Accountable people and review processes",
    ),
    Path("docs/worksheets/ai-assisted-change-evidence.md"): (
        "**Exception owner, expiry, and compensating controls:**",
    ),
    Path("docs/governance/control-catalog.md"): (
        "Record unmet outcome, exposure, compensating control, owner, expiry, and remediation",
    ),
    Path("docs/examples/worked-golden-thread.md"): (
        "results, exceptions, and decision",
    ),
}
DECISION_AUTHORITY_INVARIANTS = {
    Path("docs/governance/operating-model.md"): (
        "One named route or deployment decision authority",
        "One named extension-admission authority",
        "do not authorize release",
    ),
    Path("docs/architecture/model-portfolio-and-routing.md"): (
        "exactly one named decision authority for each",
        "routing-plan decision and each exact-deployment admission decision",
        "their rows are not a vote",
        "decision to **Hold** unless",
    ),
    Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"): (
        "## Final routing-plan decision",
        "**Named route-decision authority and authority basis:**",
        "Supporting rows are not votes",
        "do not edit a decision-bound record",
        "**route-eligible** and its linked, current admission decision is **Approve**",
        "A lifecycle label alone grants no authority",
    ),
    Path("docs/security/agent-extension-supply-chain.md"): (
        "one named extension-admission authority",
        "do not create approval by vote or majority",
        "an active,",
        "**Hold**, **Reject**",
        "`pilot` or `active`",
    ),
    Path("docs/worksheets/agent-extension-assessment.md"): (
        "## Final admission decision",
        "**Named extension-admission authority and authority basis:**",
        "Supporting rows are not votes",
        "do not edit it to manufacture",
    ),
    Path("docs/examples/worked-golden-thread.md"): (
        "one fictional named route-decision",
        "One fictional named extension-admission authority",
        "`approve / hold / reject`",
        "`pilot`, `active`, or `quarantined` lifecycle",
    ),
}
DECISION_AUTHORITY_FORBIDDEN = {
    Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"): (
        "state is **approved**",
        "- **approved** — central policy may select",
    ),
    Path("docs/security/agent-extension-supply-chain.md"): (
        "## Risk decision",
        "| Quarantine | incomplete provenance",
        "| Pilot | bounded value",
    ),
    Path("docs/worksheets/agent-extension-assessment.md"): (
        "**Decision:** reject / quarantine / pilot / approve",
    ),
    Path("docs/examples/worked-golden-thread.md"): (
        "approve, pilot, quarantine, or reject",
    ),
}
PUBLIC_RELEASE_RESULT_INVARIANTS = {
    Path("docs/worksheets/public-release-readiness.md"): (
        "## R0–R5 result contract",
        "Every R0–R5 checklist item and every applicable artifact or",
        "Missing evidence, ownership, review capacity, or unresolved",
        "Any **Fail**, **Unknown**, or **Stale**",
        "Only R6 may decide a policy-permitted exception",
        "R6 cannot relabel, backfill, or",
        "## R0–R5 result register",
        "This register is the sole authoritative R0–R5 result",
        "**R0–R5 candidate disposition:** publication-ready public-review candidate /",
        "## R6 — Findings, decision, and exceptions",
        "R6 is append-only governance over the preserved R0–R5 results",
        "Unknown, Stale, blank, unjustified N/A",
        "**Outcome mapping:** ordinary **Go** requires a decision-bound R0–R5",
        "Any other Hold",
        "missing required owner or unaccepted",
        "unresolved applicable obligation or required treatment",
        "recoverable secret, credential, cookie, connection string, private key",
        "### R6 publication decision",
        "**Named publication-decision authority and authority basis:**",
        "**Decision:** go / conditional go under governed exception / hold / reject",
        "**Decision-bound R0–R5 assessment ID and disposition:**",
        "**Manifest ID, source revision, and artifact digest:**",
        "**Linked residual-risk decision IDs:**",
        "**Finding and condition IDs:**",
        "**Separate exception decision IDs:**",
        "**Attributable decision-evidence URI and digest:**",
        "## R7 — Publication and readback",
        "R7 is satisfied only when every prescribed public-state check",
        "Stop further promotion",
        "## R8 — Monitoring, takedown, and retirement",
        "R8 **continue** requires a current, unexpired R6 Go or governed-exception",
        "readback forbids Continue",
        "R8 cannot extend or relabel R6",
        "returns to the earliest affected gate and requires a new R6 decision before",
        "**Operational disposition:** continue / correct / restrict / withdraw /",
    ),
    Path("docs/delivery/public-release-and-external-distribution.md"): (
        "## R0–R5 result semantics",
        "All applicable R0–R5 control rows must be **Pass**",
        "Missing evidence, owner, review capacity, or unresolved applicability is not",
        "Any **Fail**, **Unknown**, or **Stale** result",
        "Only R6 may decide a policy-permitted exception",
        "The exception cannot change the underlying R0–R5",
        "R6 is append-only governance over the preserved R0–R5 results",
        "preserves every underlying Fail and Hold disposition",
        "Do not waive Unknown, Stale, blank, unjustified N/A",
        "**Outcome mapping:** ordinary **Go** requires a decision-bound R0–R5",
        "Any other Hold",
        "missing required owner",
        "unresolved applicable obligation or required treatment",
        "recoverable secret, credential, cookie, connection string, private",
        'H -. "known, evidenced, exception-eligible Fail only; preserve Hold" .-> R6',
        'R7 -. "readback non-pass" .-> H',
        'R8 -. "stop or expiry" .-> H',
        "R7 is satisfied only when every prescribed public-state check",
        "Stop further promotion",
        "R8 **continue** requires a current, unexpired R6 Go or governed-exception",
        "readback forbids Continue",
        "R8 cannot extend or relabel R6",
        "returns to the earliest affected gate and requires a new R6 decision before",
    ),
}
ROUTING_SERVING_BOUNDARY_INVARIANTS = {
    Path("docs/architecture/model-portfolio-and-routing.md"): (
        "## Serving boundary and final invocation enforcement",
        "one immutable version of a serving-boundary",
        "`serving_boundary_revision`",
        "`serving_boundary_digest`",
        "guide-defined",
        "no cited source mandates this exact design",
        "Supplier-operated or jointly managed service",
        "Enterprise-operated deployment",
        "serving trusted computing base (TCB)",
        "separate decision-bound serving-runtime identity",
        "authenticated freshness-bounded deployment/load",
        "runtime self-report alone is insufficient",
        "from `issued` to `committed-to-invoke`",
        "internal endpoint, DNS, loopback, IPC",
        "Connected PEPs perform the authoritative live check",
        "PEP/device/workload",
        "pre-carved non-overlapping",
        "rollback-resistant",
        "copying the package or restoring a VM/device snapshot invalidates it",
        "An administrative status change alone is",
        "An isolated or on-premises route never falls back",
        "A token-only estimate is incomplete for a capacity-backed route",
    ),
    Path("docs/architecture/deployment-patterns.md"): (
        "one decision-bound",
        "`serving_boundary_id`, revision, and digest",
        "supplier-operated or jointly managed services",
        "enterprise-operated serving",
        "separate",
        "decision-bound serving-runtime identity",
        "authenticated freshness-bounded deployment/load measurement",
        "`committed-to-invoke`",
        "material change, not an invisible",
        "bound to one PEP/device key and measured runtime",
        "rollback-resistant local consume/lease/epoch state",
        "A block remains pending",
    ),
    Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"): (
        "## Serving boundary records",
        "Operating responsibility",
        "Exact invocation target; final invocation PEP",
        "Serving boundary ID / revision / digest",
        "model or weights digest, provenance",
        "serving-runtime identities",
        "authenticated deployment/load measurement",
        "Runtime self-report alone is insufficient",
        "provider service, account/project, endpoint, region",
        "available provider readback",
        "PEP/device/workload proof key",
        "pre-reserved non-overlapping",
        "rollback-resistant local",
        "reconciliation-before-refresh",
        "without raw grants, credentials, internal addresses, weights",
        "boundary revision/digest mismatch",
        "VM/device snapshot copied, cloned, or rolled back",
        "A token-only estimate is invalid",
        "Direct enterprise invocation-admission identity, serving-runtime identity, internal endpoint",
        "Unapproved cross-boundary or on-premises-to-cloud fallback",
    ),
    Path("docs/worksheets/agent-execution-and-telemetry-contract.md"): (
        "serving-boundary ID, revision, and digest",
        "authenticated deployment/load measurement ID and freshness result",
        "no raw attestation evidence",
        "Route invocation lease",
        "`committed-to-invoke`",
        "model/artifact and runtime/configuration identity",
        "rollback-resistant local",
        "Disconnected package or VM/device snapshot copied, cloned, rolled back",
        "independent local/physical disablement proof",
        "Final model-invocation approval, measurement, and lease service",
        "Direct managed-provider, enterprise invocation-admission",
        "normalized usage class, meter source, resource/capacity allocation",
    ),
    Path("docs/platform/platform-engineering.md"): (
        "decision-bound serving-boundary ID, revision, and digest",
        "provider credentials and provider-bound egress",
        "separate decision-bound serving-runtime identity",
        "Runtime self-report alone is not an integrity source",
        "rollback-resistant local package/epoch/consume/lease state",
        "administrative record says the PEP is disabled",
        "`committed-to-invoke`",
        "Cross-boundary fallback is never implicit",
    ),
    Path("docs/operations/finops-and-value.md"): (
        "enterprise-operated, capacity-backed serving",
        "Normalize those",
        "same root-execution record used for managed-service usage",
        "disconnected route's",
        "pre-carved allocation reserved",
        "transfers patching, serving, safety, capacity, hardware, and model lifecycle",
    ),
    Path("docs/security/security-architecture.md"): (
        "exclusive final model-invocation boundary across hosting modes",
        "separate decision-bound serving-runtime identity",
        "authenticated, freshness-bounded deployment/load measurement",
        "runtime self-report alone is",
        "non-overlapping pre-reserved allocation",
        "snapshot",
        "A block remains pending",
        "`committed-to-invoke`",
        "inside fallback or migration",
    ),
    Path("docs/architecture/model-and-provider-candidate-catalog.md"): (
        "**Scope boundary:** this dated snapshot covers managed cloud-service discovery",
        "not the universe of permitted deployment patterns",
        "organization's controlled artifact inventory",
        "requires separate",
        "deployment approvals",
    ),
    Path("docs/examples/worked-golden-thread.md"): (
        "`SB-PEA-001@SB-PEA-001-r1`",
        "`SBD-PEA-001`",
        "fallback or disconnected package",
        "Routing and serving boundary",
        "authenticated measurement reference and freshness result",
        "`MSTATE-PEA-0042`",
        "`committed-to-invoke`",
    ),
    Path("docs/decisions/0001-security-first-ai-dlc-and-governed-routing.md"): (
        "enterprise-operated",
        "final model-invocation policy enforcement point",
        "serving-boundary ID/revision/digest",
        "PEP/device holder binding",
        "rollback-resistant local state",
        "`committed-to-invoke`",
    ),
}
ROUTING_SERVING_BOUNDARY_FORBIDDEN = {
    Path("docs/architecture/model-portfolio-and-routing.md"): (
        "portfolio of cloud-hosted models",
        "final provider-egress policy enforcement point",
        "from `issued` to `committed-to-send`",
    ),
    Path("docs/architecture/deployment-patterns.md"): (
        "only the approved gateway or harness adapter holds provider credentials",
        "final provider-egress",
    ),
    Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"): (
        "Exclusive provider-credential and egress owner",
        "direct provider-egress path",
        "final egress transactionally",
        "`issued` to `committed-to-send` lease transition",
    ),
    Path("docs/platform/platform-engineering.md"): (
        "provider access, the final egress point",
    ),
    Path("docs/decisions/0001-security-first-ai-dlc-and-governed-routing.md"): (
        "approve exact cloud deployments only",
        "exclusive provider-egress enforcement point",
    ),
}


def markdown_files(root: Path, include_untracked: bool) -> list[Path]:
    command = ["git", "ls-files", "--cached"]
    if include_untracked:
        command.extend(["--others", "--exclude-standard"])
    command.extend(["-z", "--", "*.md"])
    result = subprocess.run(
        command,
        cwd=root,
        check=True,
        capture_output=True,
    )
    return [
        root / item.decode("utf-8")
        for item in result.stdout.split(b"\0")
        if item
    ]


def is_reference_source_scope(relative: str) -> bool:
    """Return whether a Markdown file is durable public guidance."""
    return relative.startswith("docs/") or relative in ROOT_PUBLIC_GUIDANCE


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def validate_links(root: Path, files: list[Path]) -> list[str]:
    failures: list[str] = []
    for source in files:
        if not source.exists():
            failures.append(f"{source.relative_to(root)}: tracked file is missing")
            continue
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = link_target(match.group(1))
            if not raw_target or raw_target.startswith("#"):
                continue
            parsed = urlparse(raw_target)
            if parsed.scheme.lower() in EXTERNAL_SCHEMES:
                continue
            local_path = unquote(parsed.path)
            if not local_path:
                continue
            target = (source.parent / local_path).resolve()
            if not target.exists():
                failures.append(
                    f"{source.relative_to(root)}: missing local target "
                    f"{match.group(1)}"
                )
    return failures


def validate_navigation(root: Path, files: list[Path]) -> list[str]:
    failures: list[str] = []
    config = (root / "mkdocs.yml").read_text(encoding="utf-8")
    nav_items = [match.group(1) for line in config.splitlines() if (match := NAV_RE.match(line))]
    nav_set = set(nav_items)
    duplicates = sorted({item for item in nav_items if nav_items.count(item) > 1})
    for duplicate in duplicates:
        failures.append(f"mkdocs.yml: duplicate navigation target {duplicate}")

    tracked_docs = {
        str(path.relative_to(root / "docs"))
        for path in files
        if path.is_relative_to(root / "docs")
    }
    for missing in sorted(tracked_docs - nav_set):
        failures.append(f"mkdocs.yml: tracked page is absent from navigation: {missing}")
    for missing in sorted(nav_set - tracked_docs):
        failures.append(f"mkdocs.yml: navigation target is not tracked: {missing}")
    return failures


def validate_reference_source_manifest(root: Path, files: list[Path]) -> list[str]:
    """Require public guidance with HTTPS sources in the CI manifest."""
    failures: list[str] = []
    manifest_path = root / REFERENCE_SOURCE_MANIFEST
    if not manifest_path.is_file():
        return [f"{REFERENCE_SOURCE_MANIFEST}: source manifest is missing"]
    tracked_manifest = subprocess.run(
        [
            "git",
            "ls-files",
            "--error-unmatch",
            str(REFERENCE_SOURCE_MANIFEST),
        ],
        cwd=root,
        capture_output=True,
    )
    if tracked_manifest.returncode != 0:
        failures.append(f"{REFERENCE_SOURCE_MANIFEST}: source manifest is not tracked")

    entries = [
        line.strip()
        for line in manifest_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    duplicates = sorted({entry for entry in entries if entries.count(entry) > 1})
    for duplicate in duplicates:
        failures.append(
            f"{REFERENCE_SOURCE_MANIFEST}: duplicate source file {duplicate}"
        )
    if entries != sorted(entries):
        failures.append(f"{REFERENCE_SOURCE_MANIFEST}: entries must be sorted")

    tracked = {path.relative_to(root).as_posix(): path for path in files}
    declared = set(entries)
    for entry in sorted(declared):
        if entry not in tracked:
            failures.append(
                f"{REFERENCE_SOURCE_MANIFEST}: source file is not tracked "
                f"Markdown: {entry}"
            )

    source_bearing = {
        relative
        for relative, path in tracked.items()
        if is_reference_source_scope(relative)
        and path.is_file()
        and HTTPS_RE.search(path.read_text(encoding="utf-8"))
    }
    for missing in sorted(source_bearing - declared):
        failures.append(
            f"{REFERENCE_SOURCE_MANIFEST}: missing source-bearing page {missing}"
        )
    for extra in sorted(declared - source_bearing):
        failures.append(
            f"{REFERENCE_SOURCE_MANIFEST}: page has no HTTPS source {extra}"
        )
    return failures


def validate_fail_closed_policy_invariants(root: Path) -> list[str]:
    """Keep prohibited-use decisions fail closed in policy and intake records."""
    failures: list[str] = []
    for relative, required_fragments in FAIL_CLOSED_POLICY_INVARIANTS.items():
        path = root / relative
        if not path.is_file():
            failures.append(f"{relative}: required policy file is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(
                    f"{relative}: missing fail-closed policy invariant {fragment!r}"
                )
    return failures


def validate_residual_risk_authority_invariants(root: Path) -> list[str]:
    """Keep residual-risk decisions category-bound and separate from gates."""
    failures: list[str] = []
    for relative, required_fragments in (
        RESIDUAL_RISK_AUTHORITY_INVARIANTS.items()
    ):
        path = root / relative
        if not path.is_file():
            failures.append(
                f"{relative}: required residual-risk authority file is missing"
            )
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(
                    f"{relative}: missing residual-risk authority invariant "
                    f"{fragment!r}"
                )
    for relative, forbidden_fragments in (
        RESIDUAL_RISK_AUTHORITY_FORBIDDEN.items()
    ):
        path = root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in forbidden_fragments:
            if fragment in text:
                failures.append(
                    f"{relative}: legacy residual-risk authority language remains "
                    f"{fragment!r}"
                )
    return failures


def validate_decision_authority_invariants(root: Path) -> list[str]:
    """Keep route and extension admission decisions singly attributable."""
    failures: list[str] = []
    for relative, required_fragments in DECISION_AUTHORITY_INVARIANTS.items():
        path = root / relative
        if not path.is_file():
            failures.append(f"{relative}: required decision-contract file is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(
                    f"{relative}: missing decision-authority invariant {fragment!r}"
                )
    for relative, forbidden_fragments in DECISION_AUTHORITY_FORBIDDEN.items():
        path = root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in forbidden_fragments:
            if fragment in text:
                failures.append(
                    f"{relative}: legacy decision taxonomy remains {fragment!r}"
                )
    return failures


def validate_public_release_result_invariants(root: Path) -> list[str]:
    """Keep R0–R5 results explicit, fail closed, and separate from R6."""
    failures: list[str] = []
    for relative, required_fragments in PUBLIC_RELEASE_RESULT_INVARIANTS.items():
        path = root / relative
        if not path.is_file():
            failures.append(f"{relative}: required public-release file is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(
                    f"{relative}: missing public-release result invariant {fragment!r}"
                )
    worksheet = root / "docs/worksheets/public-release-readiness.md"
    if worksheet.is_file():
        text = worksheet.read_text(encoding="utf-8")
        r6_index = text.find("## R6 — Findings, decision, and exceptions")
        decision_index = text.find("### R6 publication decision")
        r7_index = text.find("## R7 — Publication and readback")
        r8_index = text.find("## R8 — Monitoring, takedown, and retirement")
        if not 0 <= r6_index < decision_index < r7_index < r8_index:
            failures.append(
                f"{worksheet.relative_to(root)}: R6 publication decision must "
                "precede R7, and R8 must remain operational"
            )
    return failures


def validate_routing_serving_boundary_invariants(root: Path) -> list[str]:
    """Keep routing enforceable across managed and enterprise-operated serving."""
    failures: list[str] = []
    for relative, required_fragments in (
        ROUTING_SERVING_BOUNDARY_INVARIANTS.items()
    ):
        path = root / relative
        if not path.is_file():
            failures.append(
                f"{relative}: required routing serving-boundary file is missing"
            )
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(
                    f"{relative}: missing routing serving-boundary invariant "
                    f"{fragment!r}"
                )
    for relative, forbidden_fragments in (
        ROUTING_SERVING_BOUNDARY_FORBIDDEN.items()
    ):
        path = root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for fragment in forbidden_fragments:
            if fragment in text:
                failures.append(
                    f"{relative}: legacy routing serving-boundary language remains "
                    f"{fragment!r}"
                )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include-untracked",
        action="store_true",
        help="also validate untracked Markdown drafts",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    files = markdown_files(root, args.include_untracked)
    tracked_files = (
        files if not args.include_untracked else markdown_files(root, False)
    )
    failures = (
        validate_links(root, files)
        + validate_navigation(root, files)
        + validate_reference_source_manifest(root, tracked_files)
        + validate_fail_closed_policy_invariants(root)
        + validate_residual_risk_authority_invariants(root)
        + validate_decision_authority_invariants(root)
        + validate_public_release_result_invariants(root)
        + validate_routing_serving_boundary_invariants(root)
    )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(
        f"Validated {len(files)} Markdown files: local targets and "
        "MkDocs navigation are consistent."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
