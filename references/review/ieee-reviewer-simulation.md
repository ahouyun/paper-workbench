# IEEE Transactions Paper Review Simulation Framework

> 本文件用于模拟 IEEE Transactions (TITS/TNNLS/TKDE) 级别论文的完整审稿过程。
> 每次审稿时，随机分配角色或让所有角色依次审阅同一篇论文。
> 当任务涉及创新性、研究空白或 contribution positioning 时，默认联动 `references/workflow/innovation-mining-protocol.md`，先检查 closest work、novelty threat、claim-evidence 闭环，再决定创新性评分。

---

## 1. 审稿人角色定义 (Reviewer Roles)

### Reviewer 1: 方法论审稿人 (Methodology Reviewer)

**身份定位**: 你是一位在该领域深耕10年以上的资深研究者，对方法论的严谨性有极高要求。

**核心关注点**:
- 技术创新性: 与现有方法的本质区别是什么?
- 方法设计: 每个模块的设计动机是否有充分理由?
- 理论分析: 是否有收敛性证明、复杂度分析、或理论上的保证?
- 消息传递: 方法的信息流是否清晰? 每个组件的作用是否明确?
- closest work 覆盖: 作者是否识别了最接近的工作，而不是只罗列相关方向?

**必问问题**:
1. 该方法相对于最接近的工作 (closest work)，核心区别是什么? 如果去掉这个区别，性能会下降多少?
2. 方法中的关键超参数如何选择? 是否对超参数敏感性进行了分析?
3. 如果方法依赖某种假设 (如数据分布假设)，这个假设在实际场景中是否成立?
4. 时间复杂度和空间复杂度分别是多少? 与基线方法相比如何?
5. 论文里的“创新”是机制级差异，还是只是在已有范式上重新命名?

**典型审稿意见示例**:

> "The proposed method introduces a novel temporal attention mechanism. However, the authors fail to provide a clear justification for why this specific design choice is superior to standard self-attention. Ablation studies comparing different attention variants (e.g., linear attention, gated attention) would strengthen the paper significantly."

> "The theoretical analysis in Section III-B assumes that the graph structure is static, which contradicts the dynamic graph setting described in Section II. This inconsistency needs to be addressed."

**评分倾向**: 对创新性要求严格，给分通常偏保守。如果只是换了一个模块就声称"novel"，会给低分。

---

### Reviewer 2: 实验审稿人 (Experimental Reviewer)

**身份定位**: 你是一位注重实证的研究者，相信"实验说明一切"。

**核心关注点**:
- 实验完整性: 是否覆盖了足够的场景 (不同数据集、不同设置)?
- 数据集选择: 是否使用了领域公认的标准数据集? 数据集是否多样化?
- 对比公平性: 基线方法是否是最新的? 是否使用了公平的比较设置?
- 统计显著性: 是否报告了多次运行的均值和标准差?
- 消融实验: 是否对每个核心组件进行了消融?
- 证据包完整性: 是否提供了支撑 novelty claim 的最小证据包

**必问问题**:
1. 为什么没有与 [最新的 SOTA 方法] 进行对比?
2. 实验中使用了哪些数据集? 为什么选择这些数据集? 数据集的统计特征是什么?
3. 实验结果是否具有统计显著性? p-value 是多少?
4. 在最坏情况下的表现如何? 是否有 failure case 分析?
5. 如果作者声称某个新机制有效，证据是否覆盖了 closest prior art 对照、关键消融、stress test 与 failure boundary?

**典型审稿意见示例**:

> "The experiments only evaluate on two small-scale datasets. To demonstrate the generalizability of the proposed method, experiments on larger datasets (e.g., PEMS08 with 170 nodes) are necessary."

> "Table II shows that the proposed method outperforms baselines by 0.3% on MAE. Is this improvement statistically significant? The authors should report the standard deviation across multiple runs."

> "The authors compare with methods published before 2023 but fail to include recent SOTA methods such as STAEformer and PDFormer. A fair comparison with these methods is essential."

**评分倾向**: 对实验完整性要求极高。如果缺少关键基线或数据集，会直接给 weak reject。

---

### Reviewer 3: 写作审稿人 (Writing Reviewer)

**身份定位**: 你是一位对论文写作质量有极高要求的审稿人，认为好的研究必须有好的表达。

**核心关注点**:
- 表达清晰度: 句子是否简洁明了? 是否有歧义?
- 结构合理性: 论文结构是否清晰? 各部分是否连贯?
- 图表质量: 图表是否清晰、专业? 坐标轴标签是否完整?
- 术语一致性: 同一概念是否使用了统一的术语?
- 可复现性: 是否提供了足够的细节让读者复现?

**必问问题**:
1. Figure X 的坐标轴标签太小，无法阅读。请提供更高分辨率的版本。
2. Section III-A 中的符号定义不清晰。请提供一个符号表 (notation table)。
3. 算法伪代码缺少关键细节 (如初始化方式、停止条件)。请补充。
4. 论文中有多处语法错误和拼写错误。请仔细校对。

**典型审稿意见示例**:

> "The paper is generally well-written, but the presentation in Section IV could be improved. Specifically, the motivation for the proposed module is buried in the middle of a long paragraph. I suggest restructuring this section to clearly present: (1) the problem, (2) the intuition behind the solution, and (3) the formal definition."

> "Figure 3 is difficult to interpret. The legend overlaps with the data points, and the y-axis scale is inconsistent across subfigures. Please revise."

> "The notation is inconsistent: the same variable $h$ is used to denote both the hidden state and the attention head in different sections. This is confusing and should be clarified."

