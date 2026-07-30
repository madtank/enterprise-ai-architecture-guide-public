from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from scripts.check_docs import (
    DECISION_AUTHORITY_INVARIANTS,
    FAIL_CLOSED_POLICY_INVARIANTS,
    PUBLIC_RELEASE_RESULT_INVARIANTS,
    RESIDUAL_RISK_AUTHORITY_INVARIANTS,
    RESIDUAL_RISK_AUTHORITY_FORBIDDEN,
    ROUTING_SERVING_BOUNDARY_FORBIDDEN,
    ROUTING_SERVING_BOUNDARY_INVARIANTS,
    ROOT_PUBLIC_GUIDANCE,
    is_reference_source_scope,
    validate_decision_authority_invariants,
    validate_fail_closed_policy_invariants,
    validate_public_release_result_invariants,
    validate_residual_risk_authority_invariants,
    validate_routing_serving_boundary_invariants,
)


class ReferenceSourceScopeTests(TestCase):
    def test_includes_durable_public_guidance_only(self) -> None:
        for relative in ROOT_PUBLIC_GUIDANCE:
            with self.subTest(relative=relative):
                self.assertTrue(is_reference_source_scope(relative))
        self.assertTrue(is_reference_source_scope("docs/references.md"))

        for relative in (
            "AGENTS.md",
            ".github/pull_request_template.md",
            "evidence/2026-07-27-review.md",
            "scripts/check_docs.py",
        ):
            with self.subTest(relative=relative):
                self.assertFalse(is_reference_source_scope(relative))


class FailClosedPolicyInvariantTests(TestCase):
    def write_required_policy_files(self, root: Path) -> None:
        for relative, fragments in FAIL_CLOSED_POLICY_INVARIANTS.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(fragments), encoding="utf-8")

    def test_accepts_required_fail_closed_language(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_policy_files(root)
            self.assertEqual(validate_fail_closed_policy_invariants(root), [])

    def test_rejects_proceed_compatible_worksheet_drift(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_policy_files(root)
            target = root / "docs/worksheets/use-case-assessment.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "only **Hold** or **Reject**",
                    "Proceed / Hold / Reject",
                ),
                encoding="utf-8",
            )
            failures = validate_fail_closed_policy_invariants(root)
            self.assertTrue(
                any(
                    "only **Hold** or **Reject**" in failure
                    for failure in failures
                )
            )

    def test_rejects_canonical_policy_drift(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_policy_files(root)
            target = root / "docs/governance/control-matrix.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "cannot make the prohibited scope releasable",
                    "may make the prohibited scope releasable",
                ),
                encoding="utf-8",
            )
            failures = validate_fail_closed_policy_invariants(root)
            self.assertTrue(
                any(
                    "cannot make the prohibited scope releasable" in failure
                    for failure in failures
                )
            )


