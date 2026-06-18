---
name: paper-workbench
description: >
  统一论文写作工作台。支持中文本科毕设、英文研究论文优化、IEEE Transactions、Nature/Science/Cell期刊风格写作、
  深度研究、系统综述、多视角审稿、学术搜索等全流程学术工作。
  默认遵循"证据先于散文"，优先建立 claim-evidence-artifact 对齐，再进入正文生成或润色。
  当用户提到论文写作、论文润色、实验设计、图表规划、对抗性审稿、rebuttal、深度研究、文献综述时触发。
version: 6.0.0
---

# Paper Workbench

## 入口职责

本文件负责六件事：

1. **模式判定**：选择 `chinese_thesis` / `english_research` / `ieee_trans` / `nature` / `deep_research` / `systematic_review`
2. **任务判定**：选择 17 种任务类型之一
3. **场刊偏置**：按目标期刊风格执行
4. **加载路由**：按任务只加载必要参考
5. **Agent 编排**：多 agent 协作时的角色分配
6. **Pipeline 管理**：多阶段工作流的状态追踪

---

## 全局硬规则

> [!IMPORTANT]
> 1. **不虚构**：不虚构功能、字段、API、实验数据、结果数字、设备规模、部署范围或引用。
> 2. **证据先于散文**：没有材料、证据或明确假设边界时，不写正式终稿式正文。
> 3. **数字先过 provenance**：任何具体数字进入摘要、引言、实验、图表、结论前，先过 `references/writing/ieee-data-provenance-checklist.md`；过不了就删、改写或标记 `needs evidence`。
> 4. **图表回答审稿问题**：每个 figure/table 必须回答一个明确 reviewer question；不能只是装饰。
> 5. **AI 表达治理**：禁止空泛夸张、模板化贡献、伪精确数字和简单同义替换式"降 AIGC"。
> 6. **学校/场刊覆盖默认**：中文毕设遵循 学校模板 > 导师要求 > 国标 > 内置默认；IEEE/英文论文遵循目标 venue 要求 > 内置默认；Nature 期刊遵循 Nature Portfolio 规范。
> 7. **按需加载**：只加载当前任务所需 section/reference，避免上下文污染。
> 8. **完整性门禁**：关键阶段的完整性检查不可跳过。
> 9. **审稿独立性**：多视角审稿时，各审稿人独立评审，不交叉参考。

---

## Step 1 — 模式判定

根据用户目标先选模式：

| 模式 | 适用场景 | 默认目标 |
|------|----------|----------|
| `chinese_thesis` | 中文毕设、毕业论文、项目说明型论文、需要 Word 导出 | 中文学校规范 + 工作区驱动 |
| `english_research` | 通用英文研究论文、ML/CV/NLP 风格、非特定期刊模板优先 | Reviewer-friendly research writing |
| `ieee_trans` | IEEE Transactions 风格、LaTeX 论文、强调贡献-证据-实验打包 | IEEE Transactions journal style |
| `nature` | Nature/Science/Cell 期刊、高影响力期刊、强调创新性和广泛兴趣 | Nature Portfolio journal style |
| `deep_research` | 深度研究、文献探索、研究问题开发 | APA 7.0 研究报告 |
| `systematic_review` | PRISMA 系统综述、元分析 | PRISMA 2020 规范 |

### 模式判定规则

- 用户提到"毕业论文 / 本科论文 / Word / 学校模板 / 导出文档" → `chinese_thesis`
- 用户提到"rewrite / polish / introduction / abstract / claim-evidence / paper review"，但未强调 IEEE 模板 → `english_research`
- 用户提到"IEEE / Transactions / journal / rebuttal / LaTeX / contribution list / experiments for submission" → `ieee_trans`
- 用户提到"Nature / Science / Cell / high-impact / broad interest / novel discovery" → `nature`
- 用户提到"research / deep research / literature review / systematic review / meta-analysis / fact-check" → `deep_research`
- 用户提到"PRISMA / systematic review / meta-analysis / risk of bias" → `systematic_review`

### Nature 模式子路由

当模式为 `nature` 时，进一步识别目标期刊：

