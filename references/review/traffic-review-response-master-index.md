# 交通论文 review-response master index

> 目标：把 `paper-workbench` 中与审稿、rebuttal、revision-order 直接相关的参考统一成一个总入口。
>
> 这个文件不重复展开所有细节，而是负责：
> 1. 先判断当前请求属于哪类 reviewer-facing 任务
> 2. 告诉 skill 先加载哪条 review / rebuttal reference
> 3. 把 reject-risk、evidence gap、response wording、revision order 串成一条最小执行链
> 4. 避免一次性把所有 review 参考全塞进上下文

---

## 1. 这个 index 管什么

当用户请求以下任务时，优先先看本文件：

- 帮我模拟审稿 / 查拒稿风险
- 帮我写 rebuttal / response letter
- 帮我排 revision order
- 帮我检查哪些 claim 会被 reviewer 打
- 帮我准备“baseline 不够强 / 实验不够全 / 图表不说明问题”的回应
- 帮我把 reviewer concern 变成修改动作

本文件只做 review-response 路由和最小决策，不替代具体参考文件。

---

## 2. review-response 路由总图

| 任务类型 | 优先加载 |
|---|---|
| reject risk / adversarial paper review | `references/review/paper-review.md` |
| response letter / rebuttal wording | `references/review/reviewer-response.md` |
| baseline / experiment / figure 相关证据回查 | `references/writing/traffic-experiment-planning-master-index.md` |
| comparator / baseline strength 相关质疑 | `references/writing/traffic-baseline-master-index.md` |
| venue-aware reviewer framing | `references/writing/traffic-cross-venue-patterns.md` |
| T-ITS 特定审稿偏置 | `references/venues/ieee-tits.md` |
| 创新不足 / contribution 不清 / closest prior art 太近 | `references/workflow/innovation-mining-protocol.md` |
| 不确定属于哪类 reviewer-facing 任务 | 先本文件，再按任务分流 |

### 硬规则

1. 不要只写 rebuttal 措辞，而不检查 concern 背后是否真的有证据。
2. 不要把 paper review 和 response letter 混成同一个输出。
3. 不要先写“我们已修改”，再去想具体改了什么。
4. 若 concern 涉及 baseline、experiment、figure、number，先回查对应 planning reference，再写回复。
5. 若 concern 涉及创新不足、与已有工作太像、贡献不清，先回查 `references/workflow/innovation-mining-protocol.md`，明确 closest prior art、novelty threat、rescue route，再写回复。

---

## 3. 六份核心文件的职责分工

### 3.1 `paper-review.md`

负责：

- adversarial 审稿视角的 reject-risk 检查
- contribution / writing / evaluation / method soundness 四类风险
- revision priority 的初步判断
- innovation claim 是否经得住 closest-work 审核

用于：

- 模拟审稿
- 检查哪里最可能被拒
- 输出 revision order 的起点

### 3.2 `reviewer-response.md`

负责：

- response letter 结构
- reviewer comment 分类
- action mapping
- rebuttal / revision letter 的语气与证据格式
- 把 innovation concern 映射成 manuscript change 与 response wording

用于：

- 写逐条回复
- 把 concern 变成 response stance
- 组织修订说明和修改位置

### 3.2.5 `innovation-mining-protocol.md`

负责：

- 创新不足 / 已有工作覆盖 / 贡献不清 这类 concern 的根因回查
- 输出 closest-work clusters、opportunity map、novelty threat、rescue route
- 决定是保留 claim、缩窄 claim、转 contribution 类型，还是放弃 claim

用于：

- reviewer 说“创新不足”
- reviewer 说“和已有工作太像”
- reviewer 说“contribution 不清楚”
- rebuttal 前先判断 concern 是否成立

### 3.3 `traffic-experiment-planning-master-index.md`

负责：

- claim -> baseline -> experiment -> artifact -> provenance -> conclusion sentence
- 回查实验、图表、数字的证据链是否闭合

用于：

- reviewer 质疑实验是否充分
- reviewer 质疑图表是否支撑 claim
- reviewer 质疑数字是否可信

### 3.4 `traffic-baseline-master-index.md`

负责：

- comparator coverage
- baseline family 路由
- “baseline 不够强 / 不够新 / 不够贴 claim” 这类质疑的定位

