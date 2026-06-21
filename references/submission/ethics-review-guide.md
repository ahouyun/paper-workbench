# 伦理审查指南 (Ethics Review Guide)

> IEEE要求作者声明是否使用了AI工具，并遵守研究伦理规范。

---

## 一、AI工具使用声明

### IEEE政策

IEEE要求作者在投稿时声明是否使用了AI工具辅助论文写作。

**必须声明的内容：**
- 是否使用了AI工具（如ChatGPT、Claude、Copilot等）
- 使用了哪些AI工具
- 用于什么目的（写作辅助、语法检查、代码生成等）
- AI工具生成的内容是否经过人工审核和修改

**声明模板：**
```
AI Tool Declaration:

The authors acknowledge the use of [工具名称] for [具体用途, e.g., 
grammar checking, code generation, literature search]. All AI-generated 
content has been thoroughly reviewed, verified, and modified by the 
authors to ensure accuracy and originality. The authors take full 
responsibility for the content of this manuscript.
```

**注意事项：**
- 即使只用了Grammarly等语法检查工具，也建议声明
- 声明不等于违规，隐瞒才等于违规
- 不同期刊可能有不同的声明要求，投稿前查阅期刊指南

---

## 二、数据隐私与合规

### 2.1 交通数据隐私问题

交通数据可能涉及的隐私信息：
- 车牌号
- 出行轨迹
- GPS定位
- 交通摄像头画面

### 2.2 数据脱敏要求

| 数据类型 | 隐私风险 | 脱敏方法 |
|---------|---------|---------|
| 车牌号 | 高 | 完全删除或加密 |
| GPS轨迹 | 高 | 聚合到区域级别 |
| 交通摄像头 | 高 | 模糊人脸和车牌 |
| 传感器数据 | 低 | 通常无需脱敏 |
| 交通流量 | 低 | 通常无需脱敏 |

### 2.3 数据使用声明模板

```
Data Availability Statement:

The traffic data used in this study are publicly available from 
[source] under [license]. The data have been [de-identified/aggregated] 
to protect individual privacy. No personally identifiable information 
is included in the dataset.

[或]

The data used in this study were collected by [机构] and made 
available under [协议]. The data have been processed to remove 
any personally identifiable information before analysis.
```

---

## 三、IRB审批

### 3.1 何时需要IRB审批

| 情况 | 是否需要IRB |
|------|------------|
| 使用公开的交通传感器数据 | 通常不需要 |
| 使用包含个人信息的轨迹数据 | 可能需要 |
| 收集新的交通数据（如调查） | 通常需要 |
| 使用社交媒体数据 | 可能需要 |
| 涉及人类受试者的研究 | 必须需要 |

### 3.2 IRB声明模板

```
Ethics Statement:

This study uses publicly available traffic data that do not contain 
personally identifiable information. As no human subjects were 
directly involved, Institutional Review Board (IRB) approval was 
not required for this research.

[或]

This research was approved by the Institutional Review Board of 
[机构名称] (Protocol #XXXX). All data collection procedures 
followed the approved protocol, and informed consent was obtained 
from all participants.
```

---

## 四、利益冲突声明

### 4.1 声明模板

```
Conflict of Interest Statement:

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to 
influence the work reported in this paper.

[或]

This research was supported by [资助机构] under grant [编号]. 
The funding agency had no role in study design, data collection, 
analysis, interpretation, or manuscript preparation.
```

---

## 五、作者贡献声明

### 5.1 CRediT分类法

IEEE推荐使用CRediT（Contributor Roles Taxonomy）分类法：

| 角色 | 说明 |
|------|------|
| Conceptualization | 概念化 |
| Methodology | 方法论 |
| Software | 软件 |
| Validation | 验证 |
| Formal Analysis | 形式分析 |
| Investigation | 调查 |
| Resources | 资源 |
| Data Curation | 数据管理 |
| Writing - Original Draft | 初稿撰写 |
| Writing - Review & Editing | 审阅和编辑 |
| Visualization | 可视化 |
| Supervision | 指导 |
| Project Administration | 项目管理 |
| Funding Acquisition | 资金获取 |

### 5.2 声明模板

```
Author Contributions:

[作者1]: Conceptualization, Methodology, Writing - Original Draft
[作者2]: Software, Validation, Formal Analysis
[作者3]: Investigation, Data Curation, Visualization
[作者4]: Supervision, Writing - Review & Editing, Funding Acquisition
```

---

## 六、引用伦理

### 6.1 必须引用的内容

- 直接引用的文字（必须用引号标注）
- 改述的观点
- 数据、图表、公式
- 方法、算法、代码

### 6.2 自引规范

- 不要过度自引（通常不超过总引用的20%）
- 自引应该是相关的，不是为了提高引用数
- 不要在审稿中要求引用自己的论文

### 6.3 引用准确性

- 确保引用的论文确实存在（参见citation-verification.md）
- 确保引用的内容与原文一致
- 不要断章取义

---

## 七、自查清单

### 投稿前
- [ ] 已声明AI工具使用情况
- [ ] 已确认数据隐私合规
- [ ] 已确认是否需要IRB审批
- [ ] 已准备利益冲突声明
- [ ] 已准备作者贡献声明
- [ ] 所有引用都准确无误
- [ ] 没有过度自引
- [ ] 没有断章取义的引用

---

> 来源：IEEE Author Center, CRediT Taxonomy
> 更新时间：2026-06-20
