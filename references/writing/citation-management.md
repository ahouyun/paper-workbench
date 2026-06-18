# 引用管理指南

借鉴 nature-citation 的引用检索和验证流程。

## 核心原则

- **不编造引用**：DOI、作者、标题、期刊信息必须可验证
- **不借引用伪装数据**：若正文中的实验规模、部署数量、样本数量、PR 数量、设备数量来自文献，必须明确是“本文复述文献结果”还是“本文自己的实验”
- **按首次出现编号**：IEEE 使用方括号编号，按在正文中首次出现的顺序排列
- **验证后再引用**：检索到文献后验证 DOI 可访问性

---

## 引用格式（IEEE）

### 期刊

```
[1] A. Author, B. Author, and C. Author, ``Title,'' \emph{IEEE Trans. Abbrev.}, vol.~X, no.~X, pp.~X--X, Month Year.
```

### 会议

```
[2] A. Author and B. Author, ``Title,'' in \emph{Proc. Conf. Name}, City, Country, Year, pp.~X--X.
```

### 书籍

```
[3] A. Author, \emph{Title of Book}. Publisher, Year.
```

### arXiv

```
[4] A. Author, ``Title,'' arXiv preprint arXiv:XXXX.XXXXX, Year.
```

---

## BibTeX 模板

```bibtex
@article{ref1,
  author  = {Author, A. and Author, B.},
  title   = {Title},
  journal = {IEEE Trans. Abbrev.},
  volume  = {X},
  number  = {X},
  pages   = {X--X},
  year    = {Year},
}

@inproceedings{ref2,
  author    = {Author, A. and Author, B.},
  title     = {Title},
  booktitle = {Proc. Conf. Name},
  address   = {City, Country},
  pages     = {X--X},
  year      = {Year},
}
```

---

## 引用检索策略

### 优先级

1. **目标期刊已发表论文** — 相关性最高
2. **同领域顶刊/顶会** — 权威性
3. **arXiv 预印本** — 时效性（需注明）
4. **经典文献** — 基础理论

### 检索流程

1. 分析段落关键词
2. 在 IEEE Xplore / Google Scholar / Semantic Scholar 检索
3. 验证 DOI 可访问性
4. 提取元数据（作者、标题、期刊、年份）
5. 格式化为 IEEE 格式
6. 插入正文引用

---

## 引用验证

### 必须验证项

- [ ] DOI 可访问（非 404）
- [ ] 作者姓名正确
- [ ] 标题完整无误
- [ ] 期刊/会议名称正确
- [ ] 卷号/期号/页码正确
- [ ] 年份正确

### 验证失败处理

- DOI 404：尝试搜索替代链接，或标记为 `needs_verification`
- 元数据不完整：从多个源交叉验证
- 无法验证：不引用，或在正文中注明"据作者所知"

---

## 引用密度

| Section | 推荐引用密度 |
|---------|-------------|
| Introduction | 每个技术点 2-5 篇 |
| Related Work | 每个子主题 3-8 篇 |
| Method（引用 prior work） | 每个模块 1-3 篇 |
| Experiments（baseline） | 每个 baseline 1 篇 |
| Conclusion | 少量（总结性引用） |

---

## 常见 IEEE 期刊缩写

| 全称 | 缩写 |
|------|------|
| IEEE Transactions on Signal Processing | IEEE Trans. Signal Process. |
| IEEE Transactions on Communications | IEEE Trans. Commun. |
| IEEE Transactions on Wireless Communications | IEEE Trans. Wireless Commun. |
| IEEE Transactions on Information Theory | IEEE Trans. Inf. Theory |
| IEEE Transactions on Neural Networks and Learning Systems | IEEE Trans. Neural Netw. Learn. Syst. |
| IEEE Transactions on Pattern Analysis and Machine Intelligence | IEEE Trans. Pattern Anal. Mach. Intell. |
| IEEE Transactions on Image Processing | IEEE Trans. Image Process. |
| IEEE Transactions on Medical Imaging | IEEE Trans. Med. Imaging |
| IEEE Transactions on Cybernetics | IEEE Trans. Cybern. |
| IEEE Access | IEEE Access |
| IEEE Internet of Things Journal | IEEE Internet Things J. |

> 注意：投稿前务必查阅目标期刊的 "Information for Authors" 确认具体缩写要求。
