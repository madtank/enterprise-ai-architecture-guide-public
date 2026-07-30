# Support

This repository provides an enterprise AI architecture guide and its supporting
worksheets. It does not provide legal advice, regulatory certification,
production incident response, or organization-specific architecture approval.

## Getting help

- Use the **Content gap** issue template when an important topic, audience, or
  decision is missing.
- Use the **Correction** issue template for inaccurate, unclear, stale, or
  internally inconsistent guidance.
- Use the **Repository or publication problem** template for reproducible
  build, validation, navigation, automation, ownership, deployment, or
  recovery failures.
- Follow [CONTRIBUTING.md](CONTRIBUTING.md) when proposing a change.
- Follow [SECURITY.md](SECURITY.md) for sensitive security concerns.

Before opening an issue, search existing issues and identify the affected page
or section. Include authoritative references and an as-of date for
time-sensitive claims.

Never post secrets, customer data, confidential prompts, internal system
details, or other sensitive information. Support is provided on a best-effort
basis without a response-time guarantee.

## Privacy, rights, and takedown notices

Use the **Privacy, rights, or takedown notice** template for a public-safe
privacy, licensing, attribution, or takedown notice. Include only the affected
public path, the requested outcome, and non-sensitive supporting references.
Do not post personal data, confidential ownership records, identity documents,
or private correspondence.

Use the private vulnerability-reporting route in [SECURITY.md](SECURITY.md)
when the concern involves exposed personal data, a leaked secret, or another
sensitive security issue. If private follow-up is needed for a non-security
rights concern, open only a minimal public notice requesting private
coordination.

## Triage and resolution

Maintainers classify a report by:

- affected readers, workflows, or published artifacts;
- security, privacy, legal, governance, and operational impact;
- whether incorrect guidance could cause unsafe implementation;
- reproducibility, spread, and availability of a safe workaround;
- whether a private security path is required.

A material issue receives an owner, priority, verification criteria, and
relevant domain reviewer. Duplicate reports should link to the owned canonical
issue rather than disappear without explanation.

For a reproducible defect:

1. preserve safe before-change evidence;
2. add a check that fails on the affected revision where practical;
3. implement the smallest focused correction;
4. require accountable maintainer review and seek qualified independent review
   for a material security, privacy, legal, safety, or control correction;
5. run strict build and local-link validation;
6. merge or publish through `DEPLOYMENT.md`;
7. verify the actual post-change result;
8. update tests, instructions, or process to prevent recurrence.

Closure should state the disposition, evidence, affected revision, and any
follow-up owner. A stale source or unresolved risk should remain visible with
an owner and review date rather than being marked fixed.
