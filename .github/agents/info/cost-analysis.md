# Agent Cost Analysis

> Pricing based on **Claude Sonnet** rates: **$3.00 / 1M input tokens** · **$15.00 / 1M output tokens**
>
> Input cost = total context tokens. Output cost estimated from response token counts per scenario.

## Single Agent (`trip-advisor.agent.md`)

- 1× system prompt (~500 tokens)
- N× web search results (~3,000–8,000 tokens per fetch)
- 1× response generation

| Metric | Value |
|---|---|
| Total context | ~10,000–20,000 tokens |
| Sub-agent overhead | None |
| Estimated input cost | ~$0.030–$0.060 |
| Estimated output cost | ~$0.008–$0.015 (~500–1,000 output tokens) |
| **Estimated total cost** | **~$0.04–$0.08 per run** |

---

## Sequential Sub-Agents

- 1× orchestrator system prompt (~600 tokens)
- 1× transportation-agent system prompt (~500 tokens)
- N× transport web fetches (~5,000–8,000 tokens)
- 1× transport response (~1,500 tokens)
- Transport result added to orchestrator context (+1,500 tokens)
- 1× foodie-agent system prompt (~500 tokens)
- N× food web fetches (~5,000–8,000 tokens)
- 1× food response (~2,000 tokens)
- Both results in context for synthesis (+3,500 tokens)
- 1× final synthesis

| Metric | Value |
|---|---|
| Total context | ~20,000–35,000 tokens |
| Sub-agent overhead | ~2,600 tokens (2× system prompts + context carry-forward) |
| Estimated input cost | ~$0.060–$0.105 |
| Estimated output cost | ~$0.068 (~4,500 output tokens across 3 responses) |
| **Estimated total cost** | **~$0.13–$0.17 per run** |

---

## Parallel Sub-Agents

> Concurrent — no carry-forward between sub-agents

- 1× orchestrator system prompt (~600 tokens)
- 1× transportation-agent system prompt (~500 tokens)
- N× transport web fetches (~5,000–8,000 tokens)
- 1× transport response (~1,500 tokens)
- 1× foodie-agent system prompt (~500 tokens)
- N× food web fetches (~5,000–8,000 tokens)
- 1× food response (~2,000 tokens)
- Both results loaded together for synthesis (~3,500 tokens)
- 1× final synthesis

| Metric | Value |
|---|---|
| Total context | ~18,000–32,000 tokens |
| Sub-agent overhead | ~2,600 tokens (same as sequential) |
| Estimated input cost | ~$0.054–$0.096 |
| Estimated output cost | ~$0.068 (~4,500 output tokens across 3 responses) |
| **Estimated total cost** | **~$0.12–$0.16 per run** |

---

## Cost Comparison Summary

| Approach | Total Context | Est. Cost per Run | vs. Single Agent |
|---|---|---|---|
| Single Agent | ~10K–20K tokens | ~$0.04–$0.08 | baseline |
| Sequential Sub-Agents | ~20K–35K tokens | ~$0.13–$0.17 | ~2–3× more expensive |
| Parallel Sub-Agents | ~18K–32K tokens | ~$0.12–$0.16 | ~2–3× more expensive |

> **Note:** Parallel and sequential sub-agent approaches carry roughly the same cost. The advantage of parallel execution is speed, not cost savings.
