# ScriptPace Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish a bilingual, responsive, multi-page static marketing and support website for 稿随 / ScriptPace on GitHub Pages.

**Architecture:** Use language-specific HTML trees under `/zh-hans/` and `/en/`, shared CSS and small JavaScript for navigation, locale routing, and accessibility behavior, and a single checked-in site configuration for App Store, support, and legal links. Keep all content static and readable without JavaScript; pages are authored as complete HTML documents rather than relying on runtime partial includes.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, GitHub Actions, GitHub Pages, local Python HTTP server for browser validation.

**Spec:** `docs/superpowers/specs/2026-09-06-scriptpace-website-design.md`

## Global Constraints

- The website is a public static marketing/support site; it has no account, backend, payment form, analytics SDK, remote font, or third-party tracking.
- Chinese and English pages must present the same product value and must never mix localized UI, captions, or screenshots.
- The public release must not claim automatic script rewriting, cloud writing/history, perfect recognition, raw-audio archiving, or a separate Apple Watch purchase.
- Apple Watch is described as a free companion; Monthly Pro and Annual Pro are auto-renewable, and Founder Lifetime is a one-time purchase.
- The App Store link uses canonical App Store ID `6805241939` and is read back before deployment.
- GitHub Pages publishes from `main`; custom-domain DNS and `CNAME` are deferred until the exact domain is explicitly approved.
- A release build must fail validation if support contact, privacy policy, terms, or App Store URLs are missing.

---

### Task 1: Project foundation and site configuration

**Files:**
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `.gitignore`
- Create: `site-config.js`
- Create: `project_docs/15-SCRIPTPACE-WEBSITE_MVP.md`
- Create: `docs/superpowers/specs/2026-09-06-scriptpace-website-design.md`
- Create: `docs/superpowers/plans/2026-09-06-scriptpace-website.md`

**Interfaces:**
- Produces the repository contract, route list, release constraints, and configuration values consumed by every page and validation script.

- [ ] **Step 1: Add repository documentation and ignore rules**

  `README.md` must identify the repository as `hddevteam/ScriptPaceWebsite`, list local preview and validation commands, and explain that `main` is the GitHub Pages source. `.gitignore` must ignore only local editor, OS, and preview output files.

- [ ] **Step 2: Add the checked-in configuration module**

  Create `site-config.js` exporting:

  ```js
  window.SCRIPTPACE_SITE = Object.freeze({
    appStoreURL: "https://apps.apple.com/app/id6805241939",
    supportEmail: "",
    repositoryURL: "https://github.com/hddevteam/ScriptPaceWebsite",
    version: "1.0"
  });
  ```

  `supportEmail` must remain empty until the product owner supplies the actual public support address. The production validation script must reject the empty value; local preview may show a clearly marked missing-contact warning.

- [ ] **Step 3: Verify the foundation**

  Run:

  ```bash
  node --check site-config.js
  git diff --check
  ```

  Expected: both commands succeed.

- [ ] **Step 4: Commit the foundation**

  ```bash
  git add README.md AGENTS.md .gitignore site-config.js project_docs docs
  git commit -m "docs: define ScriptPace website MVP"
  ```

---

### Task 2: Shared HTML shell, responsive CSS, and accessibility behavior

**Files:**
- Create: `assets/css/site.css`
- Create: `assets/js/site.js`
- Create: `index.html`

**Interfaces:**
- Consumes `site-config.js` and the route contract from the spec.
- Produces the shared visual system, root locale redirect, mobile navigation, language switch, footer links, and reduced-motion behavior used by all localized pages.

- [ ] **Step 1: Write static validation expectations**

  Add `scripts/check-site.py` with checks that every localized HTML file contains a skip link, one `h1`, a language attribute, a viewport meta tag, a privacy link, a terms link, a support link, and a language-switch link. Make the checker report the exact file and missing selector.

- [ ] **Step 2: Implement the shared stylesheet**

  Define CSS custom properties for warm white, graphite, soft gray, accent, spacing, radius, and maximum content width. Implement the `320px`, `768px`, and `1200px` layout behavior, visible keyboard focus, reduced motion, responsive screenshot frames, and a mobile disclosure menu without horizontal overflow.