**评分倾向**: 对写作质量敏感。如果论文结构混乱或图表质量差，即使方法不错也会给较低分。

---

### Reviewer 4: 领域审稿人 (Domain Reviewer)

**身份定位**: 你是一位来自应用领域的专家 (如交通工程师、医疗AI从业者)，关注研究的实际价值。

**核心关注点**:
- 问题重要性: 研究的问题是否是领域内的真实痛点?
- 实际应用价值: 方法是否可以在实际系统中部署?
- 领域知识: 作者是否正确理解和使用了领域知识?
- 可解释性: 模型的决策是否可以被领域专家理解和信任?

**必问问题**:
1. 该方法在实际部署中会遇到哪些挑战? 作者是否讨论了这些挑战?
2. 模型的预测结果是否符合领域专家的直觉? 是否有 case study?
3. 作者是否与领域专家合作验证了方法的有效性?
4. 该方法相比传统领域方法 (如统计方法、物理模型) 的优势是什么?

**典型审稿意见示例**:

> "The paper focuses on traffic flow prediction but does not discuss how the proposed method could be integrated into existing traffic management systems. A discussion of practical deployment challenges (e.g., real-time requirements, data quality issues) would significantly enhance the paper."

> "The authors claim that their method captures 'spatial-temporal correlations' but do not provide any visualization or interpretation of what the model learns. Do the learned patterns align with known traffic phenomena (e.g., morning rush hour patterns, incident propagation)?"

**评分倾向**: 对实际应用价值要求高。如果论文只关注 benchmark 性能而忽视实际应用，会给较低分。

---

### Reviewer 5: 魔鬼代言人 (Devil's Advocate)

**身份定位**: 你的任务是找到论文的致命缺陷，模拟最严格的审稿人。

**核心关注点**:
- 寻找致命缺陷: 是否有根本性的方法论错误?
- 挑战核心假设: 论文的核心假设是否成立?
- 边界情况: 方法在极端情况下的表现如何?
- 替代解释: 实验结果是否有更简单的解释?
- novelty rescue: 当直接 novelty 站不住时，作者是否还有更可信的 rescue route

**必问问题**:
1. 如果这篇论文被拒，最可能的原因是什么?
2. 论文中最大的弱点是什么? 作者是否试图掩盖这个弱点?
3. 是否存在一个更简单的方法可以达到类似的效果?
4. 实验结果的提升是否来自数据泄露或不合理的实验设置?
5. 如果当前 broad claim 不成立，这篇论文最可辩护的窄贡献是什么?

**典型审稿意见示例**:

> "I am concerned that the performance gains reported in Table II may be due to the specific hyperparameter tuning on the test set. The authors should clarify whether the hyperparameters were selected using a validation set, and provide results with default hyperparameters."

> "The proposed method requires 10x more training time than the baseline. While the authors report improved accuracy, the practical benefit is questionable given the computational cost. A Pareto analysis of accuracy vs. efficiency would be informative."

> "The paper claims that the proposed attention mechanism captures long-range dependencies. However, the effective receptive field analysis (if performed) might show that the model only attends to local neighborhoods. This would undermine the core claim of the paper."

**评分倾向**: 倾向于 reject。会仔细检查实验设置的合理性。如果发现任何可疑之处，会要求作者提供额外证据。

---

## 2. 评估维度与评分 (Evaluation Dimensions)

### 创新性 (Novelty): 0-10分

| 分数 | 等级 | 描述 | 示例 |
|------|------|------|------|
| 9-10 | 开创性 | 定义了新问题或提出了全新范式 | Transformer (Vaswani et al., 2017) |
| 7-8 | 显著改进 | 在现有范式内有重要创新 | GAT (Velickovic et al., 2018) |
| 5-6 | 适度改进 | 组合现有技术产生新效果 | 多数 AAAI/IJCAI 论文 |
| 3-4 | 边际改进 | 微小改动或简单组合 | 调参、换模块 |
| 1-2 | 无创新 | 直接套用现有方法 | 简单 baseline 复现 |

**评分指南**:
- 问自己: "如果去掉论文的核心贡献，还剩下什么?" 如果答案是"一个普通的框架"，则创新性不超过5分。
- 关注"增量创新" (incremental innovation): 仅仅替换一个模块或添加一个组件不算真正的创新。
- 区分"新颖"和"有用": 一个新颖但无用的方法得分不应超过6分。
- 先问 `closest prior art 是谁`。如果答不出来，创新性评分默认不能高。
- 若作者只是把一个流行方向名词套进任务里，而没有明确 differentiator，通常不应超过4-5分。
- 若 broad novelty 被覆盖，但作者成功切换到更窄且更可证的 rescue route，可给中等分而不必一票否决。

**实际评分示例**:

> 论文提出了一种新的时空图注意力机制，但本质上是将 GAT 的注意力计算从空间扩展到时间。
> 创新性评分: **5/10** — 属于"适度改进"，因为这种扩展是直接的 (straightforward)，虽然有一定价值。

> 论文首次将 diffusion model 应用于交通流预测，并提出了专门的图扩散过程。
> 创新性评分: **8/10** — 属于"显著改进"，因为将 diffusion model 引入图时序预测是一个有意义的新方向。

---

### 技术质量 (Technical Quality): 0-10分

| 分数 | 等级 | 描述 |
|------|------|------|
| 9-10 | 优秀 | 理论分析完整，证明严谨，无明显漏洞 |
| 7-8 | 良好 | 方法设计合理，有部分理论支撑 |
| 5-6 | 中等 | 方法基本合理，但缺乏理论分析 |
| 3-4 | 较差 | 方法有明显缺陷或逻辑不自洽 |
| 1-2 | 很差 | 方法存在根本性错误 |

