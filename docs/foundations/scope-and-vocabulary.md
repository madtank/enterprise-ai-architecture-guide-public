# Scope and vocabulary

## In scope

- predictive machine learning;
- foundation-model and generative-AI applications;
- retrieval-augmented generation;
- tool-using assistants and agents;
- embedded and end-user AI capabilities;
- shared enterprise AI platforms;
- governance, delivery, and production operations.

## Out of scope

This guide does not replace legal advice, sector-specific regulation, detailed cloud landing-zone standards, or organization-specific data classification policies. Those should be linked as authoritative overlays.

## System boundaries

Use these terms consistently:

- **AI use case** — a business capability or workflow that uses one or more AI techniques.
- **AI system** — the full sociotechnical system: users, workflow, software, models, data, tools, controls, and operations.
- **Model** — a learned component producing predictions, representations, or generated output.
- **Foundation model** — a broadly trained model adapted through prompting, retrieval, fine-tuning, or tools.
- **Agent** — a system that uses a model to choose or sequence actions toward a goal. Agency is a spectrum, not a product label.
- **Tool** — a capability an AI system may invoke through a defined contract.
- **Guardrail** — a preventive or detective control applied to input, context, output, or action.
- **Evaluation** — repeatable measurement of quality, safety, security, performance, and business fitness.
- **Human-in-the-loop** — a person must approve or alter an outcome before it takes effect.
- **Human-on-the-loop** — a person supervises operation and can intervene, but each action may not require approval.

## Classification dimensions

Classify a use case along all of these dimensions:

| Dimension | Questions |
|---|---|
| Impact | What happens if the system is wrong, unavailable, manipulated, or unfair? |
| Data | What sensitivity, residency, consent, and retention constraints apply? |
| People | Are employees, customers, patients, applicants, or the public affected? |
| Autonomy | Does the system advise, draft, decide, or act? |
| Scale | How many decisions, users, records, or dollars are affected? |
| Reversibility | Can a result be detected and corrected before harm occurs? |
| Exposure | Is the system internal, partner-facing, customer-facing, or public? |
