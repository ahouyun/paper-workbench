# IEEE Writing Spine

## Goal

Provide a minimal execution spine for IEEE Transactions-style paper work so the main skill can route requests without loading every reference at once.

Use this file only as the execution backbone. Load the detailed writing, experiment, visual, provenance, review, and venue-specific references on demand.

---

## Core Principle

**Lock evidence before prose.**

For IEEE-style work, the paper should be built in this order:

1. article type,
2. venue bias,
3. contribution-evidence map,
4. key figures/tables,
5. section spine,
6. section drafting,
7. adversarial review.

If the work starts with sentence polishing before these elements are stable, the draft usually becomes fluent but structurally weak.

---

## Step 1. Identify article type

Use `references/writing/chapter-patterns-ieee.md` to classify the paper as one of:

- `survey_or_roadmap`
- `method_or_system`
- `benchmark_or_dataset`
- `empirical_or_software_engineering`
- `critical_review`

### Hard rule

Do not force every paper into:

`System Model -> Method -> Theory -> Experiments`

If the true contribution is empirical, survey-driven, benchmark-oriented, or critique-oriented, choose the corresponding section spine instead.

---

## Step 2. Identify venue bias

Ask or infer:

1. target journal or conference,
2. whether the user needs generic IEEE style or a venue-specific style,
3. whether the paper is more theory-heavy, system-heavy, or empirical.

### IEEE T-ITS bias

If the target is **IEEE Transactions on Intelligent Transportation Systems**, prioritize:

- real traffic scenarios or auditable simulation scenarios,
- deployment-aware constraints,
- latency/robustness/safety tradeoffs,
- practical evaluation scope,
- engineering-style claims over hype.

Load venue-specific traffic references when needed.

---

## Step 3. Lock contribution-evidence map

Before drafting full prose, create a compact map:

| Contribution | Artifact | Evidence | Section |
|---|---|---|---|
| What is new? | model / system / dataset / theorem / protocol / taxonomy | experiment / proof / benchmark / synthesis artifact | where it is defended |

### Hard rules

Each contribution must have:

1. one strong verb,
2. one concrete artifact,
3. one evidence location,
4. one section anchor.

If a contribution lacks evidence, either:

- weaken it,
- split it,
- move it to future work,
- or delete it.

---

## Step 4. Lock Figure 1 and Table I roles

Before large-scale drafting, identify the first major visual artifacts.

### Figure 1 role

Choose one:

- pipeline figure,
- teaser figure,
- taxonomy/roadmap,
- system model,
- study design.

### Table I role

Choose one:

- main benchmark table,
- synthesis table,
- dataset overview table,
- study corpus / subject-system table.

### Hard rule

Every figure or table must answer a reviewer question.
If an artifact cannot be justified as evidence, it should not be generated.

Use:

- `references/writing/ieee-visual-playbook.md`
- venue-specific figure references when needed

---

## Step 5. Choose section spine

After article type and key artifacts are fixed, choose the paper structure.

### Typical method/system spine

1. Introduction
2. Related Work
3. Problem Formulation / System Model
4. Proposed Method
5. Theoretical Analysis (if needed)
6. Experimental Results
7. Discussion / Limitations
8. Conclusion

### Typical empirical/software-engineering spine

1. Introduction
2. Background
3. Research Questions
4. Approach / Study Design
5. Results by RQ
6. Discussion
7. Threats to Validity
8. Conclusion

### Typical survey spine

1. Introduction
2. Preliminaries / Background
3. Taxonomy
4. Family-by-family synthesis
5. Comparison and open problems
6. Conclusion

---

## Step 6. Draft or revise section-by-section

Draft by task type, not by habit.

### If the task is `outline_only`

Output:

1. article type,
2. section spine,
3. section goals,
4. contribution anchors,
5. evidence needed per section.

### If the task is `section_rewrite`

Output:

1. section goal,
2. mini-outline,
3. revised text,
4. claim-evidence map,
5. missing evidence or risk notes.

### If the task is `full_draft`

Only draft full sections after the contribution-evidence map and section spine are explicit.

---

## Step 7. Check provenance before concrete numbers land

Before a number appears in:

- title or subtitle,
- abstract,
- introduction,
- experiment section,
- tables,
- figures,
- discussion,
- conclusion,

run a provenance pass using:

- `references/writing/ieee-data-provenance-checklist.md`

### Allowed outcomes

- `verified`
- `secondary_reported`
- `needs evidence`
- rewritten to qualitative wording without false precision

### Hard rule

Never let unsupported counts, scales, runtime, speedups, deployment numbers, or subject counts enter final prose.

---

## Step 8. Run adversarial review

Before finalizing, run a skeptical reviewer pass using:

- `references/review/paper-review.md`
- `references/review/reviewer-response.md` when rebuttal readiness matters

Check:

1. unsupported claims,
2. missing baselines,
3. weak ablations,
4. visual artifacts that do not prove anything,
5. article-type mismatch,
6. venue mismatch,
7. overclaiming in abstract and introduction.

---

## Fast routing table

| If the user asks for... | Load first |
|---|---|
| IEEE section rewrite | `references/writing/ieee-expression-patterns.md` + target section guide |
| IEEE experiment design | `references/writing/ieee-experiment-playbook.md` |
| IEEE figure/table planning | `references/writing/ieee-visual-playbook.md` |
| IEEE number verification | `references/writing/ieee-data-provenance-checklist.md` |
| IEEE review / reject risk | `references/review/paper-review.md` |
| IEEE rebuttal | `references/review/reviewer-response.md` |
| IEEE T-ITS writing | venue profile + traffic references |