class ResidualRiskAuthorityInvariantTests(TestCase):
    def write_required_risk_files(self, root: Path) -> None:
        for relative, fragments in RESIDUAL_RISK_AUTHORITY_INVARIANTS.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(fragments), encoding="utf-8")

    def test_accepts_required_residual_risk_authority_language(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_risk_files(root)
            self.assertEqual(validate_residual_risk_authority_invariants(root), [])

    def test_rejects_supporting_vote_drift(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_risk_files(root)
            target = root / "docs/governance/operating-model.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "supporting rows are not votes",
                    "supporting rows determine the majority vote",
                ),
                encoding="utf-8",
            )
            failures = validate_residual_risk_authority_invariants(root)
            self.assertTrue(
                any("supporting rows are not votes" in failure for failure in failures)
            )

    def test_rejects_removed_category_boundary(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_risk_files(root)
            target = root / "docs/worksheets/ai-risk-impact-assessment.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "**Risk category and reserved authority boundary:**",
                    "**Risk description:**",
                ),
                encoding="utf-8",
            )
            failures = validate_residual_risk_authority_invariants(root)
            self.assertTrue(
                any("reserved authority boundary" in failure for failure in failures)
            )

    def test_rejects_one_optional_cross_category_decision(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_risk_files(root)
            target = root / "docs/worksheets/use-case-assessment.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "current decision for every required category",
                    "one optional decision for all categories",
                ),
                encoding="utf-8",
            )
            failures = validate_residual_risk_authority_invariants(root)
            self.assertTrue(
                any(
                    "every required category" in failure
                    for failure in failures
                )
            )

    def test_rejects_waivable_nonwaivable_condition(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_risk_files(root)
            target = root / "docs/worksheets/production-readiness-review.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "Any such non-waivable condition forces **hold** or **abort**",
                    "A non-waivable condition may be exception approved",
                ),
                encoding="utf-8",
            )
            failures = validate_residual_risk_authority_invariants(root)
            self.assertTrue(
                any("non-waivable condition forces" in failure for failure in failures)
            )

    def test_rejects_removed_nonwaivable_exception_clause(self) -> None:
        protected_fragments = (
            "missing operating or distribution rights",
            "mandatory duty, precondition, or deadline",
            "uncertain applicability",
            "expired, widened, unowned, out-of-category, or",
        )
        for fragment in protected_fragments:
            with self.subTest(fragment=fragment), TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_required_risk_files(root)
                target = root / "docs/worksheets/production-readiness-review.md"
                target.write_text(
                    target.read_text(encoding="utf-8").replace(
                        fragment,
                        "removed non-waivable clause",
                    ),
                    encoding="utf-8",
                )
                failures = validate_residual_risk_authority_invariants(root)
                self.assertTrue(
                    any(fragment.splitlines()[0] in failure for failure in failures),
                    fragment,
                )

    def test_rejects_removed_canonical_nonwaivable_clause(self) -> None:
        protected_fragments = (
            "It cannot waive a clear legal, regulatory, contractual,",
            "cure missing rights or a mandatory",
            "make a Tier 4 scope releasable",
            "unresolved non-waivable, blocking, or",
        )
        for fragment in protected_fragments:
            with self.subTest(fragment=fragment), TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_required_risk_files(root)
                target = root / "docs/governance/operating-model.md"
                target.write_text(
                    target.read_text(encoding="utf-8").replace(
                        fragment,
                        "removed canonical clause",
                    ),
                    encoding="utf-8",
                )
                failures = validate_residual_risk_authority_invariants(root)
                self.assertTrue(
                    any(fragment in failure for failure in failures),
                    fragment,
                )

    def test_rejects_removed_required_input_fail_closed_clause(self) -> None:
        cases = (
            (
                Path("docs/governance/operating-model.md"),
                "out-of-scope required input",
            ),
            (
                Path("docs/worksheets/ai-risk-impact-assessment.md"),
                "out-of-scope required input",
            ),
            (
                Path("docs/worksheets/production-readiness-review.md"),
                "required discipline inputs\n  are current and are not treated as votes",
            ),
        )
        for relative, fragment in cases:
            with self.subTest(relative=relative), TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_required_risk_files(root)
                target = root / relative
                target.write_text(
                    target.read_text(encoding="utf-8").replace(
                        fragment,
                        "required inputs may be missing",
                    ),
                    encoding="utf-8",
                )
                failures = validate_residual_risk_authority_invariants(root)
                self.assertTrue(
                    any(fragment.splitlines()[0] in failure for failure in failures),
                    fragment,
                )

    def test_rejects_removed_separate_exception_contract(self) -> None:
        cases = (
            (
                Path("docs/worksheets/ai-assisted-change-evidence.md"),
                "**Separate policy-exception decision ID:**",
            ),
            (
                Path("docs/delivery/security-first-ai-dlc.md"),
                "separate decision ID and one named policy-designated exception authority",
            ),
            (
                Path("docs/delivery/code-deployment.md"),
                "every exception links a separate decision ID",
            ),
            (
                Path("docs/governance/control-catalog.md"),
                "Exceptions are explicit, separate, and temporary",
            ),
        )
        for relative, fragment in cases:
            with self.subTest(relative=relative), TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_required_risk_files(root)
                target = root / relative
                target.write_text(
                    target.read_text(encoding="utf-8").replace(
                        fragment,
                        "generic exception owner",
                    ),
                    encoding="utf-8",
                )
                failures = validate_residual_risk_authority_invariants(root)
                self.assertTrue(
                    any(fragment in failure for failure in failures),
                    fragment,
                )

    def test_rejects_removed_ai_change_nonwaivable_clause(self) -> None:
        protected_fragments = (
            "clear legal, regulatory, contractual, license, or",
            "missing rights or mandatory duty",
            "uncertain\n  applicability",
            "missing required owner, discipline decision, approval,\n  independence, or evidence",
            "or Tier 4 scope",
        )
        for fragment in protected_fragments:
            with self.subTest(fragment=fragment), TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_required_risk_files(root)
                target = root / "docs/worksheets/ai-assisted-change-evidence.md"
                target.write_text(
                    target.read_text(encoding="utf-8").replace(
                        fragment,
                        "removed non-waivable clause",
                    ),
                    encoding="utf-8",
                )
                failures = validate_residual_risk_authority_invariants(root)
                self.assertTrue(
                    any(fragment.splitlines()[0] in failure for failure in failures),
                    fragment,
                )

    def test_rejects_legacy_generic_acceptor_field(self) -> None:
        cases = (
            (
                Path("docs/worksheets/vendor-assessment.md"),
                "**Residual-risk acceptor:**",
            ),
            (
                Path("docs/worksheets/regulatory-obligation-register.md"),
                "| Residual-risk acceptor, when a permitted risk remains |",
            ),
            (
                Path("docs/worksheets/threat-model.md"),
                "residual risks and accountable acceptors;",
            ),
            (
                Path("docs/delivery/evaluation-strategy.md"),
                "an approver for residual risk",
            ),
            (
                Path("docs/operations/incident-problem-and-corrective-action.md"),
                "| Accept residual product risk | business or product owner |",
            ),
            (
                Path("docs/operations/incident-problem-and-corrective-action.md"),
                "permanent fix released or an explicit time-bounded risk decision",
            ),
            (
                Path("docs/worksheets/incident-and-corrective-action-record.md"),
                "The permanent fix is released or residual risk is explicitly accepted.",
            ),
            (
                Path("docs/security/agent-extension-supply-chain.md"),
                "acceptable residual risk, named owner",
            ),
            (
                Path("docs/security/security-architecture.md"),
                "unresolved findings and risk acceptances;",
            ),
            (
                Path("docs/delivery/security-first-ai-dlc.md"),
                "Named qualified owner records the decision and conditions",
            ),
            (
                Path("docs/architecture/model-portfolio-and-routing.md"),
                "and residual-risk approval.",
            ),
            (
                Path("docs/delivery/public-release-and-external-distribution.md"),
                "accountable acceptor, remediation owner",
            ),
            (
                Path("docs/worksheets/agent-extension-assessment.md"),
                "Conditions, finding and policy-permitted exception IDs",
            ),
            (
                Path("docs/worksheets/evaluation-plan-and-report.md"),
                "accountable approvers;",
            ),
            (
                Path("docs/worksheets/agent-execution-and-telemetry-contract.md"),
                "authorized residual-risk or loss decision",
            ),
            (
                Path("docs/worksheets/agent-execution-and-telemetry-contract.md"),
                "qualified decision authority",
            ),
            (
                Path("docs/worksheets/agent-execution-and-telemetry-contract.md"),
                "authorized-residual-unknown",
            ),
            (
                Path("docs/worksheets/transfer-decommissioning-and-retirement.md"),
                "policy basis, qualified authority, decision ID",
            ),
            (
                Path("docs/architecture/reference-architecture.md"),
                "Accountable people and review processes",
            ),
            (
                Path("docs/worksheets/ai-assisted-change-evidence.md"),
                "**Exception owner, expiry, and compensating controls:**",
            ),
            (
                Path("docs/delivery/security-first-ai-dlc.md"),
                "stop conditions, and exception owner;",
            ),
            (
                Path("docs/delivery/code-deployment.md"),
                "exceptions identify exposure, compensating control, owner, and expiry",
            ),
            (
                Path("docs/governance/control-catalog.md"),
                "Record unmet outcome, exposure, compensating control, owner, expiry, and remediation",
            ),
            (
                Path("docs/examples/worked-golden-thread.md"),
                "results, exceptions, and decision",
            ),
            (
                Path("docs/worksheets/incident-and-corrective-action-record.md"),
                "The permanent fix is released or every residual risk",
            ),
        )
        for relative, fragment in cases:
            with self.subTest(relative=relative), TemporaryDirectory() as directory:
                root = Path(directory)
                self.write_required_risk_files(root)
                target = root / relative
                target.write_text(
                    target.read_text(encoding="utf-8") + "\n" + fragment,
                    encoding="utf-8",
                )
                failures = validate_residual_risk_authority_invariants(root)
                self.assertTrue(
                    any(
                        "legacy residual-risk authority language" in failure
                        for failure in failures
                    )
                )