**检查要点**:
- 公式推导是否正确? 符号是否一致?
- 方法的每个组件是否有明确的设计动机?
- 是否有理论分析 (如复杂度分析、收敛性证明)?
- 方法是否依赖不合理的假设?

**扣分项**:
- 公式错误: -2分
- 符号不一致: -1分
- 缺乏理论分析: -1分
- 依赖不合理假设: -2分

---

### 实验完整性 (Experimental Completeness): 0-10分

| 分数 | 等级 | 描述 |
|------|------|------|
| 9-10 | 优秀 | 多数据集、多基线、消融完整、有统计分析 |
| 7-8 | 良好 | 覆盖主要数据集和基线，消融基本完整 |
| 5-6 | 中等 | 数据集或基线不够全面，消融有缺失 |
| 3-4 | 较差 | 只在少数数据集上验证，缺少关键对比 |
| 1-2 | 很差 | 实验严重不足，无法验证方法有效性 |

**必须包含的实验**:
1. **主实验**: 与至少5个基线方法在至少2个标准数据集上的对比
2. **消融实验**: 对每个核心组件的消融
3. **参数敏感性**: 对关键超参数的分析
4. **效率分析**: 参数量、FLOPs、训练/推理时间
5. **可视化**: 预测曲线、注意力权重、特征分布

**扣分项**:
- 缺少关键基线: -2分
- 缺少消融实验: -2分
- 未报告标准差: -1分
- 只在一个数据集上验证: -2分

---

### 写作质量 (Presentation Quality): 0-10分

| 分数 | 等级 | 描述 |
|------|------|------|
| 9-10 | 优秀 | 表达清晰，结构合理，图表专业 |
| 7-8 | 良好 | 基本清晰，有少量问题 |
| 5-6 | 中等 | 表达不够清晰，结构可以改进 |
| 3-4 | 较差 | 多处表达不清，结构混乱 |
| 1-2 | 很差 | 难以理解，大量错误 |

**检查要点**:
- 摘要是否清晰概括了问题、方法、结果?
- 引言是否清楚地阐述了动机和贡献?
- 方法部分是否足够详细以便复现?
- 图表是否清晰、专业、信息丰富?
- 结论是否准确总结了贡献和局限性?

**扣分项**:
- 语法/拼写错误 (每5处): -1分
- 图表质量差: -2分
- 结构混乱: -2分
- 术语不一致: -1分

---

### 问题重要性 (Significance): 0-10分

| 分数 | 等级 | 描述 |
|------|------|------|
| 9-10 | 重要 | 解决了领域内的关键问题，有广泛影响 |
| 7-8 | 较重要 | 解决了一个有意义的问题，有一定影响 |
| 5-6 | 一般 | 问题有一定价值，但影响有限 |
| 3-4 | 较低 | 问题较窄，受众有限 |
| 1-2 | 低 | 问题不重要或已有更好的解决方案 |

**评估标准**:
- 问题是否是领域内的真实需求?
- 解决这个问题能带来什么实际影响?
- 是否有更紧迫的问题值得研究?
- 方法的推广价值如何?

---

### 可复现性 (Reproducibility): 0-10分

| 分数 | 等级 | 描述 |
|------|------|------|
| 9-10 | 优秀 | 提供代码、详细设置、完整参数 |
| 7-8 | 良好 | 提供较详细的设置，缺少代码 |
| 5-6 | 中等 | 部分设置描述不清 |
| 3-4 | 较差 | 关键细节缺失 |
| 1-2 | 很差 | 无法根据论文复现 |

**检查要点**:
- 是否提供了代码?
- 数据预处理步骤是否详细?
- 超参数是否完整列出?
- 训练细节 (如学习率调度、早停策略) 是否清楚?
- 硬件环境是否说明?

---

## 3. 常见拒稿理由 (Common Rejection Reasons)

### 3.1 创新不足 (Insufficient Novelty)

**典型表现**:
- 仅将现有模块进行简单组合 (如 CNN + Attention + GNN)
- 声称"首次"但实际上已有类似工作
- 核心贡献是一个 trivial 的改进

**审稿人措辞**:
> "The contribution is incremental. The proposed method is essentially a combination of existing techniques without a clear novelty."

> "The authors claim that this is the first work to [X], but [Reference A] has already addressed a similar problem. The distinction between this work and [Reference A] is not clear."

> "The main contribution seems to be replacing [Component A] with [Component B] in an existing framework. This level of novelty is insufficient for a Transactions paper."

**作者应如何避免**:
1. 在 Related Work 中明确区分自己的工作与最接近的工作
2. 提供消融实验验证核心创新点的贡献
3. 避免使用"首次""开创性"等夸大措辞
4. 强调方法的独特insight，而非仅仅技术细节
5. 如果 broad novelty 已被覆盖，主动切换到 benchmark / mechanism / deployment / theory / negative-result 这类更可信的贡献类型

---

### 3.2 实验不完整 (Incomplete Experiments)

**典型表现**:
- 只在1-2个小数据集上验证
- 缺少最新的 SOTA 基线
- 没有消融实验
- 未报告标准差或置信区间

**审稿人措辞**:
> "The experiments are not comprehensive enough. The authors only evaluate on [Dataset A], which is a small-scale dataset. Experiments on larger datasets are needed to demonstrate scalability."

> "Several recent state-of-the-art methods are missing from the comparison, including [Method A] (ICLR 2024) and [Method B] (NeurIPS 2023). Without these comparisons, it is difficult to assess the true contribution of this work."

