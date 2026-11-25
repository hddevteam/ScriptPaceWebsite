# 15 — 稿随产品官网 MVP

- MVP ID: `15-SCRIPTPACE-WEBSITE`
- Product: 稿随 / ScriptPace
- Repository: `https://github.com/hddevteam/ScriptPaceWebsite`（公开 Pages 发布仓库：`https://github.com/scriptpace/scriptpace.github.io`，默认生产源：`https://scriptpace.github.io`）
- Hosting: GitHub Pages
- Status: Video-recording workflow & bilingual SEO refactoring implemented and validated locally on `feature/website-mvp` (`2026-11-25`); public App Store record & `main` Pages deployment pending
- Source content: `/Users/ming/projects/scriptpace/project_docs/12-APP-STORE-LISTING-COPY.md`、`/Users/ming/projects/scriptpace/project_docs/14-SCRIPTPACE-SCREENSHOT-STORYBOARD.md`、`/Users/ming/projects/scriptpace/project_docs/23-DEV-016-MACOS_SCREEN_RECORDING_MVP.md`

## 1. Outcome

让视频创作者、讲师和产品演示者在第一次打开稿随官网时，在一个简洁、可信、符合 Apple 审美的静态网站中完成四件事：

1. 一眼看懂稿随如何解决**视频录制中的眼神飘移、固定滚屏追赶、停顿卡壳重来与多工具切换**问题；
2. 分清**当下即可投入视频拍摄的能力**（搭配相机/OBS/录屏工具的浮动提词、Voice Follow、iPhone/Apple Watch 镜头外盲操与转录复盘）与**即将发布的内置 Mac 屏幕/人像/音频同录、按讲稿自动归档与成片导入管理能力**（`DEV-016`）；
3. 通过搜索“Mac 提词器 / 视频录制提词 / 录课提词 / Mac teleprompter for video recording”等真实场景词准确找到对应语言的页面，并在社交分享时获得清晰的预览卡片；
4. 在遇到使用问题或需要查看隐私与条款信息时找到可靠入口。

网站是独立的静态项目，不引入账号、数据库、支付页面、云端脚本管理或后台内容系统。App Store 下载和购买仍由 App Store 完成。

## 2. User story

你要录制一段口播视频、在线课程或软件演示，但不想眼神离开镜头追着固定速度滚动的提词器读，更不想一停顿或即兴发挥就得伸手摸鼠标找段落、留下低头废片。你通过搜索引擎或社交分享进入稿随官网：先看到贴近摄像头的 Mac 浮动提词器如何跟着声音推进、如何在排练后对照转录打磨表达、如何用 iPhone Remote 或 Apple Watch 在镜头外静默调回段落；同时也清楚看到即将接入同一条工作流的 Mac 屏幕/摄像头/音频录制与字幕导出方案，最后前往 App Store 下载或查看支持说明。

## 3. Information architecture

网站使用语言独立路径，避免依赖 JavaScript 才能阅读主要内容，并补齐搜索引擎索引与社交分享所需的静态入口：

```text
/
├── zh-hans/
│   ├── index.html
│   ├── features.html
│   ├── support.html
│   ├── privacy.html
│   └── terms.html
├── en/
│   ├── index.html
│   ├── features.html
│   ├── support.html
│   ├── privacy.html
│   └── terms.html
├── assets/
│   ├── brand/
│   ├── css/site.css
│   ├── js/site.js
│   ├── og/
│   │   ├── zh-Hans/
│   │   └── en/
│   └── screenshots/
│       ├── zh-Hans/
│       └── en/
├── index.html
├── robots.txt
└── sitemap.xml
```

根路径 `index.html` 在浏览器首次访问时根据语言偏好导向 `/zh-hans/` 或 `/en/`，同时自身保留完整的中英文产品摘要与两套语言页面的静态直链，作为 `hreflang="x-default"` 的爬虫友好落地页，避免搜索引擎只抓到空壳分流页。每个本地化页面都能独立打开、带预览卡片分享、并通过 `canonical` 与 `hreflang` 被搜索引擎准确索引。

### 3.1 Home

首页不再把产品割裂为“只能练习的现在”和“才能录制的未来”，也不丢掉稿随最打动人的**语音跟随提词核心亮点**，而是按**核心提词体验 → 三端同步实拍证明 → 三大录制场景 → 即将发布的内置录制归档**组织叙事：

- **Hero（直击镜头眼神与自然语速）**：
  - 主张聚焦“直视镜头自然讲，讲稿与录制跟上你的节奏”；首屏不引入 Pro/Ultra 订阅等级名称，购买层级统一放在价值说明之后。
  - 副文案用自然第一方产品语气直接陈述固有能力（不加“现在即可 / 现已可用”等生硬限定词）：`将 Mac 悬浮提词窗贴在摄像头下方，搭配相机、OBS 或任意录屏工具实拍，并用 iPhone 与 Apple Watch 在镜头外无声调整段落。支持内置 Mac 屏幕、摄像头与音频录制接入同一工作流（即将发布）。`
  - 首屏主视觉使用**双语成对的真实 Mac 桌面录制场景截图**（主体面板采用日间浅色主题 `.aqua` 以突出界面层次，底层背景为深色讲稿/课程演示内容，上方贴近镜头位置悬浮未裁切的稿随提词器，旁侧停靠录制控制扩展与摄像头画中画预览），明确图注“Mac 贴镜头悬浮语音跟随提词 · 内置录屏扩展（即将发布）”，严禁使用卡通/AI 概念插画替代，也避免消极的“尚未发布”措辞。
