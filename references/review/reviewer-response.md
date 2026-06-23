# 审稿回复信指南

借鉴 nature-response 的结构化回复流程，适配 IEEE Transactions 审稿。

## 核心原则

审稿回复信是"面向编辑的验证文档"，不是辩护书。

---

## 回复结构

### 开头

```
Dear Editor and Reviewers,

We sincerely thank the Editor and Reviewers for their constructive comments
and suggestions, which have significantly improved the quality of this manuscript.
Below, we provide a point-by-point response to each comment.

[Revision summary paragraph: major changes overview]
```

### 逐条回复格式

```
\textbf{Reviewer 1, Comment 1:}
``[Original comment text]''

\textbf{Response:}
[Your response text]

[Concrete evidence: page/line/figure/table changes]

\textit{[In the revised manuscript, the corresponding changes are highlighted in blue.]}
```

### 结尾

```
We believe that the revised manuscript has been substantially improved based
on the Reviewers' valuable comments. We hope that the revised manuscript is
now suitable for publication in [Journal Name].
```

---

## 评论分类

| 类型 | 说明 | 回复策略 |
|------|------|----------|
| Factual error | 审稿人指出事实错误 | 承认并修正，或礼貌解释为什么正确 |
| Missing content | 缺少内容（实验、分析、引用） | 补充并说明在何处添加 |
| Clarity issue | 表述不清 | 重写并提供新文本 |
| Disagreement | 学术观点分歧 | 提供证据支持你的立场，尊重对方 |
| Suggestion | 建议性意见 | 采纳或解释为什么不采纳 |
| Minor edit | 小修改 | 直接修改，简短确认 |

---

## 动作映射

| 动作 | 说明 |
|------|------|
| ACCEPT_TEXT | 直接采纳审稿人建议的文本 |
| ACCEPT_ANALYSIS | 采纳分析建议，补充实验 |
| SOFTEN_CLAIM | 弱化过度声明 |
| CLARIFY | 重写不清晰的段落 |
| ADD_EXPERIMENT | 补充新实验 |
| ADD_REFERENCE | 补充引用 |
| AUTHOR_INPUT_NEEDED | 需要作者提供额外信息 |
| DECLINE_WITH_EVIDENCE | 礼貌拒绝，提供证据 |

---

## 回复原则

### 态度

- 合作、尊重、感谢
- 不要对抗或防御
- 不要暗示审稿人误解了论文

### 证据

- 每条回复引用具体修改位置（Section/Page/Line/Figure/Table）
- 修改必须实际存在于修订稿中
- 不要编造未做的修改

### 格式

- 每条评论有唯一 ID（Reviewer X, Comment Y）
- 回复和原文修改分开标注
- 修订稿中的修改用蓝色高亮

---

## 困难情况处理

### 审稿人之间矛盾

- 分别回复每位审稿人
- 如果建议冲突，在回复中说明你如何权衡
- 请编辑做最终决定

### 不可能的实验

- 说明为什么无法执行（资源/数据/伦理限制）
- 提供替代验证（理论分析、小规模实验、引用相关工作）
- 不要忽略或假装没看到

### 缺少证据的 Major Revision

- 诚实说明当前证据的局限
- 补充力所能及的实验
- 明确说明哪些是新补充的，哪些需要未来工作

---

## 真实审稿回复示例

### 示例1：Baseline不足

**审稿人意见：**
> "The paper only compares with 3 baselines. Please include more recent methods like STAEformer and PDFormer."

**回复：**
> "We thank the reviewer for this suggestion. We have added STAEformer and PDFormer as additional baselines in Table 2. The results show that our method outperforms STAEformer by 2.3% MAE on METR-LA and PDFormer by 1.8% MAE on PEMS-BAY. We have also added a discussion of these methods in Section 4.2."

**关键技巧：**
- 感谢审稿人
- 说明具体修改
- 提供新的实验结果
- 引用修改位置

### 示例2：消融实验不足

**审稿人意见：**
> "The ablation study is incomplete. Please show the contribution of each component."

**回复：**
> "We have expanded the ablation study in Table 3 to include all key components. Removing the attention module reduces MAE by 3.2% on METR-LA, removing the graph convolution reduces MAE by 2.1%, and removing the temporal attention reduces MAE by 1.5%. These results demonstrate that all components contribute to the final performance."

**关键技巧：**
- 说明具体修改
- 提供量化结果
- 解释各组件贡献

### 示例3：写作不清晰

**审稿人意见：**
> "The method section is hard to follow. Please improve the clarity."

**回复：**
> "We have revised Section 3 to improve clarity. Specifically, we added a pipeline figure (Figure 2) to illustrate the overall architecture, added motivation sentences at the beginning of each subsection, and improved the flow between subsections. We hope the revised version is clearer."

**关键技巧：**
- 说明具体改进措施
- 引用修改位置
- 表达希望改进的意愿

### 示例4：数据集不足

**审稿人意见：**
> "The experiments only use 2 datasets. Please evaluate on more datasets."

**回复：**
> "We have added experiments on PeMS04 and PeMS08 datasets in Table 4. The results show that our method achieves consistent improvements across all 4 datasets: 2.3% MAE reduction on METR-LA, 1.8% on PEMS-BAY, 2.1% on PeMS04, and 1.9% on PeMS08."

**关键技巧：**
- 说明新增数据集
- 提供所有数据集的结果
- 强调一致性

### 示例5：理论分析不足

**审稿人意见：**
> "The paper lacks theoretical analysis. Please provide theoretical justification."

**回复：**
> "We have added Theorem 1 in Section 3.2, which proves that our attention mechanism has O(N log N) complexity. The proof is provided in Appendix A. We have also added a discussion of the theoretical implications in Section 5."

**关键技巧：**
- 说明新增理论内容
- 引用定理和证明位置
- 讨论理论意义

## 检查清单

- [ ] 每条评论都有 ID 和回复
- [ ] 回复映射到具体修改位置
- [ ] 修改实际存在于修订稿
- [ ] 没有编造实验、分析或引用
- [ ] 态度合作、尊重
- [ ] 分歧有证据支持
- [ ] 蓝色高亮标记所有修改
