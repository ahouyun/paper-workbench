---
name: paper-workbench
description: >
  工具无关的统一论文写作工作台。支持 Claude Code, Codex CLI, Cursor, Windsurf 等多种 AI 编程工具。
  支持中文本科毕设、英文研究论文优化、IEEE Transactions (T-ITS/TNNLS/TVT/TIV)、
  顶会 (NeurIPS/ICML/ICLR/CVPR/KDD/VLDB/AAAI/IJCAI) 论文写作、深度研究、系统综述、多视角审稿、
  学术搜索、审稿回复（triage→point-by-point→QA）、IMRAD/CONSORT/PRISMA/STROBE/ARRIVE报告规范检查、
  中英文对照阅读、LaTeX排版诊断等全流程学术工作。
  整合了 academic-research-skills (v3.13.0) 的深度研究、多视角审稿、完整流水线编排、风格校准等能力。
  整合了 scipilot-figure-skill (v2.1.0) 的科研数据可视化顾问能力——先思考后绘制，主动拦截画图错误，视觉自检闭环。
  默认遵循"证据先于散文"，优先建立 claim-evidence-artifact 对齐，再进入正文生成或润色。
  当用户提到论文写作、论文润色、实验设计、图表规划、对抗性审稿、rebuttal、深度研究、文献综述、完整流程、端到端、
  科研画图、数据可视化、不知道用什么图、怎么展示数据、用什么图好、期刊投稿图、figure、出版级图表时触发。
version: 7.9.0
---

# Paper Workbench

## Quick Start

**How to invoke:** Mention "paper writing", "论文润色", "experiment design", "figure planning", "peer review", "rebuttal", "literature review", or related keywords.

**Minimal input:** Provide your paper draft or describe your research. Specify target venue if known.

**Expected output:** Structured guidance with section-specific templates, anti-AI patterns, and reviewer-checklist validation.

---

## 入口职责

本文件负责六件事：

1. **模式判定**：选择 `chinese_thesis` / `english_research` / `ieee_trans` / `conference` / `deep_research` / `systematic_review`
2. **任务判定**：选择 17 种任务类型之一
3. **场刊偏置**：按目标期刊风格执行
4. **加载路由**：按任务只加载必要参考
5. **Agent 编排**：多 agent 协作时的角色分配
6. **Pipeline 管理**：多阶段工作流的状态追踪

---

## 全局硬规则

> [!IMPORTANT]
> 1. **不虚构 (No Fabrication)**：不虚构功能、字段、API、实验数据、结果数字、设备规模、部署范围或引用。
> 2. **证据先于散文 (Evidence Before Prose)**：没有材料、证据或明确假设边界时，不写正式终稿式正文。
> 3. **数字先过 provenance (Number Provenance)**：任何具体数字进入摘要、引言、实验、图表、结论前，先过 `references/writing/ieee-data-provenance-checklist.md`；过不了就删、改写或标记 `needs evidence`。
> 4. **图表回答审稿问题 (Figures Answer Reviewers)**：每个 figure/table 必须回答一个明确 reviewer question；不能只是装饰。
> 5. **AI 表达治理 (AI Expression Governance)**：禁止空泛夸张、模板化贡献、伪精确数字和简单同义替换式"降 AIGC"。
> 6. **学校/场刊覆盖默认 (Venue Overrides)**：中文毕设遵循 学校模板 > 导师要求 > 国标 > 内置默认；IEEE/英文论文遵循目标 venue 要求 > 内置默认；顶会遵循会议规范。
> 7. **按需加载 (On-Demand Loading)**：只加载当前任务所需 section/reference，避免上下文污染。
> 8. **完整性门禁 (Completeness Gates)**：关键阶段的完整性检查不可跳过。
> 9. **审稿独立性 (Review Independence)**：多视角审稿时，各审稿人独立评审，不交叉参考。

---

## Step 1 — 模式判定

根据用户目标先选模式：

