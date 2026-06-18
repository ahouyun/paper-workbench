# IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS) Venue Profile

## Goal

Capture the structural, evidential, and stylistic bias that paper-writing should follow when the target venue is **IEEE Transactions on Intelligent Transportation Systems (T-ITS)**.

Use this profile to bias drafting, rewriting, experiment planning, figure/table planning, reviewer-facing framing, and rebuttal preparation.

This file is not a generic IEEE guide. It exists to make the writing and evidence package feel native to T-ITS rather than merely IEEE-shaped.

---

## 1. Venue Identity

T-ITS papers usually sit closer to **transportation systems engineering** than to purely abstract ML benchmarking.

Even when the technical core is a neural architecture, reviewers often expect the paper to answer system-facing questions:

1. What traffic problem is being solved?
2. Under what sensing / network / operational assumptions?
3. Why does the proposed mechanism fit the transportation phenomenon?
4. What is the practical cost in latency, robustness, deployment complexity, or data dependence?
5. Under what traffic conditions does the method weaken?

### Writing implication

Do not present the paper as a generic predictive model with traffic as a decorative application.
The transportation setting should shape:

- the problem formulation,
- the evaluation scope,
- the baselines,
- the discussion of operational value,
- and the limitations.

---

## 2. Article Types Common in T-ITS

Common patterns include:

1. **method_or_system**
   - new prediction / control / perception / coordination method for ITS tasks
2. **empirical_or_software_engineering**
   - measurement study, benchmark study, deployment study, comparative evaluation
3. **benchmark_or_dataset**
   - traffic dataset construction, multimodal benchmark, scenario corpus, incident dataset
4. **survey_or_roadmap**
   - less common than method papers, but still possible for mature subareas

### Hard rule

If the paper is fundamentally an empirical transportation study, do not disguise it as a pure ML-method paper.
Use research-question or study-design structure where appropriate.

---

## 3. Preferred Introduction Logic for T-ITS

A strong T-ITS introduction usually follows this progression:

1. **Operational importance**
   - traffic forecasting, control, safety, routing, perception, incident response, energy, or coordination
2. **Domain-specific technical difficulty**
   - nonstationarity, sensor sparsity, missing data, propagation delay, topology uncertainty, multimodal coupling, rare events, safety constraints
3. **Existing method families**
   - graph-based, sequence-based, transformer-based, probabilistic, control-oriented, or foundation-model-style approaches
4. **Concrete domain gap**
   - not only “accuracy is limited,” but *why current assumptions fail in transportation settings*
5. **Method response or study goal**
6. **Contribution list with evidence anchors**

### Strong opening moves

Prefer:

- physical or operational phenomena,
- system constraints,
- decision impact,
- measurable deployment stakes.

Avoid:

- broad AI hype,
- generic “with the rapid development of…” openings,
- venue-independent intro templates.

---

## 4. Contribution Style That Fits T-ITS

T-ITS contributions should feel **auditable and engineering-relevant**.

Each contribution should bind together:

- a concrete artifact,
- a transportation motivation,
- an evidence mechanism.

### Good contribution patterns

- method + transportation mechanism + measured gain
- system design + deployment constraint + evaluation evidence
- benchmark/dataset + coverage dimension + baseline study
- study finding + operational implication + scoped evidence

### Weak contribution patterns

- “we propose a novel framework” with no operational anchor
- “extensive experiments prove effectiveness” with no scope
- “significant improvement” without baselines, metrics, and scenario boundary

---

## 5. Evidence Expectations in T-ITS

T-ITS reviewers often care about more than leaderboard performance.

### Evidence dimensions commonly expected

1. **Main effectiveness**
   - strong baselines, standard metrics, realistic horizons / tasks
2. **Scenario scope**
   - multiple datasets, multiple horizons, multiple networks, or multiple traffic conditions
3. **Operational cost**
   - latency, memory, parameter count, runtime, or sensing burden when relevant
4. **Robustness**
   - missing data, sparse sensors, noisy inputs, nonrecurrent events, topology perturbation, domain shift
5. **Ablation / mechanism verification**
   - whether the claimed transportation mechanism actually matters
6. **Failure boundary**
   - where the method weakens and why

### Hard rule

A T-ITS paper should not read like a benchmark-only ML paper if it claims transportation value.
If deployment relevance is claimed, at least one artifact should make that relevance auditable.

---

## 6. Typical Figure Families for T-ITS

### Figure 1 roles that work well

Choose one:

1. **framework / pipeline figure**
2. **traffic-phenomenon-to-method teaser**
3. **system architecture / sensing layout**
4. **study design overview**

### Figure families commonly useful

- road network / sensor layout diagrams
- model framework diagrams
- horizon-wise prediction comparison plots
- robustness or missing-rate plots
- attention / correlation / adjacency heatmaps
- qualitative incident or congestion case studies
- efficiency-vs-performance scatter plots

### Figure anti-patterns

- flashy architecture diagrams with no transportation meaning
- figures that introduce modules absent from the text
- decorative congestion maps that do not support a claim
- visualizations with unlabeled scenario scope

Use `references/writing/traffic-figure-patterns.md` and `references/writing/ieee-visual-playbook.md` together.

