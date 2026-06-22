# Paper Workbench v7.2.0 整合总结

## 整合来源

### 1. academic-research-skills (Imbad0202)

**版本**：v3.13.0（2026-06-22 更新）

**核心组件**：
- deep-research：13 个 Agent，7 种模式
- academic-paper：12 个 Agent，10 种模式
- academic-paper-reviewer：7 个 Agent，6 种模式
- academic-pipeline：10 阶段编排

**关键特性**：
- 多视角审稿系统
- Socratic 引导模式
- Sprint Contract 预承诺
- Material Passport 跨阶段追踪
- Integrity Gate 完整性门禁
- Anti-sycophancy 反谄媚协议
- 风格校准协议（6 维度）
- Nature/venue 政策支持
- PRISMA/RAISE 合规支持

### 2. nature-skills (Yuan1z0825)

**版本**：最新

**核心组件**：
- nature-figure：Nature 标准图表生成
- nature-polishing：Nature 风格润色
- nature-writing：Nature 风格写作
- nature-citation：Nature/CNS 引用管理
- nature-data：数据可用性声明
- nature-response：审稿回复
- nature-academic-search：学术搜索
- nature-reader：论文阅读
- nature-paper2ppt：论文转 PPT

**关键特性**：
- Nature 期刊风格规范
- 12 步润色流程
- 图表三级信息层次
- 英式英语规范
- FAIR 数据原则

---

## 整合成果

### 1. 模式扩展

**新增模式**：
- `nature`：Nature/Science/Cell 期刊风格
- `deep_research`：深度研究、文献综述
- `systematic_review`：PRISMA 系统综述
- `pipeline`：完整学术流水线（研究→写作→审稿→修改→定稿）

**模式总数**：7 种（原有 3 种 + 新增 4 种）

### 2. 任务类型扩展

**新增任务**：
- `deep_research`：深度研究
- `quick_research`：快速研究概览
- `socratic_guide`：苏格拉底引导
- `fact_check`：事实核查
- `lit_review`：文献综述
- `nature_polish`：Nature 风格润色
- `data_availability`：数据可用性声明
- `paper2ppt`：论文转 PPT
- `citation_convert`：引用格式转换
- `academic_search`：学术搜索
- `style_calibration`：学习作者写作风格（ARS 整合）
- `socratic_research`：苏格拉底式引导研究（ARS 整合）
- `disclosure`：生成 AI 使用声明（ARS 整合）
- `re_review`：验证修改是否回应审稿意见（ARS 整合）
- `calibration`：校准审稿准确性（ARS 整合）

**任务总数**：22 种（原有 7 种 + 新增 15 种）

### 3. 参考文件

**新增文件**（约 85 个）：

**Venue 参考**：
- `references/venues/nature-portfolio.md`
- `references/venues/nature-policy.md`（ARS 整合）

**Writing 参考**：
- `references/writing/nature-writing-style.md`
- `references/writing/nature-figure-standards.md`
- `references/writing/nature-polishing-rules.md`
- `references/writing/nature-citation-format.md`
- `references/writing/nature-data-availability.md`
- `references/writing/style-calibration-protocol.md`（ARS 整合）
- `references/writing/protected-hedging-phrases.md`（ARS 整合）
- `references/writing/word-count-conventions.md`（ARS 整合）
- `references/writing/psychometric-terminology-glossary.md`（ARS 整合）

**Workflow 参考**：
- `references/workflow/deep-research-workflow.md`
- `references/workflow/socratic-guidance.md`
- `references/workflow/systematic-review-protocol.md`
- `references/workflow/handoff-schemas.md`（ARS 整合）
- `references/workflow/compliance-checkpoint-protocol.md`（ARS 整合）
- `references/workflow/raise-framework.md`（ARS 整合）
- `references/workflow/prisma-trAIce-protocol.md`（ARS 整合）
- `references/workflow/cross-model-verification.md`（ARS 整合）
- `references/workflow/mode-spectrum.md`（ARS 整合）
- `references/workflow/intent-clarification-protocol.md`（ARS 整合）
- `references/workflow/ground-truth-isolation-pattern.md`（ARS 整合）
- `references/workflow/artifact-reproducibility-pattern.md`（ARS 整合）

**Research 参考**：
- `references/research/source-verification.md`
- `references/research/bibliography-management.md`

**Review 参考**：
- `references/review/nature-response-template.md`
- `references/review/devils-advocate-protocol.md`
- `references/review/ethics-review-checklist.md`
- `references/review/calibration-rubric.md`
- `references/review/collaboration-depth-rubric.md`（ARS 整合）