| 模式 | 适用场景 | 默认目标 |
|------|----------|----------|
| `chinese_thesis` | 中文毕设、毕业论文、项目说明型论文、需要 Word 导出 | 中文学校规范 + 工作区驱动 |
| `english_research` | 通用英文研究论文、ML/CV/NLP 风格、非特定期刊模板优先 | Reviewer-friendly research writing |
| `ieee_trans` | IEEE Transactions 风格 (T-ITS/TNNLS/TVT/TIV)、LaTeX 论文、强调贡献-证据-实验打包 | IEEE Transactions journal style |
| `conference` | 顶会论文 (NeurIPS/ICML/ICLR/CVPR/KDD/VLDB/AAAI/IJCAI)、强调创新性和实验完整性 | 顶会论文风格 |
| `deep_research` | 深度研究、文献探索、研究问题开发 | APA 7.0 研究报告 |
| `systematic_review` | PRISMA 系统综述、元分析 | PRISMA 2020 规范 |
| `pipeline` | 完整学术流水线：研究→写作→审稿→修改→定稿 | 端到端论文产出 |

### 论文类型与叙事弧

在写作前先识别论文类型，不同类型对应不同叙事弧（narrative arc）：

| 论文类型 | 叙事弧 | 核心结构 |
|---------|--------|---------|
| **discovery** 发现/机制类 | 问题→证据 | 背景→方法→结果→意义→展望 |
| **methods** 方法/算法类 | 问题→解决方案 | 问题→现有缺陷→创新→验证→应用 |
| **resource** 数据集/平台类 | 工作流→验证 | 动机→构建→规模→基准→用例 |
| **clinical** 临床/人群类 | 设计→推断 | 问题→设计→结果→临床 implications |
| **review** 综述/观点类 | 证据地图 | 现状→共识→争议→未来方向 |

> 在 `full_draft` / `outline_only` / `paper2ppt` 任务前，必须先确认论文类型并锁定叙事弧。

### 模式判定规则

- 用户提到"毕业论文 / 本科论文 / Word / 学校模板 / 导出文档" → `chinese_thesis`
- 用户提到"rewrite / polish / introduction / abstract / claim-evidence / paper review"，但未强调 IEEE 模板 → `english_research`
- 用户提到"IEEE / Transactions / T-ITS / TNNLS / TVT / TIV / journal / rebuttal / LaTeX / contribution list / experiments for submission" → `ieee_trans`
- 用户提到"NeurIPS / ICML / ICLR / CVPR / KDD / VLDB / AAAI / IJCAI / conference / poster / spotlight / oral" → `conference`
- 用户提到"research / deep research / literature review / systematic review / meta-analysis / fact-check" → `deep_research`
- 用户提到"PRISMA / systematic review / meta-analysis / risk of bias" → `systematic_review`
- 用户提到"完整流程 / 端到端 / 研究到发表 / academic pipeline" → `pipeline`
- 用户提到"审稿回复 / rebuttal / reviewer response / point-by-point / 返修" → `rebuttal` 任务
- 用户提到"IMRAD / CONSORT / PRISMA合规 / STROBE / ARRIVE / 报告规范" → `imrad_check` 任务
- 用户提到"中英对照 / bilingual / 双语阅读 / 术语对照" → `bilingual_reading` 任务
- 用户提到"LaTeX排版 / Float too large / 页面稀疏 / 排版修复" → `latex_diagnosis` 任务

### Conference 模式子路由

当模式为 `conference` 时，进一步识别目标会议：

| 会议 | 风格偏置 |
|------|----------|
| NeurIPS | 理论深度 + 实验完整性 + 创新性 |
| ICML | 方法严谨 + 理论贡献 + 大规模实验 |
| ICLR | 创新性 + 清晰表达 + 可复现性 |
| CVPR | 视觉效果 + 实验对比 + 应用价值 |
| KDD | 实用性 + 大规模验证 + 工程贡献 |
| VLDB | 系统设计 + 性能优化 + 数据管理 |
| AAAI | AI创新 + 应用场景 + 理论基础 |
| IJCAI | AI综合 + 跨领域应用 + 理论深度 |
| ECCV | 视觉效果 + 实验对比 + 应用价值 |
| ACL/EMNLP | NLP创新 + 语言理解 + 生成质量 |
| SIGGRAPH | 图形创新 + 视觉质量 + 实时性能 |
| WSDM/RecSys | 推荐系统 + 用户行为 + 大规模验证 |

