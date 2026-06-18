# 交通论文 writing-execution master index

> 目标：把 `paper-workbench` 中与 section writing、section rewrite、polish 直接相关的参考统一成一个总入口。
>
> 这个文件不重复展开所有细节，而是负责：
> 1. 先判断当前请求属于哪类写作执行任务
> 2. 告诉 skill 先加载哪条 section / writing / polishing reference
> 3. 把 section goal、outline、draft、clarity、polish 串成一条最小执行链
> 4. 避免一次性把所有写作参考全塞进上下文

---

## 1. 这个 index 管什么

当用户请求以下任务时，优先先看本文件：

- 帮我写某一节
- 帮我重写摘要 / 引言 / related work / method / experiments / conclusion
- 帮我润色一段 / 一节 / 全文
- 帮我把已有材料扩成正式 prose
- 帮我检查段落是否清晰、流畅、像论文
- 帮我把 T-ITS / IEEE 风格真正落到段落级写作上

本文件只做 writing-execution 路由和最小决策，不替代具体参考文件。

---

## 2. writing-execution 路由总图

| 任务类型 | 优先加载 |
|---|---|
| 摘要 / 引言 / related work / method / experiments / conclusion 重写 | `references/sections/<target-section>.md` |
| IEEE / T-ITS prose drafting | `references/writing/ieee-expression-patterns.md` |
| paragraph flow / clarity / transition | `references/writing/paragraph-clarity.md` |
| 全段/全文 polish | `references/writing/ieee-polishing.md` |
| traffic / ITS 任务专项结果叙事 | `references/writing/traffic-writing-patterns.md` |
| trajectory / demand 专项叙事 | `references/writing/trajectory-demand-patterns.md` |
| 不确定属于哪类 section-writing 任务 | 先本文件，再按任务分流 |

### 硬规则

1. 不要在没有 section goal 和 evidence boundary 时直接写终稿式正文。
2. 不要把 rewrite 和 polish 混成同一个动作。
3. 不要只做措辞替换，而不调整段落逻辑和 claim-evidence 对齐。
4. 若用户给的是已有段落，先判是要重构逻辑，还是只做语言 polish。

---

## 3. 六类核心文件的职责分工

### 3.1 `references/sections/*.md`

负责：

- 各 section 的目标、常见结构、应写什么不应写什么
- abstract / introduction / related work / method / experiments / conclusion 的局部 spine

用于：

- 写具体 section
- 重写某一节
- 先锁 section goal 与 mini-outline

### 3.2 `ieee-expression-patterns.md`

负责：

- IEEE Transactions 风格下的贡献句、过渡句、结果句、总结句表达骨架
- 把段落写成 reviewer-friendly 的正式学术 prose

用于：

- 把大纲扩成 IEEE prose
- 重写句子时保持 IEEE 风格一致

### 3.3 `paragraph-clarity.md`

负责：

- 外部读者视角的段落清晰度检查
- topic sentence、reverse outline、transition 关系检查

用于：

- 用户问“通不通顺、流不流畅、清不清楚”
- rewrite 后做 paragraph-level clarity audit

### 3.4 `ieee-polishing.md`

负责：

- 12-step polish 流程
- tense audit、template check、overclaim detection、caption style、house style

用于：

- 已有 draft 的语言精修
- section polish 或 full-manuscript polish
- rewrite 完成后的 final cleanup

### 3.5 `traffic-writing-patterns.md`

负责：

- traffic / ITS 论文的 intro tension、results narration、contribution framing、failure boundary 表达
- 更偏 T-ITS / TVT 风格的段落叙事

用于：

- 把通用 IEEE prose 改成交通任务更自然的写法
- 尤其是 introduction、results、conclusion 的交通 grounding

### 3.6 `trajectory-demand-patterns.md`

负责：

- trajectory prediction 与 demand forecasting 的专项叙事
- multi-modal / interaction / map / region heterogeneity / event sensitivity 这些局部逻辑

用于：

- trajectory / demand 论文的 section rewrite
- 避免直接套 traffic flow forecasting 的默认 prose 模板

---

## 4. 最小 writing-execution 决策树

### Step 1: 先判当前任务类型

问自己：

1. 这是 **从零起草**、**重写**，还是 **polish**？
2. 这是 **单段**、**单节**，还是 **多节连动**？
3. 这是通用 IEEE 写作，还是 traffic / trajectory / demand 专项任务？

### Step 2: 再判当前最缺什么

问自己：

- 缺 section goal 吗？
- 缺 mini-outline 吗？
- 缺 IEEE prose pattern 吗？
- 缺 paragraph flow 吗？
- 缺 overclaim / tense / style cleanup 吗？

### Step 3: 再判先加载哪条链

- 不知道这一节该写什么 -> 先 `references/sections/<target-section>.md`
- 已有提纲，要扩成正式 prose -> 先 `ieee-expression-patterns.md`
- 已有 draft，但逻辑不清 -> 补 `paragraph-clarity.md`
- 已有 draft，主要做语言与风格精修 -> 先 `ieee-polishing.md`
- 属于 traffic / ITS 结果或引言叙事 -> 补 `traffic-writing-patterns.md`
- 属于 trajectory / demand 专项任务 -> 补 `trajectory-demand-patterns.md`

