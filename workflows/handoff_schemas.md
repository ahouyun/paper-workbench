# 交接数据规范

## 核心原则

### 1. 标准化

**要求**：
- 统一的数据格式
- 明确的字段定义
- 标准的验证规则

### 2. 完整性

**要求**：
- 必要字段完整
- 信息准确无误
- 关联信息完整

### 3. 可追溯

**要求**：
- 来源可追溯
- 变更可追踪
- 历史可查询

---

## 交接类型

### 1. 阶段间交接

**类型**：
- Stage 1 → Stage 2：研究成果交接
- Stage 2 → Stage 2.5：论文初稿交接
- Stage 2.5 → Stage 3：完整性报告交接
- Stage 3 → Stage 4：审稿意见交接
- Stage 4 → Stage 3'：修订论文交接
- Stage 3' → Stage 4'：复审意见交接
- Stage 4' → Stage 4.5：最终论文交接
- Stage 4.5 → Stage 5：定稿批准交接

### 2. 角色间交接

**类型**：
- 研究者 → 写作者：研究资料交接
- 写作者 → 审稿人：论文稿件交接
- 审稿人 → 写作者：审稿意见交接
- 写作者 → 编辑：最终稿件交接

### 3. 系统间交接

**类型**：
- 搜索系统 → 文献管理系统：文献数据交接
- 数据分析系统 → 写作系统：分析结果交接
- 写作系统 → 审稿系统：稿件交接
- 审稿系统 → 出版系统：定稿交接

---

## 交接数据结构

### 1. 交接元数据

**字段**：
- `handoff_id`：交接唯一标识符
- `handoff_type`：交接类型
- `from_stage`：来源阶段
- `to_stage`：目标阶段
- `created_at`：创建时间
- `status`：交接状态
- `version`：数据版本

**示例**：
```json
{
  "handoff_id": "HO-2024-001",
  "handoff_type": "STAGE_TO_STAGE",
  "from_stage": "RESEARCH",
  "to_stage": "WRITE",
  "created_at": "2024-01-01T00:00:00Z",
  "status": "COMPLETE",
  "version": "1.0.0"
}
```

### 2. 交接内容

**字段**：
- `artifacts`：交接工件列表
- `metadata`：元数据信息
- `quality_assurance`：质量保证信息
- `dependencies`：依赖信息

**示例**：
```json
{
  "artifacts": [
    {
      "artifact_id": "A001",
      "artifact_type": "RESEARCH_REPORT",
      "name": "research_report.md",
      "format": "markdown",
      "size": 1024,
      "checksum": "abc123",
      "location": "/path/to/file"
    }
  ],
  "metadata": {
    "research_question": "What is the effect of X on Y?",
    "methodology": "Systematic review",
    "scope": "Adults aged 18-65"
  },
  "quality_assurance": {
    "completeness": "HIGH",
    "accuracy": "HIGH",
    "consistency": "HIGH"
  },
  "dependencies": []
}
```

### 3. 交接工件

**字段**：
- `artifact_id`：工件唯一标识符
- `artifact_type`：工件类型
- `name`：工件名称
- `format`：工件格式
- `size`：工件大小
- `checksum`：校验和
- `location`：存储位置
- `created_at`：创建时间
- `created_by`：创建者

**示例**：
```json
{
  "artifact_id": "A001",
  "artifact_type": "RESEARCH_REPORT",
  "name": "research_report.md",
  "format": "markdown",
  "size": 1024,
  "checksum": "abc123",
  "location": "/path/to/file",
  "created_at": "2024-01-01T00:00:00Z",
  "created_by": "Researcher A"
}
```

---

## 交接流程

### 1. 准备交接

**活动**：
- 检查交接内容
- 验证数据完整性
- 准备交接文档
- 通知接收方

**检查项**：
- [ ] 交接内容完整
- [ ] 数据质量达标
- [ ] 文档准备齐全
- [ ] 接收方已通知

### 2. 执行交接

**活动**：
- 传输数据
- 验证数据
- 确认接收
- 记录交接

**检查项**：
- [ ] 数据传输成功
- [ ] 数据验证通过
- [ ] 接收已确认
- [ ] 交接已记录

### 3. 完成交接

**活动**：
- 更新状态
- 记录完成
- 通知相关方
- 归档文档

**检查项**：
- [ ] 状态已更新
- [ ] 完成已记录
- [ ] 相关方已通知
- [ ] 文档已归档

---

## 交接验证

### 1. 完整性验证

**检查项**：
- [ ] 必要字段完整
- [ ] 工件列表完整
- [ ] 元数据完整
- [ ] 依赖信息完整

**验证方法**：
- 字段完整性检查
- 工件存在性检查
- 元数据一致性检查
- 依赖关系验证

### 2. 准确性验证

**检查项**：
- [ ] 数据准确无误
- [ ] 格式符合规范
- [ ] 内容逻辑一致
- [ ] 引用信息正确

**验证方法**：
- 数据校验
- 格式检查
- 逻辑检查
- 引用验证

### 3. 一致性验证

**检查项**：
- [ ] 与源数据一致
- [ ] 与规范一致
- [ ] 与历史一致
- [ ] 与依赖一致

**验证方法**：
- 源数据对比
- 规范检查
- 历史对比
- 依赖关系检查

### 4. 时效性验证

**检查项**：
- [ ] 数据新鲜度
- [ ] 版本最新性
- [ ] 状态有效性
- [ ] 期限合规性

**验证方法**：
- 时间戳检查
- 版本号检查
- 状态检查
- 期限检查

---

## 交接规范

### 1. Stage 1 → Stage 2 交接

**交接内容**：
- 研究问题
- 文献综述
- 研究假设
- 方法论
- 数据来源

