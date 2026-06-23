# AI Writing Patterns Detection for Academic Papers

Based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and [blader/humanizer](https://github.com/blader/humanizer) v2.5.1.

## Why This Matters for Papers

Reviewers increasingly recognize AI-generated text. These patterns signal low effort and undermine credibility. Removing them makes writing sound authoritative and human.

---

## Content Patterns

### 1. Significance Inflation
**Flag:** "pivotal moment", "serves as a testament", "underscores the importance"
**Fix:** State facts directly. "This method improves accuracy by 3%" beats "This method serves as a pivotal advancement."

### 2. Notability Name-Dropping
**Flag:** Listing venues without context ("published in NeurIPS, CVPR, ICCV")
**Fix:** Cite specific work: "Li et al. (2024) showed X at NeurIPS."

### 3. Superficial -ing Analyses
**Flag:** "symbolizing", "reflecting", "showcasing", "highlighting"
**Fix:** Remove or replace with concrete claims.

### 4. Promotional Language
**Flag:** "groundbreaking", "state-of-the-art", "novel framework", "seamless integration"
**Fix:** Use specific descriptors. "We propose a transformer-based detector" beats "We introduce a groundbreaking framework."

### 5. Vague Attributions
**Flag:** "It is widely believed", "Previous work suggests"
**Fix:** Cite specific papers: "Zhang et al. (2023) demonstrated X."

### 6. Formulaic Challenges Sections
**Flag:** "Despite these challenges, our method..."
**Fix:** State challenges concretely, then address them with evidence.

---

## Language Patterns

### 7. AI Vocabulary (High-Frequency)
**Flag:** additionally, crucial, delve, emphasize, enduring, enhance, fostering, garner, highlight, interplay, intricate, key, landscape, pivotal, showcase, tapestry, testament, underscore, valuable, vibrant

**Academic-specific flags:** novel (overused), state-of-the-art, comprehensive, extensive, significant improvement

**Fix:** Use precise terms. "Our method outperforms X by 2%" beats "Our method significantly outperforms X."

### 8. Copula Avoidance
**Flag:** "serves as", "stands as", "represents a" instead of "is"
**Fix:** "The model is a transformer" beats "The model serves as a transformer-based architecture."

### 9. Negative Parallelisms
**Flag:** "Not only X, but also Y", "It's not just about X, it's about Y"
**Fix:** State directly: "X and Y both contribute to Z."

### 10. Rule of Three
**Flag:** Forced triads: "innovative, effective, and scalable"
**Fix:** Use two or four items, or be specific about why three.

### 11. Synonym Cycling
**Flag:** Alternating "model", "framework", "approach", "method" for the same thing
**Fix:** Pick one term and use it consistently.

### 12. False Ranges
**Flag:** "from simple baselines to complex architectures"
**Fix:** Be specific: "We compare against CNN, RNN, and transformer baselines."

### 13. Passive Voice Overuse
**Flag:** "Experiments were conducted", "Results were obtained"
**Fix:** Use active voice when the actor matters: "We evaluated on ImageNet" beats "Evaluation was performed on ImageNet."

---

## Style Patterns

### 14. Em Dash Overuse
**Flag:** Frequent use of — in academic text
**Fix:** Use commas, parentheses, or separate sentences.

### 15. Boldface Overuse
**Flag:** Excessive bolding of terms or results
**Fix:** Bold only section headers and key terms on first introduction.

### 16. Inline-Header Lists
**Flag:** **Performance:** The model achieves... **Efficiency:** The runtime is...
**Fix:** Write flowing prose or use proper subsections.

### 17. Title Case in Headings
**Flag:** "Related Work And Experiments"
**Fix:** Use sentence case: "Related work and experiments"

### 18. Emojis in Headings
**Flag:** Any emoji in academic text
**Fix:** Remove entirely.

### 19. Curly Quotes
**Flag:** "..." instead of "..."
**Fix:** Use straight quotes in academic writing.

---

## Communication Patterns

### 20. Chatbot Artifacts
**Flag:** "I hope this helps", "Let me know if you need..."
**Fix:** Remove entirely.

### 21. Knowledge-Cutoff Disclaimers
**Flag:** "As of our last update", "Based on available information"
**Fix:** Cite the actual date or source.

### 22. Sycophantic Tone
**Flag:** "Great question!", "Excellent point!"
**Fix:** Remove entirely.

---

## Filler and Hedging

### 23. Filler Phrases
- "In order to" → "To"
- "Due to the fact that" → "Because"
- "At this point in time" → "Now"
- "It is important to note that" → (delete)
- "The system has the ability to" → "The system can"

### 24. Excessive Hedging
**Flag:** "could potentially possibly", "might perhaps"
**Fix:** Use one qualifier: "may" or "could"

### 25. Generic Conclusions
**Flag:** "The future looks promising", "This represents a significant step forward"
**Fix:** State specific next steps or implications.

---

## Additional Patterns (v2.5.0+)

### 26. Hyphenated Word Pairs
**Flag:** "cross-functional", "data-driven", "end-to-end" (overused)
**Fix:** Use sparingly; prefer "end to end" when not modifying a noun.

### 27. Persuasive Authority Tropes
**Flag:** "At its core, what matters is...", "The key insight is..."
**Fix:** State the insight directly without preamble.

### 28. Signposting Announcements
**Flag:** "Let's dive in", "Moving on to...", "Now we turn to..."
**Fix:** Use section headers and transitions naturally.

### 29. Fragmented Headers
**Flag:** Header followed by a sentence restating it
**Fix:** Either the header or the sentence is redundant; remove one.

---

## Academic-Specific Patterns (from 100+ IEEE Trans Papers)

### 30. Empty Evidence Claims
**Flag:** "Extensive experiments demonstrate...", "Comprehensive evaluation shows...", "Numerous results confirm..."
**Fix:** State the actual evaluation scope. "We evaluate on COCO, LVIS, and ADE20K" beats "Extensive experiments on multiple benchmarks."
**Real example (good):** SAM: "We built the largest segmentation dataset to date, with over 1 billion masks on 11M images."

### 31. Generic Superiority Claims
**Flag:** "Our method outperforms all baselines", "achieves state-of-the-art performance"
**Fix:** Cite specific comparisons with numbers. "Outperforms DINO by 2.1 AP on COCO" beats "achieves state-of-the-art."
**Real example (good):** Llama 2: "Our models outperform open-source chat models on most benchmarks we tested, and may be a suitable substitute for closed-source models."

### 32. Filler "In This Paper"
**Flag:** "In this paper, we propose...", "This paper presents..."
**Fix:** Start directly. "We propose X" beats "In this paper, we propose X."
**Real example (good):** FlashAttention: "We propose FlashAttention, an IO-aware exact attention algorithm..."

### 33. Hedging Stacking
**Flag:** "It is worth noting that", "It should be mentioned that", "Interestingly,"
**Fix:** Delete the hedge and state the fact.

### 34. Vague Quantifiers
**Flag:** "significant improvement", "substantial gains", "remarkable performance"
**Fix:** Use specific numbers. "3.2% AP improvement" beats "significant improvement."
**Real example (good):** YOLOv7: "E2E-YOLO is the first real-time end-to-end object detector with 56.8 AP."

### 35. Forced Motivation Sentences
**Flag:** "With the rapid development of deep learning...", "In recent years, ... has attracted increasing attention..."
**Fix:** State the specific technical problem directly.
**Real example (good):** Mamba: "Prior subquadratic models fall short of Transformers on information-dense data."

### 36. Template Contribution Bullets
**Flag:** "We propose a novel method that...", "We are the first to..."
**Fix:** Be specific about what, why, and how much.
**Real example (good):** UniAD: "We design the first fully differentiable multi-task framework that unifies perception, prediction, and planning modules."

### 37. Conclusion Boilerplate
**Flag:** "In conclusion, this paper proposes...", "The experimental results fully demonstrate..."
**Fix:** End with a specific insight or implication.

### 38. "Novel" Overuse
**Flag:** Every other sentence contains "novel", "innovative", "unique"
**Fix:** Use "proposed" or "our" once per paragraph max.

### 39. Parallel Structure Abuse
**Flag:** Three+ sentences with identical structure
**Fix:** Vary sentence structure. Combine related points.

### 40. "Leverage" and "Harness" Overuse
**Flag:** "We leverage attention mechanisms...", "We harness the power of..."
**Fix:** "We use attention to..." or "Attention enables..."

### 41. Empty "Notably" / "Importantly"
**Flag:** "Notably, our method...", "Importantly, we observe..."
**Fix:** Delete. If it's notable, the reader will notice.

### 42. Scope Inflation
**Flag:** "across all domains", "in every scenario", "for any application"
**Fix:** State actual tested scope.

### 43. Abstract-Specific: The "Despite" Template
**Flag:** "Despite significant progress, ... remains challenging."
**Fix:** State the specific challenge without the "despite" preamble.
**Real example (good):** FlashAttention: "Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length."

### 44. Abstract-Specific: The "However" Crutch
**Flag:** Starting every other sentence with "However,"
**Fix:** Use "But" or restructure. "However" once per abstract is fine.

### 45. Abstract-Specific: Vague Dataset Mentions
**Flag:** "experiments on several benchmarks", "evaluated on multiple datasets"
**Fix:** Name the datasets. "We evaluate on COCO, LVIS, and ADE20K."

### 46. Figure Caption Template
**Flag:** "Fig. X shows the architecture of our proposed method."
**Fix:** "Fig. X. [Descriptive title]. [Key observation or design rationale]."
**Real example (good):** "Fig. 1. Pipeline of UniAD. All modules share unified queries from tracking to planning."

---

## Voice Calibration for Academic Writing

When revising, match the user's natural academic voice:

1. **Sentence rhythm:** Mix short declarative sentences with longer explanatory ones
2. **Hedging level:** Match the field's conventions (ML is direct, social sciences are more hedged)
3. **First person:** Use "we" for multi-author papers, avoid "I" in most contexts
4. **Technical density:** Match the target venue's expected level

## Process

1. Scan the text for all 46 patterns
2. Flag each occurrence with the pattern number
3. **Cluster detection** — identify paragraphs with 3+ co-occurring patterns
4. Rewrite flagged sections preserving meaning
5. Verify academic tone is maintained
6. Check that technical precision is not lost
7. Present revised text with change summary

## Cluster Detection Philosophy

**Key insight:** A single pattern instance means nothing; multiple patterns co-occurring in proximity is a confession.

**Detection rules:**
- **Paragraph-level:** 3+ distinct AI patterns within one paragraph = high-risk zone
- **Section-level:** 5+ distinct patterns across a section = section-level rewrite needed
- **Severity aggregation:** Individual low-severity + cluster = medium severity

## False Positives and Contextual Exceptions

**Do NOT flag these patterns in the following contexts:**

| Pattern | Acceptable When |
|---------|----------------|
| "novel" | Once per abstract/introduction, with specific contribution |
| "state-of-the-art" | Immediately followed by benchmark numbers |
| "end-to-end" | Technical term in ML systems papers |
| Passive voice | Methods sections describing procedures |
| "However" | Once per abstract; flag only at 2+ occurrences |
| "comprehensive" | When listing actual scope (e.g., "across 5 benchmarks") |
| Hedging words | When discussing limitations or future work |

## What NOT to Flag (By Section)

**Abstract:** "We propose...", "novel" (once), "However" (once)
**Introduction:** "In this paper, we present...", hedging when discussing prior work
**Methods:** Passive voice, technical jargon, "We use/adopt/employ"
**Results:** "significant" with statistical backing, direct comparisons
**Discussion:** Hedging ("suggests", "may indicate"), limitation acknowledgment
