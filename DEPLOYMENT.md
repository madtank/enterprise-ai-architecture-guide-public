# Repository deployment

This file governs validation, merge, and any future publication of the
Enterprise AI Architecture Guide. For general software deployment controls,
see
[`docs/delivery/code-deployment.md`](docs/delivery/code-deployment.md).

## Current state

The repository currently has:

- a strict MkDocs build;
- a universal, hash-locked Python dependency closure reproduced byte for byte
  with a verified, repository-pinned resolver before binary-only installation;
- repository-owned uv and Lychee versions, official release URLs, and archive
  digests verified before execution;
- deterministic offline validation of tracked local Markdown links and MkDocs
  navigation, with a fail-closed guard against a zero-link extraction;
- a GitHub Actions validation workflow in `.github/workflows/docs.yml`;
- a monthly, non-merge-blocking external reference check in
  `.github/workflows/reference-currency.yml`;
- no configured GitHub Pages, custom-domain, package, or other production
  publication workflow.

The tracked reference-source manifest covers durable guide pages and public
repository guidance. `PUBLICATION.md` defines the source-distribution boundary
without including private working history or operational evidence.

A successful `Validate documentation` workflow provides evidence that the
checked revision built and that the local links and navigation scanned in that
run resolved. It does **not** prove external sources remain current or publish
a website. The Git repository is currently the canonical deliverable.

The repository is designed for a clean public history rather than a visibility
change to a private working repository. Repository rules, security features,
and private vulnerability reporting are effective only after their live
settings and public behavior are read back and tested.

## Local validation

