# Contributing

## Editorial standard

Contributions should be:

- vendor-neutral unless a vendor-specific example is clearly labeled;
- explicit about assumptions, trade-offs, and failure modes;
- testable through evidence, not only policy statements;
- proportional to use-case risk;
- understandable by architecture, engineering, and assurance readers.

Avoid treating a model as the whole system. Address data, identity, orchestration, human workflows, observability, ownership, and decommissioning.

## Change process

1. Open or link an issue for a material content gap, correction, repository
   problem, or publication change.
2. Name the change owner, intended reader, and decision the change helps them
   make.
3. Reproduce a defect before fixing it where practical, and define the
   verification that must fail before and pass afterward.
4. Open or update an architecture decision record for a consequential design
   or governance choice.
5. Link controls to observable evidence.
6. Require passing checks and accountable maintainer review. Seek qualified
   independent subject-matter review for material security, privacy, legal,
   safety, or organizational-control changes.
7. Run `python scripts/check_docs.py` and `mkdocs build --strict`, and record
   the result.
8. Merge or publish only through the authorized protected path in
   `DEPLOYMENT.md`.

Changes to security, privacy, safety, compliance, or risk guidance require
review by the owning discipline. When an independent reviewer is unavailable,
disclose that limitation and do not characterize the result as independently
assured, certified, or approved for organizational adoption. Legal requirements
must identify jurisdiction and an as-of date.

## Contribution license and rights

By submitting a contribution, you agree to license it under the repository's
[MIT License](LICENSE). You retain any copyright you hold.

Submit only material that you have authority to contribute. Identify any
third-party material, its source, and its applicable license or other terms in
the pull request. Do not submit material whose terms are incompatible with this
repository or whose redistribution has not been approved.

## AI-assisted contributions

AI-assisted work is welcome when an accountable human reviews and understands
it. For a non-trivial change:

- disclose AI assistance;
- identify the material skills and tools used;
- keep the change focused;
- use the
  [AI-assisted change evidence](docs/worksheets/ai-assisted-change-evidence.md)
  worksheet or equivalent concise PR evidence;
- include prompts or a sanitized decision trace only when safe and useful;
- do not publish raw logs, hidden reasoning, system instructions, credentials,
  private paths, or unrelated work;
- run trusted checks independently of the change-producing agent;
- do not let an agent approve, merge, or publish its own change.

Changes to `AGENTS.md`, skills, CI, required checks, ownership, or publication
policy are control changes and require explicit owner review.

## Definition of done

- Navigation and internal links work.
- Terms match the glossary.
- Diagrams have accompanying prose.
- Required controls identify an accountable owner and evidence.
- Time-sensitive claims include a source and review date.
- Examples do not contain secrets, production data, or confidential prompts.
- Defect fixes include before-and-after evidence or explain why reproduction
  was not possible.
- The accountable contributor understands the change and its evidence.
- Publication impact, rollback, and follow-up ownership are recorded when
  applicable.
- Any artifact leaving the established access boundary has a completed
  [public-release readiness record](docs/worksheets/public-release-readiness.md)
  bound to the exact candidate.
