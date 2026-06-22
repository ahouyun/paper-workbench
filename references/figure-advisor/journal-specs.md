# 期刊/会议图表规范

主流顶会和期刊对投稿图表的硬性要求汇总。**画图前先查目标会议/期刊**，把栏宽、字号、DPI、推荐字体、矢量格式偏好记下来再开 matplotlib。

---

## 一、顶会图表规范

### 1.1 NeurIPS / ICML / ICLR

机器学习三大顶会，图表规范相似。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **3.25 inch ≈ 82.5 mm** |
| 双栏宽 | **6.75 inch ≈ 171.5 mm** |
| 字号 | 8–10 pt（正文），图内最小 6 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica/Arial |
| 矢量首选 | PDF / EPS |
| 位图 | **300 DPI**（彩色）/ 600 DPI（线条图） |
| 子图标签 | **(a), (b), (c)** 或 **a, b, c**（左上角） |
| 颜色 | 色盲友好；避免红绿对比 |

**坑**：
- NeurIPS 2025 起要求所有图表必须**可访问**（alt text）
- ICLR 要求图表在黑白打印下仍可区分
- ICML 对图表质量审核严格，模糊图直接拒稿

---

### 1.2 CVPR / ICCV / ECCV

计算机视觉三大会议。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **3.0 inch ≈ 76.2 mm** |
| 双栏宽 | **6.25 inch ≈ 158.8 mm** |
| 字号 | 8–10 pt（正文），图内最小 6 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica |
| 矢量首选 | PDF / EPS |
| 位图 | **300 DPI**（彩色）/ 600 DPI（线条图） |
| 子图标签 | **(a), (b), (c)**（左上角） |
| 颜色 | 色盲友好；建议冗余编码 |

**坑**：
- CVPR 对图表质量要求极高，模糊/低分辨率图直接拒稿
- ECCV 要求图表在移动端也能清晰显示
- 建议使用 **PDF 矢量格式**，避免位图

---

### 1.3 KDD / AAAI / IJCAI

数据挖掘和人工智能顶会。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **3.0 inch ≈ 76.2 mm** |
| 双栏宽 | **6.5 inch ≈ 165.1 mm** |
| 字号 | 8–10 pt（正文），图内最小 6 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica/Arial |
| 矢量首选 | PDF / EPS |
| 位图 | **300 DPI**（彩色）/ 600 DPI（线条图） |
| 子图标签 | **(a), (b), (c)** 或 **a, b, c** |
| 颜色 | 色盲友好 |

**坑**：
- KDD 要求图表必须清晰可读，模糊图直接拒稿
- AAAI 对图表质量审核严格
- IJCAI 要求图表在黑白打印下仍可区分

---

### 1.4 VLDB / ICDE / SIGMOD

数据库三大顶会。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **3.0 inch ≈ 76.2 mm** |
| 双栏宽 | **6.5 inch ≈ 165.1 mm** |
| 字号 | 8–10 pt（正文），图内最小 6 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica/Arial |
| 矢量首选 | PDF / EPS |
| 位图 | **300 DPI**（彩色）/ 600 DPI（线条图） |
| 子图标签 | **(a), (b), (c)** 或 **a, b, c** |
| 颜色 | 色盲友好 |

**坑**：
- VLDB 对图表质量要求高，模糊图直接拒稿
- ICDE 要求图表必须清晰可读
- SIGMOD 要求图表在黑白打印下仍可区分

---

### 1.5 ACL / EMNLP / NAACL

自然语言处理顶会。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **3.0 inch ≈ 76.2 mm** |
| 双栏宽 | **6.5 inch ≈ 165.1 mm** |
| 字号 | 8–10 pt（正文），图内最小 6 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica/Arial |
| 矢量首选 | PDF / EPS |
| 位图 | **300 DPI**（彩色）/ 600 DPI（线条图） |
| 子图标签 | **(a), (b), (c)** 或 **a, b, c** |
| 颜色 | 色盲友好 |

**坑**：
- ACL 对图表质量要求高，模糊图直接拒稿
- EMNLP 要求图表必须清晰可读
- NAACL 要求图表在黑白打印下仍可区分

---

## 二、期刊图表规范

### 2.1 IEEE Transactions

涵盖 *IEEE Trans. on PAMI* / *Trans. on Image Processing* / *Trans. on Knowledge and Data Engineering* / *Trans. on Intelligent Transportation Systems* 等。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **3.5 inch ≈ 88.9 mm** |
| 双栏宽 | **7.16 inch ≈ 181.9 mm** |
| 字号 | 8–10 pt（正文），图内最小 6 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica/Arial |
| 矢量首选 | PDF / EPS |
| 位图 | **600 DPI**（线条图）/ 300 DPI（照片/灰度图） |
| 黑白可读 | **明确要求**——彩色图要在灰度下仍能区分类别 |
| 子图标签 | (a) (b) (c) 小写带括号 |