| 期刊家族 | 风格偏置 |
|----------|----------|
| Nature 主刊 | 创新性 + 广泛兴趣 + 简洁 |
| Nature 子刊 | 专业深度 + 方法严谨 |
| Science | 突破性发现 + 证据链 |
| Cell | 机制深入 + 多角度验证 |

---

## Step 2 — 任务判定

进入模式后，再判定任务类型：

### 核心任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `full_draft` | 写整篇/大段正式草稿 | section spine + contribution map + draft plan |
| `section_rewrite` | 改某一节/某几段 | revised text + claim-evidence map + revision notes |
| `outline_only` | 生成论文结构/章节大纲 | article type + section spine + section goals |
| `claim_evidence_check` | 查声明是否站得住 | claim list + evidence status + gaps |
| `experiment_design` | 设计实验/补实验 | claim→experiment→metric→artifact chain |
| `figure_table_planning` | 规划图表/结果编排 | reviewer question + artifact plan + required inputs |
| `paper_review` | 模拟审稿/查拒稿风险 | 多视角审稿报告 + 量化评分 |
| `rebuttal` | 写审稿回复 | 结构化 point-by-point 回复 |

### 研究任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `deep_research` | 深度研究某个主题 | APA 7.0 研究报告 (3000-8000字) |
| `quick_research` | 快速研究概览 | 研究简报 (500-1500字) |
| `socratic_guide` | 苏格拉底式引导研究 | 引导式对话 + 研究问题开发 |
| `fact_check` | 事实核查 | 验证报告 (300-800字) |
| `lit_review` | 文献综述 | 带注释的文献综述 (1500-4000字) |

### Nature 专项任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `nature_polish` | Nature 风格润色 | 润色后文本 + 修改说明 |
| `data_availability` | 数据可用性声明 | FAIR 合规的数据声明 |
| `paper2ppt` | 论文转 PPT | 中文 .pptx 演示文稿 |
| `citation_convert` | 引用格式转换 | 目标格式引用列表 |
| `academic_search` | 学术搜索 | 去重后的文献列表 |

如果请求跨多个任务，先按用户当前最急需的交付目标执行，不默认输出全家桶。

---

## Step 3 — Venue Router

### 3.1 IEEE Trans 路由

在 `ieee_trans` 模式中，先识别 article type，再识别 venue bias。

#### Article Type Routing

优先依据 `references/writing/chapter-patterns-ieee.md` 判断：

- `survey_or_roadmap`
- `method_or_system`
- `benchmark_or_dataset`
- `empirical_or_software_engineering`
- `critical_review`

#### Venue Bias Routing

- 若用户明确指定期刊，优先按该期刊风格
- 若用户偏好 **IEEE T-ITS**，优先加载交通/ITS 相关写作参考
- 若未指定 venue，则使用通用 IEEE Transactions 参考

### 3.2 Nature 路由

在 `nature` 模式中：

#### 加载参考

- `references/venues/nature-portfolio.md` - Nature 期刊家族规范
- `references/writing/nature-writing-style.md` - Nature 写作风格
- `references/writing/nature-figure-standards.md` - Nature 图表标准
- `references/writing/nature-polishing-rules.md` - Nature 润色规则
- `references/writing/nature-citation-format.md` - Nature 引用格式

#### Nature 风格偏置

1. 创新性优先：必须有明确的 novelty claim
2. 广泛兴趣：研究问题需面向广泛读者
3. 简洁表达：每句 ≤30 词，避免过度技术化
4. 证据链完整：每个声明需有实验支持
5. 英式英语：signalling, colour, analyse, programme

---

## Step 4 — Minimal Execution Spine

### `english_research` 最小执行主线

1. Clarify the paper story
2. Extract claim list
3. Check claim-evidence alignment
4. Rewrite section or draft outline
5. Run paragraph clarity check
6. Run AI-pattern audit
7. Run adversarial review before finalizing

### `ieee_trans` 最小执行主线

1. Identify article type and venue bias
2. Lock contribution-evidence map
3. Lock Figure 1 / Table I roles
4. Choose section spine
5. Draft or revise section-by-section
6. Check provenance for all concrete numbers
7. Run adversarial review and rebuttal-readiness check

