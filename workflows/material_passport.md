# 物料护照系统

## 核心原则

### 1. 可追溯性

**要求**：
- 记录所有物料来源
- 追踪物料状态变化
- 保留完整历史记录

### 2. 完整性

**要求**：
- 记录所有关键信息
- 信息准确无误
- 更新及时同步

### 3. 一致性

**要求**：
- 格式统一规范
- 字段定义明确
- 版本管理清晰

---

## 护照结构

### 1. 基本信息

**字段**：
- `passport_id`：护照唯一标识符
- `version`：版本号（单调递增）
- `created_at`：创建时间
- `updated_at`：更新时间
- `stage`：当前阶段
- `status`：当前状态

**示例**：
```json
{
  "passport_id": "PP-2024-001",
  "version": "1.0.0",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-15T12:00:00Z",
  "stage": "WRITE",
  "status": "IN_PROGRESS"
}
```

### 2. 研究信息

**字段**：
- `research_question`：研究问题
- `hypothesis`：研究假设
- `methodology`：方法论
- `scope`：研究范围

**示例**：
```json
{
  "research_question": "What is the effect of X on Y?",
  "hypothesis": "X improves Y by Z%",
  "methodology": "Randomized controlled trial",
  "scope": "Adults aged 18-65"
}
```

### 3. 文献信息

**字段**：
- `literature_corpus`：文献语料库
- `search_strategy`：搜索策略
- `inclusion_criteria`：纳入标准
- `exclusion_criteria`：排除标准

**示例**：
```json
{
  "literature_corpus": [
    {
      "id": "L001",
      "title": "Study A",
      "authors": ["Smith et al."],
      "year": 2020,
      "doi": "10.xxxx/xxxxx",
      "quality_score": 85,
      "relevance_score": 90
    }
  ],
  "search_strategy": "PubMed, Web of Science, Scopus",
  "inclusion_criteria": "RCT, adults, X intervention, Y outcome",
  "exclusion_criteria": "Non-English, animal studies"
}
```

### 4. 数据信息

**字段**：
- `data_sources`：数据来源
- `data_collection`：数据收集
- `data_processing`：数据处理
- `data_quality`：数据质量

**示例**：
```json
{
  "data_sources": ["Clinical trial database", "Survey responses"],
  "data_collection": "2023-01 to 2023-12",
  "data_processing": "Cleaning, normalization, imputation",
  "data_quality": "High completeness, low missing rate"
}
```

### 5. 写作信息

**字段**：
- `drafts`：草稿列表
- `revisions`：修订记录
- `reviews`：审稿记录
- `comments`：评论记录

**示例**：
```json
{
  "drafts": [
    {
      "version": "1.0",
      "date": "2024-01-01",
      "author": "Author A",
      "status": "Draft"
    }
  ],
  "revisions": [
    {
      "version": "1.1",
      "date": "2024-01-15",
      "changes": "Added experiments section",
      "reviewer_comments": "Addressed R1 comment 1"
    }
  ],
  "reviews": [
    {
      "reviewer": "R1",
      "date": "2024-01-10",
      "score": 75,
      "decision": "Major Revision"
    }
  ]
}
```

### 6. 完整性信息

**字段**：
- `integrity_checks`：完整性检查记录
- `compliance_status`：合规状态
- `audit_trail`：审计追踪
- `risk_assessment`：风险评估

**示例**：
```json
{
  "integrity_checks": [
    {
      "stage": "WRITE",
      "date": "2024-01-05",
      "status": "PASS",
      "issues": []
    }
  ],
  "compliance_status": {
    "ethics": "APPROVED",
    "data_sharing": "COMPLIANT",
    "ai_disclosure": "COMPLETE"
  },
  "audit_trail": [
    {
      "timestamp": "2024-01-01T00:00:00Z",
      "action": "CREATE",
      "user": "Author A",
      "details": "Initial passport creation"
    }
  ]
}
```

### 7. 交接信息

**字段**：
- `handoffs`：交接记录
- `dependencies`：依赖关系
- `blockers`：阻塞问题
- `next_steps`：后续步骤

**示例**：
```json
{
  "handoffs": [
    {
      "from_stage": "RESEARCH",
      "to_stage": "WRITE",
      "date": "2024-01-01",
      "artifacts": ["research_report.md", "literature_review.md"],
      "status": "COMPLETE"
    }
  ],
  "dependencies": [
    {
      "type": "DATA",
      "source": "Clinical trial database",
      "status": "AVAILABLE"
    }
  ],
  "blockers": [],
  "next_steps": ["Complete experiments section", "Add figures"]
}
```

---

## 版本管理

### 1. 版本号规则

**格式**：`MAJOR.MINOR.PATCH`

**规则**：
- MAJOR：重大变更（结构变化、功能变化）
- MINOR：次要变更（内容更新、字段增加）
- PATCH：小修小补（格式调整、错误修复）

**示例**：
- `1.0.0`：初始版本
- `1.1.0`：增加新字段
- `1.1.1`：修复格式错误

### 2. 版本更新

**更新触发**：
- 阶段转换
- 内容变更
- 状态变化
- 问题修复