---

## 5. 统一执行顺序

默认按下面顺序执行写作任务：

1. identify section and task family
2. lock section goal
3. build mini-outline or paragraph role list
4. confirm claim-evidence boundary
5. draft or rewrite the prose
6. run paragraph clarity check
7. run IEEE polish pass
8. only then output final section text

### 最小链条

`section goal -> mini-outline -> claim/evidence boundary -> draft -> clarity -> polish`

如果中间任何一环缺失，说明写作还没锁定。

---

## 6. rewrite 与 polish 的分工

### 6.1 什么时候算 `rewrite`

属于以下情况时，优先按 rewrite 处理：

- 段落主旨不清
- 结构顺序不对
- claim 与 evidence 对不上
- 这一节写成了别的论文类型或别的 venue 风格
- 需要换 section spine，而不是只修句子

输出重点：

1. section goal
2. mini-outline
3. revised text
4. claim-evidence map
5. revision risks

### 6.2 什么时候算 `polish`

属于以下情况时，优先按 polish 处理：

- 结构基本正确
- 只是句子重、时态乱、过渡硬、措辞模板化
- 需要 IEEE / T-ITS 风格一致性
- 需要 overclaim cleanup

输出重点：

1. polished text
2. wording-level changes
3. remaining overclaim / evidence risks

### 硬规则

- 结构错了，不要假装 polish 就够。
- 证据没锁定，不要用华丽措辞掩盖。

---

## 7. 典型用户请求 -> 加载策略

### 7.1 “帮我重写 introduction”

加载顺序：

1. `references/sections/introduction.md`
2. `ieee-expression-patterns.md`
3. 若是 traffic / T-ITS，再补 `traffic-writing-patterns.md`
4. 重写后用 `paragraph-clarity.md` 做检查
5. 最后用 `ieee-polishing.md` 做精修

### 7.2 “帮我润色 abstract”

加载顺序：

1. `references/sections/abstract.md`
2. `ieee-polishing.md`
3. 若摘要里有结果数字，再确保它们已过 provenance

### 7.3 “帮我写 experiments section”

加载顺序：

1. `references/sections/experiments.md`
2. 若实验包未锁定，先回到 `traffic-experiment-planning-master-index.md`
3. `ieee-expression-patterns.md`
4. `traffic-writing-patterns.md`
5. `ieee-polishing.md`

### 7.4 “帮我把 related work 写得更像顶刊”

加载顺序：

1. `references/sections/related-work.md`
2. 若 baseline 家族没锁定，先回到 `traffic-baseline-master-index.md`
3. `ieee-expression-patterns.md`
4. 若要压 venue 风格，再补 `traffic-cross-venue-patterns.md`

### 7.5 “帮我看这一段顺不顺”

加载顺序：

1. `paragraph-clarity.md`
2. 若只是措辞问题，再补 `ieee-polishing.md`

### 7.6 “帮我改 trajectory / demand 的结果分析”

加载顺序：

1. `trajectory-demand-patterns.md`
2. `references/sections/experiments.md`
3. `ieee-expression-patterns.md`
4. `ieee-polishing.md`

---

## 8. reviewer-friendly 的统一检查框架

无论是哪类写作任务，最终至少回答以下问题：

1. 这一节的唯一核心目标是什么？
2. 每段分别承担什么功能？
3. 这一节的 claim 是否都能追溯到 evidence？
4. 读者能否在第一句或前两句看出段落在做什么？
5. 这次任务需要 rewrite，还是只需要 polish？
6. 是否已经去掉空泛 praise、模板贡献句和 scope inflation？

如果有一个问题答不上来，就说明还需要继续加载对应 reference。

---

## 9. 写作风险快速检查

若出现以下情况，说明 writing-execution 链没有闭合：

1. 段落句子很顺，但 claim-evidence 对不上
2. 语言像 IEEE，但 section spine 不对
3. 只做同义替换，没有改逻辑结构
4. abstract / intro 写得很满，但 evidence boundary 不清
5. trajectory / demand 结果分析还在套 traffic flow 模板
6. traffic / T-ITS 论文没有交代场景、代价、失效边界
7. rewrite 后没有做 clarity audit
8. polish 后仍然保留 overclaim 或 AI 模板句

---

## 10. 给 `paper-workbench` 的直接执行提示

当用户提到：

- section writing
- rewrite this section
- polish this paragraph
- make it more IEEE
- make it more T-ITS
- improve flow / clarity

先调用本 index 做分流，再决定加载具体 reference。

### 最小执行顺序

1. identify section and task type
2. load one primary writing reference
3. only then load the supporting clarity / polish / task-specific reference

不要默认一次把 section、expression、clarity、polish、traffic、trajectory 参考全部加载进上下文。

---

## 11. 最终硬规则

1. section writing、rewrite、polish 不是一回事，先判任务再执行。
2. 每次写作都要先锁定 section goal，而不是直接改句子。
3. rewrite 必须改逻辑和证据对齐，polish 只在结构已基本成立时做。
4. traffic、trajectory、demand 三类任务默认不用同一套 prose 模板。
5. 当用户只问写作执行时，优先加载本 index + 当前最关键的一条写作 reference，不要把所有写作参考一起塞进上下文。