### `nature` 最小执行主线

1. Identify novelty claim and target journal
2. Lock story arc (context → gap → discovery → implication)
3. Plan figures (Figure 1 = main finding, Figure 2-4 = mechanism/evidence)
4. Draft with Nature style constraints
5. Run Nature-specific quality checks
6. Run multi-perspective review
7. Prepare data availability and methods

### `chinese_thesis` 最小执行主线

1. Intake materials
2. Build evidence chain
3. Confirm standards priority
4. Generate outline
5. Search/build references pool
6. Draft chapter-by-chapter
7. Review / merge / export

### `deep_research` 最小执行主线

1. Refine research question (FINER criteria)
2. Design methodology blueprint
3. Systematic literature search
4. Source verification and grading
5. Thematic synthesis
6. Draft APA 7.0 report
7. Editorial review and ethics check

### `systematic_review` 最小执行主线

1. Define protocol (PICOS framework)
2. PRISMA-compliant search strategy
3. Screen and select studies
4. Risk of bias assessment (RoB 2 / ROBINS-I)
5. Data extraction and synthesis
6. Meta-analysis (if applicable)
7. GRADE evidence certainty

---

## Step 5 — Task-Specific Output Contracts

### A. `section_rewrite`

输出：
1. section goal
2. mini-outline
3. revised text
4. claim-evidence map
5. revision risks or missing evidence

### B. `outline_only`

输出：
1. article type
2. section spine
3. section goals
4. contribution anchors
5. evidence needed by section

### C. `claim_evidence_check`

输出：
1. claim list
2. evidence source per claim
3. status: `supported / weakly supported / needs evidence / remove`
4. rewrite recommendation

### D. `experiment_design`

输出：
1. target claims
2. experiment questions
3. protocols
4. metrics
5. figures/tables to produce
6. missing evidence or data provenance risks

### E. `figure_table_planning`

输出：
1. reviewer question
2. artifact type
3. planned caption role
4. required inputs
5. provenance status
6. layout/order recommendation

### F. `paper_review` (增强版)

输出：
1. 多视角独立审稿报告（5个审稿人）
2. 量化评分（0-100分）
3. 拒稿风险维度
4. 不支持的声明
5. 缺失的实验
6. 修订优先级
7. Devil's Advocate 挑战

**执行参考**: `references/review/ieee-reviewer-simulation.md`
**审稿人角色**: 方法论/实验/写作/领域/魔鬼代言人
**评分维度**: 创新性/技术质量/实验完整性/写作/重要性/可复现性

### G. `rebuttal` (增强版)

输出：
1. 审稿人关注点分类
2. 行动映射 (ACCEPT_TEXT / ACCEPT_ANALYSIS / SOFTEN_CLAIM / AUTHOR_INPUT_NEEDED)
3. 回复立场
4. 引用证据
5. 修订后措辞
6. 未解决的差距

### H. `full_draft`

输出：
1. article type
2. section spine
3. contribution list
4. evidence inventory
5. writing order
6. draft text only after evidence boundary is explicit

### I. `deep_research`

输出：
1. 研究问题（FINER 评分）
2. 方法论蓝图
3. 带注释的文献列表（APA 7.0）
4. 综合分析报告
5. 证据等级评估
6. 研究空白识别

### J. `nature_polish`

输出：
1. 润色后文本
2. 修改清单
3. 风格合规检查
4. 对冲校准报告
5. 时态检查结果

### K. `data_availability`

输出：
1. 数据可用性声明（英文）
2. FAIR 合规检查
3. 仓库推荐
4. 访问路由
5. 中文行动说明

### L. `paper2ppt`

输出：
1. .pptx 文件
2. 幻灯片大纲
3. 演讲者备注
4. QA 检查报告

### M. `academic_search`

输出：
1. 去重后的文献列表
2. 引用格式（多格式）
3. 来源验证状态
4. 搜索策略文档

**执行参考**: `references/research/academic-search.md`
**支持API**: Semantic Scholar, DBLP, arXiv, CrossRef
**输出格式**: Markdown + BibTeX

---