**数据结构**：
```json
{
  "research_question": {
    "question": "What is the effect of X on Y?",
    "finer_score": {
      "feasible": true,
      "interesting": true,
      "novel": true,
      "ethical": true,
      "relevant": true
    }
  },
  "literature_review": {
    "total_papers": 50,
    "included_papers": 30,
    "key_findings": ["Finding 1", "Finding 2"],
    "research_gaps": ["Gap 1", "Gap 2"]
  },
  "hypothesis": "X improves Y by Z%",
  "methodology": {
    "design": "Randomized controlled trial",
    "sample_size": 100,
    "data_collection": "Surveys and experiments"
  },
  "data_sources": ["Clinical trial database", "Survey responses"]
}
```

### 2. Stage 2 → Stage 2.5 交接

**交接内容**：
- 论文初稿
- 参考文献
- 图表
- 补充材料

**数据结构**：
```json
{
  "manuscript": {
    "title": "Effect of X on Y",
    "abstract": "...",
    "sections": ["Introduction", "Methods", "Results", "Discussion"],
    "word_count": 5000,
    "format": "IEEE"
  },
  "references": {
    "total": 30,
    "format": "IEEE",
    "verified": true
  },
  "figures": [
    {
      "figure_id": "F001",
      "title": "Figure 1",
      "description": "Main finding",
      "format": "PNG"
    }
  ],
  "supplementary": [
    {
      "material_id": "S001",
      "name": "Supplementary Data",
      "format": "CSV"
    }
  ]
}
```

### 3. Stage 2.5 → Stage 3 交接

**交接内容**：
- 完整性报告
- 问题清单
- 改进建议
- 论文稿件

**数据结构**：
```json
{
  "integrity_report": {
    "check_date": "2024-01-05",
    "status": "PASS",
    "checks": [
      {
        "check_type": "DATA_INTEGRITY",
        "status": "PASS",
        "issues": []
      },
      {
        "check_type": "CITATION_INTEGRITY",
        "status": "PASS",
        "issues": []
      }
    ]
  },
  "issues": [],
  "recommendations": [],
  "manuscript": {}
}
```

### 4. Stage 3 → Stage 4 交接

**交接内容**：
- 审稿报告
- 评分结果
- 修订建议
- 决策建议

**数据结构**：
```json
{
  "review_report": {
    "reviewers": [
      {
        "reviewer_id": "R001",
        "role": "METHODOLOGY_REVIEWER",
        "score": 75,
        "decision": "MAJOR_REVISION",
        "comments": [
          {
            "comment_id": "C001",
            "section": "Methods",
            "comment": "Sample size is too small",
            "severity": "MAJOR"
          }
        ]
      }
    ],
    "overall_score": 72,
    "overall_decision": "MAJOR_REVISION"
  },
  "revision_suggestions": [
    {
      "suggestion_id": "S001",
      "priority": "HIGH",
      "description": "Increase sample size to 200",
      "effort": "HIGH"
    }
  ]
}
```

---

## 交接错误处理

### 1. 错误类型

**数据错误**：
- 数据不完整
- 数据格式错误
- 数据不一致
- 数据过期

**传输错误**：
- 传输失败
- 传输中断
- 数据损坏
- 校验失败

**验证错误**：
- 验证失败
- 规范不符
- 逻辑错误
- 依赖错误

### 2. 错误处理流程

**发现错误**：
- 记录错误
- 分类错误
- 评估影响
- 通知相关方

**分析错误**：
- 分析原因
- 确定责任
- 评估严重性
- 制定解决方案

**修复错误**：
- 实施修复
- 验证修复
- 记录修复
- 更新状态

**预防错误**：
- 分析根本原因
- 改进流程
- 加强验证
- 培训人员

### 3. 错误记录

**记录内容**：
- 错误类型
- 错误描述
- 发生时间
- 影响范围
- 解决方案
- 预防措施

**记录格式**：
```json
{
  "error_id": "E001",
  "error_type": "DATA_ERROR",
  "description": "Missing required field: research_question",
  "timestamp": "2024-01-01T00:00:00Z",
  "impact": "Handoff cannot proceed",
  "resolution": "Request missing field from source",
  "prevention": "Add validation check before handoff"
}
```

---

## 交接监控

### 1. 监控指标

**性能指标**：
- 交接成功率
- 交接完成时间
- 错误发生率
- 验证通过率

**质量指标**：
- 数据完整性
- 数据准确性
- 数据一致性
- 数据时效性

### 2. 监控方式

**实时监控**：
- 交接状态监控
- 错误实时告警
- 性能实时统计
- 质量实时评估

**定期监控**：
- 日报/周报/月报
- 趋势分析
- 问题分析
- 改进建议

### 3. 监控报告

**报告内容**：
- 监控指标
- 问题分析
- 改进建议
- 行动计划

**报告格式**：
```
报告时间：[时间]
监控指标：
- 交接成功率：[数值]
- 平均完成时间：[数值]
- 错误发生率：[数值]
- 验证通过率：[数值]

问题分析：
- [问题1]
- [问题2]

改进建议：
- [建议1]
- [建议2]

行动计划：
- [计划1]
- [计划2]
```

---

## 自检清单

### 交接规范

- [ ] 交接类型定义清晰
- [ ] 数据结构定义明确
- [ ] 字段规范完整
- [ ] 验证规则明确

### 交接流程

- [ ] 准备流程完整
- [ ] 执行流程清晰
- [ ] 完成流程规范
- [ ] 错误处理完善

### 交接验证

- [ ] 完整性验证充分
- [ ] 准确性验证严格
- [ ] 一致性验证完整
- [ ] 时效性验证及时

### 交接监控

- [ ] 监控指标全面
- [ ] 监控方式有效
- [ ] 监控报告完整
- [ ] 改进机制健全