**坑**：IEEE 对**黑白可读**抠得很死——会议印刷常黑白印。**线型 + marker + 颜色三重冗余**编码是必须的。

---

### 2.2 ACM Transactions

涵盖 *ACM Computing Surveys* / *ACM Trans. on Information Systems* / *ACM Trans. on Knowledge Discovery from Data* 等。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **3.0 inch ≈ 76.2 mm** |
| 双栏宽 | **6.5 inch ≈ 165.1 mm** |
| 字号 | 8–10 pt（正文），图内最小 6 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica/Arial |
| 矢量首选 | PDF / EPS |
| 位图 | **300 DPI**（彩色）/ 600 DPI（线条图） |
| 子图标签 | **(a), (b), (c)** 或 **a, b, c** |
| 颜色 | 色盲友好 |

**坑**：
- ACM 对图表质量要求高，模糊图直接拒稿
- ACM Computing Surveys 对图表质量要求极高

---

### 2.3 Elsevier 系列

涵盖 *Information Sciences* / *Knowledge-Based Systems* / *Expert Systems with Applications* / *Neurocomputing* 等。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **90 mm ≈ 3.54 inch** |
| 1.5 栏宽 | 140 mm ≈ 5.5 inch |
| 双栏宽 | **190 mm ≈ 7.48 inch** |
| 字号 | 7–9 pt |
| 推荐字体 | Helvetica / Arial（无衬线） |
| 矢量首选 | EPS / PDF |
| 位图 | **300 DPI（彩色 + 灰度）**；线条图 1000 DPI |
| 子图标签 | (A) (B) (C) 大写带括号 |
| 颜色 | RGB；color blind safe |

---

### 2.4 Springer 系列

涵盖 *Neural Computing and Applications* / *Applied Intelligence* / *The Journal of Supercomputing* 等。

| 维度 | 要求 |
|---|---|
| 单栏宽 | **84 mm ≈ 3.31 inch** |
| 双栏宽 | **174 mm ≈ 6.85 inch** |
| 字号 | 8–10 pt |
| 推荐字体 | **Times New Roman**（正文）；图内可用 Helvetica/Arial |
| 矢量首选 | PDF / EPS |
| 位图 | **300 DPI**（彩色）/ 600 DPI（线条图） |
| 子图标签 | **(a), (b), (c)** 或 **a, b, c** |
| 颜色 | 色盲友好 |

---

### 2.5 中文核心期刊通用要求

适用于 *中国科学* 系列、*计算机学报*、*软件学报*、*自动化学报* 等。**具体期刊以投稿须知为准**——以下是通用约定。

| 维度 | 通用要求 |
|---|---|
| 单栏宽 | **8 cm ≈ 3.15 inch** |
| 双栏宽 | **17 cm ≈ 6.7 inch** |
| 字号 | 中文 6 号（≈8 pt）/ 小 5 号（≈9 pt） |
| 字体 | **中文宋体 + 西文/数字 Times New Roman** 混排 |
| 矢量 | EPS / PDF（部分接受 TIFF） |
| 位图 | **>= 600 DPI**（线条图）/ 300 DPI（照片） |
| 颜色 | 部分期刊只接受黑白图，投稿须知必看 |
| 子图标签 | (a) (b) (c) 或 (甲) (乙) (丙)，与期刊样例一致 |

**坑 1**：中文期刊的 EPS 上传后预览常出方框——出图时务必用中文字体配置，且 `savefig` 用 PDF 而非 EPS（EPS 对 TrueType 中文支持差）。

**坑 2**：数字、变量名、单位**必须**走 Times New Roman（西文衬线），不能用中文宋体——这是排版规范。

---

## 三、跨会议/期刊速查表