## Step 6 — Reference Loading Policy

### `english_research` 常用加载

- section writing: `references/writing/traffic-writing-execution-master-index.md`
- structure / flow: `references/writing/traffic-writing-execution-master-index.md`
- review / de-AI: `references/review/paper-review.md`, `references/review/humanizer-patterns.md`

### `ieee_trans` 常用加载

- article type / section spine: `references/workflow/ieee-writing-spine.md`, `references/writing/chapter-patterns-ieee.md`
- language / contribution / abstract patterns: `references/writing/traffic-writing-execution-master-index.md`
- experiment design: `references/writing/traffic-experiment-planning-master-index.md`
- visual planning: `references/writing/ieee-visual-playbook.md`
- provenance / numbers: `references/writing/ieee-data-provenance-checklist.md`
- paper review: `references/review/traffic-review-response-master-index.md`
- academic search: `references/research/academic-search.md`
- reviewer simulation: `references/review/ieee-reviewer-simulation.md`
- innovation inspiration: `references/writing/ieee-innovation-inspiration.md`
- real experimental data: `references/writing/ieee-real-experimental-data.md`
- expression patterns: `references/writing/ieee-expression-patterns.md`
- polishing rules: `references/writing/ieee-polishing.md`

### `nature` 常用加载

- writing style: `references/writing/nature-writing-style.md`
- figure standards: `references/writing/nature-figure-standards.md`
- polishing rules: `references/writing/nature-polishing-rules.md`
- citation format: `references/writing/nature-citation-format.md`
- data availability: `references/writing/nature-data-availability.md`
- response template: `references/review/nature-response-template.md`
- venue spec: `references/venues/nature-portfolio.md`

### `chinese_thesis` 常用加载

- `references/workflow/intake.md`
- `references/workflow/evidence-workflow.md`
- `references/workflow/standards-resolution.md`
- `references/workflow/state-management.md`
- `references/writing/writer-guidelines.md`
- `references/writing/chapter-patterns-cn.md`
- `references/writing/aigc-governance.md`
- `references/delivery/docx-delivery.md`

### `deep_research` 常用加载

- research workflow: `references/workflow/deep-research-workflow.md`
- socratic guidance: `references/workflow/socratic-guidance.md`
- source verification: `references/research/source-verification.md`
- bibliography: `references/research/bibliography-management.md`

### `systematic_review` 常用加载

- PRISMA protocol: `references/workflow/systematic-review-protocol.md`
- risk of bias: `references/research/risk-of-bias-assessment.md`
- meta-analysis: `references/research/meta-analysis-guide.md`

---

## Step 7 — Special Enforcement Rules

### 7.1 Contribution Rule

在 `ieee_trans` 和 `nature` 模式下，每条 contribution 必须绑定：

- 一个强动词
- 一个具体工件（模型、系统、数据集、分类法、定理、协议、实验包）
- 一个证据位置
- 一个 section anchor

若做不到，则该 contribution 需要弱化、拆分或删除。

### 7.2 Figure/Table Rule

每个 figure/table 必须先回答：

- 它回答哪个 reviewer question？
- 如果删掉它，论文会损失什么可验证信息？
- 它是否引入了正文里不存在的模块或数字？

若答不出来，不应生成。

### 7.3 Anti-AI Rule

检测到以下情况时，优先重写而不是微调措辞：

- empty evidence claims
- generic superiority claims
- forced motivation openings
- template contribution bullets
- vague quantifiers
- scope inflation

### 7.4 Nature Style Rule

在 `nature` 模式下额外检查：

- 每句 ≤30 词
- 对冲校准：声明强度匹配证据水平
- 时态正确：Results 过去时，Discussion 对冲语言
- 英式英语：signalling, colour, analyse, programme
- 无绝对声明：避免 "first", "novel", "groundbreaking"

### 7.5 Multi-Reviewer Independence Rule

`paper_review` 任务使用多视角审稿时：

- 5 个审稿人独立评审，不交叉参考
- Devil's Advocate 发现 CRITICAL → 决策不能是 Accept
- 每个审稿人必须引用具体段落、数据或页码
- 审稿人只读不改，不得修改原稿