**ARS 整合参考**（40 个文件）：
- `references/ars-references/apa7-style-guide.md`
- `references/ars-references/source-quality-hierarchy.md`
- `references/ars-references/methodology-patterns.md`
- `references/ars-references/logical-fallacies.md`
- `references/ars-references/ethics-checklist.md`
- `references/ars-references/socratic-questioning-framework.md`
- `references/ars-references/failure-paths.md`
- `references/ars-references/mode-selection-guide.md`
- `references/ars-references/systematic-review-toolkit.md`
- `references/ars-references/argumentation-reasoning-framework.md`
- `references/ars-references/socratic-mode-protocol.md`
- `references/ars-references/systematic-review-protocol.md`
- `references/ars-references/cross-agent-quality-definitions.md`
- `references/ars-references/writing-quality-check.md`
- `references/ars-references/disclosure-mode-protocol.md`
- `references/ars-references/venue-disclosure-policies.md`
- `references/ars-references/paper-structure-patterns.md`
- `references/ars-references/abstract-writing-guide.md`
- `references/ars-references/statistical-visualization-standards.md`
- `references/ars-references/credit-authorship-guide.md`
- `references/ars-references/funding-statement-guide.md`
- `references/ars-references/journal-submission-guide.md`
- `references/ars-references/apa7-extended-guide.md`
- `references/ars-references/apa7-chinese-citation-guide.md`
- `references/ars-references/citation-format-switcher.md`
- `references/ars-references/academic-writing-style.md`
- `references/ars-references/writing-judgment-framework.md`
- `references/ars-references/hei-domain-glossary.md`
- `references/ars-references/latex-template-reference.md`
- `references/ars-references/plan-mode-protocol.md`
- `references/ars-references/workflow-phase-details.md`
- `references/ars-references/irb-decision-tree.md`
- `references/ars-references/equator-reporting-guidelines.md`
- `references/ars-references/preregistration-guide.md`
- `references/ars-references/review-criteria-framework.md`
- `references/ars-references/top-journals-by-field.md`
- `references/ars-references/editorial-decision-standards.md`
- `references/ars-references/statistical-reporting-standards.md`
- `references/ars-references/quality-rubrics.md`
- `references/ars-references/review-quality-thinking.md`
- `references/ars-references/re-review-mode-protocol.md`
- `references/ars-references/guided-mode-protocol.md`
- `references/ars-references/calibration-mode-protocol.md`

**ARS 整合 Agent 定义**（3 个文件）：
- `references/ars-agents/report-compiler-agent.md`
- `references/ars-agents/research-architect-agent.md`
- `references/ars-agents/synthesis-agent.md`

**ARS 整合模板**（7 个文件）：
- `references/ars-templates/evidence-assessment-template.md`
- `references/ars-templates/literature-matrix-template.md`
- `references/ars-templates/editorial-decision-template.md`
- `references/ars-templates/peer-review-report-template.md`
- `references/ars-templates/revision-response-template.md`
- `references/ars-templates/progress-dashboard-template.md`
- `references/ars-templates/pipeline-status-template.md`

**Workflow 文件**：
- `workflows/pipeline_stages.md`
- `workflows/integrity_gates.md`
- `workflows/material_passport.md`
- `workflows/handoff_schemas.md`

**Agent 定义**：
- `agents/deep_research_agents.md`
- `agents/nature_writing_agents.md`
- `agents/review_agents.md`
- `agents/pipeline_agents.md`

**脚本索引**：
- `scripts/nature_scripts_INDEX.md`

### 4. SKILL.md 更新

**版本**：5.0.0 → 7.2.0

**主要更新**：
- 新增 4 种模式路由（含 pipeline 模式）
- 新增 15 种任务类型（含 5 种 ARS 整合任务）
- 新增 Nature 风格偏置
- 新增 Deep Research 路由
- 新增 Systematic Review 路由
- 新增 Pipeline 路由
- 新增 Agent 编排章节（含 ARS 整合 Agent）
- 新增质量保证章节
- 新增 ARS 整合规则（7.7 ARS Integration Rule）
- 更新参考文件加载策略（含 ARS 整合参考）
- 更新强制执行规则

---

## 核心能力

### 1. 多模式写作

**支持模式**：
- 中文毕设论文
- 通用英文研究论文
- IEEE Transactions 风格
- Nature/Science/Cell 期刊风格
- 深度研究
- PRISMA 系统综述
- 完整学术流水线（ARS 整合）

### 2. 多任务处理

**核心任务**：
- 全文撰写
- 章节改写
- 大纲生成
- 声明验证
- 实验设计
- 图表规划
- 论文审稿
- 审稿回复

**研究任务**：
- 深度研究
- 快速研究
- 苏格拉底引导
- 事实核查
- 文献综述

**Nature 专项任务**：
- Nature 风格润色
- 数据可用性声明
- 论文转 PPT
- 引用格式转换
- 学术搜索

**ARS 整合任务**：
- 风格校准
- 苏格拉底式引导研究
- AI 使用声明生成
- 审稿回应验证
- 审稿准确性校准