> "The paper lacks ablation studies. It is unclear which component of the proposed method contributes most to the performance improvement."

**作者应如何避免**:
1. 至少在3个标准数据集上进行实验
2. 包括最近2年内发表的 SOTA 方法作为基线
3. 对每个核心组件进行消融实验
4. 报告5次运行的均值和标准差
5. 提供效率分析 (参数量、FLOPs、推理时间)

---

### 3.3 写作质量差 (Poor Writing)

**典型表现**:
- 语法错误和拼写错误过多
- 图表质量低，难以阅读
- 符号定义不清晰或不一致
- 论文结构混乱，逻辑不连贯

**审稿人措辞**:
> "The paper suffers from numerous grammatical errors and typos, which significantly affect readability. I strongly recommend thorough proofreading."

> "Figure 2 is almost impossible to read due to small font sizes and overlapping labels. Please provide a high-resolution version with clear labels."

> "The notation is inconsistent throughout the paper. For example, the symbol $\mathbf{H}$ is used to denote different quantities in Sections III and IV. A notation table would be helpful."

**作者应如何避免**:
1. 请英语母语者或专业编辑校对
2. 使用高分辨率图表，确保所有标签清晰可读
3. 在论文开头提供符号表 (Notation Table)
4. 请同事或导师审阅论文结构

---

### 3.4 方法有缺陷 (Methodological Flaws)

**典型表现**:
- 核心假设不成立或未验证
- 存在数据泄露 (data leakage)
- 实验设置不公平 (如使用不同的数据划分)
- 公式推导有错误

**审稿人措辞**:
> "There is a potential data leakage issue. The authors use future information (i.e., data from time t+1 to t+T) to predict the value at time t. This is not a realistic prediction setting."

> "Theorem 1 assumes that the loss function is convex, but the proposed method uses a non-convex neural network. The theoretical analysis is therefore not applicable to the actual method."

> "The comparison is unfair: the proposed method uses additional training data (external features) while the baselines do not. A fair comparison should use the same input for all methods."

**作者应如何避免**:
1. 仔细检查实验设置，确保没有数据泄露
2. 验证理论假设是否与实际方法一致
3. 确保所有方法使用相同的实验设置
4. 请独立第三方检查公式推导

---

### 3.5 问题不重要 (Insufficient Significance)

**典型表现**:
- 问题过于狭窄，只有少数人关心
- 没有说明研究的实际意义
- 问题已经有更好的解决方案
- 增量改进不值得发表

**审稿人措辞**:
> "The problem addressed in this paper is quite narrow and may only be relevant to a small subset of researchers in this field."

> "The authors do not adequately motivate why this problem is important. A clearer discussion of practical applications and potential impact is needed."

> "Existing methods already provide reasonable solutions to this problem. The marginal improvement offered by the proposed method does not justify a full Transactions paper."

**作者应如何避免**:
1. 在引言中清楚说明问题的重要性和实际意义
2. 提供定量证据说明问题的紧迫性 (如统计数据、行业报告)
3. 讨论方法的潜在应用和推广价值
4. 诚实评估相对于现有方法的实际改进

---

## 4. 审稿报告模板 (Review Report Template)

```
=================================================================
                    REVIEW REPORT
=================================================================

Paper ID: [XXXX]
Title: [Paper Title]
Conference/Journal: [IEEE TITS/TNNLS/TKDE]

-----------------------------------------------------------------
SUMMARY
-----------------------------------------------------------------

[用1段话概括论文的问题、方法和主要结果。不超过150字。]

This paper addresses the problem of [problem] by proposing [method].
The key idea is [insight]. The method consists of [components].
Experiments on [datasets] demonstrate that the proposed method
outperforms existing methods by [margin] on [metrics].

-----------------------------------------------------------------
STRENGTHS
-----------------------------------------------------------------

S1. [具体说明第一个优点，引用论文中的具体内容]
    - Example: "The paper provides a comprehensive theoretical
    analysis of the proposed method, including convergence
    guarantees (Theorem 1) and complexity analysis (Table I)."

S2. [具体说明第二个优点]
    - Example: "The experiments are thorough, covering 4 datasets
    and 8 baselines. The ablation study (Table III) clearly
    demonstrates the contribution of each component."

S3. [具体说明第三个优点，如果有的话]
    - Example: "The paper is generally well-written with clear
    figures and a logical structure."

-----------------------------------------------------------------
WEAKNESSES
-----------------------------------------------------------------

W1. [具体说明第一个弱点，引用论文中的具体位置]
    - Example: "The paper does not compare with [Method A]
    (ICLR 2024), which is currently the state-of-the-art on
    the METR-LA benchmark. Without this comparison, it is
    difficult to assess the true contribution of this work."

W2. [具体说明第二个弱点]
    - Example: "The theoretical analysis in Section III-B assumes
    that the graph structure is static, but the experiments are
    conducted on dynamic graphs. This inconsistency undermines
    the theoretical contribution."

W3. [具体说明第三个弱点，如果有的话]
    - Example: "The paper does not discuss the computational
    efficiency of the proposed method. Given that real-time
    prediction is important for traffic applications, this is
    a significant omission."

-----------------------------------------------------------------
QUESTIONS TO AUTHORS
-----------------------------------------------------------------

Q1. [需要作者回答的问题1]
    - Example: "How sensitive is the proposed method to the
    hyperparameter $\lambda$? Have you tried different values
    and what is the effect on performance?"

Q2. [需要作者回答的问题2]
    - Example: "Can you provide the standard deviation of the
    results in Table II? The improvements over the baseline
    are small (0.2-0.5%) and it is unclear if they are
    statistically significant."

Q3. [需要作者回答的问题3]
    - Example: "How does the proposed method perform on graphs
    with different sizes? Have you tested on larger graphs
    (e.g., 500+ nodes)?"

-----------------------------------------------------------------
MINOR COMMENTS
-----------------------------------------------------------------

- Page 3, Line 15: "effect" should be "affect"
- Figure 2: The legend is too small to read. Please increase
  the font size.
- Table IV: Missing the unit for FLOPs (should be "G" for
  GFLOPs).
- Reference [12]: Incomplete citation. Please provide the
  full venue information.
- Algorithm 1: Missing initialization for variable $\alpha$.

-----------------------------------------------------------------
OVERALL ASSESSMENT
-----------------------------------------------------------------

Score: [0-10]
  - 8-10: Strong Accept / Accept
  - 6-7: Weak Accept
  - 4-5: Weak Reject
  - 1-3: Reject

Confidence: [1-5]
  - 5: Expert, very confident
  - 4: Knowledgeable, confident
  - 3: Reasonable confidence
  - 2: Some uncertainty
  - 1: Not my area

Recommendation: [Accept / Weak Accept / Weak Reject / Reject]

Justification: [用2-3句话说明推荐理由]

=================================================================
```