- [ ] **Step 3: Implement the shared JavaScript**

  Add only these behaviors:

  ```js
  initLocaleRedirect();
  initMobileNavigation();
  initLanguageSwitch();
  initYearLabel();
  initMissingContactWarning();
  ```

  The root redirect must preserve a safe fallback to `/zh-hans/`; navigation must be operable by keyboard and must not hide the footer links when JavaScript is disabled.

- [ ] **Step 4: Implement the root fallback page**

  `index.html` must contain a readable fallback with two explicit links, `/zh-hans/` and `/en/`, plus the locale redirect script. It must not display a blank loading state.

- [ ] **Step 5: Run shared checks**

  Run:

  ```bash
  python3 scripts/check-site.py
  python3 -m http.server 4173
  ```

  Expected: the checker passes for the root page and the local server serves the repository.

- [ ] **Step 6: Commit the shared shell**

  ```bash
  git add assets index.html scripts/check-site.py site-config.js
  git commit -m "feat: add responsive bilingual site shell"
  ```

---

### Task 3: Bilingual home and features pages

**Files:**
- Create: `zh-hans/index.html`
- Create: `zh-hans/features.html`
- Create: `en/index.html`
- Create: `en/features.html`
- Create: `assets/screenshots/zh-Hans/` with the five final Chinese PNGs
- Create: `assets/screenshots/en/` with the five final English PNGs

**Interfaces:**
- Consumes the shared shell and final screenshot assets from the app repository's screenshot storyboard.
- Produces the public story, workflow, pricing, privacy promise, and device explanations in both languages.

- [ ] **Step 1: Add screenshot assets and verify their locale**

  Copy only these assets:

  ```text
  zh-Hans/01-remote-connected.png
  zh-Hans/02-mac-script.png
  zh-Hans/03-practice-library.png
  zh-Hans/04-voice-practice.png
  zh-Hans/05-watch-remote.png
  en/01-remote-connected.png
  en/02-mac-script.png
  en/03-practice-library.png
  en/04-voice-practice.png
  en/05-watch-remote.png
  ```

  Do not copy validation captures or fixture Markdown files into the public site.

- [ ] **Step 2: Build the Chinese home page**

  Use the story sequence: fixed-speed teleprompter pain → natural voice-following → hear/practice/follow/recover → Mac/iPhone/Watch workflow → screenshots → pricing → privacy → download. The page must not claim source editing or automatic rewriting.

- [ ] **Step 3: Build the English home page**

  Translate the same sequence with equivalent user value and use only English screenshots and captions. Keep the prices, entitlement language, free Watch companion, and privacy claims identical in meaning to Chinese.

- [ ] **Step 4: Build both features pages**

  Organize detailed features into six user-value sections: natural pacing, Mac Voice Follow, iPhone practice, QR-connected Remote, Apple Watch companion, and read-only transcript review. Each section needs a semantic heading, one concise explanation, one screenshot or device visual, and a next-step CTA.

- [ ] **Step 5: Run content checks**

  Extend `scripts/check-site.py` to reject public HTML containing `自动改稿`, `云端写作`, `cloud writing`, `perfect recognition`, `raw microphone audio`, or `separate Watch purchase` claims. Verify each localized screenshot path exists.

- [ ] **Step 6: Commit the marketing pages**

  ```bash
  git add zh-hans en assets/screenshots scripts/check-site.py
  git commit -m "feat: add bilingual product marketing pages"
  ```

---

### Task 4: Support, privacy, and terms pages

**Files:**
- Create: `zh-hans/support.html`
- Create: `en/support.html`
- Create: `zh-hans/privacy.html`
- Create: `en/privacy.html`
- Create: `zh-hans/terms.html`
- Create: `en/terms.html`

**Interfaces:**
- Consumes `site-config.js` for support and App Store links.
- Produces stable public URLs suitable for App Store Connect Support URL and Privacy Policy URL fields.

- [ ] **Step 1: Build support content**

  Include quick start, Mac workflow, iPhone Remote pairing and recovery, Apple Watch controls, purchase/restore, FAQ, supported-system note, and a visible support email link generated from `supportEmail`. When the contact value is empty, the page must show a non-production warning and the production checker must fail.

- [ ] **Step 2: Build the bilingual privacy policy**

  State the actual release boundary: no application account, no advertising tracker, no self-hosted telemetry, no raw microphone-audio storage, local-first processing where supported, system/App Store services as platform dependencies, retention/deletion behavior, and a support contact. Add effective date and an explicit note that the policy must be updated before any data-practice change.