### ACM 模式子路由

当用户提到"ACM / CHI / SIGCOMM / SIGMOD / SIGIR / SIGKDD"时：

| 会议 | 风格偏置 |
|------|----------|
| CHI | 人机交互 + 用户研究 + 设计创新 |
| SIGCOMM | 网络系统 + 性能优化 + 协议设计 |
| SIGMOD | 数据管理 + 查询优化 + 系统设计 |
| SIGIR | 信息检索 + 用户行为 + 评估方法 |
| SIGKDD | 数据挖掘 + 大规模验证 + 实用性 |

### Springer 模式子路由

当用户提到"Springer / LNCS / ECCV / WSDM"时：

| 会议 | 风格偏置 |
|------|----------|
| ECCV | 视觉效果 + 实验对比 + 应用价值 |
| WSDM | 网络搜索 + 数据挖掘 + 用户行为 |
| ECML-PKDD | 机器学习 + 数据挖掘 + 知识发现 |

### 冲突解决规则

当关键词匹配多个模式时，按以下优先级判定：

1. **明确场馆关键词优先** — "IEEE" + "CVPR" → `ieee_trans`（IEEE 优先于 conference）
2. **任务关键词优先于模式关键词** — "rebuttal" + "IEEE" → `rebuttal` 任务
3. **默认降级** — 无法判定时 → `english_research`

**示例：**
- "IEEE Transactions rebuttal for CVPR submission" → `ieee_trans` 模式 + `rebuttal` 任务
- "NeurIPS paper with IEEE formatting" → `conference` 模式（NeurIPS 优先）
- "Chinese thesis with CVPR experiments" → `chinese_thesis` 模式（中文论文优先）

---

## Step 2 — 任务判定

进入模式后，再判定任务类型：

### 核心任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `full_draft` | 写整篇/大段正式草稿 | 完整论文初稿（Abstract+Introduction+Related Work+Method+Experiments+Conclusion） |
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

### 顶会专项任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `conference_polish` | 顶会风格润色 | 润色后文本 + 修改说明 |
| `poster_design` | 海报设计 | 海报布局 + 内容建议 |
| `slide_design` | 幻灯片设计 | PPT结构 + 演讲要点 |
| `rebuttal_writing` | Rebuttal撰写 | 结构化回复 + 策略建议 |
| `data_availability` | 数据可用性声明 | FAIR 合规的数据声明 |
| `paper2ppt` | 论文转 PPT | 中文 .pptx 演示文稿 |
| `citation_convert` | 引用格式转换 | 目标格式引用列表 |
| `academic_search` | 学术搜索 | 去重后的文献列表 |

### 扩展任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `imrad_check` | IMRAD/报告规范合规检查 | 逐条合规报告（✅/⚠️/❌） |
| `bilingual_reading` | 中英文对照阅读 | 中英并排 Markdown + 术语对照表 |
| `latex_diagnosis` | LaTeX 排版诊断修复 | 问题定位 + 精确行号 + 替换代码 + 修订报告 |

### ARS 整合任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `style_calibration` | 学习作者写作风格 | Style Profile（6 维度） |
| `socratic_research` | 苏格拉底式引导研究 | 研究计划 + INSIGHT 集合 |
| `disclosure` | 生成 AI 使用声明 | venue 特定的 AI-usage disclosure |
| `re_review` | 验证修改是否回应审稿意见 | R&R Traceability Matrix + 残留问题 |
| `calibration` | 校准审稿准确性 | Calibration Report（FNR/FPR/balanced accuracy） |

### 图表顾问任务

| task_type | 用户意图 | 必要输出 |
|-----------|----------|----------|
| `figure_advisor` | 科研数据可视化顾问 | 数据剖析 + 图型推荐 + 理由 + 备选 |
| `figure_review` | 图表合规审查 | 语义合规 + 形式合规 + 视觉自检报告 |
| `figure_polish` | 图表出版级润色 | 期刊规范适配 + 配色优化 + 字号调整 |

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