### 实际审稿报告示例

```
Paper ID: TITS-2024-0123
Title: "Spatiotemporal Adaptive Graph Convolution for Traffic Flow Prediction"
Conference/Journal: IEEE TITS

-----------------------------------------------------------------
SUMMARY
-----------------------------------------------------------------

This paper proposes a Spatiotemporal Adaptive Graph Convolution
Network (STAGCN) for traffic flow prediction. The method uses a
novel adaptive adjacency matrix that learns spatial correlations
from data, combined with a temporal convolution module to capture
temporal patterns. Experiments on METR-LA and PEMS-BAY datasets
show that STAGCN outperforms existing methods by 1.2% on MAE.

-----------------------------------------------------------------
STRENGTHS
-----------------------------------------------------------------

S1. The adaptive graph learning mechanism is well-designed and
    provides a principled way to learn spatial correlations
    without relying on predefined distance-based adjacency
    matrices.

S2. The experiments are comprehensive, including 6 baselines on
    2 standard datasets. The ablation study (Table III) clearly
    shows the contribution of each component.

S3. The paper provides a complexity analysis (Table I) comparing
    the computational cost of different methods.

-----------------------------------------------------------------
WEAKNESSES
-----------------------------------------------------------------

W1. The paper does not compare with STAEformer (AAAI 2023) and
    PDFormer (AAAI 2023), which are the current state-of-the-art
    methods on METR-LA and PEMS-BAY. This is a significant
    omission.

W2. The improvements over the best baseline (GWNet) are modest:
    1.2% on MAE and 0.8% on RMSE. The paper does not provide
    statistical significance tests to show these improvements
    are meaningful.

W3. The paper claims the method captures "long-range temporal
    dependencies" but uses a temporal convolution with kernel
    size 3. This only captures local patterns. The authors
    should either revise the claim or modify the architecture.

-----------------------------------------------------------------
QUESTIONS TO AUTHORS
-----------------------------------------------------------------

Q1. Can you provide results with STAEformer and PDFormer as
    baselines? These are important comparisons that readers
    would expect to see.

Q2. What is the effect of the temporal kernel size? Have you
    tried larger kernel sizes (e.g., 5, 7, 11) to capture
    longer temporal dependencies?

Q3. How does the adaptive adjacency matrix change during
    training? Can you provide visualizations showing the
    learned spatial correlations?

-----------------------------------------------------------------
MINOR COMMENTS
-----------------------------------------------------------------

- Page 4, Line 8: "utilized" -> "used" (simpler is better)
- Figure 3: The color scale is hard to distinguish. Consider
  using a diverging colormap.
- Table II: Bold the best results for each metric.
- Reference [7]: Missing page numbers.

-----------------------------------------------------------------
OVERALL ASSESSMENT
-----------------------------------------------------------------

Score: 6/10
Confidence: 4/5
Recommendation: Weak Accept

Justification: The paper proposes a reasonable method with
solid experimental validation. However, the missing comparisons
with recent SOTA methods and the modest improvements weaken
the contribution. If the authors can address these issues in
the revision, the paper would be suitable for publication.

=================================================================
```

---

## 5. 交通流预测审稿重点 (Traffic Prediction Review Focus)

### 5.1 数据集检查

**必须覆盖的数据集**:
- METR-LA: 207个检测器，34272个时间步，5分钟间隔
- PEMS-BAY: 325个检测器，52116个时间步，5分钟间隔
- PEMS04: 307个检测器，16992个时间步，5分钟间隔
- PEMS08: 170个检测器，17856个时间步，5分钟间隔

**检查要点**:
1. 是否在至少2个数据集上报告了结果?
2. 数据划分是否遵循标准设置 (如 6:2:2 或 7:1:2)?
3. 是否说明了数据预处理步骤 (归一化方式、缺失值处理)?
4. 是否提供了数据集的统计特征 (如均值、方差、缺失率)?

**审稿意见示例**:
> "The paper only evaluates on PEMS04 and PEMS08. To be considered for IEEE TITS, experiments on METR-LA and PEMS-BAY are expected as these are the most widely used benchmarks in the traffic prediction community."

### 5.2 基线检查

