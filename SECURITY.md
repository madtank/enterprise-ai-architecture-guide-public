# Security Policy

## Supported version

The latest commit on `main` is the only supported version of this guide and its
documentation build.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability, leaked secret, or
other sensitive security concern.

Use GitHub's private vulnerability reporting or draft security advisory
workflow for this repository. If that option is unavailable, do not post
sensitive details. Open a minimal **Repository or publication problem** issue
stating only that private security intake is unavailable and request private
follow-up from `@madtank`.

Include only the information needed to reproduce and assess the concern:

- the affected file, workflow, dependency, or guidance;
- the potential impact and plausible abuse path;
- reproduction steps or a minimal proof of concept;
- any known mitigations; and
- whether the issue has been disclosed elsewhere.

Do not include customer data, credentials, confidential prompts, or production
system details. The maintainer will acknowledge reports on a best-effort basis
and coordinate next steps before public disclosure.

The maintainer will triage impact, contain exposure, preserve restricted
evidence, reproduce the issue where safe, add a regression check where
practical, require passing checks and accountable maintainer review, seek
qualified independent review for material findings, and verify the released
correction. If independent review is unavailable, the maintainer will disclose
that limitation rather than claim independent assurance. Public disclosure
timing depends on remediation and affected-party needs.
The
[public release and external distribution gate](docs/delivery/public-release-and-external-distribution.md)
applies to advisories, examples, and other outgoing security artifacts, but it
does not replace this private reporting and coordinated-disclosure path.

The repository currently has one named owner. `OWNERSHIP.md` requires an
accepted backup security and repository maintainer before production reliance
or use as an organizational control source.

## Scope

Security reports may cover:

- unsafe or misleading security guidance;
- examples that could expose data or bypass authorization;
- vulnerable documentation dependencies;
- GitHub Actions or repository configuration; and
- accidentally committed sensitive information.

Editorial corrections and requests for additional coverage should use the
repository's issue templates instead.