class DecisionAuthorityInvariantTests(TestCase):
    def write_required_decision_files(self, root: Path) -> None:
        for relative, fragments in DECISION_AUTHORITY_INVARIANTS.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(fragments), encoding="utf-8")

    def test_accepts_required_decision_authority_language(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_decision_files(root)
            self.assertEqual(validate_decision_authority_invariants(root), [])

    def test_rejects_route_vote_drift(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_decision_files(root)
            target = (
                root
                / "docs/worksheets/model-routing-and-agent-dispatch-plan.md"
            )
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "Supporting rows are not votes",
                    "Supporting rows determine the majority vote",
                ),
                encoding="utf-8",
            )
            failures = validate_decision_authority_invariants(root)
            self.assertTrue(
                any("Supporting rows are not votes" in failure for failure in failures)
            )

    def test_rejects_extension_authority_drift(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_decision_files(root)
            target = root / "docs/worksheets/agent-extension-assessment.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "**Named extension-admission authority and authority basis:**",
                    "**Extension approvers:**",
                ),
                encoding="utf-8",
            )
            failures = validate_decision_authority_invariants(root)
            self.assertTrue(
                any(
                    "Named extension-admission authority" in failure
                    for failure in failures
                )
            )

    def test_rejects_legacy_extension_decision_taxonomy(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_decision_files(root)
            target = root / "docs/security/agent-extension-supply-chain.md"
            target.write_text(
                target.read_text(encoding="utf-8") + "\n## Risk decision\n",
                encoding="utf-8",
            )
            failures = validate_decision_authority_invariants(root)
            self.assertTrue(
                any("legacy decision taxonomy" in failure for failure in failures)
            )

    def test_rejects_legacy_route_lifecycle_taxonomy(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_decision_files(root)
            target = (
                root
                / "docs/worksheets/model-routing-and-agent-dispatch-plan.md"
            )
            target.write_text(
                target.read_text(encoding="utf-8")
                + "\nAn application may use only records whose state is **approved**.\n",
                encoding="utf-8",
            )
            failures = validate_decision_authority_invariants(root)
            self.assertTrue(
                any("legacy decision taxonomy" in failure for failure in failures)
            )


class RoutingServingBoundaryInvariantTests(TestCase):
    def write_required_routing_files(self, root: Path) -> None:
        for relative, fragments in ROUTING_SERVING_BOUNDARY_INVARIANTS.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(fragments), encoding="utf-8")

    def test_accepts_managed_and_enterprise_operated_contract(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_routing_files(root)
            self.assertEqual(
                validate_routing_serving_boundary_invariants(root),
                [],
            )

    def test_rejects_missing_boundary_enforcement_invariants(self) -> None:
        protected_fragments = (
            (
                Path("docs/architecture/model-portfolio-and-routing.md"),
                "`serving_boundary_revision`",
            ),
            (
                Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"),
                "Serving boundary ID / revision / digest",
            ),
            (
                Path("docs/worksheets/agent-execution-and-telemetry-contract.md"),
                "no raw attestation evidence",
            ),
            (
                Path("docs/security/security-architecture.md"),
                "authenticated, freshness-bounded deployment/load measurement",
            ),
            (
                Path("docs/architecture/model-and-provider-candidate-catalog.md"),
                "not the universe of permitted deployment patterns",
            ),
            (
                Path("docs/examples/worked-golden-thread.md"),
                "`SB-PEA-001@SB-PEA-001-r1`",
            ),
        )
        for relative, fragment in protected_fragments:
            with self.subTest(relative=relative, fragment=fragment):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.write_required_routing_files(root)
                    target = root / relative
                    target.write_text(
                        target.read_text(encoding="utf-8").replace(
                            fragment,
                            "removed invariant",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    failures = validate_routing_serving_boundary_invariants(root)
                    self.assertTrue(
                        any(fragment in failure for failure in failures),
                        failures,
                    )

    def test_rejects_removed_mode_specific_operator_records(self) -> None:
        protected_fragments = (
            (
                Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"),
                "model or weights digest, provenance",
            ),
            (
                Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"),
                "provider service, account/project, endpoint, region",
            ),
            (
                Path("docs/platform/platform-engineering.md"),
                "separate decision-bound serving-runtime identity",
            ),
            (
                Path("docs/worksheets/agent-execution-and-telemetry-contract.md"),
                "authenticated deployment/load measurement ID and freshness result",
            ),
        )
        for relative, fragment in protected_fragments:
            with self.subTest(relative=relative, fragment=fragment):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.write_required_routing_files(root)
                    target = root / relative
                    target.write_text(
                        target.read_text(encoding="utf-8").replace(
                            fragment,
                            "removed mode-specific record",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    failures = validate_routing_serving_boundary_invariants(root)
                    self.assertTrue(
                        any(fragment in failure for failure in failures),
                        failures,
                    )

    def test_rejects_removed_offline_anti_rollback_contract(self) -> None:
        protected_fragments = (
            (
                Path("docs/architecture/model-portfolio-and-routing.md"),
                "copying the package or restoring a VM/device snapshot invalidates it",
            ),
            (
                Path("docs/worksheets/model-routing-and-agent-dispatch-plan.md"),
                "rollback-resistant local",
            ),
            (
                Path("docs/worksheets/agent-execution-and-telemetry-contract.md"),
                "independent local/physical disablement proof",
            ),
        )
        for relative, fragment in protected_fragments:
            with self.subTest(relative=relative, fragment=fragment):
                with TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.write_required_routing_files(root)
                    target = root / relative
                    target.write_text(
                        target.read_text(encoding="utf-8").replace(
                            fragment,
                            "removed offline anti-rollback contract",
                            1,
                        ),
                        encoding="utf-8",
                    )
                    failures = validate_routing_serving_boundary_invariants(root)
                    self.assertTrue(
                        any(fragment in failure for failure in failures),
                        failures,
                    )

    def test_rejects_token_only_capacity_economics(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_routing_files(root)
            target = (
                root
                / "docs/worksheets/model-routing-and-agent-dispatch-plan.md"
            )
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "A token-only estimate is invalid",
                    "A token-only estimate is sufficient",
                ),
                encoding="utf-8",
            )
            failures = validate_routing_serving_boundary_invariants(root)
            self.assertTrue(
                any("A token-only estimate is invalid" in failure for failure in failures)
            )

    def test_rejects_legacy_cloud_only_routing_language(self) -> None:
        for relative, forbidden_fragments in (
            ROUTING_SERVING_BOUNDARY_FORBIDDEN.items()
        ):
            for fragment in forbidden_fragments:
                with self.subTest(relative=relative, fragment=fragment):
                    with TemporaryDirectory() as directory:
                        root = Path(directory)
                        self.write_required_routing_files(root)
                        target = root / relative
                        target.write_text(
                            target.read_text(encoding="utf-8")
                            + f"\n{fragment}\n",
                            encoding="utf-8",
                        )
                        failures = validate_routing_serving_boundary_invariants(
                            root
                        )
                        self.assertTrue(
                            any(
                                "legacy routing serving-boundary language"
                                in failure
                                for failure in failures
                            ),
                            failures,
                        )


class PublicReleaseResultInvariantTests(TestCase):
    def write_required_release_files(self, root: Path) -> None:
        for relative, fragments in PUBLIC_RELEASE_RESULT_INVARIANTS.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(fragments), encoding="utf-8")

    def test_accepts_explicit_fail_closed_release_results(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            self.assertEqual(validate_public_release_result_invariants(root), [])

    def test_rejects_non_pass_result_that_no_longer_forces_hold(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = root / "docs/worksheets/public-release-readiness.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "Any **Fail**, **Unknown**, or **Stale**",
                    "Only selected failures",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any(
                    "Any **Fail**, **Unknown**, or **Stale**" in failure
                    for failure in failures
                )
            )

    def test_rejects_unjustified_not_applicable_drift(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = (
                root
                / "docs/delivery/public-release-and-external-distribution.md"
            )
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "Missing evidence, owner, review capacity, or unresolved applicability is not",
                    "Missing evidence may be treated as",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any("unresolved applicability is not" in failure for failure in failures)
            )

    def test_rejects_r6_result_relabeling_drift(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = root / "docs/worksheets/public-release-readiness.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "R6 cannot relabel, backfill, or",
                    "R6 may relabel, backfill, or",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any("R6 cannot relabel, backfill, or" in failure for failure in failures)
            )

    def test_rejects_ordinary_go_without_publication_ready_precondition(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = root / "docs/worksheets/public-release-readiness.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "**Outcome mapping:** ordinary **Go** requires a decision-bound R0–R5",
                    "Ordinary Go may ignore the R0–R5",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any("ordinary **Go** requires" in failure for failure in failures)
            )

    def test_rejects_removed_nonwaivable_release_blocker(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = (
                root
                / "docs/delivery/public-release-and-external-distribution.md"
            )
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "unresolved applicable obligation or required treatment",
                    "unresolved applicable obligation may be waived",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any(
                    "unresolved applicable obligation or required treatment" in failure
                    for failure in failures
                )
            )

    def test_rejects_publication_decision_after_publication(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = root / "docs/worksheets/public-release-readiness.md"
            text = target.read_text(encoding="utf-8")
            target.write_text(
                text.replace(
                    "### R6 publication decision",
                    "### Publication decision moved out of sequence",
                )
                + "\n### R6 publication decision\n",
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any("R6 publication decision must precede R7" in failure for failure in failures)
            )

    def test_rejects_r7_readback_that_no_longer_fails_closed(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = root / "docs/worksheets/public-release-readiness.md"
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "R7 is satisfied only when every prescribed public-state check",
                    "R7 may be satisfied before every public-state check",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any("R7 is satisfied only when" in failure for failure in failures)
            )

    def test_rejects_r8_continue_without_current_r6_and_readback(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = (
                root
                / "docs/delivery/public-release-and-external-distribution.md"
            )
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "R8 **continue** requires a current, unexpired R6 Go or governed-exception",
                    "R8 **continue** may ignore an expired R6 decision",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any("R8 **continue** requires" in failure for failure in failures)
            )

    def test_rejects_material_correction_without_new_r6_decision(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_required_release_files(root)
            target = (
                root
                / "docs/delivery/public-release-and-external-distribution.md"
            )
            target.write_text(
                target.read_text(encoding="utf-8").replace(
                    "returns to the earliest affected gate and requires a new R6 decision before",
                    "may be published without returning to an earlier gate or decision",
                ),
                encoding="utf-8",
            )
            failures = validate_public_release_result_invariants(root)
            self.assertTrue(
                any("requires a new R6 decision" in failure for failure in failures)
            )