- **Core teleprompter highlight（`#teleprompter` 核心亮点 · Voice Follow 语音跟随提词）**：保留并强化上一版最具说服力的提词痛点共鸣与四步工作流：
  - 先用故事对比讲透核心亮点：**“你已经准备好了内容。录制开始后，提词器不该成为新的负担。”**——解释传统匀速滚屏在停顿思考、临场发挥或口误重录时为何迫使人移开视线，而稿随贴近镜头的 Voice Follow 如何随声音推进、停顿时等待、重来时回退并支持只读转录复盘。
  - 紧接四步卡片闭环：**`01 听一遍 · 02 练一遍 · 03 跟着声音走 · 04 从容再来`**，让第一次接触稿随的创作者一眼读懂从听稿、iPhone 离线练习、Mac 贴镜头跟读到转录复盘与镜头外无声调整段落的完整提词亮点。
- **Current multi-device story（`#pro` 一个故事 · 三端自然配合）**：紧随核心提词亮点，展示同一份讲稿第三段在 Mac Voice Follow、iPhone Remote 与免费 Apple Watch 配套端上的同步真实截图（中英文各自匹配，采用自然第一方产品语气，不保留生硬的第三方旁白导语），先用已上线的完整体验建立信任。
- **Video recording use cases（`#scenarios` 三大视频录制场景）**：用创作者能直接对号入座的实拍场景展开应用方式，不堆叠重复的状态徽章：
  1. **镜头口播与多机位拍摄（深度结合 Voice Follow 语音跟随特点）**：提词窗贴近摄像头正下方保持自然眼神，**Voice Follow 随自然语速实时推进、停顿思考时自动等待、临场发挥回到原稿也能顺畅接上**；配合微单、iPhone 连续互通相机或 OBS 拍摄，并用 iPhone Remote 或 Apple Watch 在镜头外无声调整段落，告别匀速滚屏扫读感与摸鼠标的低头废片。
  2. **在线课程与长视频讲授**：先用系统朗读听顺口语感，在 iPhone 上试讲熟悉节奏，回到 Mac 正式开拍；单遍结束后对照只读语音转录快速复盘下一条 Take。
  3. **软件演示与产品 Walkthrough（解决“准备讲稿 + 设定录制范围 + 确保导出符合标准”三重痛点）**：稿随让备稿与语音跟随提词保持自然，提供全屏、单窗口、选定区域等多种录制模板并支持保存录制预置与摄像头布局预设，一键加载随时进入录制模式；导出预置既可直接合成成片，也可拆成多层素材满足直发或精剪不同场景。
- **Upcoming Mac recording（`#recording` 录制模板预置联动 + 讲稿归档/标准化导出预置双视图）**：以 `DEV-016` 真实能力为依据，直击创作者录屏时“又要准备稿子、又要反复设定录制范围、还要确保导出符合标准”的核心痛点；不在每个小标题、卡片角标和首屏胶囊上反复强调“即将发布”，仅在区块底部保留一处克制的浅色小字说明（`注：内置 Mac 屏幕、摄像头与音频录制及导出归档工作台随 Ultra 版本即将发布，具体上线时间以 App Store 页面为准。`，不使用“尚未发布 / not yet available”）：
  - **录制模板与预置联动（Capture Templates & Saved Presets）**：提供全屏、单窗口、选定区域，以及仅音频、仅摄像头多种模板；支持将录制模式、采集范围、系统声音、麦克风（可选 48 kHz/24-bit Apple Lossless）与摄像头画中画布局**保存为录制预置（`ScreenRecordingCapturePreset` + 摄像头布局预设）**，随时一键切换进入标准开拍状态；倒计时结束自动开始捕获并切入提词推进；录制中支持同步暂停/恢复（自动剔除暂停片段）；每条录制完成即存为本地独立 Take，**无需等待导出即可连续开拍下一条**。
  - **按讲稿自动归档、成片导入管理与标准化导出预置（Archive & Export Presets）**：展示真实的日间主题 **Export Editor**（左侧为展开的讲稿关联文件夹、原始录制 Take、标注 `导入`/`Imported` 徽章的外部生产成片、`全部 / 收藏 / 导入` 筛选栏、星标与单条/批量备注及 `+ 导入影片…` 入口；右侧为 `Info` / `Video` / `Camera` / `Pointer` / `Audio` / `Subtitles` 标签页、底部导出预置菜单与深色演示画面预览）。重点讲清：**关联提词讲稿录制的视频会自动按讲稿建夹归档**，支持将剪辑好的生产成片导入同一讲稿夹对照管理（移除导入项绝不误删外部原文件）；同时提供**内置导出模板（网页与设备兼容、小文件、ProRes 422 高画质、屏幕画面主体抠像、摄像头叠加素材、AAC 语音、无损音频）与可保存的自定义导出预置**——**导出的预置既可以直接合成带人像成片，也可以拆成屏幕、人像、音轨与同步 `.srt` 字幕的多层素材包**，满足快速直发与专业剪辑时间线等不同场景需求。
