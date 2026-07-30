# Dated model and provider candidate catalog

**Candidate and price snapshot captured:** 2026-07-27

**Product, lifecycle, and data claims verified:** 2026-07-28

**Price basis:** public USD list-price examples, with endpoint, region, and plan
basis stated per entry; generally per one million text tokens

**Required review:** monthly for price and lifecycle; quarterly and on material
change for product capability, policy, and data handling

This page owns fast-changing discovery inputs: model candidates, public price
examples, service plans, product-specific harness features, lifecycle notices,
and provider data-boundary statements. It is deliberately separate from the
durable
[governed model routing and agent dispatch](model-portfolio-and-routing.md)
architecture.

**Scope boundary:** this dated snapshot covers managed cloud-service discovery
only. It is not the universe of permitted deployment patterns and does not
prefer managed service over enterprise operation. An enterprise-operated
candidate starts from the organization's controlled artifact inventory,
provenance and license record, runtime/capacity design, and support lifecycle;
it then passes the same serving-boundary, exact-deployment, evaluation, route,
revocation, cost, and readback gates. Do not copy the cloud price rows or
provider data statements into an enterprise-operated approval.

Use this catalog to form an evaluation shortlist. Use the
[model routing and agent dispatch plan](../worksheets/model-routing-and-agent-dispatch-plan.md)
to approve an exact deployment, route, and harness adapter. A catalog entry is
not an approval, procurement recommendation, performance result, or claim that
the provider configuration meets organization policy.

!!! warning "Candidate is not approved"
    A family named on this page becomes production-approved only when the exact
    serving-boundary ID/revision/digest, provider service, model revision where
    exposed or
    monitored mutable-service record, endpoint, region, data configuration,
    processing plan, tool scope, evaluation bundle, owner, and review date are
    recorded and accepted. The same model family through two cloud services,
    or through a managed and enterprise-operated path, requires separate
    deployment approvals.

No model is “safe” by name. Safety is a property of the full use-case system:
provider and deployment controls, data handling, prompts, retrieval, tools,
authorization, output validation, human oversight, evaluation, monitoring,
and incident response.

## Illustrative candidate portfolio

This table is a discovery shortlist, not a universal recommendation or a
procurement quote. Prices vary by contract, region, context length, modality,
caching, batch mode, and service tier. Refresh the exact meter before approval.
Rates are per one million text tokens. OpenAI entries use direct, non-regional
Standard short-context rates and label cache reads and writes separately;
eligible OpenAI regional-processing endpoints carry the provider's stated 10%
uplift.[^openai-pricing] Google entries use the listed global on-demand rates
unless the row says otherwise.

| Role | Candidate cloud deployment | Public price snapshot on 2026-07-27 | Candidate treatment |
|---|---|---:|---|
| Frontier coordinator | OpenAI API GPT-5.6 Sol | $5 input / $0.50 cache read / $6.25 cache write / $30 output[^openai-pricing] | Difficult planning, synthesis, or verification after task evaluation |
| Balanced coordinator or worker | OpenAI API GPT-5.6 Terra | $2.50 input / $0.25 cache read / $3.125 cache write / $15 output[^openai-pricing] | General OpenAI candidate |
| Economical worker | OpenAI API GPT-5.6 Luna | $1 input / $0.10 cache read / $1.25 cache write / $6 output[^openai-pricing] | Bounded, high-volume work |
| Role-specific Azure deployment | Azure OpenAI approved GPT family | Meter, region, deployment type, and contract specific[^azure-models][^azure-pricing] | Candidate when Azure identity, network, data-zone, and commercial controls fit |
| Frontier coordinator | Amazon Bedrock Claude Opus 4.8 | Region- and plan-specific; retrieve the applicable meter[^bedrock-pricing] | Exception candidate where measured benefit justifies cost |
| Balanced coordinator or worker | Amazon Bedrock Claude Sonnet 5 | Promotional $2 input / $10 output through 2026-08-31; then $3 / $15[^bedrock-pricing] | General Bedrock candidate, subject to evaluation and price refresh |
| Economical worker | Amazon Bedrock Nova 2 Lite | $0.30 input / $2.50 output[^nova-lite] | Narrow classification, extraction, transformation, and evaluated tool workflows |
| Balanced coordinator or worker | Vertex AI Gemini 3.6 Flash | $1.50 input / $0.15 cached input / $7.50 output on the global endpoint[^vertex-pricing] | GA short-term candidate; Google says it retires 45 days after a replacement is released and lists no current retirement date[^vertex-lifecycle] |
| Economical worker | Vertex AI Gemini 3.5 Flash-Lite | $0.30 input / $0.03 cached input / $2.50 output on the global endpoint[^vertex-pricing] | Low-cost high-volume candidate |
| Transitional coordinator | Vertex AI Gemini 2.5 Pro | Up to 200K context: $1.25 input / $10 output; above 200K: $2.50 / $15[^vertex-pricing] | Existing-workload bridge only; Google lists retirement on 2026-10-16[^vertex-lifecycle] |
| Embedding | OpenAI `text-embedding-3-small` / `text-embedding-3-large` | $0.02 / $0.13 input respectively[^openai-pricing] | Select dimensions and retrieval quality through evaluation |
| Embedding | Amazon Titan Text Embeddings V2 | $0.02 input[^titan-embedding] | AWS-native retrieval candidate |
| Embedding | Vertex Gemini Embedding | $0.15 online / $0.12 batch input[^vertex-pricing] | Google-native retrieval candidate |
| Safety | OpenAI `omni-moderation-latest` | No charge[^openai-moderation] | Supplemental classifier, not application authorization |
| Safety | Amazon Bedrock Guardrails | Usage and policy meters vary[^bedrock-guardrails] | Supplemental content, topic, PII, prompt-attack, and grounding controls |
| Safety | Vertex configurable safety filters | Model-specific configuration[^vertex-safety] | Configure explicitly and test rather than relying on defaults |