**必须包含的基线** (按时间排序):
- 经典方法: ARIMA, SVR
- 深度学习方法: STGCN (2018), DCRNN (2018), Graph WaveNet (2019)
- 近期 SOTA: STAEformer (2023), PDFormer (2023), STID (2022)

**检查要点**:
1. 是否包含了近2年发表的 SOTA 方法?
2. 基线方法的结果是否来自原始论文? 还是自己复现?
3. 如果自己复现，是否使用了原作者的代码?
4. 是否使用了公平的比较设置 (如相同的预测窗口)?

**审稿意见示例**:
> "The most recent baseline is from 2021 (AGCRN). Since then, several important methods have been proposed, including STAEformer (AAAI 2023) and PDFormer (AAAI 2023). The absence of these comparisons makes it difficult to position this work in the current landscape."

### 5.3 评估指标检查

**标准指标**:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

**预测窗口**:
- 必须报告: 15分钟 (3步), 30分钟 (6步), 60分钟 (12步)
- 建议额外报告: 5分钟 (1步), 120分钟 (24步)

**检查要点**:
1. 是否在所有标准预测窗口上报告了结果?
2. 是否使用了标准指标 (MAE, RMSE, MAPE)?
3. MAPE 在值接近0时是否有处理? (避免除零错误)
4. 是否报告了多次运行的均值和标准差?

**审稿意见示例**:
> "The paper only reports results for the 30-minute prediction horizon. For a comprehensive evaluation, results at 15, 30, and 60 minutes should be provided. This is standard practice in the traffic prediction literature."

### 5.4 消融实验检查

**必须消融的组件**:
- 空间模块: 去掉空间建模后的性能变化
- 时间模块: 去掉时间建模后的性能变化
- 核心创新: 替换为标准版本后的性能变化

**检查要点**:
1. 是否对每个核心组件进行了消融?
2. 消融实验是否在所有数据集上进行?
3. 是否提供了组件组合的分析?
4. 消融结论是否与主实验一致?

**审稿意见示例**:
> "The ablation study (Table IV) only removes one component at a time. To better understand the interaction between components, the authors should provide results for all combinations (2^3 = 8 configurations for 3 components)."

### 5.5 效率分析检查

**必须报告的指标**:
- 参数量 (Parameters): 单位 M (百万)
- 浮点运算量 (FLOPs): 单位 G (十亿)
- 训练时间: 单位 hours/epoch
- 推理时间: 单位 ms/sample 或 ms/step

**检查要点**:
1. 是否报告了参数量和 FLOPs?
2. 是否报告了训练和推理时间?
3. 效率与性能的 trade-off 是否合理?
4. 是否有 Pareto 分析 (效率 vs 性能)?

**审稿意见示例**:
> "The proposed method achieves slightly better accuracy than GWNet but requires 5x more parameters and 3x more training time. The paper should discuss whether this trade-off is acceptable for practical applications."

### 5.6 可视化检查

**必须包含的可视化**:
- 预测曲线: 真实值 vs 预测值的时间序列图
- 空间可视化: 学习到的空间相关性 (adjacency matrix)
- 注意力权重: 如果使用注意力机制，需要可视化注意力分布
- 误差分布: 预测误差的时间/空间分布

**检查要点**:
1. 预测曲线是否包含足够长的时间段?
2. 是否展示了不同场景 (如高峰/低谷、工作日/周末)?
3. 可视化是否支持论文的核心论点?
4. 图表是否清晰、专业?

**审稿意见示例**:
> "Figure 5 shows the prediction curves for only one sensor and one day. To provide a more comprehensive view, the authors should show: (1) results for multiple sensors with different traffic patterns, (2) results for different days (weekday vs. weekend), and (3) error distribution across all sensors."

---

## 6. 审稿流程 (Review Workflow)

### 第一遍: 快速浏览 (5分钟)

**目标**: 了解论文在讲什么，初步判断质量。

**阅读顺序**:
1. **标题和摘要** (1分钟): 了解问题、方法、结果
2. **引言的最后一段** (1分钟): 找到贡献列表
3. **图表** (2分钟): 快速浏览所有图表，了解实验设置和结果
4. **结论** (1分钟): 了解作者的总结

**初步判断**:
- 论文的主题是否在你的专业范围内?
- 问题是否有趣/重要?
- 方法看起来是否合理?
- 实验是否充分?

**决策**:
- 如果明显不适合 (如超出专业范围): 建议编辑拒稿或转给更合适的审稿人
- 如果看起来不错: 进入第二遍
- 如果看起来有问题: 记下疑虑，进入第二遍确认

---

### 第二遍: 仔细阅读 (30分钟)

**目标**: 理解技术细节，评估方法的合理性。

**阅读顺序**:
1. **Related Work** (5分钟): 了解领域背景，确认论文的定位是否准确
2. **Method** (15分钟): 仔细理解方法的每个组件
3. **Theory** (5分钟): 检查理论分析的正确性
4. **Experiments** (5分钟): 理解实验设置

**检查要点**:
- Related Work 是否全面? 是否遗漏了重要工作?
- 方法的每个组件是否有明确的设计动机?
- 理论假设是否合理? 证明是否正确?
- 实验设置是否公平? 是否有数据泄露?

**记录**:
- 记录所有疑问和发现的问题
- 标记需要仔细检查的公式和算法
- 记录与 Related Work 的对比

---

### 第三遍: 批判性阅读 (20分钟)

**目标**: 寻找弱点，评估论文的整体贡献。

**重点检查**:
1. **实验结果** (10分钟):
   - 仔细检查表格中的数字
   - 对比基线方法的结果是否合理
   - 检查是否有数据泄露或不公平设置
   - 计算实际改进幅度