---

## 7. Typical Table Families for T-ITS

### High-value table roles

1. **Main benchmark table**
   - by dataset and by horizon
2. **Ablation table**
   - each module tied to one claimed transportation challenge
3. **Robustness table**
   - missing rate, sparse coverage, domain shift, event cases
4. **Efficiency table**
   - runtime, parameters, memory, throughput
5. **Dataset / scenario summary table**
   - sensors, granularity, temporal range, split protocol

### T-ITS-specific preference

When claims involve realistic deployment or multi-condition generalization, tables should preserve the evaluation scope explicitly.
Do not compress away the scenario information that would let reviewers judge realism.

---

## 8. Language Bias for T-ITS

### Prefer

- operationally grounded wording
- physically interpretable motivation when applicable
- conditional claims with explicit scope
- honest explanation of where gains appear
- reviewer-friendly causal analysis

### Avoid

- generic smart-city hype
- venue-neutral AI boilerplate
- overclaiming social impact without evidence
- “state-of-the-art” as a substitute for real comparison
- abstract praise words when metric deltas exist

### Strong sentence tendencies

- tie model design to transportation phenomena,
- explain which conditions amplify the gain,
- distinguish short-horizon vs long-horizon behavior,
- distinguish dense-sensor vs sparse-sensor settings,
- discuss failure under missingness, incident, or nonstationarity.

Use:

- `references/writing/traffic-writing-patterns.md`
- `references/writing/traffic-logic-rigor.md`
- `references/writing/traffic-anti-ai-writing.md`

---

## 9. Experiment Design Bias for T-ITS

When planning experiments, prioritize questions like:

1. Does the method outperform strong baselines on standard traffic benchmarks?
2. At what horizons or operating conditions do gains appear?
3. Does the claimed transportation mechanism survive ablation?
4. What is the inference/training cost?
5. How robust is the method to missing sensors, sparse topology, or unstable traffic patterns?
6. Does the method fail under incidents, regime shifts, or noisy sensing?

### Strong evaluation packages

- standard datasets + realistic train/val/test protocol
- horizon-wise analysis
- multi-dataset coverage
- ablations aligned with introduction claims
- robustness study
- case study on a traffic event, sparse region, or hard scenario

### Common weak packages

- one aggregate average with no horizon breakdown
- no explanation of why the method wins
n- no robustness or missing-data check for a paper that claims real-world utility
- no deployment cost discussion for a method framed as practical ITS support

---

## 10. Data and Provenance Rules

Traffic papers often contain numbers that sound plausible but are easy to fake accidentally.

Numbers needing verification include:

- sensor count,
- road segment count,
- sampling interval,
- date range,
- missing rate,
- latency,
- speedup,
- training cost,
- deployment scale,
- event count,
- incident frequency,
- travel-time reduction,
- energy or safety gains.

### Hard rule

If a number is not grounded in:

- the user’s experiment records,
- verified logs,
- cited benchmark facts,
- or explicitly attributed prior literature,

it should not appear as a concrete value.

Use:

- `references/writing/ieee-data-provenance-checklist.md`
- `references/writing/ieee-real-experimental-data.md`

---

## 11. Common Reject Risks in T-ITS

1. **Generic ML framing with weak transportation grounding**
2. **Method motivation not tied to real traffic phenomena**
3. **Evaluation ignores realistic data issues**
4. **No robustness under missingness / sparsity / instability**
5. **Ablation does not verify the claimed mechanism**
6. **Operational significance is asserted but not evidenced**
7. **Figures and tables look polished but do not answer reviewer questions**
8. **Abstract and introduction overclaim beyond the measured scope**
9. **No honest failure boundary**
10. **Benchmark gains are small and uncontextualized**

---

## 12. Rebuttal Bias for T-ITS

When answering reviewers, prioritize:

1. evaluation realism,
2. data protocol clarity,
3. robustness and deployment cost,
4. why the method helps specifically in transportation settings,
5. whether the claimed mechanism is truly verified.

A strong rebuttal should cite:

- exact section anchors,
- exact tables/figures,
- exact protocol clarifications,
- exact limitation wording when a concern is valid.

Avoid defensive hype.
Prefer scoped clarification and verifiable evidence.

---

## 13. Fast Routing for T-ITS Tasks

| User asks for... | Load first |
|---|---|
| T-ITS outline | this file + `references/workflow/ieee-writing-spine.md` + `references/writing/chapter-patterns-ieee.md` |
| T-ITS introduction rewrite | this file + `references/writing/traffic-writing-patterns.md` + `references/sections/introduction.md` |
| T-ITS experiment design | this file + `references/writing/ieee-experiment-playbook.md` + `references/writing/traffic-logic-rigor.md` |
| T-ITS figure/table planning | this file + `references/writing/traffic-figure-patterns.md` + `references/writing/ieee-visual-playbook.md` |
| T-ITS anti-AI polishing | this file + `references/writing/traffic-anti-ai-writing.md` |
| T-ITS number checking | this file + `references/writing/ieee-data-provenance-checklist.md` + `references/writing/ieee-real-experimental-data.md` |
| T-ITS paper review | this file + `references/review/paper-review.md` |
