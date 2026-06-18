# Nature 润色规则

## 核心原则

### 1. 简洁优先 (Conciseness First)

**目标**：删除冗余，保留核心信息

**策略**：
- 删除不必要的修饰词
- 合并重复表达
- 使用主动语态
- 简化复杂句式

### 2. 清晰表达 (Clear Expression)

**目标**：让读者快速理解

**策略**：
- 使用具体词汇
- 避免专业术语堆砌
- 逻辑结构清晰
- 段落主题明确

### 3. 风格统一 (Consistent Style)

**目标**：保持 Nature 风格

**策略**：
- 英式英语拼写
- 时态使用正确
- 对冲校准恰当
- 格式规范统一

---

## 12 步润色流程

### Step 1: 句子拆分

**目标**：将长句拆分为短句

**规则**：
- 每句 ≤30 词
- 一个句子一个观点
- 避免嵌套从句

**示例**：
```
❌ It is important to note that the results of our experiment, which was conducted 
   under controlled conditions, clearly demonstrate the effectiveness of our approach.
✅ Our controlled experiments show that our approach is effective.
```

### Step 2: 章节识别

**目标**：识别当前章节，应用对应规则

**章节类型**：
- Abstract: 简洁，无引用
- Introduction: 背景 → 问题 → 解决方案
- Methods: 过去时，详细
- Results: 过去时，客观
- Discussion: 现在时，解释意义

### Step 3: 时态审计

**目标**：检查时态使用是否正确

**规则**：
- Abstract: 过去时（描述本文发现）
- Introduction: 现在时（背景）+ 过去时（具体研究）
- Methods: 过去时
- Results: 过去时
- Discussion: 现在时（解释）+ 过去时（引用本文）

### Step 4: 词汇升级

**目标**：替换 AI 特征词汇

**替换表**：
| 原词 | 替换词 |
|------|--------|
| additionally | also, and |
| crucial | important, essential |
| delve | explore, examine |
| emphasize | highlight, stress |
| enhance | improve, increase |
| foster | promote, encourage |
| garner | gain, receive |
| highlight | show, indicate |
| interplay | interaction, relationship |
| intricate | complex, detailed |
| key | main, important |
| landscape | field, area |
| pivotal | important, crucial |
| showcase | show, demonstrate |
| tapestry | fabric, structure |
| testament | evidence, proof |
| underscore | highlight, emphasize |
| valuable | useful, important |
| vibrant | active, lively |

### Step 5: 模板检查

**目标**：删除模板化表达

**常见模板**：
```
❌ In recent years, ... has attracted increasing attention.
❌ Despite significant progress, ... remains challenging.
❌ It is well known that...
❌ As we all know...
```

**替换**：
```
✅ [直接陈述具体问题]
✅ [具体说明挑战]
✅ [引用具体研究]
✅ [删除]
```

### Step 6: 引用审计

**目标**：检查引用格式和完整性

**规则**：
- 作者+年份格式 (Smith et al., 2024)
- DOI 必需
- 数量符合限制
- 无自引过多

### Step 7: 内部风格

**目标**：检查内部风格一致性

**检查项**：
- 术语一致
- 缩写定义
- 格式统一
- 标点正确

### Step 8: 校对

**目标**：检查语法和拼写

**检查项**：
- 语法错误
- 拼写错误
- 标点错误
- 格式错误

### Step 9: 英式英语

**目标**：确保英式英语拼写

**常见差异**：
| 美式 | 英式 |
|------|------|
| color | colour |
| analyze | analyse |
| program | programme |
| signaling | signalling |
| modeling | modelling |
| behavior | behaviour |
| favor | favour |
| honor | honour |
| organize | organise |
| recognize | recognise |

### Step 10: 对冲校准

**目标**：检查对冲语言是否恰当

**规则**：
- 强证据：show, demonstrate, establish
- 中等证据：suggest, indicate, support
- 弱证据：may, could, might
- 推测：speculate, hypothesize, propose

