# Abstract Writing Guide

## Goal

Write a strong abstract by doing three things repeatedly:

1. Think through the abstract logic first.
2. Follow one template (Version 1/2/3 below).
3. Revise the abstract many times.

## Pre-Writing Questions (Important)

Answer these before writing:

1. What technical problem do we solve, and why is there no well-established solution? (important)
2. What is our technical contribution?
3. Why can our method work in essence?
4. What technical advantage and new insight do we provide? (important)

## Version 1: Challenge -> Contribution

Introduce the technical challenge, then use one to two sentences to present the technical contribution that solves the challenge.

### Structure

1. Task.
2. Technical challenge for previous methods.
3. One to two sentences introducing the technical contribution for solving the challenge.
4. Benefits of the technical contribution.
5. Experiment summary.

### Expert Notes

1. Discuss previous work around the technical challenge that we actually solve.
2. For the contribution sentence(s), usually mention the technical term/name only; do not explain every detailed step.
3. The technical term must be easy to understand; readers should not feel a jump.
4. This ability is very important for writing a good abstract.

Version 1 local cite:

1. `references/examples/abstract/template-a.md`

## Version 2: Challenge -> Insight -> Contribution

Introduce the technical challenge, then use one to two sentences to present the insight for solving the challenge, and then one sentence to present the technical contribution that implements this insight.

### Structure

1. Task.
2. Technical challenge for previous methods.
3. One sentence introducing the insight for solving the challenge.
4. One to two sentences introducing the technical contribution that implements the insight.
5. Benefits of technical novelty.
6. Experiment summary.

### Expert Notes

1. Discuss previous work around the technical challenge that we actually solve.
2. Introduce the insight in one clear sentence.
3. For the implementation sentence(s), usually mention the technical term/name only; do not explain every detailed step.
4. The technical term must be easy to understand; do not create a jump in reading.
5. This ability is very important for writing a good abstract.

Version 2 local cite:

1. `references/examples/abstract/template-b.md`

## Version 3: Multiple Contributions

Version 3: When there are multiple technical contributions, describe each contribution together with its technical advantage.

### Structure

1. Task.
2. If needed, one contrast sentence about prior methods.
3. Contribution sentence 1 + technical advantage.
4. Contribution sentence 2 + technical advantage.
5. Contribution sentence 3 + technical advantage.
6. Experiment summary.

### Expert Notes

1. When there are multiple technical contributions, describe each contribution together with its technical advantage.
2. The ability to express "contribution + advantage" in one sentence is very important for writing a good abstract.

Version 3 local cite:

1. `references/examples/abstract/template-c.md`

## Example Bank

1. `references/examples/abstract-examples.md`
2. `references/examples/abstract/template-a.md`
3. `references/examples/abstract/template-b.md`
4. `references/examples/abstract/template-c.md`

## Abstract Quality Checklist

1. Can a reader identify task, challenge, insight/contribution, and results in one pass?
2. Are all major claims supported by experiments?
3. Are technical names self-contained and readable?
4. Is there any sentence that mixes too many messages?

## Anti-AI Patterns for Abstracts (去AI味)

### Pattern A1: The "Despite Significant Progress" Opening
**Bad:** "Despite significant progress in deep learning, image segmentation remains a challenging task."
**Good:** "Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length." (FlashAttention)
**Rule:** State the specific technical bottleneck, not a generic "challenging task."

### Pattern A2: The "In This Paper" Filler
**Bad:** "In this paper, we propose a novel framework for..."
**Good:** "We propose FlashAttention, an IO-aware exact attention algorithm..." (FlashAttention)
**Rule:** Delete "In this paper." Start with the contribution.

### Pattern A3: The "Extensive Experiments" Vague Claim
**Bad:** "Extensive experiments on multiple benchmarks demonstrate the effectiveness of our method."
**Good:** "Zero-shot performance is often competitive with or superior to prior fully supervised results." (SAM)
**Rule:** State what was actually evaluated and what the result was.

### Pattern A4: The "Novel" Overuse
**Bad:** "We propose a novel and innovative approach that leverages a novel architecture..."
**Good:** "We propose DINO, which improves denoising anchor boxes for end-to-end object detection." (DINO)
**Rule:** "Novel" once per abstract max. Better: just state what you built.

### Pattern A5: The "Comprehensive" Inflation
**Bad:** "We conduct comprehensive experiments and thorough analysis..."
**Good:** "We built the largest segmentation dataset to date, with over 1 billion masks on 11M images." (SAM)
**Rule:** Replace adjectives with numbers.

### Pattern A6: The "Promising Results" Ending
**Bad:** "Experimental results show promising performance and demonstrate the potential of our approach."
**Good:** "Our models outperform open-source chat models on most benchmarks we tested, and may be a suitable substitute for closed-source models." (Llama 2)
**Rule:** End with a specific, qualified claim — not empty optimism.

### Pattern A7: The "However" Crutch
**Bad:** "However, existing methods... However, this approach... However, challenges remain..."
**Good:** Use "However" once max. Restructure other sentences.

### Pattern A8: Forced Motivation
**Bad:** "With the rapid development of artificial intelligence, deep learning has been widely applied in various fields."
**Good:** "Modern autonomous driving systems are typically developed as a stack of standalone modules." (UniAD)
**Rule:** Skip the history lesson. State the current situation directly.

### Pattern A9: Vague Dataset Mentions
**Bad:** "Experiments on several benchmarks confirm..."
**Good:** "We evaluate on COCO, LVIS, and ADE20K."
**Rule:** Name the datasets.

### Pattern A10: Template Superiority
**Bad:** "Our method achieves state-of-the-art performance."
**Good:** "E2E-YOLO is the first real-time end-to-end object detector with 56.8 AP." (YOLOv7)
**Rule:** Specific method name + specific metric + specific number.

### Abstract De-AI Checklist

- [ ] No "Despite significant progress" opening
- [ ] No "In this paper" filler
- [ ] No "Extensive experiments" without naming datasets
- [ ] "Novel" appears at most once
- [ ] No "Comprehensive" or "Thorough" without evidence
- [ ] Ending has a specific, qualified claim (not "promising results")
- [ ] "However" appears at most once
- [ ] No "With the rapid development of..." forced motivation
- [ ] All datasets are named
- [ ] All comparisons cite specific methods with numbers

## IEEE Trans Evidence Gate

When the target venue is an IEEE Transactions journal, apply these extra rules:

1. If the abstract reports a concrete number, that number must already be grounded in evidence.
2. Prefer auditable scope descriptors such as dataset size, subject count, device count, or named public datasets.
3. If exact numbers are not yet verified, rewrite the sentence without fake precision or mark the claim as `needs evidence`.
4. Do not write vague summaries such as `extensive experiments show ...` unless the next clause states the actual evaluation scope.

Safe patterns:

- `We evaluate the method on ...`
- `Experiments on real-world ... demonstrate ...`
- `Across multiple benchmark settings, ...`

Unsafe patterns when evidence is missing:

- `Our method achieves 12.7% improvement ...`
- `We test on 300 devices ...`
- `Extensive experiments show ...`