- **Pricing（`#plans` 提词方案与录制方案清晰呈现）**：面向用户使用自然的产品标题（如“专注镜头提词，或一站式完成屏幕录制与归档”，严禁把“把当前可用权益与即将发布的录制方案清楚分开”等内部 PRD 合规元话术直接印在页面上）。Pro 月度 `$1.99/月`、年度 `$15.99/年`（明确说明**仅限语音跟随提词、语音练习与多端遥控等稿随核心功能，不包含内置屏幕录制**）与 Ultra 年度 `$29.99/年`、永久买断 `$89.99` 同级清晰展示，**将 `推荐` / `Recommended` 主推标记放在 `年度 Ultra` / `Annual Ultra` 上**，并在价格区底部用一行轻量说明提示试用规则与 Ultra 即将发布状态。
- **Privacy promise（本地优先承诺）**：标题使用自然用户表达（“本地优先，讲稿与音视频留在你的设备上”，不写“把……边界说清楚”等内部文档措辞）；无需应用账号，说明 Voice Follow/练习语音不保存为原始麦克风音频，而内置录制（即将发布）将音视频与导入成片保存在本地 Mac、不上传稿随服务器。
- **Footer**：功能、支持、隐私政策、使用条款、App Store、支持邮箱、语言切换。

#### 3.1.1 与竞品的差异点（内部定位草案）

**核对日期：2026-11-25。** 以下依据竞品官方公开页面和稿随当前产品/MVP 文档整理，用于指导网站叙事，不是全市场功能审计。竞品页面未提到某项能力，不能据此推断其产品一定不支持该能力。

**核心定位**

稿随服务需要直视镜头口播、录制课程和边讲解边演示屏幕的人：让讲稿跟随自然表达，并把听稿备课、iPhone 试讲、Mac 近镜头提词、iPhone/Watch 镜头外盲操调位，以及即将推出的 Mac 屏幕/人像录制与字幕导出组织成一条连续的视频创作工作流。Mac 内置录制仍在开发中；发布前不得把内置录屏描述成当前已经可用，但应当充分展示当前版本配合外部相机/录屏工具实拍视频的真实场景价值。

**当前可以讲的产品价值（现已支持视频实拍）**

1. **实拍眼神与自然语速**：Mac 浮动提词窗口可紧贴摄像头下方，Voice Follow 根据实时识别到的表达推进讲稿，减少固定滚屏造成的追赶、等待与读稿感；遇到停顿或重录口令时可快速回到上一句重拍。
2. **拍前排练与转录复盘**：创作者可先用系统声音听稿检查口语顺畅度、在 iPhone 上离线试讲，再上 Mac 实拍；结束后对照只读语音转录定位卡壳段落，完善下一条 Take。
3. **镜头外无声控场**：搭配相机、OBS 或其他录屏软件实拍时，可用 iPhone Remote 扫码连接或抬腕用免费的 Apple Watch 数码表冠切换上一段/下一段，避免因即兴发挥或错位去摸鼠标而产生需要剪掉的低头镜头。这些能力服务于连续拍摄，但不单独宣称为行业独有。

**计划中的差异方向（DEV-016）**

DEV-016 完成并发布后，用户可以直接在稿随内选择显示器、窗口或选定区域，录制屏幕与系统/麦克风声音并按需加入摄像头；有讲稿时，倒计时归零自动启动录制并与 Mac 提词联动推进，支持多条 Take 连拍。每条关联讲稿录制的视频会自动按当前讲稿建夹归档，同时支持将外部剪辑定稿的生产视频导入同一讲稿夹中，通过 `全部 / 收藏 / 导入` 筛选、星标收藏与备注与原始录制素材放在一起对照管理（从列表移除导入项绝不删除外部原文件）。录制素材保留在本地，可在非破坏性导出编辑器中调整摄像头画中画形状与位置、开关鼠标点击高亮、按需启用主体抠像，并导出单一影片或分层素材包及同步 `.srt` 字幕/逐词时间 JSON。这个“拍前练节奏 → 拍中跟声音并捕捉画面 → 拍后按讲稿自动归档、管理成片并本地出字幕”的闭环体验，是网站重点验证和展示的差异方向。

| 比较对象 | 官方页面公开强调的能力 | 对稿随定位的启示 |
| --- | --- | --- |
| PromptSmart | VoiceTrack 随说话推进，停顿或即兴时暂停并在回到讲稿时继续；也提供网页控制台管理内容。 | 语音跟随本身不是稿随独有。应突出稿随贴近真实视频拍摄的“听稿排练 → 转录复盘 → Remote 盲操恢复 → 计划中的 Mac 演示同录与字幕交付”完整链路。 |
| Teleprompter.com | VoiceGlide、视频/音频录制、直播、跨平台使用与录制文件同步，并公开提供 Apple Watch 和远程控制能力。 | 不要声称语音跟随、提词录制、跨设备或 Watch 控制独家。稿随应聚焦 Mac 桌面课程/软件演示录制、多 Take 本地管理与非破坏性画中画/字幕导出的结合，并如实说明发布状态。 |
| Screen Studio | macOS 全屏/窗口/区域录制、摄像头、麦克风和 Mac 声音，另有讲者备注、转录编辑、字幕、相机布局与本地处理。 | 单独凭录屏编辑能力难以形成稳固差异（定位推断）。稿随的差异应落在实时语音跟随提词、拍前练习复盘、iPhone/Watch 跨端控场与 Mac 演示录制的深度衔接。 |

**推荐的用户表达**

