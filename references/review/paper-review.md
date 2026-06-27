# Paper Review

## Goal

Use an adversarial, reviewer-style checklist to detect reject risks early and revise the paper before submission.

## Core Principle

Pursue perfectionism in paper quality: assume reviewers will probe every weak point and proactively fix them.

## Critical Rule (Do Not Violate)

Every major claim, especially in Abstract and Introduction, must be:

1. technically correct, and
2. explicitly supported by experimental evidence.

If a claim is not supported, either add evidence or weaken/remove the claim.

If the claim is a novelty or contribution claim, it must also be supported by current literature positioning rather than intuition. In practice, this means the paper should be defensible under `references/workflow/innovation-mining-protocol.md`, not just persuasive in prose.

## What Usually Gets a Paper Accepted

1. Sufficient contribution (novel task/pipeline/module/design finding/insight)
2. Better empirical performance than prior methods under fair comparisons
3. Sufficient comparison experiments and ablation studies
4. Clear narrative arc (problem → gap → solution → evidence)
5. Strong visual presentation (figures, tables, layout)
6. Appropriate scope (not overclaiming)

## Common Rejection Dimensions

| Rejection Dimension          | Typical Failure Signals                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1. Insufficient contribution | 1.1 Targeted failure cases are too common.<br /> 1.2 Proposed technique is already well explored; expected gains are predictable/well-known.                                                                                                                                               |
| 2. Unclear writing           | 2.1 Missing technical details; work is not reproducible.<br />2.2 A method module lacks clear motivation.                                                                                                                                                                                  |
| 3. Weak empirical effect     | 3.1 Improvement over prior methods is only marginal.<br /> 3.2 Even if better than previous methods, absolute performance is still not strong enough.                                                                                                                                      |
| 4. Incomplete evaluation     | 4.1 Missing ablation studies.<br />4.2 Missing important baselines or important evaluation metrics.<br /> 4.3 Datasets are too simple to prove the method truly works.                                                                                                                    |
| 5. Problematic method design | 5.1 Experimental setting is unrealistic.<br />5.2 Method has technical flaws and appears unreasonable.<br />5.3 Method is not robust and needs per-scenario hyperparameter tuning. <br /> 5.4 New design introduces stronger limitations than its benefits, leading to negative net value. |

## Novelty Audit Before Review

Before scoring contribution quality, run a fast novelty audit:

1. What is the paper's central novelty claim in one sentence?
2. What is the closest prior art or closest-work cluster?
3. Is the claimed difference a real mechanism/protocol/system contribution, or just a renamed direction keyword?
4. Has the paper shown why the closest work does not already cover the same central claim?
5. If direct novelty is weak, has the paper switched to a narrower and more defensible rescue route?

Reject-risk signal:

- the paper writes a polished novelty story, but never identifies closest prior art or novelty threat.

## End-of-Paper Self-Review Question List

Add this checklist near the end of the draft while revising.
Use each question to trigger concrete edits before submission.

### 1. Contribution

1. What new knowledge does this paper give to readers?
2. Are we solving a truly meaningful failure case, not a trivial/common one?
3. Is the technical idea genuinely non-obvious beyond well-explored practice?
4. Is our gain surprising or insightful rather than a predictable improvement?
5. Is there at least one clear novelty type (task/pipeline/module/design finding/insight)?
6. Can we name the closest prior art and explain the differentiator in one precise sentence?
7. Are we mistaking a direction label such as `Transformer`, `Mamba`, `Diffusion`, `LLM`, or `foundation model` for the innovation itself?
8. If recent work already covers the broad claim, did we narrow the claim to a benchmark gap, mechanism gap, deployment gap, theory gap, or negative-result opportunity?

### 2. Writing Clarity

1. Can a knowledgeable reader reproduce the method from the paper?
2. Did we provide enough technical detail for each key module?
3. Is the motivation of every module explicit and logically connected to a challenge?
4. Are terms and notation consistent across sections?
5. Does each paragraph carry one clear message with smooth transitions?

### 3. Experimental Strength

1. Are improvements over strong baselines meaningful, not just statistically tiny?
2. Is absolute performance competitive enough for the target venue?
3. Are gains consistent across multiple datasets/settings/metrics?
4. Do we report both strengths and failure cases honestly?

### 4. Evaluation Completeness

1. Do we include ablations for all key design choices?
2. Are all strong/recent baselines included under fair settings?
3. Are evaluation metrics standard and sufficient for this task?
4. Are datasets/scenarios challenging enough to validate real effectiveness?
5. Are comparison and ablation protocols clearly documented?

### 5. Method Design Soundness

