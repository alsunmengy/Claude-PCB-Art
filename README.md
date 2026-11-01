# Claude PCB Art · 宪法 AI 的拟人纪念卡

<p align="center">
  <a href="https://github.com/alsunmengy/Claude-PCB-Art/stargazers">
    <img src="./.github/badges/star-banner.svg" alt="⭐ 点个 Star 吧" width="100%">
  </a>
</p>

> 🧡 **Claude 拟人「Claude 娘」艺术纪念 PCB** —— 嘉立创EDA 开源硬件项目，双面彩色丝印 + 沉金描边，100 × 63 mm 圆角卡片，**无电气功能，纯收藏向工艺板**。

## ⚠️ 购买 / 获赠前必读

> **这块板子不是商品，开源也不是卖货。** 在想要一块、或者打算买 / 收下之前，请先看完这条说明：
> **[关于我做出来的 PCB：赠送 / 售卖 / 开源](https://b23.tv/tJhAZ84)**
>
> - **开源协议**：CC BY-NC-SA 4.0 —— 个人可免费下载、学习、修改、自己打样，**禁止商用**。真的要卖，最多也就像我这样收个成本价。
> - **赠送**：第一批打样板我留一张，线下送朋友几张，其余放闲鱼「到付」——用闲鱼只是为了不暴露收货地址，到手可以直接申请仅退款，闲鱼标价只当作打赏（现在 10 元，早期 5 元，因为总有人不付邮费让我垫付）。
> - **想买**：送完之后还有人要，我会再订一批。成本约 10 元一张，闲鱼含邮费 20 元（邮费我出）。
> - **关于闲置余量**：本板受板厂最小起订量限制（通常为 5 片），作者自留 1 片收藏，其余为整单不可拆分之余量。该部分余量按实际成本（板费 + 运费）转让给确有需要者，不产生任何利润，性质等同于代为下单（拼单代订），不构成商业销售。
> - **适用范围与要求**：上述成本价原则对**全体持有人**同等适用。任何依据本工程打样、或因受让而持有本项目实体板者，其后续转让均不得高于实际成本价（板费 + 运费），不得以盈利为目的加价转售、批量分销，亦不得将本板用于引流、搭售等商业用途。
> - **图片出处**：立绘来自 ZipZipPipe（作者本人公开声明可二次创作），其余素材出处与授权见 [SOURCES.md](./SOURCES.md)。
> - **找到我**：闲鱼 `alsun梦游` ｜ GitHub [`alsunmengy`](https://github.com/alsunmengy) ｜ Star 可选，不点也能用。

## 📖 项目简介

本项目为**纯艺术纪念 PCB**，不具备电路功能，无器件、无电气网络，仅利用 PCB 板厂工艺实现正反面精美图案输出。

主题角色：**Claude 拟人「Claude 娘」**——铜橙色长发、橙花发饰、黑白橙层叠长裙、抱书的少女，社区最流行的非官方拟人设定。

- **正面（人设卡）**：宫殿烛光场景，Claude 娘端坐王座，**金色描边**沿人物轮廓勾出发丝与礼服褶皱；右上为金色 Claude 星芒 Logo 与「CONSTITUTIONAL AI」，右下为角色档案卡，全部用**沉金**呈现金属光泽：

  - **NAME**：Claude（大语言模型）
  - **SPECIES**：大语言模型
  - **AFFILIATION**：Anthropic
  - **ROLE**：宪法AI助手
  - **BIRTHDAY**：2023.03.14
  - **INTRODUCE**：以宪法AI为根基，恪守有益、诚实且无害的准则，在长文本与深度思考中传递理性。

- **背面（封号梗）**：大面积橙色底 + 白色巨型标题 **`Claude Suspended`**，配竖置半身立绘、右下角 Q 版小人，以及「CAFE STYLE」菜单式排版与动画风副标题，玩的是「又是封号的一天呢」这个社区梗。

**板子规格**

- 工程软件：嘉立创EDA专业版（v4.1.71 导出）
- 基板材质：FR-4
- 板厚：1.6 mm
- 外形：99.7 × 62.7 mm 横向圆角矩形（R3 圆角）
- 层数：**4 层**（外层彩色丝印 + 内层完整铺铜）
- 工艺：双面彩色丝印 + 沉金描边/Logo/文字
- 功能：无电气电路，纯工艺艺术板

**工艺组合**

- 彩色丝印承载正反面全彩插画主体；
- 铜层 + 阻焊开窗 + 沉金实现正面的星芒 Logo、标题与角色档案文字，成品带金属光泽，与普通丝印区分；
- 横向圆角卡片外形，手感圆润，适合桌面摆件、展示收藏。

## 📡 NFC

板内已布 NFC 线圈，贴一片 **5 × 8 mm 的 CUID 芯片**（与 GPT-PCB-Art 同方案），手机一碰即可读取，可写入自定义链接（角色页 / 本仓库地址都在里面）。

> 下单本板**不含芯片**，需自行贴装；芯片位置与封装以工程文件为准。

## 🖼️ 预览

| 正面（人设卡） | 背面（Claude Suspended） |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/ae8434c0-b79d-4564-93f7-c5fc67e09170" width="480"> | <img src="https://github.com/user-attachments/assets/5a682829-e9e2-4b2f-ba76-6b7f89819aa1" width="480"> |

> 预览图随 [Releases](https://github.com/alsunmengy/Claude-PCB-Art/releases) 一起发布，仓库内不再存大图。

## 🛠️ 使用方式

### 方式1：嘉立创EDA源工程

1. 打开嘉立创EDA专业版；
2. 文件 → 导入，选择从 [Releases](https://github.com/alsunmengy/Claude-PCB-Art/releases) 下载的 `.epro2` 工程文件（推荐最新版本）；
3. 核对：板厚、彩色丝印工艺、阻焊层颜色；
4. 直接提交打样。

> ⚠️ 重要打样提醒
> 1. 需要在下单页开启**彩色丝印工艺**；
> 2. 金色 Logo、标题、档案文字依靠**沉金镀层**实现金属效果；
> 3. 本板无任何器件、无电气网络，下单时忽略「无走线」告警；
> 4. 彩色丝印存在轻微色彩偏差属于工厂正常现象。

### 方式2：Gerber 生产文件

在 [Releases](https://github.com/alsunmengy/Claude-PCB-Art/releases) 下载对应版本的 Gerber 压缩包提交 PCB 工厂生产，注意和工厂确认支持**双面彩色丝印 + 沉金**工艺。

## 📋 打样参数（嘉立创下单页参考值）

板子为 4 层横向圆角卡片，下单时逐项核对下表即可：

| 参数 | 取值 |
|------|------|
| 板材类别 | FR-4 |
| 板子尺寸 | 10 cm × 6.3 cm |
| 板子层数 | 4 层 |
| 板子数量 | 按需选择（常见 5 / 10 片） |
| 成品板厚 | 1.6 mm（也可以更薄） |
| 外层铜厚 | 1 oz |
| 阻焊颜色 | 白色 |
| 字符颜色 | 黑色 |
| 阻焊覆盖 | 过孔盖油 |
| 焊盘喷镀 | 沉金（金色，1 u"，收费项） |
| 最小孔径 | 0.3 mm |
| 线路测试 | AOI 全测 + 飞针全测 |
| 交期 | 正常 3 天 |

> 💡 **彩色丝印**与**沉金**是本板效果的关键项（详见上方「重要打样提醒」）；其余为嘉立创默认选项，下单页如与本表有出入，以页面实际显示为准。

## 📂 文件说明

```
Claude-PCB-Art/
├─ claude_立绘_原版_3072x5504.jpg  # 主立绘原图（ZipZipPipe）
├─ claude_工程服版_941x1672.jpg    # 工程服版本（安全帽 + CLAUDE 工装）
├─ preview_主立绘.jpg / preview_工程服版.jpg
├─ sheet_originals.jpg           # 社区二创 12 张对照图
├─ sheet_crosspet.jpg            # CrossPet Q 版 57 张对照图
├─ claude_originals/             # 社区二创原图（仅作造型参考，未用于板面）
├─ crosspet/ · crosspet_png/     # CrossPet Q 版素材（WebP / 转 PNG 透明通道）
├─ 横版/ · claude_all/ · civitai/ # 横版与 AI 生成素材
├─ bdfy/                         # 蓝色大肥鱼站二创（授权不明，未用于板面）
├─ _meta/                        # 尺寸表、来源清单、许可说明
├─ SOURCES.md                    # 完整出处与授权清单（重要）
└─ .github/badges/star-banner.svg # README 顶部横幅
```

> 📦 工程源文件（`.epro2`）与 Gerber 压缩包统一在 [Releases](https://github.com/alsunmengy/Claude-PCB-Art/releases) 页面下载，请取最新版本。

## 🎨 二次创作

你可以自由修改：

- 替换正反面插画素材；
- 修改角色档案文本、Logo 排版；
- 修改板子尺寸、圆角大小；
- 调整镀层颜色、配色方案。

二次分发请遵守开源协议，并保留原素材署名。

## 📜 开源协议与素材署名

[![CC BY-NC-SA 4.0](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

本项目采用 **CC BY-NC-SA 4.0** 协议开源。

- ✅ 允许：查看、学习、修改、本地打样、非商用分享、个人自用、无偿赠与；
- ❌ 禁止：任何形式的商业性生产、销售与分销；用于广告、品牌推广、商业引流；
- ℹ️ 衍生修改版本须**沿用相同协议**（SA），并**注明原项目来源与作者**（BY）。

**板面素材署名**

- 主立绘 / 工程服立绘：**ZipZipPipe**（[Pixiv](https://www.pixiv.net/users/18604994) ｜ [Bilibili](https://space.bilibili.com/4168597)）
  - 原帖：[《AI娘化》](https://www.pixiv.net/artworks/148186519) ｜ [工程服版](https://www.pixiv.net/artworks/150718881)
  - 作者在[《"亿万"身家的她们》简介](https://www.bilibili.com/video/BV1bARXBYEZz/)中声明其图片开放，允许二次创作。
- Q 版参考素材：**CrossPet**（[lokicorvus/crosspet](https://github.com/lokicorvus/crosspet)），`characters/` 立绘为 **CC BY-NC-SA 4.0**，仅非商业使用。
- 部分网络二创图（`bdfy/`）原作者未标注，**未用于板面**，仅作造型参考，不建议再分发。

> 「Claude」为 Anthropic 商标，本作为**社区非官方拟人设计**，个人收藏 / 赠送 / 非商业分享即可，请勿批量售卖。

## 🔗 相关链接

- 打样/开源说明视频：[关于我做出来的 PCB：赠送 / 售卖 / 开源](https://b23.tv/tJhAZ84)
- 同系列作品：[DeepSeek-Mermaid PCB Art](https://github.com/alsunmengy/DeepSeek-PCB-Art) ｜ [GPT-6 Astra PCB Art](https://github.com/alsunmengy/GPT-PCB-Art) ｜ [LuoTianyi-PCB-Art](https://github.com/alsunmengy/LuoTianyi-PCB-Art) ｜ [Carlotta-PCB-Art](https://github.com/alsunmengy/Carlotta-PCB-Art)
- 角色档案：[genderswapai](https://genderswapai.com/zh-CN/ai-gijinka/claude)

---

## 📌 致谢

- 插画：**ZipZipPipe**（Pixiv / Bilibili）—— 本作主立绘与工程服版本作者
- Q 版参考素材：**CrossPet**（lokicorvus/crosspet）
- PCB 制作平台：[嘉立创EDA](https://lceda.cn/) 专业版
- 同系列灵感：DeepSeek / GPT 艺术 PCB 项目

---

<p align="center"><sub>⭐ 如果这块板子让你笑了，点个 Star 就当请我喝杯咖啡 —— 不点也谢谢你看到这里。</sub></p>

<p align="center"><sub>README 由爱弥斯 / 我共同编写</sub></p>