- 中文主张：`直视镜头自然讲，让讲稿与录制跟上你的节奏。`（副句：`将 Mac 悬浮提词窗贴在摄像头下方，搭配相机、OBS 或任意录屏工具实拍，并用 iPhone 与 Apple Watch 在镜头外无声调整段落。支持内置 Mac 屏幕、摄像头与音频录制接入同一工作流（即将发布）。`）
- 英文主张：`Deliver naturally on camera. Keep your script and recording in rhythm.`（Subcopy: `Pin the floating Mac teleprompter right beneath your camera to film with any camera, OBS, or screen recorder—and adjust paragraphs silently off-camera from iPhone and Apple Watch. Built-in Mac screen, camera, and audio recording connects into the same workflow (coming soon).`）
- 首页先讲核心语音跟随提词亮点与多端同步实拍，再展开三大录制场景与即将发布的内置录制归档，进入价格区才解释 Pro/Ultra；面向用户的标题严禁搬用内部 PRD 合规话术（如“把当前可用权益与即将发布的录制方案清楚分开”）。订阅等级是购买方式，不是用户理解产品的入口。

**对外文案边界**

- 不宣称稿随是第一款、唯一款或最好的语音跟随提词器/录屏工具；本次核对的竞品已覆盖其中多项单点能力。
- 不把本地处理、免账号、Apple Watch、iPhone Remote 或提词时录制作为单独的独家卖点；可以将它们作为稿随视频工作流的信任属性和组成部分。
- 在 DEV-016 发布前，不写“现在即可在稿随内录制屏幕”“一键开始录屏并自动跟随”等会让用户误以为内置录屏已上线的句子；凡涉及内置采集、按讲稿归档与成片导入管理、Export Editor、画中画合成与 SRT 导出，统一附带正向清晰的“即将发布 / Coming soon”状态标识（不使用消极生硬的“尚未发布 / not yet available”）。
- 在 Universal Purchase 和各平台实际权益验证前，不对外承诺一次购买覆盖所有 Apple 平台。
- 竞品资料以官方页面为准，页面信息可能变化。面向公开发布前应重新核对；如要使用“优于/独有”等比较级，需额外证据支持。

**核对来源**

- PromptSmart 官方产品页：<https://www.promptsmart.com/> — VoiceTrack 及网页内容控制说明。
- Teleprompter.com 官方平台功能页：<https://www.teleprompter.com/platform-features> — VoiceGlide、录制、跨设备与 Remote/Apple Watch 说明。
- Screen Studio 官方产品页：<https://screen.studio/> — Mac 屏幕录制、音频/摄像头、讲者备注与编辑功能说明。
- 稿随产品能力源文件：`/Users/ming/projects/scriptpace/project_docs/12-APP-STORE-LISTING-COPY.md`；录屏状态和范围：`/Users/ming/projects/scriptpace/project_docs/23-DEV-016-MACOS_SCREEN_RECORDING_MVP.md`。

### 3.2 Features

功能页围绕**视频录制的三个阶段**组织，不堆叠底层 API，也不在标题或标签中强迫访客先理解 Pro/Ultra 等级名称：

1. **阶段一 · 拍前备稿与试讲（当前可用）**
   - **Mac 讲稿预览与系统朗读**：导入 Markdown/纯文本等受支持讲稿，开拍前用系统声音按可调语速听一遍，提前发现拗口长句。
   - **iPhone 语音练习**：上镜前在 iPhone 上用碎片时间完成跟读排练，建立段落熟悉度。
   - **只读转录对照回看**：试讲或单遍实拍后，将实际说出的只读转录文本与原讲稿并排对照（必须配中英文真实界面截图，严禁使用英文纯文字占位卡），明确声明稿随不会自动改写用户讲稿。
2. **阶段二 · 实拍眼神与镜头外控场（当前可用）**
   - **贴近镜头的 Mac 浮动提词器**：将提词面板置于摄像头正下方或演示区域旁，搭配相机、OBS 或第三方录屏软件实拍时保持自然平视眼神。
   - **Voice Follow 实时语音跟随**：讲稿随自然语速推进，停顿思考时不乱滚，重录上一句时快速回位。
   - **iPhone Remote 扫码盲操**：录制中即兴发挥或段落偶发错位时，在镜头外轻点上一段/下一段静默恢复位置，不打断拍摄状态。
   - **Apple Watch 免费配套控制**：站立讲授或双手演示不便拿手机时，旋动 Digital Crown 或轻点腕上按钮调整段落。
3. **阶段三 · 内置 Mac 屏幕人像录制与讲稿素材归档（即将发布）**
   - **多源采集与提词倒计时联动**：支持全屏、单窗口、选定区域，以及仅音频、仅摄像头录制；倒计时结束自动启动采集并切入提词推进；支持录中暂停剔除与多条 Take 连续录制。
   - **按讲稿自动归档、成片导入管理与非破坏性导出**：关联讲稿录制的视频自动归入同名讲稿文件夹，支持导入外部生产成片（标注 `导入` / `Imported`）与源素材同夹管理、星标收藏、写备注及按 `全部 / 收藏 / 导入` 筛选（移除导入项绝不删除外部原文件）；并在内置 Export Editor 中独立调整摄像头画中画（圆形/矩形/方形/镜像/四角位置）、鼠标指针与点击高亮、主体背景移除，按需导出单一影片、分层素材包或同步 `.srt` 字幕文件。统一标为“即将发布 / Coming soon”。

公开网站不得声称自动改稿、云端写作、云端历史、完美识别、练习模式原始音频归档或单独购买 Apple Watch。发布版本不公开宣传源文件编辑能力。

### 3.3 Support

支持页包含：