Microsoft Foundry and Azure OpenAI provide enterprise deployment
surfaces for approved model families, including GPT models. Treat every Azure
deployment as its own candidate and record the applicable Azure meter, SKU,
region, deployment type, quota, data boundary, and lifecycle rather than
copying OpenAI direct pricing.[^azure-models][^azure-pricing]

Preview status is a discovery attribute, not an approval. Apply the
[durable preview and exact-deployment admission controls](model-portfolio-and-routing.md#candidate-discovery-boundary).
Model names and provider tiers are not comparable performance benchmarks.

## Service and price-plan candidates

Every entry means “where supported for the exact model, region, account, and
feature.” Support varies by provider and deployment; verify the current
provider documentation before evaluation or purchase.[^openai-pricing][^azure-deployments][^bedrock-pricing][^vertex-pricing]

| Cloud surface | Evaluation/default | Predictable latency or capacity | Delay-tolerant | Data-boundary decision |
|---|---|---|---|---|
| OpenAI API | Standard | Priority or Reserved Tier[^openai-reserved] | Batch or Flex | endpoint retention and Zero Data Retention eligibility |
| Azure OpenAI | Standard pay-as-you-go | provisioned throughput | batch where supported | Global, Data Zone, or Regional deployment |
| Amazon Bedrock | on-demand | priority, reserved, or provisioned where supported | flex or batch where supported | in-region, geographic cross-region, or global routing |
| Vertex AI | pay-as-you-go | Priority or Provisioned Throughput | Flex or batch where supported | endpoint availability, processing location, and feature-specific residency |

For Gemini Enterprise Agent Platform model endpoints, neither a global nor
regional endpoint alone guarantees data residency or in-region ML processing.
A global endpoint cannot satisfy a locality requirement by itself.[^vertex-locations]

Start with pay-as-you-go during evaluation. Purchase priority, reserved, or
provisioned capacity only after measuring demand and service objectives. Use
batch or flexible processing for evaluation, indexing, migrations, and bulk
transformation where delay is acceptable.

## Product-specific harness capabilities

These examples show why role-specific routing is plausible, not why a product
is approved. Product behavior, availability, and maturity can change:

- OpenAI Codex supports defaults and model or reasoning overrides for
  subagents.[^codex-subagents]
- Claude Code subagents can use a configured or per-invocation model, subject
  to organizational model availability policy.[^claude-subagents]
- Google ADK assigns a model to each LLM agent. Its documented model and agent
  routing APIs are experimental and, on the verification date, supported only in
  ADK TypeScript v1.0.0.[^google-routing]
- Amazon Bedrock AgentCore is framework- and model-flexible; its managed
  Harness supports model defaults and invocation overrides. Bedrock prompt
  routing selects within a configured model set and has service-specific
  limitations.[^agentcore][^bedrock-routing]

AWS states that AgentCore Harness treats invocation inputs and skill content as
trusted. Pass-through fields can change endpoints, headers, roles, providers,
models, or regions, and callers can override skill sources.[^agentcore-security]
Apply the durable
[harness adapter boundary](model-portfolio-and-routing.md#harness-adapter-boundary)
to those product-specific risks.

These features do not make unrestricted model self-selection safe. Each
integration must consume the enterprise route grant, map it to the
product-specific configuration, reject unsupported constraints, and return
conformance telemetry. Verify current product behavior before relying on it.

## Illustrative price arithmetic

Assume the direct, non-regional Standard short-context rates above, one Sol
coordinator call with 20K input and 5K output, plus ten workers with 10K input
and 2K output each, with no caching, tools, retries, or auxiliary charges:

- all Sol: approximately **$1.35 per run**;
- Sol coordinator with Terra workers: approximately **$0.80**, about 41% lower;
- Sol coordinator with Luna workers: approximately **$0.47**, about 65% lower.

This proves only the arithmetic under the stated 2026-07-27 price assumptions.
It does not show that a worker meets quality or lowers end-to-end latency.
Recalculate it from the current applicable meter before using it in a decision.

## Provider data-boundary statements

- OpenAI states that API business data is not used for training by default;
  endpoint retention and Zero Data Retention eligibility depend on features
  and approval.[^openai-data][^openai-retention]
- Microsoft states that Azure OpenAI prompts and outputs are not exposed to
  underlying model providers or used to improve models without permission.
  Global, Data Zone, and Regional deployments have different processing
  boundaries.[^azure-privacy][^azure-deployments]
- AWS states that Bedrock model providers cannot access customer prompts and
  completions. Cross-region and global inference require an explicit
  destination and residency decision.[^bedrock-data][^bedrock-regions]
- Google states that managed models are not trained on customer data without
  permission, while zero-retention and residency eligibility are
  feature-specific. For Gemini Enterprise Agent Platform model endpoints,
  Google also states that neither global nor regional endpoints guarantee data
  residency or in-region ML processing.[^vertex-zdr][^vertex-security][^vertex-locations]

These are provider statements, not proof that a particular application
configuration meets organizational policy. Validate contracts, current
documentation, settings, logs, and negative tests for the exact deployment.

[^openai-pricing]: OpenAI, [API pricing](https://developers.openai.com/api/docs/pricing).
[^openai-reserved]: OpenAI, [Reserved Tier](https://openai.com/api-reserved-tier/).
[^openai-moderation]: OpenAI, [`omni-moderation-latest`](https://developers.openai.com/api/docs/models/omni-moderation-latest).
[^openai-data]: OpenAI, [Business data privacy, security, and compliance](https://openai.com/business-data/).
[^openai-retention]: OpenAI, [Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data).
[^azure-models]: Microsoft, [Azure models sold directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai).
[^azure-pricing]: Microsoft, [Azure OpenAI pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/).
[^azure-deployments]: Microsoft, [Azure model deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types).
[^azure-privacy]: Microsoft, [Data, privacy, and security for Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy).
[^bedrock-pricing]: AWS, [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).
[^nova-lite]: AWS, [Nova 2 Lite cost-optimized processing example](https://aws.amazon.com/blogs/machine-learning/pair-nova-2-lite-with-claude-for-cost-optimized-document-processing/).
[^titan-embedding]: AWS, [Amazon Titan Text Embeddings V2](https://aws.amazon.com/blogs/machine-learning/get-started-with-amazon-titan-text-embeddings-v2-a-new-state-of-the-art-embeddings-model-on-amazon-bedrock/).
[^bedrock-guardrails]: AWS, [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html).
[^bedrock-data]: AWS, [Amazon Bedrock data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).
[^bedrock-regions]: AWS, [Geographic cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html).
[^vertex-pricing]: Google Cloud, [Vertex AI generative AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing).
[^vertex-lifecycle]: Google Cloud, [Model versions and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions).
[^vertex-safety]: Google Cloud, [Configure content safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters).
[^vertex-zdr]: Google Cloud, [Zero data retention](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention).
[^vertex-security]: Google Cloud, [Vertex AI security controls](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/security-controls).
[^vertex-locations]: Google Cloud, [Gemini Enterprise Agent Platform deployments and endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations).
[^codex-subagents]: OpenAI, [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).
[^claude-subagents]: Anthropic, [Claude Code subagents](https://code.claude.com/docs/en/sub-agents).
[^google-routing]: Google, [ADK model routing](https://adk.dev/agents/models/routing/) and [agent routing](https://adk.dev/agents/routing/).
[^agentcore]: AWS, [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/) and [Harness models](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-models.html).
[^agentcore-security]: AWS, [AgentCore Harness security and access controls](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-security.html).
[^bedrock-routing]: AWS, [Bedrock Intelligent Prompt Routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html).
