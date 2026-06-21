# IEEE Transactions 投稿指南

> 从准备到提交的完整操作指南。

---

## 一、投稿前准备

### 1.1 文件准备清单

| 文件 | 格式 | 说明 |
|------|------|------|
| 主稿件 | PDF 或 LaTeX | 双栏，10pt，IEEEtran格式 |
| Cover Letter | PDF | 半页到1页 |
| 补充材料 | PDF | 可选 |
| 高分辨率图表 | PDF/EPS/TIFF | 300 DPI以上 |
| 源文件 | LaTeX + BibTeX | 可选，但推荐 |
| 数据/代码 | ZIP 或 GitHub链接 | 可选，但推荐 |

### 1.2 LaTeX格式要求

```latex
\documentclass[journal,10pt]{IEEEtran}  % 期刊模式
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{algorithmic}
\usepackage{booktabs}  % 专业表格
\usepackage{multirow}

% 图表格式
\usepackage[caption=false,font=footnotesize]{subfig}
```

### 1.3 图表格式要求

| 要求 | 规范 |
|------|------|
| 分辨率 | ≥300 DPI |
| 格式 | PDF/EPS（矢量图优先）或 TIFF |
| 字体 | Arial/Helvetica，≥8pt |
| 颜色 | 色盲友好，避免纯红绿 |
| 单栏宽度 | 8.9 cm (3.5 in) |
| 双栏宽度 | 17.8 cm (7.0 in) |

---

## 二、ScholarOne投稿流程

### 步骤1：创建账号
- 访问 https://mc.manuscriptcentral.com/ieee-tits
- 注册或登录ScholarOne账号

### 步骤2：开始新投稿
- 点击 "Start New Submission"
- 选择文章类型（通常为 "Regular Paper"）

### 步骤3：填写信息
- **Title**: 论文标题
- **Abstract**: 复制摘要（不超过200词）
- **Keywords**: 3-5个关键词
- **Authors**: 添加所有作者，指定通讯作者

### 步骤4：上传文件
- 上传主稿件（PDF）
- 上传Cover Letter
- 上传补充材料（如有）
- 上传高分辨率图表（如有）

### 步骤5：推荐审稿人
- 推荐3-5位审稿人
- 包含姓名、机构、邮箱
- 避免推荐合作者或同一机构的人

### 步骤6：确认提交
- 检查所有信息
- 同意版权声明
- 提交

---

## 三、审稿流程时间线

| 阶段 | 时间 | 说明 |
|------|------|------|
| 初审 | 1-2周 | 编辑检查格式和范围 |
| 外审 | 4-8周 | 2-3位审稿人评审 |
| 决定 | 1-2周 | 编辑做出决定 |
| **总计** | **6-12周** | 从提交到首次决定 |

### 可能的决定

| 决定 | 说明 | 下一步 |
|------|------|--------|
| Accept | 直接接收 | 很少，通常需要小修 |
| Minor Revision | 小修 | 2-4周内提交修改稿 |
| Major Revision | 大修 | 4-8周内提交修改稿 |
| Reject & Resubmit | 拒稿但鼓励重投 | 重大修改后重新投稿 |
| Reject | 拒稿 | 考虑其他期刊 |

---

## 四、审稿回复指南

### 4.1 回复信结构

```
Dear Editor and Reviewers,

Thank you for the constructive comments on our manuscript 
"[标题]". We have carefully addressed all the concerns 
and revised the manuscript accordingly. Below is a 
point-by-point response to each comment.

[对每位审稿人的回复]

Reviewer #1:
R1.1: [审稿人意见]
Response: [你的回复]
Revision: [修改说明和位置]

R1.2: [审稿人意见]
Response: [你的回复]
Revision: [修改说明和位置]

...

[总结]
We believe that the revised manuscript has been significantly 
improved based on the reviewers' comments. We hope that the 
revised version is now suitable for publication in [期刊名].

Sincerely,
[作者]
```

### 4.2 回复原则

| 原则 | 说明 |
|------|------|
| **逐条回复** | 每条意见都要回复，不要遗漏 |
| **感谢审稿人** | 即使不同意，也要感谢 |
| **引用修改位置** | 说明在稿件中的具体修改位置 |
| **提供证据** | 用数据或引用支持你的回复 |
| **保持礼貌** | 即使审稿人误解了，也要礼貌解释 |

### 4.3 回复模板

**同意并修改：**
```
We thank the reviewer for this insightful comment. 
Following the suggestion, we have [具体修改]. 
The revised text can be found in Section X, Page Y.
```

**部分同意：**
```
We appreciate the reviewer's suggestion. While we agree 
that [同意的部分], we believe that [不同意的部分] because 
[理由]. Nevertheless, we have added [补充说明] to clarify 
this point. See Section X, Page Y.
```

**不同意（需要充分理由）：**
```
We thank the reviewer for this comment. However, we 
respectfully disagree because [详细理由，需要引用支持]. 
We have added additional discussion in Section X to 
address this concern.
```

---

## 五、常见审稿意见及应对

### 5.1 "实验不充分"

**审稿人意见：** "The experiments are not comprehensive enough."

**应对：**
- 添加更多数据集
- 添加更多基线方法
- 添加消融实验
- 添加效率分析

### 5.2 "创新性不足"

**审稿人意见：** "The novelty is limited."

**应对：**
- 更清晰地阐述创新点
- 与现有方法进行更详细的对比
- 提供理论分析或证明
- 展示独特的实验发现

### 5.3 "写作质量差"

**审稿人意见：** "The paper is poorly written."

**应对：**
- 请母语者校对
- 重新组织论文结构
- 改善图表质量
- 检查语法和拼写

---

## 六、修改稿提交

### 6.1 修改说明文档

```markdown
# Revision Summary

## Major Changes
1. [修改1]: [原因和位置]
2. [修改2]: [原因和位置]
3. [修改3]: [原因和位置]

## Minor Changes
1. [修改1]: [原因和位置]
2. [修改2]: [原因和位置]

## New Figures/Tables
- Figure X: [说明]
- Table Y: [说明]

## Page/Line References
- Page 5, Line 12: [修改内容]
- Page 8, Table 3: [修改内容]
```

### 6.2 修改稿标注

在修改稿中标注所有修改：
- **删除的内容**: ~~删除线~~ 或 红色字体
- **添加的内容**: **加粗** 或 蓝色字体
- **位置标注**: 在页边距标注 "R1.1" 等审稿意见编号

---

## 七、自查清单

### 提交前
- [ ] 论文格式符合IEEE要求
- [ ] Cover Letter已准备
- [ ] 图表分辨率≥300 DPI
- [ ] 参考文献格式统一
- [ ] 所有作者信息正确
- [ ] 关键词已选择

### 修改稿提交前
- [ ] 所有审稿意见已回复
- [ ] 修改已标注
- [ ] 修改说明文档已准备
- [ ] 新增内容已整合到正文

---

> 来源：IEEE Author Center, ScholarOne Manuscripts
> 更新时间：2026-06-20