### 3.2 Conference 路由

在 `conference` 模式中：

#### 加载参考

- `references/figure-advisor/journal-specs.md` - 顶会图表规范
- `references/writing/ieee-expression-patterns-core.md` - 表达模式
- `references/writing/ieee-polishing.md` - 润色规则
- `references/writing/ieee-experiment-playbook.md` - 实验设计
- `references/figure-advisor/chart-selection.md` - 图表选择

#### Conference 风格偏置

1. 创新性优先：必须有明确的 novelty claim
2. 实验完整性：完整的消融实验 + 对比实验
3. 清晰表达：逻辑清晰，避免过度技术化
4. 可复现性：代码和数据可获取
5. 图表质量：高质量可视化，符合会议规范

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

### `conference` 最小执行主线

1. Identify novelty claim and target conference
2. Lock story arc (problem → method → experiments → contribution)
3. Plan figures (Figure 1 = framework, Figure 2-5 = experiments)
4. Draft with conference style constraints
5. Run conference-specific quality checks
6. Run multi-perspective review
7. Prepare code release and reproducibility checklist

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

### `pipeline` 最小执行主线

1. **RESEARCH** — deep-research: RQ Brief, Methodology, Bibliography, Synthesis
2. **WRITE** — academic-paper: Paper Draft
3. **INTEGRITY** — integrity_verification_agent: 完整性验证报告
4. **REVIEW** — academic-paper-reviewer: 5 份审稿报告 + Editorial Decision
5. **REVISE** — academic-paper: 修订稿, Response to Reviewers
6. **RE-REVIEW** — academic-paper-reviewer: 验证审稿报告
7. **FINAL INTEGRITY** — integrity_verification_agent: 最终验证报告
8. **FINALIZE** — academic-paper: 最终论文（MD/DOCX/LaTeX/PDF）
9. **PROCESS SUMMARY** — orchestrator: 论文创作过程记录

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

**执行参考**: `references/review/ieee-reviewer-simulation.md`, `references/review/reviewer-response.md`
**审稿人角色**: 方法论/实验/写作/领域/魔鬼代言人
**评分维度**: 创新性/技术质量/实验完整性/写作/重要性/可复现性

#### Rebuttal 工作流（三阶段）

**阶段一：Triage 分类**

对每条审稿意见先分类：
- `MAJOR_CONCERN` — 必须做实验/补数据才能响应
- `CLARIFICATION` — 可通过解释/澄清解决
- `POLITE_DISAGREE` — 审稿人主观意见，可礼貌不同意并提供证据

输出修改策略总结：哪里需要补实验、哪里只需解释、哪里可以措辞分歧。

**阶段二：Point-by-Point 回复起草**

格式：
```
[R1.1] 审稿人原文
→ 作者回复：[回复内容]
→ 修改位置：[Section/Page/Line/Figure/Table]
→ 状态：[已完成 / 需作者补充 [AUTHOR_INPUT_NEEDED: XXX]]
```

原则：
- 语气尊重但坚定，措辞学术化
- 不编造实验结果；需作者补充的标注 `[作者需提供：XXX]`
- 每条声称的修改必须映射到具体论文位置

**阶段三：回复信 QA 检查**

- [ ] 每条审稿意见是否都有回复（无遗漏）？
- [ ] 每个声称的修改是否都映射到具体论文位置？
- [ ] 语气是否尊重且学术化？
- [ ] 是否有编造数据或声称了不存在的修改？
- [ ] 是否有需要作者决定但还未填入的 placeholder？

#### 难以响应的意见处理

当审稿意见难以直接响应时：
1. 判断是技术缺陷还是主观偏好
2. 是否必须做实验，还是可通过澄清+补充讨论解决
3. 在不补实验的情况下，寻找论文中已有的证据支持立场
4. 给出具体回复措辞建议

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

### J. `conference_polish`