| 会议/期刊 | 单栏 (inch) | 双栏 (inch) | 字号 (pt) | 推荐字体 | DPI | 矢量首选 |
|---|---|---|---|---|---|---|
| **NeurIPS/ICML/ICLR** | 3.25 | 6.75 | 8–10 | Times/Helvetica | 300+ | PDF/EPS |
| **CVPR/ICCV/ECCV** | 3.0 | 6.25 | 8–10 | Times/Helvetica | 300+ | PDF/EPS |
| **KDD/AAAI/IJCAI** | 3.0 | 6.5 | 8–10 | Times/Helvetica | 300+ | PDF/EPS |
| **VLDB/ICDE/SIGMOD** | 3.0 | 6.5 | 8–10 | Times/Helvetica | 300+ | PDF/EPS |
| **ACL/EMNLP/NAACL** | 3.0 | 6.5 | 8–10 | Times/Helvetica | 300+ | PDF/EPS |
| **IEEE Trans.** | 3.5 | 7.16 | 8–10 | Times | 600 | PDF/EPS |
| **ACM Trans.** | 3.0 | 6.5 | 8–10 | Times/Helvetica | 300+ | PDF/EPS |
| **Elsevier** | 3.54 | 7.48 | 7–9 | Helvetica/Arial | 300+ | EPS/PDF |
| **Springer** | 3.31 | 6.85 | 8–10 | Times/Helvetica | 300+ | PDF/EPS |
| **中文核心** | 3.15 | 6.7 | 8–9 | 宋体+TNR | 600 | PDF |

---

## 四、通用建议

### 4.1 字体选择

| 场景 | 推荐字体 |
|---|---|
| 正文 | Times New Roman（衬线） |
| 图内标签 | Helvetica / Arial（无衬线） |
| 中文 | 宋体 + Times New Roman 数字混排 |

### 4.2 配色方案

| 场景 | 推荐配色 |
|---|---|
| 色盲友好 | Okabe-Ito / seaborn `colorblind` |
| 热力图（单向） | viridis / magma / inferno / cividis |
| 热力图（双向） | RdBu_r / PiYG / seismic + center=0 |
| **永远不用** | rainbow / jet / hsv |

### 4.3 子图标签风格

| 会议/期刊 | 标签风格 | 位置 |
|---|---|---|
| NeurIPS/ICML/ICLR | (a), (b), (c) 或 a, b, c | 左上角 |
| CVPR/ICCV/ECCV | (a), (b), (c) | 左上角 |
| KDD/AAAI/IJCAI | (a), (b), (c) 或 a, b, c | 左上角 |
| IEEE Trans. | (a) (b) (c) | 左上角 |
| 中文核心 | (a) (b) (c) 或 (甲) (乙) (丙) | 左上角 |

### 4.4 导出建议

| 格式 | 适用场景 | 不适用场景 |
|---|---|---|
| PDF | 数据图、流程图、架构图 | 照片 |
| SVG | 网页展示、交互图 | 投稿（部分期刊不支持） |
| EPS | 传统期刊投稿 | 现代会议（更推荐PDF） |
| PNG | 照片、网页展示 | 数据图（用矢量） |
| TIFF | 照片（高质量） | 数据图（用矢量） |
| **JPEG** | **永远不用** | 数据图、照片 |

---

## 中文字体安装指南

中文 matplotlib 出方框的根本原因：默认字体（DejaVu Sans 等）不含 CJK 字符表。自动做两件事：

1. 按优先级查中文字体：`Noto Sans CJK SC` > `Source Han Sans SC` > `SimHei` > `Microsoft YaHei`
2. 修负号方框：`plt.rcParams['axes.unicode_minus'] = False`

找不到任何 CJK 字体会抛清晰的安装提示（不会让你画完发现是方框）。

**中文期刊的"宋体 + 数字 Times New Roman"混排**：传 `serif_for_zh=True`，优先选 Noto Serif CJK / Source Han Serif / SimSun。

### Linux

```bash
# Debian / Ubuntu
sudo apt install fonts-noto-cjk fonts-noto-cjk-extra

# Fedora / RHEL / CentOS
sudo dnf install google-noto-sans-cjk-fonts google-noto-serif-cjk-fonts

# 安装后刷新 matplotlib 字体缓存
python -c "import matplotlib.font_manager; matplotlib.font_manager._load_fontmanager(try_read_cache=False)"
```

### macOS

```bash
# 推荐：Homebrew Cask
brew install --cask font-noto-sans-cjk-sc font-noto-serif-cjk-sc

# 或手动从 Google Fonts / Adobe 下载
# https://fonts.google.com/noto/specimen/Noto+Sans+SC
```

macOS 本身自带 PingFang SC / Heiti SC / Songti SC，已经够用。

### Windows

1. 去 https://github.com/notofonts/noto-cjk/releases 下载 `Noto_Sans_CJK_SC.zip`
2. 解压，全选 `.otf`/`.ttf` 文件，右键 **"为所有用户安装"**
3. 重启 Python，**或** 删 matplotlib 缓存：
   ```bash
   python -c "import matplotlib; print(matplotlib.get_cachedir())"
   # 把那个目录里的 fontlist*.json 删掉
   ```

Windows 自带 SimHei / SimSun / Microsoft YaHei，最低限度也够用。
