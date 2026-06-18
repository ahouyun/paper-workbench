# traffic-paper-workbench master router

> 目标：把 `paper-workbench` 中面向 traffic / ITS / spatiotemporal / trajectory / demand 论文的四个总入口再统一成一个顶层路由。
>
> 这个文件不重复展开所有细节，而是负责：
> 1. 先判断用户当前是在做 baseline、experiment、review，还是 writing
> 2. 告诉 skill 优先加载哪一个 master index
> 3. 把 claim-evidence-artifact-review 这条总链压成一个最小执行顺序
> 4. 避免一次性把所有 traffic 参考全塞进上下文

---

## 1. 这个 router 管什么

当用户请求以下任务时，优先先看本文件：

- 帮我做 traffic / ITS / ST / trajectory / demand 方向论文
- 帮我挑 baseline、设计实验、规划图表、写 section、做 paper review
- 帮我按 T-ITS 风格推进整篇论文
- 帮我准备 submission package 或 revision package
- 我不知道下一步该先补 baseline、实验、写作还是 rebuttal

本文件只做顶层 traffic-paper-workbench 路由和最小决策，不替代下游 master index。

---

## 2. 四个下游总入口

| 工作类型 | 先加载 |
|---|---|
| baseline / comparator / related-work baseline framing | `references/writing/traffic-baseline-master-index.md` |
| experiment / figure / table / provenance / artifact planning | `references/writing/traffic-experiment-planning-master-index.md` |
| paper review / reject risk / rebuttal / revision order | `references/review/traffic-review-response-master-index.md` |
| section writing / rewrite / polish / prose execution | `references/writing/traffic-writing-execution-master-index.md` |

### 顶层硬规则

1. 不要还没判任务类型就直接加载多个 master index。
2. 不要把 baseline、experiment、review、writing 当成同一步。
3. 若用户请求跨多步，先锁当前最急需的交付物，再只加载一个 primary router。
4. 只有当当前 router 明确缺一环时，才补加载相邻 router。

---

## 3. 顶层任务分流图

### A. baseline router

用户在问：

- 该和谁比
- baseline 是否够强
- related work 该写哪些方法家族
- 主表 comparator 是否合理

先加载：
`references/writing/traffic-baseline-master-index.md`

### B. experiment-planning router

用户在问：

- 实验包怎么设计
- Figure 1 / Table I / case study 怎么规划
- 哪个 claim 需要哪个实验
- 哪些数字能不能写进摘要/引言/结果

先加载：
`references/writing/traffic-experiment-planning-master-index.md`

### C. review-response router

用户在问：

- 会不会被拒
- reviewer 会打哪里
- rebuttal 怎么写
- revision order 怎么排

先加载：
`references/review/traffic-review-response-master-index.md`

### D. writing-execution router

用户在问：

- 某一节怎么写
- 某段怎么重写
- prose 怎么更像 IEEE / T-ITS
- 全文怎么 polish

先加载：
`references/writing/traffic-writing-execution-master-index.md`

---

## 4. 最小顶层决策树

### Step 1: 先判当前要交付什么

问自己：

1. 用户当前要的是 **选对手**、**补实验**、**过审稿**，还是 **写正文**？
2. 用户是要 **解决问题定位**，还是 **直接输出成文结果**？
3. 当前最缺的是 **comparator**、**artifact**、**response strategy**，还是 **prose**？

### Step 2: 再判当前卡在哪一环

问自己：

- claim 还没落到 baseline 吗？
- baseline 已定，但 experiment/figure 没锁吗？
- 实验包有了，但 prose 没写好吗？
- 论文写出来了，但 reviewer-facing defense 没准备好吗？

### Step 3: 再判是否需要相邻 router

- baseline 定不下来 -> 先 baseline router
- baseline 已有，但实验没闭环 -> 补 experiment router
- 实验已闭环，但写作不稳 -> 补 writing router
- draft 已成型，但要找 reject risk / rebuttal -> 补 review router

---

## 5. 统一总执行顺序

默认按下面顺序推进 traffic paper：