- 快速开始：下载、打开 Mac、导入讲稿、将浮动窗放在摄像头附近、扫码连接 Remote，以及**如何配合外部相机/OBS/录屏软件直接投入当前视频拍摄**。
- Mac：提词器、朗读、Voice Follow、转录对照回看，并明确内置录屏及按讲稿自动归档/成片导入工作台即将发布；发布后的购买权益以 App Store 页面为准。
- iPhone Remote：配对、连接、上一段/下一段、实拍即兴表达后的错位恢复。
- Apple Watch：免费配套关系、Digital Crown、上一段/下一段。
- 购买与恢复：月度/年度 Pro（仅限提词、练习与多端遥控，不含内置屏幕录制）、即将开放购买的年度/永久买断 Ultra、同一 Apple Account、Universal Purchase 和 Restore Purchases。
- 常见问题（同时服务长尾支持与 `FAQPage` 搜索展现）：内置屏幕录制当前是否可用、当前如何配合相机/其他录屏工具拍视频、Remote 未连接排查、实拍中段落错位如何无声恢复、跨设备恢复购买、练习语音与录制媒体的本地隐私边界。
- 联系支持：可点击的支持邮箱和版本/设备信息请求说明。

Support URL 必须能让用户找到真实的联系方式，并与 App Store Connect 中配置的 Support URL 保持一致。

### 3.4 Privacy Policy

隐私政策必须说明：

- 收集或不收集哪些数据。
- 脚本和练习转录的本地处理边界。
- 麦克风与媒体保存边界：明确区分 **Voice Follow 与语音练习不会保存原始麦克风音频**，而未来版本若用户主动使用内置屏幕/摄像头/音频录制，其主动录制的源素材仅保存在用户本地 Mac（如本地录制目录）直至用户自行删除，绝不上传至稿随自建服务器。在 DEV-016 正式上架前同步完成隐私条款与 App Store 隐私申报核对。
- App Store、StoreKit 和系统语音服务的角色。
- 数据保留、删除和用户咨询路径。
- 不使用应用账号、广告追踪或自建遥测服务的事实；如发布前实现发生变化，必须先更新文本和 App Store 隐私申报。
- 生效日期、联系邮箱和中英文版本对应关系。

### 3.5 Terms of Use

使用条款必须覆盖：

- 软件许可和允许的使用方式。
- 月度/年度自动续期订阅和取消路径。
- 买断方案是一次性购买，只永久解锁购买时约定范围内的当前稿随功能集，不承诺未来云服务或其他独立产品线。
- 购买、退款和 Apple 作为支付平台的边界。
- 语音跟随、转录结果与导出字幕的合理使用限制。
- 服务变化、免责声明、联系方式和生效日期。

## 4. Visual system

- 视觉方向：Apple 风格的克制、留白、清晰层级和**富有临场感的真实视频录制画面**。
- 背景：暖白和浅灰为主；深色 Hero 用于建立桌面录制与镜头提词的沉浸对比，但不使用廉价渐变堆叠。
- 强调色：从稿随图标提取的低饱和暖色，仅用于 CTA、发布状态胶囊和重点步骤索引。
- 字体：优先系统字体栈，中文使用系统中文字体，英文使用系统无衬线字体。
- 圆角：卡片和按钮使用中等圆角，避免过度“玻璃拟态”。
- 动效：仅保留淡入、悬停和移动端菜单过渡；`prefers-reduced-motion` 下关闭非必要动画。
- **截图与真实性硬性规范**：
  - **严禁使用 AI 概念插画或假 UI 插图**（如卡通人物、虚构时间轴）替代产品画面；严禁在中文页面使用英文纯文字占位卡替代缺失截图。
  - **中英文 1:1 严格对称**：`assets/screenshots/zh-Hans/` 与 `assets/screenshots/en/` 必须拥有一一对应的真实应用截图（包含桌面录制场景预览图、Export Editor 预览图、转录对照图及多端同步图），界面语言与演示讲稿语言严格一致。
  - **还原真实视频录制上下文**：展示 Mac 提词与录制扩展时，桌面背景应呈现真实的被演示内容（如课程幻灯片或产品窗口）与自然激活状态（提词首行完整无半截裁切、音频/状态栏显示自然），避免孤立黑底设置框造成的“静态配置弹窗感”。
  - **禁止裁切 UI 边缘与防止布局偏移**：产品截图容器不得使用会裁断窗口边缘的 `object-fit: cover`；所有 `<img>` 必须显式声明真实 `width` 与 `height` 属性，提供压缩后的 WebP（含 PNG 回退，单张主图目标 `< 350 KB`），首屏主图添加 `fetchpriority="high"`，首屏以下图片使用 `loading="lazy"`。

## 5. Responsive behavior

- Mobile: `320px` 至 `767px`，单列内容、紧凑导航、截图自适应完整展示且不横向溢出。
- Tablet: `768px` 至 `1199px`，双列场景/功能卡和适度缩短 Hero 间距。
- Desktop: `1200px` 以上，最大内容宽度 `1120px`，两列或三列布局，截图与说明并排。
- 所有主要操作和正文在键盘、触摸和屏幕阅读器下可访问。
- 不依赖 hover 才能发现功能；焦点状态必须清晰可见。

## 6. SEO 与搜索可见性规范（SEO & Discoverability）

### 6.1 搜索意图与双语关键词策略

页面 `<title>`、`<meta name="description">`、`<h1>` 与二级标题必须围绕**视频创作者的真实搜索词**撰写，不在标题中堆砌访客尚未认知的内部代号（如单独写 `Pro 与 Ultra`、`Voice Follow`）：