用于：

- reviewer 质疑 baseline 选择
- rebuttal 中解释为什么这些 comparator 合理

### 3.5 `traffic-cross-venue-patterns.md`

负责：

- 把 reviewer concern 写成 venue-aware 的叙事
- 区分 T-ITS / TVT / TKDE / KDD / NeurIPS / ICML / ICLR 的审稿关注点

用于：

- 调整回复语气和 framing
- 避免用错 venue 的 defense 逻辑

### 3.6 `ieee-tits.md`

负责：

- T-ITS 特定的审稿偏置
- evaluation realism、protocol clarity、robustness、deployment cost、mechanism verification 这些高频 concern

用于：

- T-ITS review / rebuttal
- T-ITS revision order 排序时的优先级判断

---

## 4. 最小 review-response 决策树

### Step 1: 先判当前任务类型

问自己：

1. 现在要做的是 **找问题**，还是 **写回复**？
2. 现在缺的是 **revision order**，还是 **response wording**？
3. concern 指向的是 **claim**、**baseline**、**experiment**、**figure**、还是 **numbers**？

### Step 2: 再判 concern 性质

问自己：

- insufficient contribution 吗？
- weak empirical effect 吗？
- incomplete evaluation 吗？
- baseline not strong enough 吗？
- figure/table not answering the question 吗？
- claim overreach / unclear scope 吗？
- novelty too weak / too close to prior art 吗？
- T-ITS 风格下缺 realism / robustness / deployment cost 吗？

### Step 3: 再判先加载哪条链

- 要找 reject risk -> 先 `paper-review.md`
- 要写 response letter / rebuttal -> 先 `reviewer-response.md`
- concern 指向创新不足 / contribution positioning -> 先补 `innovation-mining-protocol.md`
- concern 指向实验或图表 -> 补 `traffic-experiment-planning-master-index.md`
- concern 指向 baseline -> 补 `traffic-baseline-master-index.md`
- concern 指向 venue 审稿偏置 -> 补 `traffic-cross-venue-patterns.md` 或 `ieee-tits.md`

---

## 5. 统一执行顺序

默认按下面顺序处理交通论文的 review / rebuttal / revision-order 任务：

1. identify venue and task family
2. classify each reviewer concern
3. map each concern to claim / closest prior art / baseline / experiment / figure / number
4. load the primary review-response reference
5. verify whether the paper already has evidence or needs revision
6. if novelty is challenged, decide whether the central claim is covered, crowded but open, or salvageable via rescue route
7. decide action: accept, clarify, soften, add experiment, add reference, reroute contribution, or decline with evidence
8. order revisions by accept/reject risk and implementation cost
9. only then write rebuttal wording or revision summary

### 最小链条

`reviewer concern -> evidence status -> closest prior art / novelty threat -> action -> manuscript change -> response wording -> revision order`

如果中间任何一环缺失，说明回复还没锁定。

---

## 6. revision-order 的默认优先级

默认优先修：

1. **会直接打掉核心 claim 的问题**
   - unsupported contribution
   - closest prior art already covers the central claim
   - wrong or weak experiment evidence
   - missing strong baseline
2. **会让 reviewer 觉得论文不可信的问题**
   - unclear protocol
   - missing provenance
   - figures/tables 不回答问题
3. **会影响 venue fit 的问题**
   - T-ITS 缺 realism / robustness / deployment cost
   - trajectory / demand 任务套错实验模板
4. **会影响可读性但不直接致命的问题**
   - unclear wording
   - paragraph flow
   - contribution bullet phrasing
5. **最后再处理微小措辞和格式问题**

### revision-order 硬规则

- 先修 evidence gap，再修 prose。
- 先修 main table / key figure / abstract overclaim，再修局部句子。
- 若一个 concern 需要新实验，不能用纯文字润色替代。

---

## 7. 典型用户请求 -> 加载策略

### 7.1 “帮我模拟审稿，看看会不会被拒”

加载顺序：

1. `paper-review.md`
2. 若是交通方向，再补 `ieee-tits.md` 或 `traffic-cross-venue-patterns.md`
3. 若 concern 落到实验证据，再补 `traffic-experiment-planning-master-index.md`