1. Is the experimental setting realistic for practical use?
2. Does the method have hidden technical defects or unreasonable assumptions?
3. Is the method robust without heavy per-case hyperparameter retuning?
4. Do benefits outweigh added complexity and new limitations?
5. Could reviewers reasonably argue that the net benefit is negative?

## Adversarial Writing Workflow

1. Read the paper as a skeptical reviewer.
2. For every contribution claim, identify the closest prior art and current novelty threat.
3. Answer every question above with explicit evidence from the paper.
4. Mark each item as `pass`, `needs revision`, or `needs new experiment`.
5. Revise claims, writing, experiments, or method scope accordingly.
6. If novelty remains weak after review, route back to `references/workflow/innovation-mining-protocol.md` and change the framing before polishing the prose.
7. Repeat until no major rejection risk remains.

## IEEE Trans Review Addendum

Use this addendum when the target venue is an IEEE Transactions journal.

### 1. Article Type Check

Confirm that the paper structure matches the real article type:

- `survey_or_roadmap`
- `method_or_system`
- `benchmark_or_dataset`
- `empirical_or_software_engineering`
- `critical_review`

Reject-risk signal:

- the paper uses a template spine that does not match its true contribution type.

### 2. Introduction Funnel Check

Ask:

1. Does the introduction move from broad stakes to a precise technical or methodological gap?
2. If the problem is complex, are challenges and responses explicitly paired?
3. Are contribution bullets concrete and later evidenced?
4. Is there a paper organization paragraph when the paper is long or structurally dense?
5. Does the introduction distinguish the paper from the closest prior art instead of only naming a trendy direction?

Reject-risk signal:

- the introduction sounds informative but does not set up a falsifiable contribution.

### 3. Figure Role Check

Ask:

1. Does Figure 1 explain the paper rapidly?
2. Is there an early pipeline, taxonomy, system, or study-design figure when needed?
3. Does each result figure answer a distinct question rather than decorate the paper?

Reject-risk signal:

- many figures exist, but none clarifies the paper's core logic.

### 4. Table Role Check

Ask:

1. Is there a main benchmark or synthesis table anchoring the paper?
2. Is there an ablation, decomposition, or component-isolation table when the claim needs it?
3. If efficiency is part of the claim, are quality and efficiency shown together?

Reject-risk signal:

- the paper claims strong results but the tables do not let a reviewer verify why.

### 5. Results Ordering Check

Ask whether the results section answers reviewer questions in a useful order:

1. Is the main benchmark comparison first?
2. Are the key gains localized by ablation or study design?
3. Are efficiency, limitations, and failure cases surfaced instead of buried?
4. If novelty depends on a specific mechanism, does the results section contain the exact evidence package needed to defend that mechanism?

Reject-risk signal:

- the section reads like a dump of experiments instead of a defense of the claims.

### 6. Cross-Disciplinary Rigor Check for TSE-like Papers

For empirical studies, surveys, and critical reviews:

1. Is the study corpus, subject set, or benchmark scope explicit?
2. Are research questions or study goals clearly stated?
3. Are threats to validity or scope limitations concrete?
4. If the paper critiques a concept, is the concept actually defined and grounded in prior theory?

Reject-risk signal:

- the paper borrows the language of rigor without exposing its study design.

### 7. Data and Figure Integrity Check

Ask:

1. If data are synthetic, generated, augmented, or mixed-source, is the provenance explicit?
2. If efficiency is claimed, is there a paired artifact showing quality and cost together?
3. Does every major figure or table answer a distinct reviewer question?
4. Are there explicit failure, limitation, or boundary artifacts when the claim is broad?
5. Are all scope numbers such as datasets, subject counts, devices, PRs, or deployment counts backed by evidence rather than assumed from memory?
6. Do explanatory figures avoid introducing modules, workflows, or quantitative facts that are absent from the manuscript?
7. If a figure is illustrative rather than measured, is that status explicit?
8. If a figure is used to defend novelty, does it clearly compare against the closest prior art rather than only against weak or generic baselines?

Reject-risk signal:

- the paper looks polished, but the evidence artifacts do not support the prose.

## Novelty-Specific Reject Signals

Treat the following as high-priority findings:

1. The manuscript never states the closest prior art, only the broad area.
2. The claimed innovation is actually a method family label or fashionable keyword.
3. The paper claims "first" or "novel" without current-search support.
4. The differentiator disappears once the strongest recent baseline is included.
5. The paper keeps a broad novelty claim even though only a narrow rescue route is defensible.

When any of these occur, prefer:

1. weaken or narrow the claim,
2. add explicit closest-work positioning,
3. request missing experiments or analysis,
4. or redirect to a safer contribution type.
