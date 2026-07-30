from __future__ import annotations

import unittest

from scripts.check_reference_urls import (
    normalize_extracted_url,
    validate_url,
)


class ReferenceUrlPolicyTests(unittest.TestCase):
    def test_allows_exact_https_source_host(self):
        self.assertEqual(validate_url("https://csrc.nist.gov/pubs/sp/800/218/final"), [])

    def test_allows_reviewed_ntia_source_host(self):
        self.assertEqual(
            validate_url(
                "https://www.ntia.gov/programs-and-initiatives/"
                "artificial-intelligence/open-model-weights-report"
            ),
            [],
        )

    def test_allows_reviewed_astral_source_host(self):
        self.assertEqual(
            validate_url("https://docs.astral.sh/uv/pip/compile/"),
            [],
        )

    def test_allows_reviewed_pypi_source_host(self):
        self.assertEqual(
            validate_url("https://pypi.org/simple"),
            [],
        )

    def test_allows_case_insensitive_scheme_for_approved_host(self):
        self.assertEqual(validate_url("HTTPS://csrc.nist.gov/pubs/sp/800/218/final"), [])

    def test_rejects_http(self):
        self.assertIn("scheme must be https", validate_url("http://csrc.nist.gov/"))

    def test_rejects_unknown_host(self):
        violations = validate_url("https://unreviewed.example/reference")
        self.assertTrue(any("not allowlisted" in item for item in violations))

    def test_rejects_unknown_host_with_uppercase_scheme(self):
        violations = validate_url("HTTPS://unreviewed.example/reference")
        self.assertTrue(any("not allowlisted" in item for item in violations))

    def test_rejects_ip_literal(self):
        violations = validate_url("https://169.254.169.254/latest/meta-data/")
        self.assertTrue(any("IP-literal" in item for item in violations))

    def test_rejects_userinfo_confusion(self):
        violations = validate_url("https://csrc.nist.gov@169.254.169.254/")
        self.assertIn("userinfo is prohibited", violations)
        self.assertTrue(any("IP-literal" in item for item in violations))

    def test_rejects_nonstandard_port(self):
        self.assertIn(
            "port must be 443 or omitted",
            validate_url("https://csrc.nist.gov:8443/reference"),
        )

    def test_rejects_backslash_authority_ambiguity(self):
        self.assertIn(
            "backslashes are prohibited in external URLs",
            validate_url("https://csrc.nist.gov\\@169.254.169.254/"),
        )

    def test_normalizes_markdown_closer_after_sentence_punctuation(self):
        self.assertEqual(
            normalize_extracted_url("https://docs.astral.sh/uv/pip/compile/)."),
            "https://docs.astral.sh/uv/pip/compile/",
        )

    def test_preserves_balanced_parenthesis_in_url(self):
        self.assertEqual(
            normalize_extracted_url("https://example.com/function_(test)."),
            "https://example.com/function_(test)",
        )


if __name__ == "__main__":
    unittest.main()
