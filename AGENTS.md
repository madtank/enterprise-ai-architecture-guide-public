# Contributor guidance

This repository is a vendor-neutral enterprise AI architecture guide.

## Content rules

- Distinguish the model from the full AI system.
- Lead with business ownership, affected people, and measurable outcomes.
- State architecture decisions as outcomes and trade-offs, not vendor features.
- Treat model output as untrusted input.
- Keep authoritative state changes behind typed, authorized business services.
- Use risk-proportionate controls and identify observable evidence.
- Mark jurisdiction-specific or time-sensitive requirements with a source and review date.
- Keep terms aligned with `docs/glossary.md`.

## Change rules

- Read the linked issue, relevant existing pages, prior ADRs, ownership, and
  deployment guidance before editing.
- Keep changes focused and preserve unrelated user work.
- Update `mkdocs.yml` when adding a page that belongs in navigation.
- Add or revise an ADR for consequential architectural direction.
- Keep diagrams in Mermaid where practical and explain them in prose.
- Never add secrets, customer data, production prompts, or confidential evaluation examples.
- Run `python scripts/check_docs.py` and `mkdocs build --strict` before
  considering documentation changes complete.
- For a defect, reproduce the failure or explain why reproduction is not
  possible; record before-and-after verification.
- For non-trivial AI-assisted work, follow
  `docs/delivery/skills-first-ai-development.md` and complete the relevant
  portions of `docs/worksheets/ai-assisted-change-evidence.md`.
- Do not publish raw session logs, hidden reasoning, system or developer
  instructions, credentials, cookies, private paths, or unrelated work.
- An agent may prepare a focused branch and draft pull request when authorized.
  It may not approve, merge, publish, deploy, change repository access, or
  weaken required checks without explicit authority.
- AI-generated review is not independent approval. Changes to agent
  instructions, skills, CI, ownership, deployment, security, or governance
  controls require human owner review.