### 7.2 “帮我写 rebuttal / response letter”

加载顺序：

1. `reviewer-response.md`
2. 若 concern 是创新不足/贡献不清，再补 `innovation-mining-protocol.md`
3. 若需要判断 concern 是否成立，再补 `paper-review.md`
4. 若要引用实验或图表证据，再补 `traffic-experiment-planning-master-index.md`
5. 若是 baseline 质疑，再补 `traffic-baseline-master-index.md`

### 7.3 “帮我排 revision order”

加载顺序：

1. `paper-review.md`
2. 若涉及 T-ITS 偏置，再补 `ieee-tits.md`
3. 若需要判断实验改动量，再补 experiment-planning master index

### 7.4 “审稿人说 baseline 不够强”

加载顺序：

1. `traffic-baseline-master-index.md`
2. `paper-review.md`
3. 若要写正式回复，再补 `reviewer-response.md`

### 7.5 “审稿人说图表不说明问题 / 实验不够完整”

加载顺序：

1. `traffic-experiment-planning-master-index.md`
2. `paper-review.md`
3. 若要输出逐条回复，再补 `reviewer-response.md`

### 7.6 “审稿人说创新不足 / 和已有工作太像 / contribution 不清楚”

加载顺序：

1. `references/workflow/innovation-mining-protocol.md`
2. `paper-review.md`
3. 若要写正式回复，再补 `reviewer-response.md`
4. 若创新主张需要新实验支撑，再补 `traffic-experiment-planning-master-index.md`

---

## 8. reviewer-friendly 的统一检查框架

无论是哪类交通论文，review-response 包至少回答以下问题：

1. reviewer concern 指向哪条核心 claim？
2. 这个 concern 是真的 evidence gap，还是表达问题？
3. 如果 concern 指向 novelty，closest prior art 是谁？当前 novelty threat 是什么？
4. 现有 paper 中哪一个 section / table / figure 能回答它？
5. 如果答不上来，需要补什么：新实验、重写、删 claim、缩窄 claim、改 contribution 类型、还是加 limitation？
6. 回复里能否给出明确 manuscript anchor？
7. revision order 是否先处理了最伤 acceptance 的问题？

如果有一个问题答不上来，就说明还需要继续加载对应 reference。

---

## 9. 审稿风险快速检查

若出现以下情况，说明 review-response 链没有闭合：

1. rebuttal 语气很完整，但没有实际修改动作
2. revision order 只按写作顺序排，而不是按 reject risk 排
3. baseline 质疑没有回到 comparator coverage
4. 实验质疑没有回到 artifact/provenance
5. reviewer concern 明明成立，却只做措辞防守
6. 创新质疑没有回到 closest prior art / novelty threat / rescue route
7. T-ITS 论文没有回应 realism / robustness / cost / failure boundary
8. response letter 说“已修改”，但找不到 section / figure / table anchor
9. concern 需要新实验，却被错误地降格成 minor wording change

---

## 10. 给 `paper-workbench` 的直接执行提示

当用户提到：

- paper review
- reject risk
- rebuttal
- response letter
- reviewer comments
- revision order
- major revision

先调用本 index 做分流，再决定加载具体 reference。

### 最小执行顺序

1. identify venue and concern type
2. load one primary review-response reference
3. only then load the evidence-checking reference needed for that concern

不要默认一次把 paper-review、reviewer-response、baseline、experiment、venue files 全部加载进上下文。

---

## 11. 最终硬规则

1. review 和 rebuttal 不是一回事，先判任务再输出。
2. 每条 reviewer concern 都要映射到 evidence status 和具体动作。
3. revision order 必须按 accept/reject 风险排，不按章节顺序排。
4. 若 concern 指向实验、baseline、figure 或数字，必须先回查对应 reference 再写回复。
5. 若 concern 指向创新不足、已有工作覆盖或 contribution 不清，必须先明确 closest prior art、novelty threat、rescue route。
6. T-ITS 审稿应对默认强调 realism、protocol clarity、robustness、deployment cost、mechanism verification。
7. 当用户只问 review/rebuttal 时，优先加载本 index + 当前最关键的一条 review-response reference，不要把所有审稿参考一起塞进上下文。