**更新流程**：
1. 检查变更内容
2. 确定版本号
3. 更新护照内容
4. 记录变更历史
5. 同步相关系统

### 3. 版本历史

**记录内容**：
- 版本号
- 更新时间
- 更新内容
- 更新人员
- 更新原因

**查询方式**：
- 版本号查询
- 时间范围查询
- 内容查询
- 人员查询

---

## 护照使用

### 1. 创建护照

**时机**：Stage 1 开始时

**内容**：
- 基本信息
- 研究信息（初步）
- 初始版本

**流程**：
1. 收集基本信息
2. 填写研究信息
3. 创建护照文件
4. 记录创建日志

### 2. 更新护照

**时机**：
- 阶段转换时
- 内容变更时
- 状态变化时
- 问题修复时

**内容**：
- 更新相关字段
- 记录变更历史
- 更新版本号
- 同步相关系统

**流程**：
1. 检查变更内容
2. 确定更新范围
3. 更新护照内容
4. 记录变更日志
5. 同步相关系统

### 3. 查询护照

**查询类型**：
- 完整护照查询
- 特定字段查询
- 历史版本查询
- 状态查询

**查询方式**：
- 按护照ID查询
- 按版本号查询
- 按时间查询
- 按状态查询

### 4. 验证护照

**验证内容**：
- 格式验证
- 完整性验证
- 一致性验证
- 时效性验证

**验证时机**：
- 阶段转换前
- 交接前
- 定期验证
- 问题修复后

---

## 护照集成

### 1. 与阶段集成

**Stage 1 → Stage 2**：
- 传递研究信息
- 传递文献信息
- 传递数据信息

**Stage 2 → Stage 2.5**：
- 传递写作信息
- 传递完整性信息
- 传递审稿信息

**Stage 2.5 → Stage 3**：
- 传递完整性报告
- 传递问题清单
- 传递改进建议

### 2. 与门禁集成

**Stage 2.5 门禁**：
- 检查护照完整性
- 验证信息准确性
- 确认状态一致性

**Stage 4.5 门禁**：
- 检查修订完整性
- 验证零回归
- 确认质量无下降

### 3. 与审稿集成

**审稿前**：
- 提供研究背景
- 提供文献信息
- 提供数据信息

**审稿后**：
- 记录审稿意见
- 记录修订内容
- 记录回复内容

---

## 护照安全

### 1. 访问控制

**权限类型**：
- 读取权限
- 写入权限
- 审核权限
- 管理权限

**权限分配**：
- 作者：读写权限
- 审稿人：读取权限
- 编辑：审核权限
- 管理员：管理权限

### 2. 数据保护

**保护措施**：
- 加密存储
- 访问日志
- 备份恢复
- 安全审计

**合规要求**：
- 隐私保护
- 数据保留
- 安全标准
- 法律合规

### 3. 审计追踪

**记录内容**：
- 访问记录
- 修改记录
- 删除记录
- 导出记录

**查询方式**：
- 时间范围查询
- 用户查询
- 操作查询
- 内容查询

---

## 护照模板

### 1. 完整护照模板

```json
{
  "passport_id": "PP-YYYY-NNN",
  "version": "1.0.0",
  "created_at": "YYYY-MM-DDTHH:MM:SSZ",
  "updated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "stage": "STAGE_NAME",
  "status": "STATUS",
  "research": {
    "research_question": "",
    "hypothesis": "",
    "methodology": "",
    "scope": ""
  },
  "literature": {
    "literature_corpus": [],
    "search_strategy": "",
    "inclusion_criteria": "",
    "exclusion_criteria": ""
  },
  "data": {
    "data_sources": [],
    "data_collection": "",
    "data_processing": "",
    "data_quality": ""
  },
  "writing": {
    "drafts": [],
    "revisions": [],
    "reviews": [],
    "comments": []
  },
  "integrity": {
    "integrity_checks": [],
    "compliance_status": {},
    "audit_trail": [],
    "risk_assessment": {}
  },
  "handoff": {
    "handoffs": [],
    "dependencies": [],
    "blockers": [],
    "next_steps": []
  }
}
```

### 2. 简化护照模板

```json
{
  "passport_id": "PP-YYYY-NNN",
  "version": "1.0.0",
  "stage": "STAGE_NAME",
  "status": "STATUS",
  "key_information": {
    "research_question": "",
    "main_findings": "",
    "current_issues": [],
    "next_steps": []
  }
}
```

---

## 自检清单

### 护照完整性

- [ ] 所有必要字段已填写
- [ ] 字段格式正确
- [ ] 信息准确无误
- [ ] 版本管理清晰

### 护照使用

- [ ] 创建时机正确
- [ ] 更新及时同步
- [ ] 查询方式便捷
- [ ] 验证流程完整

### 护照集成

- [ ] 与阶段集成完整
- [ ] 与门禁集成清晰
- [ ] 与审稿集成顺畅
- [ ] 状态管理一致

### 护照安全

- [ ] 访问控制合理
- [ ] 数据保护到位
- [ ] 审计追踪完整
- [ ] 合规要求满足
