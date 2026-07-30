# Repository ownership

This file records who is accountable for this repository and how ownership,
review, merge, publication, incident response, and continuity are handled.

## Current owner

- **Accountable repository steward:** `@madtank`
- **Repository:** `madtank/enterprise-ai-architecture-guide`
- **Current status:** source-only public reference repository; original
  repository content licensed under MIT
- **Canonical branch:** `main`
- **Review routing:** `.github/CODEOWNERS`
- **Merge enforcement:** repository rules and required checks described in
  `DEPLOYMENT.md`; verify live settings after any visibility or plan change
- **Accepted backup / independent reviewer:** not yet designated
- **Security reporting:** `SECURITY.md`
- **Deployment status:** see `DEPLOYMENT.md`

`@madtank` owns the scope, maintainer appointments, merge and publication
authority, future licensing changes, and transfer or archival decision.

## Maintainer responsibilities

Maintainers:

- triage content, correction, repository, build, and security reports;
- preserve the guide's vendor-neutral editorial standard;
- verify authoritative sources and as-of dates;
- review architecture, governance, security, delivery, and automation changes
  with the relevant domain owner;
- keep navigation, links, validation, ownership, and contribution paths
  working;
- protect confidential information and private security reports;
- keep release and recovery instructions current;
- record material decisions and known limitations.

## Review and merge authority

- Pull requests by the repository owner are internal-owned work, but remain
  subject to relevant checks and risk-proportionate review.
- `CODEOWNERS` routes review; it does not enforce approval. Repository rules
  and required checks provide enforcement only after their live configuration
  is read back and tested.
- Changes to `.github/**`, `AGENTS.md`, `OWNERSHIP.md`, `DEPLOYMENT.md`,
  governance, security, deployment, incident, and control guidance require
  passing checks and explicit owner review. Seek qualified independent
  subject-matter review for material changes.
- Automation and AI agents may prepare branches, evidence, and draft pull
  requests. They may not auto-merge or publish without explicit authority.
- Security, privacy, legal, and other time-sensitive claims require review by
  the owning discipline and a dated authoritative source.
- Repository visibility, future license changes, custom-domain changes, and
  transfer of ownership are owner decisions, not ordinary editorial merges.
- Any external distribution must apply the
  [public release and external distribution gate](docs/delivery/public-release-and-external-distribution.md)
  and bind approval to the exact sanitized artifact and channel.

## Sole-maintainer limitation

This repository currently has one named steward and therefore does not provide
enterprise separation of duties. Until an accepted second reviewer exists:

- require pull requests and the validation workflow for every change;
- require conversation resolution and block force pushes and branch deletion;
- disclose when a material change lacks qualified independent review;
- do not describe owner-only review, AI review, or a successful workflow as
  independent approval; and
- do not rely on this repository as an organizational control source.

Owner review, an AI review, or a successful workflow is not independent
approval.

## AI-assisted changes

An accountable human must review and understand AI-assisted work. Use the
[AI-assisted change evidence](docs/worksheets/ai-assisted-change-evidence.md)
worksheet for non-trivial changes. Do not publish raw session logs, hidden
reasoning, system instructions, tokens, private paths, or unrelated work.

AI-generated review is supplemental. The change-producing agent cannot provide
independent approval for its own change or weaken a required check and then
use the weakened result as evidence.

## Continuity

The repository currently has one named GitHub owner. Before it receives
production dependencies, becomes operationally critical, or is relied upon as
an organizational control source:

1. designate at least one accepted backup maintainer;
2. prefer a team or organization-owned repository over personal continuity;
3. document recovery for account loss and inaccessible credentials;
4. record the publishing environment, domain, and credentials owner;
5. test transfer, archival, and rollback procedures;
6. review owner, collaborator, application, deploy-key, and bypass access at a
   defined interval.

Do not invent or list a backup until that person or team accepts the duty.

## Transfer or archival

Transfer or archival requires:

- a completed
  [transfer, decommissioning, and retirement record](docs/worksheets/transfer-decommissioning-and-retirement.md)
  for the exact repository, publishing, integration, and downstream boundary;
- an accountable decision and effective date;
- inventory of branches, issues, pull requests, releases, domains,
  integrations, credentials, and downstream links;
- accepted successor ownership or an explicit no-successor decision;
- preservation of required records and security reports;
- revocation of obsolete identities and deployment access;
- clear notice to readers and contributors;
- validation that redirects, published artifacts, and retention behave as
  intended.

The repository owner approves final transfer or archival.