输出：
1. 润色后文本
2. 修改清单
3. 风格合规检查
4. 创新性强化建议
5. 实验完整性检查

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

### N. `imrad_check`

输出：
1. 论文类型识别（RCT/观察性/Meta分析/动物实验/病例报告/方法类）
2. 适用报告规范判定（CONSORT/STROBE/PRISMA/ARRIVE/CARE/IMRAD）
3. 逐条合规检查（✅ 合规 / ⚠️ 部分合规 / ❌ 缺失）
4. 缺失内容补充建议
5. 合规报告（Word）

#### 支持的报告规范

| 规范 | 适用类型 | 核心要求 |
|------|---------|---------|
| **CONSORT 2025** | 随机对照试验（RCT） | 25条目，含分配隐藏、盲法、CONSORT流程图 |
| **PRISMA 2020** | 系统综述/Meta分析 | 27条目，含检索策略、PRISMA流程图、偏倚评估 |
| **STROBE** | 观察性研究（队列/病例对照/横断面） | 22条目，含暴露/结局定义、失访处理 |
| **ARRIVE 2.0** | 动物实验 | 21条目，含样本量计算、随机化、盲法 |
| **IMRAD** | 实验性研究（通用） | Introduction/Methods/Results/Discussion 四段结构 |

### O. `bilingual_reading`

输出：
1. 中英文并排 Markdown 文档（每个章节：英文原文 + 中文翻译）
2. 图表在对应文字位置就近呈现（非末尾集中）
3. 术语对照表（英文术语 | 中文译法 | 首次出现位置）
4. 完整内容保留（非摘要/概述）
5. 所有参考文献编号保留

### P. `latex_diagnosis`

输出：
1. 问题诊断（页面稀疏/图表不填满/Float too large/标题孤立等）
2. 精确定位（具体行号/环境/命令）
3. 可直接替换的 LaTeX 代码
4. 修改前后对比
5. 修订报告（Word）

#### 常见 LaTeX 排版问题速查

| 问题 | 典型原因 | 修复方向 |
|------|---------|---------|
| 页面稀疏 | 浮动体参数过严 | 调整 `[htbp]` 或使用 `!ht` |
| Float too large | 图/表超出页面 | 缩放 `\includegraphics[width=\textwidth]` |
| 标题孤立 | 分页不当 | `\needspace` 或调整内容位置 |
| 多面板排列混乱 | `subfigure` 参数错误 | 统一宽度比例 |
| 公式溢出 | 长公式未换行 | `split` / `multline` 环境 |

### Q. `style_calibration`

输出：
1. Style Profile（6 维度）
   - 句子长度分布
   - 段落长度分布
   - 词汇偏好
   - 引用整合风格
   - 修饰语风格
   - 语域变化
2. 写作风格样本分析
3. 风格校准建议

**执行参考**: `references/writing/style-calibration-protocol.md`

### R. `socratic_research`

输出：
1. 研究问题开发（FINER 评分）
2. 研究计划
3. INSIGHT 集合
4. 方法论蓝图

**执行参考**: `references/ars-references/socratic-mode-protocol.md`, `references/ars-references/socratic-questioning-framework.md`

### S. `disclosure`

输出：
1. venue 特定的 AI-usage disclosure
2. 支持的 venue: NeurIPS, ICML, ICLR, CVPR, KDD, VLDB, AAAI, IJCAI, ACL, EMNLP, IEEE
3. 声明合规检查

**执行参考**: `references/ars-references/disclosure-mode-protocol.md`, `references/ars-references/venue-disclosure-policies.md`

### T. `re_review`

输出：
1. R&R Traceability Matrix
2. 残留问题列表
3. 新的 Editorial Decision
4. 修订回应清单

**执行参考**: `references/ars-references/re-review-mode-protocol.md`, `references/ars-references/review-criteria-framework.md`

### U. `calibration`

输出：
1. Calibration Report
   - FNR（假阴性率）
   - FPR（假阳性率）
   - balanced accuracy
2. 审稿准确性评估
3. 校准建议

**执行参考**: `references/ars-references/calibration-mode-protocol.md`, `references/ars-references/quality-rubrics.md`