### 3. 多 Agent 协作

**Deep Research Agents**：13 个
**Nature Writing Agents**：11 个
**Review Agents**：7 个
**Pipeline Agents**：5 个
**ARS 整合 Agents**：3 个

**总 Agent 数**：39 个

### 4. 质量保证

**完整性门禁**：
- Stage 2.5：预审完整性检查
- Stage 4.5：最终完整性检查

**质量检查**：
- 数据完整性
- 引用完整性
- 伦理合规性
- 方法可重复性

**反谄媚协议**：
- 审稿独立性
- 修订合理性
- 声明真实性

### 5. 状态管理

**Material Passport**：
- 跨阶段物料追踪
- 版本单调递增
- 交接点必携

**Handoff Schemas**：
- 标准化交接格式
- 完整性验证
- 一致性检查

---

## 文件结构

```
paper-workbench/
├── SKILL.md (主入口，v7.2.0)
├── INTEGRATION_SUMMARY.md (本文件)
├── INTEGRATION_SUMMARY_ARS.md (ARS 整合总结)
├── agents/
│   ├── deep_research_agents.md
│   ├── nature_writing_agents.md
│   ├── review_agents.md
│   └── pipeline_agents.md
├── prompts/
│   ├── aigc_reducer_prompt.md
│   ├── reference_citation_prompt.md
│   └── idiom_replacement_dict.md
├── references/
│   ├── delivery/
│   ├── review/
│   │   ├── nature-response-template.md
│   │   ├── devils-advocate-protocol.md
│   │   ├── ethics-review-checklist.md
│   │   ├── calibration-rubric.md
│   │   ├── paper-review.md
│   │   ├── humanizer-patterns.md
│   │   └── collaboration-depth-rubric.md (ARS 整合)
│   ├── research/
│   │   ├── source-verification.md
│   │   └── bibliography-management.md
│   ├── sections/
│   ├── venues/
│   │   ├── nature-portfolio.md
│   │   └── nature-policy.md (ARS 整合)
│   ├── workflow/
│   │   ├── deep-research-workflow.md
│   │   ├── socratic-guidance.md
│   │   ├── systematic-review-protocol.md
│   │   ├── intake.md
│   │   ├── evidence-workflow.md
│   │   ├── standards-resolution.md
│   │   ├── state-management.md
│   │   ├── handoff-schemas.md (ARS 整合)
│   │   ├── compliance-checkpoint-protocol.md (ARS 整合)
│   │   ├── raise-framework.md (ARS 整合)
│   │   ├── prisma-trAIce-protocol.md (ARS 整合)
│   │   ├── cross-model-verification.md (ARS 整合)
│   │   ├── mode-spectrum.md (ARS 整合)
│   │   ├── intent-clarification-protocol.md (ARS 整合)
│   │   ├── ground-truth-isolation-pattern.md (ARS 整合)
│   │   └── artifact-reproducibility-pattern.md (ARS 整合)
│   ├── writing/
│   │   ├── nature-writing-style.md
│   │   ├── nature-figure-standards.md
│   │   ├── nature-polishing-rules.md
│   │   ├── nature-citation-format.md
│   │   ├── nature-data-availability.md
│   │   ├── writer-guidelines.md
│   │   ├── chapter-patterns-cn.md
│   │   ├── style-calibration-protocol.md (ARS 整合)
│   │   ├── protected-hedging-phrases.md (ARS 整合)
│   │   ├── word-count-conventions.md (ARS 整合)
│   │   ├── psychometric-terminology-glossary.md (ARS 整合)
│   │   └── ...
│   ├── ars-references/ (ARS 整合，40 个文件)
│   │   ├── apa7-style-guide.md
│   │   ├── source-quality-hierarchy.md
│   │   ├── methodology-patterns.md
│   │   ├── logical-fallacies.md
│   │   ├── ethics-checklist.md
│   │   ├── socratic-questioning-framework.md
│   │   ├── failure-paths.md
│   │   ├── mode-selection-guide.md
│   │   ├── systematic-review-toolkit.md
│   │   ├── argumentation-reasoning-framework.md
│   │   ├── socratic-mode-protocol.md
│   │   ├── systematic-review-protocol.md
│   │   ├── cross-agent-quality-definitions.md
│   │   ├── writing-quality-check.md
│   │   ├── disclosure-mode-protocol.md
│   │   ├── venue-disclosure-policies.md
│   │   ├── paper-structure-patterns.md
│   │   ├── abstract-writing-guide.md
│   │   ├── statistical-visualization-standards.md
│   │   ├── credit-authorship-guide.md
│   │   ├── funding-statement-guide.md
│   │   ├── journal-submission-guide.md
│   │   ├── apa7-extended-guide.md
│   │   ├── apa7-chinese-citation-guide.md
│   │   ├── citation-format-switcher.md
│   │   ├── academic-writing-style.md
│   │   ├── writing-judgment-framework.md
│   │   ├── hei-domain-glossary.md
│   │   ├── latex-template-reference.md
│   │   ├── plan-mode-protocol.md
│   │   ├── workflow-phase-details.md
│   │   ├── irb-decision-tree.md
│   │   ├── equator-reporting-guidelines.md
│   │   ├── preregistration-guide.md
│   │   ├── review-criteria-framework.md
│   │   ├── top-journals-by-field.md
│   │   ├── editorial-decision-standards.md
│   │   ├── statistical-reporting-standards.md
│   │   ├── quality-rubrics.md
│   │   ├── review-quality-thinking.md
│   │   ├── re-review-mode-protocol.md
│   │   ├── guided-mode-protocol.md
│   │   └── calibration-mode-protocol.md
│   ├── ars-agents/ (ARS 整合，3 个文件)
│   │   ├── report-compiler-agent.md
│   │   ├── research-architect-agent.md
│   │   └── synthesis-agent.md
│   ├── ars-templates/ (ARS 整合，7 个文件)
│   │   ├── evidence-assessment-template.md
│   │   ├── literature-matrix-template.md
│   │   ├── editorial-decision-template.md
│   │   ├── peer-review-report-template.md
│   │   ├── revision-response-template.md
│   │   ├── progress-dashboard-template.md
│   │   └── pipeline-status-template.md
│   └── ars-integration-index.md (ARS 整合索引)
├── scripts/
│   ├── nature_scripts_INDEX.md
│   ├── aigc/
│   ├── charts/
│   ├── document_exporter/
│   └── ...
└── workflows/
    ├── pipeline_stages.md
    ├── integrity_gates.md
    ├── material_passport.md
    ├── handoff_schemas.md
    ├── step_0_init.md
    ├── step_3_outline.md
    ├── step_4_writing.md
    └── ...
```