- **中文核心场景词**：`Mac 提词器`、`语音跟随提词器`、`视频录制提词器`、`口播提词软件`、`录课提词器`、`Mac 录屏提词`、`iPhone 遥控提词器`、`Apple Watch 控制提词器`。
- **英文核心场景词**：`Mac teleprompter app`、`voice-following teleprompter`、`voice-activated teleprompter for Mac`、`teleprompter for video recording`、`teleprompter for course & screen recording`、`Apple Watch teleprompter remote`。
- **关键页面元数据基准**：
  - `zh-hans/index.html` Title：`稿随 ScriptPace — Mac 语音跟随提词器 · 口播、录课与屏幕演示工作流`
  - `en/index.html` Title：`ScriptPace — Voice-Following Mac Teleprompter for Video & Screen Recording`
  - `zh-hans/features.html` Title：`稿随功能 — Mac 悬浮提词、语音声控跟读、iPhone/Watch 遥控与录屏计划`
  - `en/features.html` Title：`ScriptPace Features — Mac Floating Teleprompter, Voice Follow, Remote & Screen Recording Plan`
  - `zh-hans/support.html` Title：`使用支持与常见问题 — 稿随 ScriptPace Mac 视频提词与遥控指南`
  - `en/support.html` Title：`Support & FAQ — ScriptPace Mac Teleprompter & Remote Setup Guide`
  - 凡在标题或描述中提及录屏能力，描述文本必须明确“内置 Mac 屏幕与音频录制即将推出 / coming soon”，避免搜索摘要产生功能已上线的误导。

### 6.2 双语索引、`canonical`、`hreflang` 与站点地图

- **唯一生产源（`siteOrigin`）**：在自定义域名 `CNAME` 确认前，统一以 `https://scriptpace.github.io` 作为绝对 URL 基准（写入 `site-config.js` 与构建校验脚本），消除文档与配置间的仓库 URL 混用。
- **`canonical` 与 `hreflang` 全覆盖**：全站 11 个 HTML 页面均须在 `<head>` 声明：
  - 指向自身绝对 URL 的 `<link rel="canonical" href="...">`；
  - 成对互指的 `<link rel="alternate" hreflang="zh-Hans" href="...">` 与 `<link rel="alternate" hreflang="en" href="...">`；
  - 指向根路径 `https://scriptpace.github.io/` 的 `<link rel="alternate" hreflang="x-default" href="...">`（子页面 `x-default` 指向对应 `/en/<page>.html`）。
- **爬虫友好的根路径 `index.html`**：保留面向真人访客的首次语言自动跳转（`sessionStorage` 防死循环），同时在 HTML 正文中提供简明双语定位说明与通往 `/zh-hans/`、`/en/` 核心页面的静态 `<a>` 链接，确保不执行跳转的爬虫仍能抓取语义内容与内链。
- **`robots.txt` 与 `sitemap.xml`**：根目录提供 `robots.txt`（声明 `Sitemap: https://scriptpace.github.io/sitemap.xml`）和包含全部公开双语路由及 `xhtml:link` 多语言映射的 `sitemap.xml`。

### 6.3 社交分享卡片（Open Graph & X/Twitter Cards）

创作者常在 B 站、小红书、微信、YouTube 简介、X、Discord 与 Slack 分享工具链接，所有公开页面（含 `index`、`features`、`support`、`privacy`、`terms`）均须配置完整预览元数据：

- `og:title`、`og:description`、`og:type="website"`、`og:url`、`og:site_name`；
- `og:locale`（中文页 `zh_CN` + `og:locale:alternate="en_US"`；英文页 `en_US` + `og:locale:alternate="zh_CN"`）；
- 本地化 `1200×630` 分享预览图 `og:image`（`assets/og/zh-Hans/social-card.png` 与 `assets/og/en/social-card.png`，展示真实视频提词工作流并附 `og:image:width="1200"`、`og:image:height="630"`、`og:image:alt`）；
- `twitter:card="summary_large_image"`、`twitter:title`、`twitter:description`、`twitter:image`。

### 6.4 结构化数据（Schema.org JSON-LD）

- **首页 `SoftwareApplication`**：中英文首页分别内嵌本地化 JSON-LD，声明 `name`、`applicationCategory: "VideoApplication"`、`operatingSystem: "macOS, iOS, watchOS"`、`url`、`downloadUrl`、`screenshot` 及**当前已上架的 Pro 订阅 `offers`**。在 Ultra 正式上架 App Store 前，不得将未开放购买的 Ultra 价格写入结构化数据 `Offer`，以免违反搜索引擎富结果规范。
- **支持页 `FAQPage`**：中英文 `support.html` 内嵌与页面可见 `<details><summary>` 问答完全一致的 `FAQPage` JSON-LD，提升长尾使用与排障问题的搜索展现。

## 7. Technical boundary

- 纯静态 HTML、CSS 和少量 JavaScript。
- 无前端框架、无第三方分析、无远程字体、无后端 API。
- 共享 `assets/css/site.css`、`assets/js/site.js` 和页面片段约定；页面主体按语言独立维护，避免运行时翻译造成内容错配。
- GitHub Pages 从公开发布仓库的 `main` 分支发布。
- 通过 Python 校验脚本与 GitHub Actions 执行 HTML 结构检查、SEO/社交元数据检查、双语截图对称性检查、链接检查和部署。
- 自定义域名先保留配置入口；在真实域名确认后再同步更新 `CNAME`、`siteOrigin`、`canonical`、`og:url` 与 `sitemap.xml`，不猜测域名。

## 8. BDD acceptance criteria

### Scenario A: Language routing and crawler-friendly root

Given a user or search crawler opens the root URL
When a browser with Simplified Chinese or English preference visits for the first time
Then the user reaches the matching localized home page and can switch language without losing the current page type
And when a crawler reads `/` without executing session redirects, it still finds bilingual product context, `hreflang` links, and crawlable links to `/zh-hans/` and `/en/`.