1. identify task family and venue bias
2. identify current deliverable
3. load one primary master router
4. lock claim-evidence-artifact relation for the current task
5. only then load adjacent router if the chain is incomplete
6. produce the requested output

### traffic paper 的总链条

`claim -> baseline -> experiment -> artifact -> prose -> review/rebuttal`

### 使用原则

- 用户只问其中一环时，不默认展开全链。
- 用户问整篇推进时，优先按上面链条排序，但仍分阶段执行。
- 任何一环没锁定时，不跳到终稿式 polish 或防守式 rebuttal。

---

## 6. 典型用户请求 -> 顶层加载策略

### 6.1 “帮我做一篇 T-ITS traffic forecasting 论文”

加载顺序：

1. 本 router
2. 若先问 baseline -> `traffic-baseline-master-index.md`
3. 若先问实验包 -> `traffic-experiment-planning-master-index.md`
4. 若先问写作 -> `traffic-writing-execution-master-index.md`
5. 若先问审稿风险 -> `traffic-review-response-master-index.md`

### 6.2 “帮我把这篇 trajectory paper 往 submission 推”

加载顺序：

1. 本 router
2. 优先看当前缺的是 baseline、experiment、writing 还是 review
3. 按当前短板只进一个 primary router

### 6.3 “帮我看下一步先补什么”

优先判断：

1. claim 有没有 comparator
2. comparator 有没有实验问题
3. 实验有没有 artifact
4. artifact 有没有 prose
5. prose 有没有 reviewer-facing defense

然后把用户路由到最先缺失的那一环。

### 6.4 “帮我准备 revision package”

加载顺序：

1. 本 router
2. `traffic-review-response-master-index.md`
3. 若 concern 指向实验或 baseline，再补对应 master index
4. 若 concern 指向段落重写，再补 writing-execution master index

---

## 7. router 之间的边界

### baseline router 负责什么

- 选谁来比
- comparator 是否覆盖 claim
- related work / result framing 中 baseline 家族是否完整

### experiment router 负责什么

- 怎么把 claim 变成 benchmark、ablation、figure、table、provenance

### writing router 负责什么

- 怎么把已锁定的材料写成 section-level prose

### review router 负责什么

- 怎么从 reviewer 视角找缺口、排修改优先级、写 response

### 边界硬规则

- 不要让 writing router 替 baseline 做 comparator 决策。
- 不要让 review router 替 experiment router 发明证据。
- 不要让 experiment router 代替 writing router 生成终稿 prose。
- 不要让 baseline router 代替 review router 判断 rebuttal 语气。

---

## 8. 顶层风险快速检查

若出现以下情况，说明顶层路由错了：

1. 用户要写 intro，却先把 baseline / experiment / review 全部展开
2. 用户要 rebuttal，却没有先确认 evidence status
3. 用户要设计实验，却直接进入 prose polishing
4. 用户要挑 baseline，却先讨论 wording
5. 用户问“下一步做什么”，却没有先判断当前卡在哪一环
6. T-ITS 论文写作时没有优先考虑交通场景、约束、鲁棒性、代价、失效边界

---

## 9. 给 `paper-workbench` 的直接执行提示

当用户提到：

- traffic paper
- T-ITS paper
- spatiotemporal forecasting paper
- trajectory paper
- demand forecasting paper
- submission package
- revision package
- what should I do next

先调用本 router 做顶层分流，再决定进入哪一个下游 master index。

### 最小执行顺序

1. identify task family and current deliverable
2. load this top-level router
3. route to one primary downstream master index
4. only then load adjacent router if needed

不要默认一次把四个 master index 全部加载进上下文。

---

## 10. 最终硬规则

1. 先判任务环节，再选 router。
2. 当前只缺哪一环，就优先只进哪一个 master index。
3. `claim -> baseline -> experiment -> artifact -> prose -> review/rebuttal` 是默认总链，但不是每次都要全跑。
4. T-ITS / traffic / trajectory / demand 任务都应优先通过本 router 分流，避免混用下游参考。
5. 当用户只说“继续”或“下一步”，默认先用本 router 判断当前最缺的环节，而不是直接进入写作或润色。
