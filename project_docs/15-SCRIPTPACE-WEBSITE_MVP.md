# 15 — 稿随产品官网 MVP

- MVP ID: `15-SCRIPTPACE-WEBSITE`
- Product: 稿随 / ScriptPace
- Repository: `https://github.com/hddevteam/ScriptPaceWebsite`
- Hosting: GitHub Pages
- Status: Implemented on `feature/website-mvp`; release configuration pending
- Source content: `project_docs/12-APP-STORE-LISTING-COPY.md` and `project_docs/assets/14-scriptpace-screenshots/`

## 1. Outcome

让第一次了解稿随的人在一个简洁、可信、适合 Apple 用户阅读的网站中完成三件事：理解稿随如何帮助自然表达，找到对应设备和工作流的功能说明，以及在遇到问题或需要查看法律信息时找到可靠入口。

网站是独立的静态项目，不引入账号、数据库、支付页面、云端脚本管理或后台内容系统。App Store 下载和购买仍由 App Store 完成。

## 2. User story

你已经准备好了课程、演讲或视频内容，但录制时不想追着固定速度滚动的提词器走。你先了解稿随如何让 Mac 提词器跟着声音推进，再在 iPhone 上练习、用 Remote 调整位置，必要时用 Apple Watch 做补充控制，最后从网站进入 App Store 或支持页面。

## 3. Information architecture

