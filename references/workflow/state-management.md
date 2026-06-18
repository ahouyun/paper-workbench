# 阶段与状态管理

适用于需要持久化进度追踪、逐步执行记录或清晰"当前在哪"状态的论文项目。

## 目标

在 `paper-context/workflow/` 下创建工作台，使 agent 可以无猜测地恢复工作。

## 状态模型

### Phase（阶段）

| 阶段 | 说明 |
|------|------|
| `intake_only` | 仅收集材料 |
| `workspace_ready` | 工作区已初始化 |
| `standards_resolved` | 标准已解析 |
| `sample_analysis_done` | 样文分析完成 |
| `evidence_built` | 证据已构建 |
| `spec_confirmed` | 规格已确认 |
| `outline_confirmed` | 大纲已确认 |
| `writing_allowed` | 允许写作 |
| `delivery_done` | 交付完成 |

### Status（状态）

| 状态 | 说明 |
|------|------|
| `pending` | 未开始 |
| `in_progress` | 进行中 |
| `blocked` | 被阻塞，缺少材料或决策 |
| `needs_review` | 已生成，需人工/学校/模板审查 |
| `done` | 已完成，足够当前阶段 |
| `deprecated` | 不再使用 |

### 阻塞状态写法

当阶段被阻塞时，在 `workflow-status.md` 中写入：

```yaml
phase: evidence_built
status: blocked
blocked_reason:
  - "缺少数据库 schema，不能生成 E-R 图。"
next_action:
  - "请提供数据库迁移文件、建表 SQL 或实体类目录。"
```

## 合法回滚表

| 当前阶段 | 触发事件 | 目标阶段 |
|----------|----------|----------|
| `writing_allowed` | 用户添加新样文、学校模板或导师要求 | `sample_analysis_done` |
| `writing_allowed` | 用户添加新源码、数据库、截图或测试 | `evidence_built` |
| `outline_confirmed` | 用户更改大纲、字数或样文/模板观察 | `sample_analysis_done` |
| `delivery_done` | 导师 Word 批注到达 | `writing_allowed` |
| `delivery_done` | 学校/导师要求变更 | `standards_resolved` |
| `delivery_done` | 新证据使旧事实失效 | `evidence_built` |

## 任务开始规则

开始论文任务时：

1. 读 `workflow-status.md`
2. 读 `user-dashboard.md`
3. 读 `step-plan.md`
4. 当状态被阻塞或请求可能解除阻塞时，读 `blocker-report.md`
5. 当请求依赖先前用户确认时，读 `user-decisions.md`
6. 当请求影响大纲、章节重点、图表、实验、附录或排除时，读 `content-decisions.md`
7. 当请求影响样文/模板分析、临时大纲或字数预算时，读 `sample-template-analysis.md`
8. 读请求相关的模块特定文件
9. 在做实质工作前更新当前阶段和下一步操作

## 任务结束规则

结束论文任务时：

1. 更新 `user-dashboard.md`：用户可见进度、待决策、缺失材料、下一步
2. 更新 `blocker-report.md`：工作被阻塞、受限、解除或等待用户选择时
3. 更新 `user-decisions.md`：用户确认选择影响范围、不可用材料、受限继续、标准、大纲、交付或文件名规则时
4. 更新 `content-decisions.md`：新证据改变应强调、摘要、移至附录、推迟或排除的内容时
5. 追加条目到 `progress-log.md`
6. 更新 `step-plan.md` 状态
7. 更新 `chapter-progress.md`：如果章节工作有变化
8. 添加未解决材料到 `evidence-gaps.md`
9. 添加实际编辑到 `revision-log.md`

## 不可协商规则

更改论文内容或工作流状态后，不得静默跳过日志更新。工作台是论文项目的记忆。

## 用户看板规则

`user-dashboard.md` 保持简短，用户可快速扫描后做决策。

当以下任何项变化时更新：

- 阶段或状态
- 缺失材料
- 材料优先级、缺失影响或继续限制
- 用户确认请求
- 内容重点、附录、推迟或排除决策
- 阻塞、选项、建议或受限继续状态
- 用户确认的范围、限制、标准、大纲或交付决策
- 大纲或字数决策
- 交付范围

看板应回答 5 个问题：

1. **我们在哪**：当前阶段和状态
2. **已处理了什么**：已完成的步骤
3. **用户需要决定什么**：待确认事项
4. **缺什么，影响什么**：缺失材料及其影响
5. **下一步建议**：推荐的下一步操作

## 内容决策规则

`content-decisions.md` 是辅助决策层，本身不阻塞。

当用户提供的模块、功能、实验、数据集、图表、截图、附录候选或特殊导师偏好时使用。如果没有候选内容，保持占位行并继续主流程。

确认大纲或起草章节前，检查活跃行：

- `正文重点`：确认证据后可塑造章节重点
- `正文简写`：可摘要不过度展开
- `附录`：有源时应引导附录/DOCX 资产规划
- `暂缓`和`待补证据`：不应成为正式声明
- `不写`和拒绝项：除非用户修改决策，否则不出现在正文中
