# ScriptPace Website Design

## Context

ScriptPace needs a standalone marketing and support website for its bilingual Apple-platform release. The App Store listing copy and screenshot storyboard already define the product story, pricing, device workflow, and language contract, but they do not define an independently deployable website.

## Decision

Build a multi-page static site in the independent `hddevteam/ScriptPaceWebsite` repository and publish it with GitHub Pages. Keep localized content in separate Chinese and English route trees so the site remains readable without runtime translation and can provide stable localized App Store, support, and legal URLs.

## Page model

Each language has five pages:

| Page | Purpose | Primary CTA |
| --- | --- | --- |
| Home | Story-led product introduction and conversion | Download on the App Store |
| Features | Explain the complete Mac/iPhone/Watch workflow | See how it works / Download |
| Support | Help users install, pair, practice, purchase, and recover | Contact support |
| Privacy | Explain data processing, retention, and privacy choices | Return to product |
| Terms | Explain license, subscriptions, lifetime purchase, and service limits | Return to product |

The root page performs a small language redirect and includes a manual language fallback. Every localized page repeats the same header/footer navigation and exposes canonical, alternate-language, title, description, and Open Graph metadata.

## Content rules

The website uses the story-led value proposition: a fixed-speed teleprompter can make a prepared recording harder by forcing the speaker to chase words, wait for the scroll, or lose their place after a pause. ScriptPace restores a natural workflow through Mac Voice Follow, iPhone practice, QR-connected Remote control, and Apple Watch companion control.

The public release does not claim automatic script rewriting, cloud writing, cloud history, perfect recognition, raw-audio archiving, or a separate Watch purchase. Read-only transcript review may be described; source-file editing is not a public website promise until independently revalidated for the release build.

Chinese and English pages use parallel meaning, not literal word-for-word translation. The five final screenshot pairs in `project_docs/assets/14-scriptpace-screenshots/` are the only screenshot assets allowed for the first release site.

## Visual and interaction system

- System font stack, with platform-native Chinese and English fallbacks.
- Warm white, graphite, soft gray, and one low-saturation accent sampled from the product icon.
- Maximum content width `1120px`; generous vertical rhythm; no heavy gradients or ornamental dashboard chrome.
- Screenshot-led feature sections alternate image and explanation on desktop and collapse to a readable single column on mobile.
- Navigation remains compact; mobile navigation is a keyboard-accessible disclosure menu.
- Focus indicators, semantic headings, alt text, skip link, contrast, and reduced-motion support are mandatory.

## Technical design

Use plain HTML, CSS, and small JavaScript modules. Do not add a framework, build-time translation system, analytics SDK, remote font, or backend. Use a shared stylesheet and script, language-specific page documents, and copied screenshot assets. GitHub Actions validates internal links and deploys the repository's `main` branch to GitHub Pages.

The App Store link is centralized in a small site configuration module using the canonical App Store ID `6805241939`; the link must be read back before public deployment because the app record is not yet released. Support and legal contact values are centralized in the same configuration boundary and must never be invented.

## Verification strategy

1. Static route and asset checks catch missing files and internal links.
2. Browser checks cover both language trees at mobile, tablet, and desktop widths.
3. Visual review confirms screenshot and caption locale alignment.
4. Accessibility checks cover semantic structure, keyboard navigation, focus, contrast, and reduced motion.
5. Deployment checks read back the GitHub Pages URL and all required support/legal routes.

## Deferred

- Blog or release-notes CMS.
- Account, payment, support-ticket backend, or user dashboard.
- Server-side localization.
- Analytics, advertising, cookies, and third-party tracking.
- Custom-domain DNS changes until the exact domain is explicitly selected.