### Scenario B: Video-recording story-led home

Given a visitor opens either localized home page
When the visitor reads the hero, video use cases, and recording workflow sections
Then the page explains how ScriptPace supports natural on-camera and walkthrough delivery today (alongside cameras or external recorders) before introducing subscription tiers
And clearly separates currently available prompting/practice/Remote capabilities from upcoming built-in Mac recording (`DEV-016` capture + Export Editor + SRT subtitles)
And presents matching real product screenshots and the same release status in both languages without AI concept illustrations.

### Scenario C: Stage-based features and symmetric locale screenshots

Given a visitor opens the features page
When the visitor reads the pre-shoot rehearsal, live prompting/Remote control, and upcoming Mac recording stages
Then every stage uses authentic, uncut screenshots whose UI language, script text, and captions match the page locale 1:1
And no Chinese page falls back to an English text placeholder card or unlocalized artwork
And Apple Watch is described as a free companion without a separate purchase.

### Scenario D: Support and contact

Given a user opens the support page
When the user follows quick-start steps for external-recorder setups or a troubleshooting FAQ
Then the user can find the relevant setup steps and a real support contact
And the page does not require login or JavaScript to reveal the contact information.

### Scenario E: Legal access and recording privacy boundary

Given a user opens any localized page
When the user navigates to the privacy policy or terms page from the footer
Then the localized legal pages are reachable
And the privacy policy clearly distinguishes non-retained practice speech from locally stored user-initiated recordings without server uploads, matching App Store Connect disclosures.

### Scenario F: Responsive accessibility and Core Web Vitals stability

Given a user opens the site at mobile, tablet, or desktop width
When the page loads and the user navigates with touch or keyboard
Then content and screenshots remain readable without horizontal overflow, cropped UI edges, or layout shift (`width`/`height` declared on all images)
And focus indicators, semantic headings, alt text, and reduced-motion behavior remain available.

### Scenario G: Upcoming recording release status

Given a visitor sees the built-in screen-recording feature, script-organized Export Editor preview, or Ultra plan
When the visitor reads the home, features, or support page
Then the page clearly marks built-in recording and Ultra plans as coming soon (`即将发布` / `Coming soon`, avoiding negative `尚未发布` / `not yet available` phrasing)
And distinguishes current Pro pricing (prompting & Remote only, excluding screen recording) from upcoming Ultra pricing without implying an unannounced availability date.

### Scenario H: Bilingual SEO, social preview, and structured data

Given a search engine crawler or social-platform link unfurler fetches any public page
When it inspects `<head>`, `/robots.txt`, and `/sitemap.xml`
Then every page exposes valid self-referencing `canonical`, paired `zh-Hans`/`en`/`x-default` `hreflang`, localized video-workflow `<title>` and `<meta description>`, and complete Open Graph / Twitter `1200×630` card tags
And localized home and support pages contain valid `SoftwareApplication` (current Pro offers only) and `FAQPage` JSON-LD matching visible page text.

## 9. Validation

- Validate every route (`/`, `/zh-hans/*`, `/en/*`, `/robots.txt`, `/sitemap.xml`) with a local static server.
- Test Chinese and English root routing in a browser with changed language preferences, plus non-redirect crawler inspection of `/`.
- Test mobile, tablet, and desktop widths in Chrome; confirm zero CLS and no `object-fit: cover` truncation on product UI screenshots.
- Verify 1:1 screenshot symmetry across `zh-Hans` and `en` against the storyboard and `DEV-016` UI; reject AI concept illustrations and mixed-language placeholder cards in `scripts/check-responsive-assets.py`.
- Enforce automated SEO & metadata checks in `scripts/check-site.py`: single `<h1>`, `canonical`, `hreflang` (`zh-Hans`, `en`, `x-default`), `og:title`/`og:description`/`og:image`/`og:url`, `twitter:card`, `img[width][height]`, and valid JSON-LD parsing without unpublished Ultra `Offer` entries.
- Run `scripts/check-links.py` and fail on missing local assets, missing `og:image` files, or broken internal links.
- Run Lighthouse for accessibility, performance, SEO, and best practices.
- Verify the GitHub Pages deployment URL (`https://scriptpace.github.io`) and all localized/legal/support routes after publishing.
- Confirm App Store Connect Support URL and Privacy Policy URL point to the deployed pages before submission.

## 10. PDCA record

### Plan

1. **Baseline MVP**: Build and publish a static bilingual product website with the smallest complete marketing, support, and legal surface required for the first App Store release.
2. **2026-11-25 Video-Recording & SEO Refactoring Plan**: Refactor narrative, visual assets, and technical SEO so the site authentically reflects video-recording workflows (on-camera talking head + course recording today; `DEV-016` screen/camera capture, non-destructive Export Editor, and SRT delivery coming soon) and ranks for real bilingual creator search queries.

### Do

The implementation is recorded in:

- `465269c` — website MVP design, numbered project document, and implementation plan;
- `30317a8` — bilingual static website, responsive visual system, ten locale-matched screenshots, support/legal pages, and GitHub Pages workflow;
- `ea5fdfd` ~ `266cc45` — device-aligned screenshot story, public support contact configuration, finalized legal preview guards, and `scriptpace` organization remote setup;
- `2026-11-25` (`feature/website-mvp` refactoring increment):
  - Refactored `index.html`, `zh-hans/{index,features,support,privacy,terms}.html`, and `en/{index,features,support,privacy,terms}.html` around the three video-recording scenarios (on-camera talking head with external cameras/OBS, online course rehearsal & review, software walkthroughs) and three creation stages, plus the dual `DEV-016` Capture + Export Editor showcase;
  - Generated 1:1 symmetric `zh-Hans` / `en` macOS UI captures (`06-mac-prompter-recording`, `07-mac-export-editor`, `08-mac-transcript-comparison`), `<picture>` WebP variants (`< 115 KB`), and `1200×630` Open Graph cards (`assets/og/{zh-Hans,en}/social-card.png`), and removed AI concept illustrations;
  - Added `/robots.txt`, `/sitemap.xml` (11 URLs, 33 `xhtml:link` alternates), self-referencing `canonical`, paired `hreflang` (`zh-Hans`, `en`, `x-default`), Open Graph / Twitter Card tags, `SoftwareApplication` & `FAQPage` JSON-LD, explicit `img[width][height]`, WCAG AA contrast tokens, and upgraded `scripts/check-site.py`, `scripts/check-links.py`, and `scripts/check-responsive-assets.py`.

### Check

Local validation & quantitative Before/After SEO benchmark evidence (`2026-11-25`):

- `node --check site-config.js` passed;
- `python3 scripts/check-site.py --production` passed;
- `python3 scripts/check-links.py` passed;
- `python3 scripts/check-responsive-assets.py` passed (all symmetric `zh-Hans` / `en` PNG + WebP screenshots and `1200×630` OG cards verified);
- `git diff --check` passed;
- Headless Chrome verification across all 13 routes (`/`, `/robots.txt`, `/sitemap.xml`, `/zh-hans/*`, `/en/*`) returned HTTP `200`, confirmed `zh-CN` → `/zh-hans/` and `en-US` → `/en/` root routing, verified zero horizontal overflow at `375px` / `900px` / `1440px`, and measured `maxCLS = 0`;
- Lighthouse audits (`chrome-devtools`):
  - `/zh-hans/` (Desktop): Accessibility `95` (36 failed nodes) → **`100` (0 failed)**; Best Practices **`100`**; SEO **`100`**; Agentic Browsing **`100`**;
  - `/en/features.html` (Mobile): Accessibility `95` (20 failed nodes) → **`100` (0 failed)**; Best Practices **`100`**; SEO **`100`**; Agentic Browsing **`100`**.

| 量化评估维度 | 改版前 (Before) | 改版后 (After) | 变化幅度 |
| --- | --- | --- | --- |
| **综合深度 SEO 指数（满分 100）** | `19.6 / 100` | **`100.0 / 100`** | **+80.4 分（5.1×）** |
| 技术索引与多语言互指（30 分：`canonical` + `hreflang` + `robots/sitemap`） | `0.0 / 30`（`0/11` 页） | **`30.0 / 30`**（`11/11` 页 + 11 URL / 33 互指） | **+30.0 分（0% → 100%）** |
| 社交卡片与结构化数据（25 分：完整 OG + Twitter + JSON-LD） | `0.0 / 25`（0 张 `og:image`，0 个实体） | **`25.0 / 25`**（11/11 页完整卡片，4 个实体 / 12 条 FAQ） | **+25.0 分（0% → 100%）** |
| 视频录制搜索意图覆盖（30 分：中英各 8 类核心创作者词簇） | `17.5 / 30`（Title/H1-H2：中 `50%` / 英 `37.5%`） | **`30.0 / 30`**（Title/H1-H2：中 **`100%`** / 英 **`100%`**） | **+12.5 分（全覆盖）** |
| Core Web Vitals 资产就绪度（15 分：宽高防偏移 + 首屏主图体积） | `2.1 / 15`（`0/41` 声明宽高；主图 中 `951 KB` / 英 `1,718 KB`） | **`15.0 / 15`**（`49/49` 声明宽高；WebP 主图 中 **`80.9 KB`** / 英 **`83.7 KB`**） | **主图体积缩减 91.5% / 95.1%** |
| 根路径 `/` 非重定向爬虫可读字符 / 内链数 | `117 字符 / 3 链接` | **`384 字符 / 9 链接`** | **+228% 文本 / 3× 内链** |
| Lighthouse Accessibility（桌面 `/zh-hans/` & 移动 `/en/features.html`） | `95 / 100`（36 处对比度与命名违规） | **`100 / 100`（0 违规）** | **+5 分（清零违规）** |

Remaining external release gates before public promotion: App Store record public visibility (current `appStoreURL` returns HTTP `404` pre-release) and explicitly authorized push/merge to the `main` GitHub Pages deployment branch.

### Act

Retain `python3 scripts/check-site.py --production`, `check-links.py`, and `check-responsive-assets.py` as mandatory CI gates in `.github/workflows/pages.yml`. Once the App Store listing goes public and `DEV-016` ships, update the release status badges and add Ultra `Offer` entries to `SoftwareApplication` JSON-LD to match live App Store entitlements.

## 11. Retrospective

The first implementation rightly excluded accounts, a CMS, support tickets, analytics, cookies, payment collection, and premature custom-domain DNS. The `2026-11-25` design review showed that strict release compliance ("built-in screen recording is not shipped yet") must not obscure the product's primary identity as a **video-recording workflow tool**: creators film today with cameras and external recorders, and need concrete visual proof—plus proper bilingual SEO, `hreflang`, social cards, and structured data—to discover ScriptPace and understand both today's on-camera prompting flow and the upcoming built-in Mac recording studio.