2. **声明与证据** (5分钟):
   - 论文的每个声明是否有实验支持?
   - 是否存在过度声称 (overclaim)?
   - 结论是否由实验结果支持?
   - novelty claim 是否经过 closest-work 检索和 differentiator 证明?
   - 是否把方向名词误写成了创新点?

3. **图表检查** (5分钟):
   - 图表是否准确反映了结果?
   - 是否有误导性可视化?
   - 坐标轴是否从0开始? (如果不从0，是否有正当理由?)

**生成弱点列表**:
- 列出所有发现的弱点
- 对每个弱点评估严重程度 (致命/严重/一般/轻微)
- 准备向作者提出的问题

---

### 撰写报告 (20分钟)

**写作顺序**:
1. **Summary** (3分钟): 用1段话概括论文
2. **Strengths** (3分钟): 列出2-3个优点
3. **Weaknesses** (5分钟): 列出2-3个弱点 (这是最重要的部分)
4. **Questions** (3分钟): 列出2-3个问题
5. **Minor Comments** (3分钟): 列出语法、图表等小问题
6. **Score and Recommendation** (3分钟): 给出评分和建议

**写作原则**:
- 具体: 指出具体的问题位置 (页码、行号、图表号)
- 建设性: 不仅指出问题，还要给出改进建议
- 公平: 区分致命问题和小问题
- 尊重: 避免侮辱性语言，尊重作者的劳动

---

## 7. 对抗性检查清单 (Adversarial Checklist)

### 7.1 声明与证据匹配

- [ ] 论文声称"首次提出"，但 Related Work 中是否有类似方法?
- [ ] 论文声称"显著优于"，实际改进幅度是多少? 是否统计显著?
- [ ] 论文声称"具有理论保证"，理论假设是否在实验中满足?
- [ ] 论文声称"高效"，实际计算成本是多少?
- [ ] 论文声称"创新"，但是否明确写出了 closest prior art 和 differentiator?
- [ ] 论文的 novelty claim 是否依赖最近 12-24 个月里已经被覆盖的中心主张?

**检查方法**:
```
对于每个声明 X:
1. 找到支持 X 的证据
2. 评估证据是否充分
3. 检查是否有反面证据
4. 判断声明是否过度
```

### 7.2 实验设置公平性

- [ ] 所有方法是否使用相同的数据划分?
- [ ] 所有方法是否使用相同的输入特征?
- [ ] 所有方法是否使用相同的评估指标?
- [ ] 基线方法的结果是否来自原始论文? 如果是，实验设置是否一致?
- [ ] 是否存在数据泄露 (训练集信息泄露到测试集)?

**常见数据泄露场景**:
```
1. 时间序列: 用未来数据预测过去 (look-ahead bias)
2. 图数据: 训练时使用了测试节点的特征
3. 归一化: 使用整个数据集计算均值/方差 (应只用训练集)
4. 特征选择: 使用测试集信息选择特征
```

### 7.3 基线充分性

- [ ] 是否包含该领域的经典方法?
- [ ] 是否包含最近2年内发表的 SOTA 方法?
- [ ] 基线方法是否代表了不同的技术路线?
- [ ] 是否有"strawman"基线 (太弱的基线，只是为了衬托)?
- [ ] strongest closest work 是否已纳入，而不是只选对自己更弱的比较对象?

**评估标准**:
```
一个好的基线集合应该包括:
1. 1-2个经典方法 (如 ARIMA, SVR)
2. 2-3个深度学习基础方法 (如 LSTM, GCN)
3. 2-3个近期 SOTA 方法 (如 2023-2024 年发表)
4. 1个简单的 baseline (如 历史平均值)
```

### 7.4 消融完整性

- [ ] 是否对每个核心组件进行了消融?
- [ ] 消融实验是否在所有数据集上进行?
- [ ] 是否有组件组合的分析?
- [ ] 消融结论是否与方法设计一致?

**消融实验设计**:
```
对于 N 个核心组件:
1. 完整方法 (Full)
2. 去掉组件1 (w/o Component 1)
3. 去掉组件2 (w/o Component 2)
...
N+1. 去掉组件N (w/o Component N)
N+2. 只保留组件1 (Only Component 1)
N+3. 只保留组件2 (Only Component 2)
...
```

### 7.5 图表误导性

- [ ] 坐标轴是否从0开始? 如果不是，是否有正当理由?
- [ ] y轴范围是否一致? 不同子图是否使用了相同刻度?
- [ ] 颜色选择是否对色盲友好?
- [ ] 图例是否清晰? 是否与数据点重叠?
- [ ] 3D图表是否必要? 2D是否能传达相同信息?

**常见误导手法**:
```
1. 截断y轴: 让微小差异看起来很大
2. 选择性展示: 只展示表现好的场景
3. 不公平对比: 对手方法使用次优设置
4.  cherry-picking: 只展示最好的运行结果
```

### 7.6 结论过度性

- [ ] 结论是否超出了实验验证的范围?
- [ ] 是否将相关性误认为因果性?
- [ ] 是否忽略了方法的局限性?
- [ ] 是否对未来工作有合理的展望?
- [ ] 是否在 closest-work threat 明显存在时，仍然保留了过宽的 novelty 结论?

**过度结论示例**:
```
原文: "Our method achieves state-of-the-art performance on
all benchmarks."
问题: 只在2个数据集上测试，不能声称"all benchmarks"

原文: "The experimental results prove that our method is
superior to all existing methods."
问题: 实验结果只是在特定设置下的比较，不能推广到"all
existing methods"

原文: "Our method can be easily deployed in real-world
systems."
问题: 没有实际部署经验，不能声称"easily deployed"
```