Use Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python scripts/check_requirements_lock.py
python -m pip install --require-hashes --only-binary=:all: -r requirements.txt
python -m unittest discover -s tests -p 'test_*.py'
python scripts/check_docs.py
python -m mkdocs build --strict
```

The documentation check operates on tracked and staged Markdown files so that
unrelated local drafts do not affect a release decision. Use
`python scripts/check_docs.py --include-untracked` when reviewing every local
draft.

Preview locally when a change affects navigation, diagrams, callouts, or
rendered structure:

```bash
python -m mkdocs serve
```

Open the loopback preview address printed by MkDocs, normally on port 8000,
and inspect the affected pages.

## Dependency and CI tool updates

Treat dependency and validation-tool changes as supply-chain changes, not
routine formatting:

1. Change direct Python pins in `requirements.in`.
2. Review the package release, provenance, compatibility, and known security
   information.
3. Use the exact uv version pinned in
   `scripts/install_verified_uv.sh` and
   `scripts/reproduce_requirements_lock.sh`. Regenerate the complete lock with
   an explicit UTC review cutoff, following the official
   [uv locking guidance](https://docs.astral.sh/uv/pip/compile/). Preserve the
   generated command in the lock header and update `LOCK_CUTOFF` in the
   reproduction script:

   ```bash
   uv --no-config --no-python-downloads pip compile requirements.in \
     --universal \
     --generate-hashes \
     --python-version 3.11 \
     --exclude-newer YYYY-MM-DDTHH:MM:SSZ \
     --upgrade \
     --only-binary :all: \
     --no-sources \
     --no-cache \
     --default-index https://pypi.org/simple \
     --output-file requirements.txt
   ```

4. Review every added, removed, or changed package and hash. Run
   `scripts/reproduce_requirements_lock.sh` to require byte-for-byte equality,
   then run the lock policy validator, its tests, and a clean Python 3.12
   installation with `--require-hashes --only-binary=:all:`.
5. When changing uv, review its official release metadata and published
   checksum, then update the version and digest in
   `scripts/install_verified_uv.sh` and the required version in
   `scripts/reproduce_requirements_lock.sh`.
6. For Lychee, review the official release metadata, then update the version,
   release URL, and archive SHA-256 together in
   `scripts/install_verified_lychee.sh`. Verify the downloaded archive before
   committing, keep `GITHUB_TOKEN` blank in link-checking steps, and preserve
   the nonempty `--dump` preflight before the real link check.
7. Record the review, commands, result, and source revision in the pull-request
   evidence, including the exact `uv --version` used to regenerate the lock.

As of 2026-07-28, CI uses the official
[uv 0.11.15 release](https://github.com/astral-sh/uv/releases/tag/0.11.15)
to reproduce the lock and the official
[Lychee 0.24.2 release](https://github.com/lycheeverse/lychee/releases/tag/lychee-v0.24.2)
for link checking on Linux x86_64. The version, release URL, and archive
SHA-256 values in the verified installer scripts are the canonical executable
inputs.
Exact versions and hashes constrain reviewed inputs; they do not prove that an
upstream release is vulnerability-free or trustworthy. Continue vulnerability
monitoring and use a focused, reviewed update rather than bypassing a pin.

## Change and merge procedure

1. Create or link an issue for a material correction, new topic, repository
   failure, or publication change.
2. Assign a change owner and relevant domain reviewer.
3. Work on a focused branch.
4. Update navigation and cross-links with the content.
5. Run the dependency policy, security-validator tests, strict build, and
   local-link validation.
6. Open a pull request using the repository template.
7. Provide before-and-after evidence for a defect and an ADR for a
   consequential architecture or governance decision.
8. Wait for trusted checks and accountable maintainer review.
9. Seek qualified independent subject-matter review for material security,
   privacy, legal, safety, or organizational-control changes. When it is
   unavailable, disclose that limitation and do not characterize the result as
   independently assured, certified, or approved for organizational adoption.
10. Merge only with explicit authority. Automation must not auto-merge.
11. Verify `main` passes the same validation after merge.

The untracked local `site/` directory is disposable build output and is not a
publication source.

## Public GitHub security baseline

As checked on 2026-07-30, GitHub Free supports branch rulesets for public
repositories, but not for a private repository owned by a personal account.
Configure and read back the following baseline before relying on this public
repository:

- create one active ruleset targeting `main`, with an empty bypass list;
- require pull requests, dismiss stale approvals, require conversation
  resolution, require the branch to be current, and require the observed
  `Build and validate` check from GitHub Actions;
- require linear history and block branch deletion and force pushes;
- permit squash merging only and delete merged head branches;
- require one approval and code-owner review only after an accepted second
  write collaborator exists. Until then, zero required approvals is a
  documented temporary control gap, not independent review or enterprise
  separation of duties;
- leave required signed commits disabled until contributors have a documented
  signing and compatible merge procedure. GitHub documents a squash-merge
  limitation when signed commits are required;
- keep Actions' default token read-only, prevent Actions from creating or
  approving pull requests, require approval for all outside-collaborator fork
  runs, allow only GitHub-owned or explicitly approved actions, and preserve
  full-commit-SHA pins;
- enable and test private vulnerability reporting, dependency graph,
  Dependabot alerts and security updates, secret scanning, and repository push
  protection. Add CodeQL as a required check only after its exact check name is
  observed passing on the public repository;
- keep Pages, packages, discussions, projects, and the wiki disabled until
  each surface has an owner and a release decision; and
- subscribe the accountable owner to security alerts and verify the private
  report path without submitting sensitive test data.

Use the current official documentation for
[ruleset availability and controls](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets),
[GitHub plan limits](https://docs.github.com/en/get-started/learning-about-github/githubs-plans),
[Actions repository settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository),
[security and analysis settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository),
and
[private vulnerability reporting](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
Rules and features are plan- and repository-state-dependent; record the
observed settings rather than treating this checklist as proof.

## Publication gate

Apply the canonical
[public release and external distribution gate](docs/delivery/public-release-and-external-distribution.md)
and complete its
[readiness record](docs/worksheets/public-release-readiness.md) for the exact
repository, generated site artifact, history, logs, metadata, and target
channel. The following repository-specific decisions remain mandatory.

Do not configure public hosting until the repository owner explicitly
approves the target audience and purpose; reuse terms; hosting platform,
canonical URL, and domain; repository and backup maintainers; enforceable
branch rules or an approved equivalent; publication, rollback, and credentials
owners; branch and environment protection; analytics, privacy, cookie,
accessibility, and legal treatment; and retention, archive, support,
vulnerability, takedown, and persistent-copy procedures.

Original tracked content is licensed under the MIT License. The source
repository is the intended distribution unit. That license does not clear
third-party dependencies, generated site assets, or another distribution unit.

## Publication procedure when decision-authorized

A future publishing workflow should:

1. trigger only from an approved protected branch or signed release;
2. use pinned workflow dependencies and minimal permissions;
3. build once from an immutable source revision;
4. retain the site artifact and its checksum;
5. deploy that exact artifact through a protected environment;
6. prevent routine self-approval and administrator bypass; when adopted policy
   expressly permits an exception, bind the named human authority, scope,
   rationale, compensating controls, and expiry to the exact artifact and do
   not represent it as independent approval;
7. record source revision, workflow identity, artifact digest, target, and
   independent-approval or governed-exception record;
8. verify the canonical URL, HTTPS, navigation, representative pages, assets,
   robots and sitemap behavior, and absence of draft or confidential content;
9. expose a clear stop and rollback path;
10. preserve the prior known-good artifact until verification completes.

Before enabling publication, use a GitHub plan or another source-control
mechanism that can enforce the adopted review and required-check policy.

If GitHub Pages is selected, keep build and deploy as distinct jobs and use the
minimum `contents: read`, `pages: write`, and `id-token: write` permissions
required by the official Pages workflow. Protect the `github-pages`
environment and confirm which platform features are available to the
repository plan.

## Publication verification

Record:

- source commit and site artifact digest;
- workflow run and approver;
- publication start and completion time;
- canonical URL and resolved DNS;
- HTTP status, TLS result, and expected redirect behavior;
- navigation and representative-page checks;
- search, sitemap, and asset checks;
- accessibility or visual checks appropriate to the change;
- known deviations and owner.

A workflow completing successfully is insufficient if the public URL serves
the wrong revision.

## Rollback

For a content or navigation defect:

1. pause further publication;
2. identify the last known-good source revision and published artifact;
3. restore the known-good artifact when the platform supports artifact
   redeployment, or create a focused revert through the protected PR path;
4. rebuild and validate rather than editing generated `site/` files;
5. publish through the protected environment;
6. read back the public revision and affected pages;
7. open or update the repository problem record;
8. add a regression check, link fix evidence, and complete corrective action.

For a security or confidential-content exposure, also remove public access
where appropriate, preserve restricted evidence, revoke affected credentials,
assess caches and history, and follow `SECURITY.md`.

## Ownership and recovery

The repository owner is identified in `OWNERSHIP.md`. Before hosting is
enabled, record a backup maintainer, publishing operator, credentials owner,
domain owner, and incident contact. Test recovery from an unavailable owner,
failed deployment, expired credential, and lost or misconfigured domain.