---

## Step 6 — Reference Loading Policy

### `english_research` 常用加载

- section writing: `references/writing/traffic-writing-execution-master-index.md`
- structure / flow: `references/writing/traffic-writing-execution-master-index.md`
- review / de-AI: `references/review/paper-review.md`, `references/review/humanizer-patterns.md`
- **2024-2025 顶会模式**: `references/writing/cs-top-venue-patterns-2024-2025.md` (VAR, Mamba, Depth Anything V2 等真实 Abstract 分析)

### `ieee_trans` 常用加载

- article type / section spine: `references/workflow/ieee-writing-spine.md`, `references/writing/chapter-patterns-ieee.md`
- language / contribution / abstract patterns: `references/writing/traffic-writing-execution-master-index.md`
- experiment design: `references/writing/traffic-experiment-planning-master-index.md`
- visual planning: `references/writing/traffic-figure-patterns.md`
- provenance / numbers: `references/writing/ieee-data-provenance-checklist.md`
- paper review: `references/review/traffic-review-response-master-index.md`
- academic search: `references/research/academic-search.md`
- reviewer simulation: `references/review/ieee-reviewer-simulation.md`
- innovation inspiration: `references/writing/ieee-innovation-inspiration.md`
- real experimental data: `references/writing/ieee-real-experimental-data.md`
- expression patterns: `references/writing/ieee-expression-patterns.md`
- polishing rules: `references/writing/ieee-polishing.md`
- **交通领域论文模式**: `references/writing/ieee-traffic-transportation-patterns.md` (T-ITS/TIV/TNNLS 2024-2025 真实 Abstract 分析: 17 篇论文，涵盖交通流预测、轨迹预测、自动驾驶、GenAI 仿真、LLM+ITS、世界模型等)
- **2024-2025 顶会模式**: `references/writing/cs-top-venue-patterns-2024-2025.md` (VAR, Mamba, DeepSeek-R1 等真实 Abstract 分析)

### `conference` 常用加载

- figure specs: `references/figure-advisor/journal-specs.md`
- expression patterns: `references/writing/ieee-expression-patterns-core.md`
- polishing rules: `references/writing/ieee-polishing.md`
- experiment design: `references/writing/ieee-experiment-playbook.md`
- chart selection: `references/figure-advisor/chart-selection.md`
- visual review: `references/figure-advisor/visual-review.md`
- **真实论文模式**: `references/writing/ieee-traffic-transportation-patterns.md` (IEEE T-ITS 真实 Abstract 分析)

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

### `rebuttal` 常用加载

- 回复结构: `references/review/reviewer-response.md`
- 审稿人模拟: `references/review/ieee-reviewer-simulation.md`
- 审稿回复主索引: `references/review/traffic-review-response-master-index.md`

### `imrad_check` 常用加载

- 报告规范: 按论文类型选择 CONSORT/PRISMA/STROBE/ARRIVE 对应条目
- 写作规范: `references/writing/writer-guidelines.md`
- 章节模式: `references/writing/chapter-patterns-cn.md` 或 `chapter-patterns-ieee.md`

### `bilingual_reading` 常用加载

- 写作规范: `references/writing/writer-guidelines.md`
- 术语管理: 随文档生成术语对照表

### `latex_diagnosis` 常用加载

- 图表标准: `references/figure-advisor/journal-specs.md` 或 `traffic-figure-patterns.md`
- 写作规范: 按目标期刊选择对应参考

### `pipeline` 常用加载

- 流水线编排: `references/ars-references/pipeline-state-machine.md`
- 完整性验证: `references/ars-references/integrity-review-protocol.md`
- 两阶段审稿: `references/ars-references/two-stage-review-protocol.md`
- 外部审稿: `references/ars-references/external-review-protocol.md`
- 过程总结: `references/ars-references/process-summary-protocol.md`
- 进度仪表盘: `references/ars-templates/progress-dashboard-template.md`

### `style_calibration` 常用加载

- 风格校准协议: `references/writing/style-calibration-protocol.md`