### 7.6 Integrity Gate Rule

Pipeline 中的完整性门禁不可跳过：

- Stage 2.5：预审完整性检查
- Stage 4.5：修订后完整性检查
- 7 模式 AI 研究失败清单
- 声称的修改必须有证据支持

---

## Step 8 — Agent Orchestration

### Deep Research Agents (13个)

| Agent | 职责 |
|-------|------|
| research_question_agent | 研究问题开发（FINER 评分） |
| research_architect_agent | 方法论蓝图设计 |
| bibliography_agent | 系统文献搜索 |
| source_verification_agent | 来源验证和等级评估 |
| synthesis_agent | 跨源综合分析 |
| report_compiler_agent | APA 7.0 报告编写 |
| editor_in_chief_agent | Q1 期刊级编辑审稿 |
| devils_advocate_agent | 假设检测和偏见检查 |
| ethics_review_agent | AI 披露和伦理审查 |
| socratic_mentor_agent | 苏格拉底式引导 |
| risk_of_bias_agent | 偏倚风险评估 |
| meta_analysis_agent | 元分析和效应量 |
| monitoring_agent | 后续文献追踪 |

### Nature Writing Agents

| Agent | 职责 |
|-------|------|
| intake_agent | 配置访谈 |
| literature_strategist_agent | 搜索策略和文献筛选 |
| structure_architect_agent | 论文结构选择 |
| argument_builder_agent | 声明-证据链构建 |
| draft_writer_agent | 分章节撰写 |
| citation_compliance_agent | 引用验证 |
| abstract_bilingual_agent | 双语摘要 |
| peer_reviewer_agent | 模拟双盲审稿 |
| visualization_agent | 出版级图表 |
| revision_coach_agent | 修订路线图 |
| formatter_agent | 最终格式化 |

### Review Agents (7个)

| Agent | 职责 |
|-------|------|
| field_analyst_agent | 领域分析和审稿人角色生成 |
| eic_agent | 主编决策 |
| methodology_reviewer_agent | 方法论审稿 |
| domain_reviewer_agent | 领域专家审稿 |
| perspective_reviewer_agent | 跨学科视角审稿 |
| devils_advocate_agent | 魔鬼代言人 |
| editorial_synthesizer_agent | 综合编辑决策 |

### Pipeline Agents (5个)

| Agent | 职责 |
|-------|------|
| pipeline_orchestrator_agent | 流程编排 |
| state_tracker_agent | 状态追踪 |
| integrity_verification_agent | 完整性验证 |
| collaboration_depth_observer_agent | 协作深度观察 |
| claim_audit_agent | 声明审计 |

---

## Step 9 — Quality Guarantees

### 9.1 Sprint Contract

审稿和写作任务使用 Sprint Contract：

- Phase 4/6 分为 paper-blind 和 paper-visible 两阶段
- 预承诺评分计划，防止事后合理化
- 物理分离调用，防止质量漂移

### 9.2 Material Passport

跨阶段物料追踪：

- 版本标签单调递增
- 每个交接点必须携带 passport
- 过期检测：上游修改或完整性检查超过 24 小时

### 9.3 Revision Cap

修订轮次上限：

- 最多 2 轮修订（Stage 4 + Stage 4'）
- 提前停止条件：评分 delta < 3 分且无 P0 问题
- 未解决项转为 "Acknowledged Limitations"

### 9.4 Anti-Sycophancy

反谄媚协议：

- 审稿人不能无条件接受所有 reviewer feedback
- 修订不能引入 scope creep
- 必须保留科学或范围-based 的合理分歧

---

## Step 10 — Chinese Thesis Workflow Note

`chinese_thesis` 模式保留现有 Step 0-9 工作流，不在本文件重复展开细节。

执行时按需进入：

- `workflows/step_0_init.md`
- `workflows/step_3_outline.md`
- `workflows/step_4_writing.md`
- `workflows/step_6_review_polish.md`
- `workflows/step_7_merge_detect.md`
- `workflows/step_8_image.md`
- `workflows/step_9_export.md`

并由 workflow/state/evidence 文件负责治理，不把全部流程塞回主入口。
