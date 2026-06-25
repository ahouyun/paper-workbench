# 段落清晰度检查

当用户询问段落是否"流畅"或"清晰"时使用。

## 快速检查

### 1. 外部读者视角

- 这段有一个明确的信息吗？
- 第一句是否说明了这段要做什么？
- 所有名词/术语是否无需隐藏上下文即可理解？
- 每句是否与前一句有明确关系（因果、对比、结果、细化、举例）？

### 2. 反向大纲

写完后提取：
- 论文/主要论点
- 每段主题句
- 每段下的论据/解释点

检查映射：主题句 → 论点，论据 → 主题句。修改或删除无法清晰映射的段落。

### 3. 添加临时标题

如果流畅度仍然较弱，在修改期间添加临时章节标题和显式过渡短语，定稿前移除不必要的标题。

### 4. 过渡词使用

按功能分类：

| 功能 | 过渡词 |
|------|--------|
| 因果 | therefore, consequently, as a result, thus |
| 比较 | likewise, similarly, in the same way |
| 对比 | however, nevertheless, on the other hand, conversely |
| 举例 | for instance, indeed, specifically, in particular |
| 递进 | furthermore, moreover, in addition, additionally |
| 时间 | eventually, meanwhile, subsequently, thereafter |
| 总结 | in short, to summarize, in conclusion, overall |

## 中文过渡词

| 避免 | 推荐 |
|------|------|
| 首先、其次、最后 | 直接陈述，或「一方面…另一方面」 |
| 此外 | 同时、与之相伴、另外 |
| 综上所述 | 总体而言、概括来说 |
| 由此可见 | 这意味着、这说明 |

## 论文段落特定模式

### Method 段落
1. 开头：模块目的
2. 中间：设计细节
3. 结尾：输出及其在流水线中的作用

### Results 段落
1. 开头：发现
2. 中间：证据（指标/表格/图表）
3. 上下文：与基线对比
4. 简要解释

### Introduction 段落
1. 广泛背景 → 具体缺口 → 提出方案（漏斗结构）

## 跨节一致性检查

- [ ] Introduction 的承诺是否在 Method 中兑现？
- [ ] Method 的每个模块是否在 Experiments 中有消融验证？
- [ ] Conclusion 是否只讨论了 Experiments 中展示的结果？
- [ ] Related Work 识别的缺口是否在 Method 中解决？
- [ ] 所有技术术语是否全文一致？

## 段落质量诊断清单

### 信息密度检查
- [ ] 每段是否只有一个核心信息？
- [ ] 是否有空洞的填充句？
- [ ] 是否有重复表达同一意思的句子？
- [ ] 是否有与主题无关的细节？

### 逻辑连贯性检查
- [ ] 句子之间的逻辑关系是否清晰？
- [ ] 是否有逻辑跳跃？
- [ ] 是否有因果关系不明确的推论？
- [ ] 是否有前提未交代的结论？

### 语言简洁性检查
- [ ] 是否有冗余的修饰词？
- [ ] 是否有可以简化的长句？
- [ ] 是否有被动语态可以改为主动语态？
- [ ] 是否有抽象表达可以改为具体表达？

## 常见段落问题及修复

### 问题1：信息密度过低
**症状：** 一段话读完后感觉什么都没说
**原因：** 填充句过多，核心信息被稀释
**修复：** 删除填充句，保留核心信息

**Before:**
> "In recent years, deep learning has attracted increasing attention in various fields. Many researchers have proposed various methods to solve this problem. These methods have achieved some results. However, there are still some challenges."

**After:**
> "Deep learning methods for traffic prediction face three challenges: (1) capturing long-range temporal dependencies, (2) modeling dynamic spatial correlations, and (3) handling missing data."

### 问题2：逻辑跳跃
**症状：** 句子之间缺乏逻辑连接
**原因：** 缺少过渡词或逻辑连接词
**修复：** 添加过渡词或重组句子

**Before:**
> "Our method uses attention mechanisms. The results show improvement."

**After:**
> "Our method uses attention mechanisms to capture long-range dependencies. As a result, the results show a 5% improvement in accuracy."

### 问题3：被动语态过多
**症状：** 句子显得生硬、不自然
**原因：** 被动语态过度使用
**修复：** 适当改为主动语态

**Before:**
> "The data was collected. The model was trained. The results were analyzed."

**After:**
> "We collected the data from three sources. We trained the model using Adam optimizer. We analyzed the results using statistical tests."