### Step 11: 纯文本输出

**目标**：输出纯文本，无格式标记

**规则**：
- 删除 markdown 标记
- 保留段落结构
- 统一标点符号

### Step 12: 最终检查

**目标**：最终质量检查

**检查项**：
- 每句 ≤30 词
- 无 AI 特征词汇
- 时态正确
- 对冲恰当
- 风格统一

---

## 常见问题修复

### 1. 句子过长

**问题**：句子超过 30 词

**解决**：
- 拆分为多个句子
- 删除冗余信息
- 简化复杂结构

**示例**：
```
❌ The results of our experiments, which were conducted under carefully controlled 
   conditions and involved multiple replicates, clearly demonstrate that our approach 
   is superior to existing methods.
✅ Our controlled experiments show that our approach outperforms existing methods. 
   We performed multiple replicates to ensure reliability.
```

### 2. AI 特征词汇

**问题**：使用 AI 常用词汇

**解决**：
- 替换为具体词汇
- 删除不必要的修饰
- 使用简单表达

**示例**：
```
❌ Our novel approach leverages cutting-edge techniques to showcase...
✅ We use [specific technique] to show...
```

### 3. 模板化表达

**问题**：使用模板化开头

**解决**：
- 直接陈述问题
- 使用具体数据
- 避免空泛表达

**示例**：
```
❌ In recent years, deep learning has attracted increasing attention.
✅ Deep learning has improved image classification accuracy by 15% since 2020.
```

### 4. 对冲过度

**问题**：对冲语言过多

**解决**：
- 删除不必要的对冲
- 匹配证据强度
- 保持自信但不夸张

**示例**：
```
❌ It might possibly be the case that our results could potentially suggest...
✅ Our results suggest...
```

### 5. 对冲不足

**问题**：对冲语言不足

**解决**：
- 添加适当对冲
- 匹配证据强度
- 避免过度自信

**示例**：
```
❌ Our results prove that X causes Y.
✅ Our results suggest that X may contribute to Y.
```

---

## 章节特化规则

### Abstract

**长度**：≤150 词

**结构**：
1. 背景和问题（1-2句）
2. 方法（1句）
3. 主要发现（2-3句）
4. 意义（1句）

**规则**：
- 无引用
- 无缩写（首次出现除外）
- 简洁有力

### Introduction

**长度**：3-5 段

**结构**：
1. 广泛背景
2. 具体问题
3. 现有研究空白
4. 本文解决方案
5. 本文贡献

**规则**：
- 倒金字塔结构
- 逻辑清晰
- 引用适当

### Methods

**长度**：根据需要

**结构**：
1. 实验设计
2. 材料和样本
3. 实验步骤
4. 数据分析

**规则**：
- 过去时
- 详细可重复
- 统计方法明确

### Results

**长度**：3-5 段

**结构**：
1. 核心发现
2. 支持证据
3. 统计分析

**规则**：
- 过去时
- 客观描述
- 数据支持

### Discussion

**长度**：4-6 段

**结构**：
1. 主要发现解释
2. 与现有研究比较
3. 机制解释
4. 局限性
5. 未来方向
6. 结论

**规则**：
- 现在时（解释）
- 过去时（引用本文）
- 对冲恰当

---

## 自检清单

### 语言检查

- [ ] 每句 ≤30 词
- [ ] 无 AI 特征词汇
- [ ] 无模板化表达
- [ ] 简单词汇优先
- [ ] 主动语态为主

### 风格检查

- [ ] 英式英语拼写
- [ ] 时态使用正确
- [ ] 对冲校准恰当
- [ ] 格式规范统一

### 内容检查

- [ ] 逻辑清晰
- [ ] 段落主题明确
- [ ] 过渡自然
- [ ] 引用适当

### 质量检查

- [ ] 无语法错误
- [ ] 无拼写错误
- [ ] 无标点错误
- [ ] 无格式错误