网站使用语言独立路径，避免依赖 JavaScript 才能阅读主要内容：

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
│   ├── screenshots/zh-Hans/
│   └── screenshots/en/
└── index.html
```

根路径根据浏览器语言将用户导向 `/zh-hans/` 或 `/en/`，并提供明确的手动语言切换。每个本地化页面都能独立打开、分享和被搜索引擎读取。

### 3.1 Home

- Hero：产品名称、核心承诺、Mac/iPhone/Apple Watch 设备组合和 App Store CTA。
- Story：固定速度提词器在真实录制中的追赶、等待、停顿和重来的问题。
- Workflow：听一遍、练一遍、跟随表达、Remote 调整、完成后回看。
- Product surfaces：Mac 主提词器、iPhone 练习与 Remote、Apple Watch 免费配套控制。
- Screenshot story：使用已确认的中英文截图，不混用语言或使用未配对状态。
- Pro pricing：月度 `$1.99/月`、年度 `$15.99/年`、创始人买断 `$45.99`，明确订阅自动续期和买断一次性付款。
- Privacy promise：无需应用账号、不保存原始麦克风音频、在支持的设备上本地处理。
- Footer：功能、支持、隐私政策、使用条款、App Store、语言切换。

### 3.2 Features

围绕用户价值解释功能，不堆叠 API 或实现细节：

1. 让讲稿跟着自然表达推进。
2. 先听讲稿，再在 iPhone 上练习。
3. 在 Mac 上完成 Voice Follow 和录制准备。
4. 用 iPhone 扫码连接 Remote，必要时调整段落位置。
5. 用 Apple Watch 在不方便拿 iPhone 时补充控制。
6. 练习结束后回看只读转录结果。

公开网站不得声称自动改稿、云端写作、云端历史、完美识别、原始音频归档或单独购买 Apple Watch。发布版本不公开宣传源文件编辑能力。

### 3.3 Support

支持页包含：

- 快速开始：下载、打开 Mac、导入讲稿、扫码连接 Remote。
- Mac：提词器、朗读、Voice Follow、练习结果回看。
- iPhone Remote：配对、连接、上一段/下一段、错位恢复。
- Apple Watch：免费配套关系、Digital Crown、上一段/下一段。
- 购买与恢复：月度、年度、买断、同一 Apple Account、Universal Purchase 和 Restore Purchases。
- 常见问题：权限、配对失败、语音服务不可用、恢复购买、支持的系统范围。
- 联系支持：可点击的支持邮箱和版本/设备信息请求说明。

Support URL 必须能让用户找到真实的联系方式，并与 App Store Connect 中配置的 Support URL 保持一致。

### 3.4 Privacy Policy

隐私政策必须说明：

- 收集或不收集哪些数据。
- 脚本和练习转录的本地处理边界。
- 原始麦克风音频不保存、不上传的产品承诺。
- App Store、StoreKit 和系统语音服务的角色。
- 数据保留、删除和用户咨询路径。
- 不使用应用账号、广告追踪或自建遥测服务的事实；如发布前实现发生变化，必须先更新文本和 App Store 隐私申报。
- 生效日期、联系邮箱和中英文版本对应关系。

### 3.5 Terms of Use

使用条款必须覆盖：

- 软件许可和允许的使用方式。
- 月度/年度自动续期订阅和取消路径。
- Founder Lifetime 是一次性购买，只永久解锁当前稿随 Pro 产品线，不承诺未来云服务或其他产品线。
- 购买、退款和 Apple 作为支付平台的边界。
- 语音跟随和转录结果的合理使用限制。
- 服务变化、免责声明、联系方式和生效日期。

## 4. Visual system

- 视觉方向：Apple 风格的克制、留白、清晰层级和真实产品画面。
- 背景：暖白和浅灰为主；深色 Hero 用于建立层次，但不使用渐变堆叠。
- 强调色：从稿随图标提取的低饱和暖色，仅用于 CTA、状态和重点数字。
- 字体：优先系统字体栈，中文使用系统中文字体，英文使用系统无衬线字体。
- 圆角：卡片和按钮使用中等圆角，避免过度“玻璃拟态”。
- 动效：仅保留淡入、悬停和移动端菜单过渡；`prefers-reduced-motion` 下关闭非必要动画。
- 截图：使用真实中英文截图，桌面画面和移动画面配合文字说明，不在原始截图上叠加不属于产品的 UI。

## 5. Responsive behavior

- Mobile: `320px` 至 `767px`，单列内容、紧凑导航、截图横向滑动或纵向堆叠。
- Tablet: `768px` 至 `1199px`，双列功能卡和适度缩短 Hero 间距。
- Desktop: `1200px` 以上，最大内容宽度 `1120px`，两列或三列布局，截图与说明并排。
- 所有主要操作和正文在键盘、触摸和屏幕阅读器下可访问。
- 不依赖 hover 才能发现功能；焦点状态必须清晰可见。

## 6. Technical boundary

- 纯静态 HTML、CSS 和少量 JavaScript。
- 无前端框架、无第三方分析、无远程字体、无后端 API。
- 共享 `assets/css/site.css`、`assets/js/site.js` 和页面片段约定；页面主体按语言独立维护，避免运行时翻译造成内容错配。
- GitHub Pages 从 `main` 分支发布。
- 通过 GitHub Actions 执行 HTML 链接检查、静态资源检查和部署。
- 自定义域名先保留配置入口；在真实域名确认后再提交 `CNAME`，不猜测域名。

## 7. BDD acceptance criteria

### Scenario A: Language routing

Given a user opens the root URL
When the browser language is Simplified Chinese or English
Then the user reaches the matching localized home page
And the user can switch language without losing the current page type.

### Scenario B: Story-led home

Given a visitor opens either localized home page
When the visitor reads the first viewport and workflow sections
Then the page explains the fixed-speed teleprompter problem before listing features
And the page presents the same user value in both languages.

### Scenario C: Device workflow

Given a visitor opens the features page
When the visitor reads the Mac, iPhone Remote, and Apple Watch sections
Then the screenshots, labels, captions, and claims match the corresponding locale
And Apple Watch is described as a free companion without a separate purchase.

### Scenario D: Support and contact

Given a user opens the support page
When the user follows a troubleshooting section
Then the user can find the relevant setup steps and a real support contact
And the page does not require login or JavaScript to reveal the contact information.

### Scenario E: Legal access

Given a user opens any localized page
When the user uses the footer
Then the localized privacy policy and terms pages are reachable
And the privacy page states the same data practices represented in the app and App Store Connect.

### Scenario F: Responsive accessibility

Given a user opens the site at mobile, tablet, or desktop width
When the user navigates with touch or keyboard
Then content remains readable without horizontal page overflow
And focus indicators, headings, alt text, and reduced-motion behavior remain available.

## 8. Validation

- Validate every route with a local static server.
- Test Chinese and English root routing in a browser with changed language preferences.
- Test mobile, tablet, and desktop widths in Chrome.
- Verify every screenshot's locale, title, paragraph content, and caption against the screenshot storyboard.
- Run an HTML/link checker and fail on missing local assets or broken internal links.
- Run Lighthouse or equivalent checks for accessibility, performance, SEO, and best practices.
- Verify the GitHub Pages deployment URL and all localized/legal/support routes after publishing.
- Confirm App Store Connect Support URL and Privacy Policy URL point to the deployed pages before submission.

## 9. PDCA record

### Plan

Build and publish a static bilingual product website with the smallest complete marketing, support, and legal surface required for the first App Store release.

### Do

The implementation is recorded in:

- `465269c` — website MVP design, numbered project document, and implementation plan;
- `30317a8` — bilingual static website, responsive visual system, ten locale-matched screenshots, support/legal pages, and GitHub Pages workflow.

The branch `feature/website-mvp` is pushed to GitHub at
`https://github.com/hddevteam/ScriptPaceWebsite/tree/feature/website-mvp`.

### Check

The current local evidence is:

- `node --check site-config.js` passed;
- `python3 scripts/check-site.py` passed in preview mode;
- `python3 scripts/check-links.py` passed;
- `python3 scripts/check-responsive-assets.py` passed and found all ten public screenshots;
- all eleven local routes returned HTTP 200 from the static server;
- Chrome inspection passed for Chinese home, English features, Chinese support, Chinese privacy, mobile navigation, language switching, and desktop/mobile layouts;
- `python3 scripts/check-site.py --production` correctly fails because the public support email is not configured.

The following release evidence is still required before merging to `main`: an approved public support email, final owner/legal review of the privacy and terms text, App Store URL readback after the app record becomes public, and a successful GitHub Pages deployment readback.

### Act

Before release, replace the preview contact warning with the approved support contact, remove the draft-review callouts after the legal text is approved, run the production gate again, and then merge/publish. Post-launch improvements will be limited to evidence from support questions, App Store review feedback, and analytics only if analytics is explicitly added and separately documented.

## 10. Retrospective

The first implementation kept out accounts, a CMS, support tickets, analytics, cookies, payment collection, and custom-domain DNS. The remaining work is release configuration rather than a missing website surface: confirm contact/legal ownership, then publish the already validated static site through GitHub Pages.
