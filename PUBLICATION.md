# Publication and provenance

## Distribution scope

This repository is a source-only public reference distribution of the
Enterprise AI Architecture Guide. It contains the guide, reusable worksheets,
repository policy, tests, and validation workflows.

The public distribution intentionally excludes:

- private working-repository history, branches, issues, pull requests,
  workflow logs, and operational evidence;
- raw agent transcripts, prompts, hidden reasoning, credentials, private
  paths, and unrelated local work;
- generated MkDocs output and other build artifacts; and
- confidential, customer, employee, or other personal data.

The public history begins with a clean source snapshot committed under the
privacy-preserving repository identity `madtank` and its GitHub-provided
noreply address. The public handle `@madtank` is intentional repository
attribution.

## AI assistance and limitations

The repository owner initiated this guide and used AI assistance during
research, drafting, review, and validation. AI review is advisory. It does not
provide independent approval, organizational adoption, certification, legal
advice, security assurance, or evidence that an implementation is effective.

The guide is a reference. Each adopter remains responsible for determining
applicability, assigning qualified owners, tailoring controls, validating the
implemented system, and approving consequential decisions.

## Validation boundary

The clean source candidate is validated with:

```bash
python scripts/check_docs.py
python scripts/check_requirements_lock.py
python -m unittest discover -s tests -p 'test_*.py'
python -m mkdocs build --strict
python scripts/check_reference_urls.py $(<scripts/reference_source_files.txt)
git diff --check
```

Before a visibility change or release, validation must run against the exact
committed tree. A clean-artifact review checks the source tree and metadata for
email addresses, private local paths, high-signal secrets, hidden bidirectional
or zero-width Unicode, unexpected binaries, symlinks, and unapproved files.
Automated scans reduce risk but do not prove that every possible issue is
absent.

GitHub Actions must pass on the public repository before its branch rules are
treated as effective. Repository security settings and private vulnerability
reporting must be read back and tested after the repository becomes public.

## Rights and generated artifacts

Original repository content is licensed under the [MIT License](LICENSE).
Referenced dependencies retain their own terms. This source distribution does
not vendor the Python packages named in the dependency lock.
See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the source and
generated-artifact boundary.

The generated MkDocs site is a separate distribution unit and is not included.
Before publishing a generated site, inventory its exact copied theme, icon,
search, JavaScript, and other assets; include the project license and all
required third-party notices; preserve embedded notices; and repeat the
clean-artifact review.

## Reporting and correction

- Use [SUPPORT.md](SUPPORT.md) for corrections, content gaps, and public-safe
  rights or takedown notices.
- Use [SECURITY.md](SECURITY.md) for vulnerabilities, leaked secrets, or
  sensitive data exposure.
- Use [CONTRIBUTING.md](CONTRIBUTING.md) for proposed changes and contribution
  rights.
- Use [DEPLOYMENT.md](DEPLOYMENT.md) for repository protection, release, and
  rollback controls.