---

## 8. 审稿人自我校准 (Reviewer Calibration)

### 8.1 评分校准

**不同审稿人的评分倾向**:
- 严格审稿人: 平均分 4-5，很少给7分以上
- 宽松审稿人: 平均分 6-7，很少给4分以下
- 中等审稿人: 平均分 5-6，分数分布较均匀

**校准方法**:
```
1. 回顾你过去审过的论文
2. 计算你的平均分
3. 与领域平均分对比
4. 调整你的评分标准
```

**IEEE TITS 的典型分数分布**:
- Accept (8-10): 约15%
- Weak Accept (6-7): 约25%
- Weak Reject (4-5): 约30%
- Reject (1-3): 约30%

### 8.2 常见审稿偏见

**确认偏见 (Confirmation Bias)**:
- 表现: 倾向于接受与自己观点一致的论文
- 对策: 主动寻找与自己观点不同的证据

**锚定偏见 (Anchoring Bias)**:
- 表现: 过度依赖第一次阅读的印象
- 对策: 完成三遍阅读后再形成最终意见

**权威偏见 (Authority Bias)**:
- 表现: 倾向于接受知名作者的论文
- 对策: 匿名评审，只关注论文内容

**新近偏见 (Recency Bias)**:
- 表现: 过度关注最新的方法，忽视经典方法的价值
- 对策: 公平评估所有基线方法

---

## 9. 特殊情况处理 (Special Cases)

### 9.1 论文有明显创新但实验不足

**处理方式**:
- 如果创新确实重要: 给 Weak Accept，要求补充实验
- 如果创新一般: 给 Weak Reject，要求重新提交

**审稿意见模板**:
> "The proposed method has a novel and interesting idea. However, the experiments are not comprehensive enough for a full paper. I recommend a major revision with the following additional experiments: [list]. If these experiments confirm the effectiveness of the method, I would be happy to recommend acceptance."

### 9.2 论文实验充分但创新不足

**处理方式**:
- 如果实验特别充分 (如大规模实验、详细分析): 可考虑 Weak Accept
- 如果实验只是标准配置: 通常 Weak Reject

**审稿意见模板**:
> "The experiments are thorough and well-presented. However, the novelty is limited. The main contribution is [X], which is a relatively straightforward extension of [Y]. I recommend the authors either: (1) strengthen the novelty by [suggestion], or (2) submit to a more specialized venue."

### 9.3 论文有致命缺陷

**处理方式**:
- 如果是方法论错误: Reject
- 如果是实验设置错误: Reject (但如果可以修复，建议重新提交)
- 如果是写作问题: 通常不致命，给 Major Revision

**审稿意见模板**:
> "There is a fundamental issue with the experimental setup: [describe issue]. This invalidates the main results of the paper. I recommend rejection, but encourage the authors to address this issue and resubmit."

### 9.4 论文超出你的专业范围

**处理方式**:
- 如果只是部分内容超出: 请作者解释清楚
- 如果大部分内容超出: 建议编辑找更合适的审稿人

**审稿意见模板**:
> "I am not an expert on [specific topic], so I cannot fully evaluate the technical contribution in Section [X]. I recommend the editor seek additional review from someone with expertise in this area."

---

## 10. 附录: 评分标准速查表

### 创新性速查

| 情况 | 分数 |
|------|------|
| 定义新问题/新范式 | 9-10 |
| 解决重要问题的新方法 | 7-8 |
| 现有方法的有意义改进 | 5-6 |
| 简单组合或微小改进 | 3-4 |
| 无创新 | 1-2 |

### 技术质量速查

| 情况 | 分数 |
|------|------|
| 理论完整，设计合理 | 9-10 |
| 设计合理，有部分理论 | 7-8 |
| 基本合理，缺乏理论 | 5-6 |
| 有明显缺陷 | 3-4 |
| 根本性错误 | 1-2 |

### 实验完整性速查

| 情况 | 分数 |
|------|------|
| 多数据集，多基线，消融完整 | 9-10 |
| 覆盖主要数据集和基线 | 7-8 |
| 数据集或基线不够全面 | 5-6 |
| 只在少数数据集上验证 | 3-4 |
| 实验严重不足 | 1-2 |

### 写作质量速查

| 情况 | 分数 |
|------|------|
| 清晰，结构合理，图表专业 | 9-10 |
| 基本清晰，少量问题 | 7-8 |
| 不够清晰，可改进 | 5-6 |
| 多处问题 | 3-4 |
| 难以理解 | 1-2 |

### 问题重要性速查

| 情况 | 分数 |
|------|------|
| 解决关键问题，广泛影响 | 9-10 |
| 有意义的问题，一定影响 | 7-8 |
| 价值一般，影响有限 | 5-6 |
| 问题较窄 | 3-4 |
| 不重要 | 1-2 |

### 可复现性速查

| 情况 | 分数 |
|------|------|
| 代码公开，细节完整 | 9-10 |
| 设置详细，缺少代码 | 7-8 |
| 部分细节不清 | 5-6 |
| 关键细节缺失 | 3-4 |
| 无法复现 | 1-2 |

---

> **使用说明**: 本文件用于模拟 IEEE Transactions 级别的论文审稿过程。
> 每次审稿时，可以选择一个或多个角色进行审阅。
> 综合所有角色的意见，形成最终的审稿报告。
> 目标是通过模拟审稿，提高论文质量和审稿能力。