- [ ] **Step 3: Build the bilingual terms**

  Cover license, acceptable use, Monthly Pro and Annual Pro auto-renewal, Founder Lifetime one-time purchase, Apple billing/refund boundary, current-product-line lifetime scope, speech/transcript limitations, service changes, disclaimers, and contact.

- [ ] **Step 4: Verify legal consistency**

  Add checker rules ensuring both privacy pages mention data processing, retention/deletion, contact, and effective date; both terms pages mention subscription renewal, lifetime purchase, and Apple billing/refund handling.

- [ ] **Step 5: Commit support and legal pages**

  ```bash
  git add zh-hans en scripts/check-site.py
  git commit -m "feat: add bilingual support and legal pages"
  ```

---

### Task 5: Automated validation and GitHub Pages workflow

**Files:**
- Create: `.github/workflows/pages.yml`
- Create: `scripts/check-links.py`
- Create: `scripts/check-responsive-assets.py`
- Modify: `README.md`

**Interfaces:**
- Consumes the static site and site configuration.
- Produces a failing CI result for missing routes, missing assets, missing legal/support links, empty production contact, forbidden claims, and broken relative links.

- [ ] **Step 1: Add internal link checking**

  `scripts/check-links.py` must parse all HTML `href` and image `src` values, ignore external URLs and anchors, resolve relative paths from each source page, and fail with the source file and missing target.

- [ ] **Step 2: Add asset and screenshot checks**

  `scripts/check-responsive-assets.py` must confirm all ten public PNGs exist, contain nonzero data, and are referenced by at least one localized page. It must also fail if any path under `validation/` or `fixture/` is copied into the public repository.

- [ ] **Step 3: Add the Pages workflow**

  Configure `.github/workflows/pages.yml` for pushes to `main` and manual dispatch. The workflow must run Node syntax checking, Python site checks, link checks, asset checks, then upload the repository root as a Pages artifact and deploy it with GitHub's Pages actions.

- [ ] **Step 4: Run all local checks**

  ```bash
  node --check site-config.js
  python3 scripts/check-site.py
  python3 scripts/check-links.py
  python3 scripts/check-responsive-assets.py
  git diff --check
  ```

  Expected: all checks pass except the deliberate production-contact check until `supportEmail` is supplied.

- [ ] **Step 5: Commit CI and validation**

  ```bash
  git add .github scripts README.md
  git commit -m "ci: validate and deploy GitHub Pages site"
  ```

---

### Task 6: Browser verification and deployment readback

**Files:**
- Modify: `project_docs/15-SCRIPTPACE-WEBSITE_MVP.md`
- Modify: `README.md` if the final Pages URL differs from the initial configuration.

**Interfaces:**
- Consumes the GitHub Pages deployment and produces final route, locale, responsive, accessibility, and deployment evidence.

- [ ] **Step 1: Preview the site locally**

  Run:

  ```bash
  python3 -m http.server 4173
  ```

  Open `/`, `/zh-hans/`, `/en/`, both features pages, both support pages, both privacy pages, and both terms pages in Chrome.

- [ ] **Step 2: Verify browser behavior**

  At mobile `390px`, tablet `834px`, and desktop `1440px` widths, verify no horizontal overflow, visible focus, keyboard navigation, menu behavior, language switching, screenshot loading, and readable legal/support text.

- [ ] **Step 3: Verify content against source evidence**

  Compare every caption and screenshot to `project_docs/assets/14-scriptpace-screenshots/`. Confirm no validation capture, mixed locale, unpaired Remote state, or unsupported product promise appears.

- [ ] **Step 4: Push and verify GitHub Pages**

  Push `main`, wait for the Pages workflow, then read back the deployment URL and request every required route. Do not add a custom domain until the exact domain is explicitly selected.

- [ ] **Step 5: Record final evidence**

  Update the MVP document with the deployed URL, commit SHA, workflow run, route results, browser dimensions, contact confirmation, and any known deferred work. Fill the PDCA Check/Act and Retrospective sections from actual evidence.

- [ ] **Step 6: Commit the evidence record**

  ```bash
  git add project_docs/15-SCRIPTPACE-WEBSITE_MVP.md README.md
  git commit -m "docs: record ScriptPace website validation"
  ```
