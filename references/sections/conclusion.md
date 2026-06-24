# Conclusion Writing Guide

## Goal

Close the paper with clear takeaways and credible limitations.

## Structure

1. Restate solved problem and core technical idea.
2. Summarize strongest evidence from experiments.
3. State practical impact or new insight.
4. Add limitation paragraph.
5. End with concrete future direction.

## Limitation Guidance

Prefer limitations tied to task goal/setting boundaries, for example:

1. Data regime limitation (e.g., only short sequences).
2. Assumption limitation (e.g., controlled viewpoints only).
3. Deployment scope limitation (e.g., specific sensor setup).

Avoid framing conclusion around fixable implementation flaws unless they critically define your method's scope.

## Distinguish Limitation Types

1. Technical defect: underperforms strong baselines on key metrics or causes unacceptable tradeoff.
2. Scope limitation: bounded by current task setting and still competitive vs. current SOTA.

## Template

1. This paper addresses [problem] by proposing [method].
2. The key idea is [core insight], which enables [main benefit].
3. Experiments show [main gains] across [datasets/settings].
4. A current limitation is [scope boundary], and extending to [future setting] is an important next step.

## Real Conclusion Examples

### SAM (Kirillov et al., TPAMI 2023)

> "We introduced the Segment Anything project: a task, model, and dataset for image segmentation. SAM achieves zero-shot transfer to 23 datasets, often matching or exceeding fully supervised results. SAM struggles with fine-grained boundaries and thin structures. Combining SAM with specialized models for specific domains is an important next step."

**Pattern:** Summary → Key result → Specific limitation → Future work

### FlashAttention (Dao et al., NeurIPS 2022)

> "We propose FlashAttention, an IO-aware attention algorithm. FlashAttention achieves 2-4x speedup and 5-20x memory reduction compared to standard attention. This enables training on sequences up to 16K tokens without approximation. Future work includes extending to sparse attention patterns."

**Pattern:** Method → Quantified result → Impact → Future work

### DeepSeek-V3 (DeepSeek, 2024)

> "We presented DeepSeek-V3, a 671B parameter MoE language model. DeepSeek-V3 matches GPT-4 performance on most benchmarks. The model was trained with only 2.788M H800 GPU hours, demonstrating that open-source models can compete with closed-source alternatives."

**Pattern:** Method → Result → Cost efficiency → Impact

## Conclusion vs. Abstract

| Dimension | Abstract | Conclusion |
|-----------|----------|------------|
| Purpose | Help reader decide whether to read | Help understand "so what" |
| Scope | Full overview | Deep interpretation and reflection |
| New information? | No | Can include new insights |
| Style | Informational, compressed | Interpretive, reflective |

## Contribution Statement Patterns

Note: Contribution statements typically appear in the Introduction. In the Conclusion, briefly re-emphasize contributions at a higher level.

- **Direct:** "Our contribution is threefold: first, ...; second, ...; third, ..."
- **Gap-filling:** "While prior work has focused on X, our paper contributes by addressing Y."
- **Novelty:** "To the best of our knowledge, this is the first study to..."

## Conclusion Length by Venue

| Venue | Length | Style |
|-------|--------|-------|
| **IEEE Trans** | 150-250 words | Comprehensive, with limitations paragraph |
| **CVPR/ECCV** | 100-200 words | Brief, often merged with discussion |
| **NeurIPS/ICML** | 150-250 words | Moderate, limitations increasingly expected |
| **ACL/EMNLP** | 200-300 words | Moderate, broader impact sometimes required |
| **Nature/Science** | 200-300 words | Emphasize significance and societal impact |

## Discussing Limitations

1. Be honest but strategic — transparent, but contextualize
2. Prioritize — focus on the most relevant limitations
3. Explain impact — how the limitation might affect results
4. Pair with mitigation — explain why findings are still valuable
5. Link to future research — frame limitations as opportunities

## Future Work Patterns

| Pattern | Example |
|---------|---------|
| Scale/Efficiency | "We plan to scale to larger datasets." |
| Generalization | "Extending to [broader domain] is a natural next step." |
| Theoretical | "A formal convergence guarantee remains open." |
| Deployment | "We intend to evaluate in production environments." |

## IEEE Trans Addendum

For IEEE Transactions papers, apply these extra rules:

### 1. Restate only evidenced gains

The conclusion may summarize the strongest results, but should not introduce any new number or scope claim
that has not already appeared in the paper.

### 2. Keep scope boundaries explicit

Prefer:

- `evaluated on ...`
- `limited to ...`
- `demonstrated under ...`

Avoid:

- `proves broad real-world applicability`
- `shows universal effectiveness`

unless the paper truly supports those claims.

### 3. Match limitation type to paper type