---

## 使用指南

### 1. 模式选择

**中文毕设**：`chinese_thesis`
**通用英文论文**：`english_research`
**IEEE Transactions**：`ieee_trans`
**Nature/Science/Cell**：`nature`
**深度研究**：`deep_research`
**系统综述**：`systematic_review`
**完整流水线**：`pipeline`（ARS 整合）

### 2. 任务选择

**论文写作**：`full_draft`, `section_rewrite`, `outline_only`
**研究任务**：`deep_research`, `quick_research`, `lit_review`
**Nature 专项**：`nature_polish`, `data_availability`, `paper2ppt`
**质量检查**：`claim_evidence_check`, `paper_review`, `fact_check`
**ARS 整合任务**：`style_calibration`, `socratic_research`, `disclosure`, `re_review`, `calibration`

### 3. 参考文件加载

**自动加载**：根据模式和任务自动加载对应参考
**手动加载**：用户可指定加载特定参考
**按需加载**：只加载当前任务所需参考
**ARS 整合参考**：`references/ars-integration-index.md` 索引所有 ARS 整合资源

---

## 后续计划

### 1. 脚本实现

**待实现**：
- academic_search.py
- citation_converter.py
- figure_renderer_nature.py
- paper2ppt.py
- data_availability_checker.py

### 2. 测试验证

**测试内容**：
- 模式路由测试
- 任务分发测试
- Nature 风格测试
- 审稿系统测试
- Pipeline 测试
- 搜索测试
- ARS 整合功能测试
  - style_calibration 测试
  - socratic_research 测试
  - disclosure 测试
  - re_review 测试
  - calibration 测试

### 3. 文档完善

**待完善**：
- 用户指南
- 开发者文档
- API 文档
- 示例文档
- ARS 整合使用指南

---

## 总结

本次整合成功将 academic-research-skills (v3.13.0) 和 nature-skills 的核心能力集成到 paper-workbench 中，创建了一个功能更强大的统一论文写作工作台。

**主要成果**：
- 7 种写作模式（新增 pipeline 模式）
- 22 种任务类型（新增 5 种 ARS 整合任务）
- 39 个协作 Agent（新增 3 个 ARS 整合 Agent）
- 85+ 个参考文件（新增 65 个 ARS 整合文件）
- 完整的质量保证体系
- 标准化的状态管理
- 风格校准能力（ARS 整合）
- Nature/venue 政策支持（ARS 整合）
- PRISMA/RAISE 合规支持（ARS 整合）

**核心价值**：
- 覆盖从研究到发表的全流程
- 支持多种期刊风格
- 提供多视角审稿
- 保证研究质量
- 提升写作效率
- 完整学术流水线编排（ARS 整合）
- 风格校准和写作质量检查（ARS 整合）
- AI 使用声明生成（ARS 整合）
