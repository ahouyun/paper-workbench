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

## Conclusion vs. Abstract

| Dimension | Abstract | Conclusion |
|-----------|----------|------------|
| Purpose | Help reader decide whether to read | Help understand "so what" |
| Scope | Full overview | Deep interpretation and reflection |
| New information? | No | Can include new insights |
| Style | Informational, compressed | Interpretive, reflective |

## Contribution Statement Patterns

- **Direct:** "Our contribution is threefold: first, ...; second, ...; third, ..."
- **Gap-filling:** "While prior work has focused on X, our paper contributes by addressing Y."
- **Novelty:** "To the best of our knowledge, this is the first study to..."

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