### `socratic_research` 常用加载

- Socratic 模式协议: `references/ars-references/socratic-mode-protocol.md`
- Socratic 提问框架: `references/ars-references/socratic-questioning-framework.md`

### `disclosure` 常用加载

- Disclosure 模式协议: `references/ars-references/disclosure-mode-protocol.md`
- Venue disclosure 政策: `references/ars-references/venue-disclosure-policies.md`
- 顶会规范: `references/figure-advisor/journal-specs.md`

### `re_review` 常用加载

- Re-review 模式协议: `references/ars-references/re-review-mode-protocol.md`
- 审稿标准框架: `references/ars-references/review-criteria-framework.md`

### `calibration` 常用加载

- Calibration 模式协议: `references/ars-references/calibration-mode-protocol.md`
- 质量评分标准: `references/ars-references/quality-rubrics.md`

### `figure_advisor` 常用加载

- 工作流: `references/figure-advisor/figure-workflow.md`
- 图表选择: `references/figure-advisor/chart-selection.md`
- 避坑清单: `references/figure-advisor/viz-pitfalls.md`
- 期刊规范: `references/figure-advisor/journal-specs.md`
- 画图配方: `references/figure-advisor/plot-recipes.md`
- 数据剖析: `references/figure-advisor/data-profiling.md`

### `figure_review` 常用加载

- 视觉自检: `references/figure-advisor/visual-review.md`
- 合规清单: `references/figure-advisor/publication-checklist.md`
- 避坑清单: `references/figure-advisor/viz-pitfalls.md`

### `figure_polish` 常用加载

- 期刊规范: `references/figure-advisor/journal-specs.md`
- 画图配方: `references/figure-advisor/plot-recipes.md`
- 合规清单: `references/figure-advisor/publication-checklist.md`

---

## Step 7 — Special Enforcement Rules

### 7.1 Contribution Rule

在 `ieee_trans` 和 `conference` 模式下，每条 contribution 必须绑定：

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

### 7.4 Conference Style Rule

在 `conference` 模式下额外检查：

- 创新性声明明确
- 实验完整性（消融 + 对比）
- 图表质量符合会议规范
- 代码和数据可获取性
- 可复现性检查

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

### 7.7 ARS Integration Rule

ARS 整合任务的额外规则：

- **风格校准**：必须基于真实写作样本，不能虚构风格特征
- **Socratic 引导**：必须遵循 FINER 标准开发研究问题
- **Disclosure**：必须按目标 venue 要求生成，不能使用通用模板
- **Re-review**：必须验证所有审稿意见是否得到回应
- **Calibration**：必须使用真实审稿数据，不能虚构校准结果

### 7.8 Figure Advisor Rule

图表顾问任务的额外规则：

- **先思考后绘制**：永远先理解数据再选图，先想清楚"这张图要论证什么"
- **主动拦截**：发现用户需求会触发画图错误时，先说明问题再给替代方案
- **五条硬性原则**：
  1. 按最终尺寸出图，不二次缩放
  2. 矢量优先，绝不 JPEG
  3. 配色对色盲友好
  4. 字号在最终尺寸下可读（≥6pt）
  5. 误差必有交代（SD/SEM/CI + n + 检验方法）
- **视觉自检闭环**：渲染 PNG → 程序自检 → AI 读图 → 回改，直到通过
- **不虚构**：不虚构数据、不虚构图表、不虚构实验结果

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

### Conference Writing Agents

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

### ARS 整合 Agents (3个)

| Agent | 职责 |
|-------|------|
| report_compiler_agent | APA 7.0 报告编写 |
| research_architect_agent | 方法论蓝图设计 |
| synthesis_agent | 跨源综合分析 |

### 图表顾问 Agents (3个)

| Agent | 职责 |
|-------|------|
| data_profiler_agent | 数据剖析：列类型/样本量/分布/异常值/相关性 |
| chart_selector_agent | 图表选择：按数据形态+论证目标推荐图型 |
| figure_reviewer_agent | 图表审查：语义合规+形式合规+视觉自检 |

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
