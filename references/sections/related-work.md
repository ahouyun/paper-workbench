# Related Work Writing Guide

## Goal

Position your work against the most relevant lines of research, and make your novelty easy to verify.

## Workflow

1. List directly competing and recent baseline papers first.
2. Group literature by technical topic (not by publication year alone).
3. For each topic: summarize common paradigm, then key limitation relevant to your challenge.
4. End each topic by clarifying your distinction.

## Topic Design

Use 2-4 focused topics, for example:

1. Task-specific mainstream methods.
2. Methods closest to your core idea.
3. Auxiliary techniques your method builds on.

## Paragraph Template

1. Topic sentence: define scope of this topic.
2. Representative methods: one compact summary.
3. Limitation tied to your target technical challenge.
4. Transition sentence that leads to your method.

## Do and Don't

1. Do compare mechanisms, assumptions, and failure modes.
2. Do emphasize the exact gap your method fills.
3. Do not make Related Work a citation dump.
4. Do not hide strongest baselines.

## Checklist

1. Are all strongest/recent competitors covered?
2. Is each topic connected to your problem setting?
3. Is your difference explained in technical terms, not marketing terms?
4. Is citation coverage complete for all core claims?

## IEEE Trans Addendum

For IEEE Transactions papers, strengthen Related Work with the following rules:

### 1. Topic-first, not citation-first

Each subsection should answer one question:

- what family of methods exists,
- what common assumption they share,
- where that family breaks down,
- and how your paper differs.

Avoid the rhythm:

- `Paper A ... Paper B ... Paper C ...`

unless the paragraph ends with synthesis.

### 2. Evidence gate for literature claims

Do not write broad claims such as:

- `most methods`
- `recent studies`
- `widely adopted approaches`

unless the cited coverage is sufficient to support the scope.

If the scope is uncertain, narrow it:

- `representative recent methods`
- `a commonly used line of work`
- `several prior approaches`

### 3. Survey and roadmap papers need synthesis artifacts

If the paper is a survey or roadmap, Related Work should usually point to:

- a taxonomy figure,
- a comparison matrix,
- or a roadmap overview.

The figure should summarize the field structure rather than repeat the text.

### 4. Strongest-baseline honesty

If a baseline is the strongest competitor, name it and explain why it is strong.
Do not hide it behind a broad family label.

---

## Anti-AI Patterns for Related Work (去AI味)

### R1: Citation Dump
**Bad:** "Paper A does X. Paper B does Y. Paper C does Z."
**Good:** "Methods in this category share a common limitation: O(n²) memory. A (2023) approximates attention with sparse patterns, B (2024) uses low-rank decomposition, and C (2024) applies hashing. All sacrifice accuracy for efficiency."
**Rule:** Synthesize, don't list. Compare mechanisms and failure modes.

### R2: Vague Attribution
**Bad:** "Previous work has shown that attention is important."
**Good:** "Vaswani et al. (2017) demonstrated that self-attention captures long-range dependencies more effectively than RNNs."
**Rule:** Cite specific papers with specific findings.

### R3: Missing Gap Identification
**Bad:** "Many methods have been proposed for this task."
**Good:** "Existing methods require O(n²) memory, limiting application to sequences longer than 4K tokens. Our method achieves linear complexity."
**Rule:** State the specific gap your method fills.

### R4: Template Openings
**Bad:** "In recent years, deep learning has been widely applied to..."
**Good:** "Transformer-based methods dominate NLP tasks due to their ability to capture long-range dependencies."
**Rule:** Start with the current paradigm, not a history lesson.

### R5: Hiding Strong Baselines
**Bad:** Only citing weak or outdated baselines.
**Good:** Include the strongest public methods, even if they perform better.
**Rule:** Reviewers will notice missing strong baselines.

### R6: Marketing Language
**Bad:** "Our method is novel and innovative, significantly outperforming all existing approaches."
**Good:** "Our method differs from A (2024) in that we use X instead of Y, which reduces memory from O(n²) to O(n)."
**Rule:** Explain differences in technical terms, not marketing terms.

### Related Work De-AI Checklist

- [ ] Not a citation dump — synthesized by topic
- [ ] All attributions are specific with paper names and findings
- [ ] Specific gap is identified for each topic
- [ ] No "In recent years" template openings
- [ ] Strong baselines are included
- [ ] Differences explained in technical terms