- Method papers: limitation should reflect operating conditions, assumptions, or deployment boundaries.
- Survey papers: limitation should reflect coverage boundary or update horizon.
- Empirical/software engineering papers: limitation should reflect corpus, protocol, or external validity.

### 4. No inflated ending

Do not use the conclusion to add prestige language that the experiments did not earn.

---

## Anti-AI Patterns for Conclusions (去AI味)

### C1: The "In Conclusion" Opening
**Bad:** "In conclusion, this paper proposes a novel method for..."
**Good:** Start directly with the key finding or contribution.
**Rule:** Delete "In conclusion." The section header already signals the conclusion.

### C2: The "Experimental Results Fully Demonstrate" Template
**Bad:** "The experimental results fully demonstrate the effectiveness of our method."
**Good:** "Our method outperforms DINO by 2.1 AP on COCO, with consistent improvements across model scales."
**Rule:** State specific results, not vague "demonstrate effectiveness."

### C3: The "Future Work" Boilerplate
**Bad:** "In the future, we will continue to improve our method and explore more applications."
**Good:** "Extending to video segmentation and 3D point clouds are natural next steps, given the method's architecture."
**Rule:** Future work should be specific and tied to the method's design.

### C4: The "Promising Results" Ending
**Bad:** "Experimental results show promising performance and demonstrate the potential of our approach."
**Good:** End with a specific insight or implication that wasn't already stated in the abstract.

### C5: Repeating the Abstract
**Bad:** Copying the abstract's structure and content.
**Good:** The conclusion should add new perspective: limitations, implications, or broader impact.

### C6: Missing Limitations
**Bad:** Only stating successes.
**Good:** "Our method assumes fixed camera intrinsics, which limits application to handheld devices."
**Rule:** Acknowledge specific limitations. This builds credibility.

### Conclusion De-AI Checklist

- [ ] No "In conclusion" opening
- [ ] No "Experimental results fully demonstrate" template
- [ ] Future work is specific and tied to method design
- [ ] No "promising results" ending
- [ ] Not a copy of the abstract
- [ ] Specific limitations are acknowledged

## Conclusion Writing Templates

### Template 1: Single-Contribution Paper

```
[1-2 sentences: Restate the problem and your solution]
[1-2 sentences: Key experimental result with specific numbers]
[1 sentence: Practical impact or broader significance]
[1-2 sentences: Specific limitations]
[1-2 sentences: Concrete future work]
```

**Example:**
> "We proposed FlashAttention, an IO-aware algorithm for exact attention computation. FlashAttention achieves 2-4x speedup and 5-20x memory reduction compared to standard attention. This enables training on sequences up to 16K tokens without approximation. Our current implementation requires custom CUDA kernels, limiting portability. Future work includes extending to sparse attention patterns and supporting additional hardware platforms."

### Template 2: Multi-Contribution Paper

```
[1 sentence: Summarize the overall contribution]
[1 sentence: Contribution 1 result]
[1 sentence: Contribution 2 result]
[1 sentence: Contribution 3 result]
[1-2 sentences: Limitations]
[1-2 sentences: Future work]
```

**Example:**
> "We presented Llama 2, a family of pretrained and fine-tuned LLMs. Llama 2-Chat achieves competitive performance with ChatGPT on human evaluations. We release both models and a comprehensive safety evaluation. Llama 2 bridges the gap between open-source and closed-source LLMs. Future work includes extending to multimodal inputs and improving alignment techniques."

### Template 3: Survey/Review Paper

```
[1 sentence: Summarize the survey scope]
[1-2 sentences: Key findings or taxonomy]
[1 sentence: Identified gaps or open challenges]
[1-2 sentences: Future research directions]
```

**Example:**
> "We surveyed 50+ parameter-efficient fine-tuning methods across 5 categories. Our analysis reveals that adapter-based and LoRA-based methods dominate current practice. However, few methods address catastrophic forgetting in continual learning settings. Future work should focus on methods that combine efficiency with robustness."

## Conclusion Length by Venue

| Venue | Recommended Length | Style |
|-------|-------------------|-------|
| IEEE Trans | 150-250 words | Comprehensive, with limitations paragraph |
| CVPR/ECCV | 100-200 words | Brief, often merged with discussion |
| NeurIPS/ICML | 150-250 words | Moderate, limitations increasingly expected |
| ACL/EMNLP | 200-300 words | Moderate, broader impact sometimes required |
| Nature/Science | 200-300 words | Emphasize significance and societal impact |

## Cross-References

**Conclusion → Introduction:**
- The limitations discussed here should connect to the gaps identified in Introduction
- The future work should extend the contributions listed in Introduction

**Conclusion → Experiments:**
- The results summarized here should come from the experiments section
- The limitations should be based on observed failure cases

**Conclusion → Method:**
- The future work should suggest method improvements based on observed limitations
