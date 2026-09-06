# ScriptPace Website Engineering Rules

## Product boundary

- This repository contains the public marketing, support, privacy, and terms website for 稿随 / ScriptPace.
- The site is a static GitHub Pages project. Do not add accounts, a backend, payment collection, cloud script storage, analytics, advertising, or remote fonts.
- App Store purchases, subscriptions, refunds, and entitlement restoration remain in the App Store and the app.

## Content boundary

- Keep Chinese and English pages semantically aligned; never mix locale-specific screenshots or captions.
- Do not claim automatic script rewriting, cloud writing/history, perfect recognition, raw-audio archiving, or a separately paid Apple Watch app.
- Describe Apple Watch as a free companion and describe Monthly/Annual Pro as auto-renewable subscriptions.
- Support contact, privacy URL, terms URL, and App Store URL must be verified before public deployment.

## Branch workflow

- `main` is the GitHub Pages source branch.
- Implement changes on `feature/*` branches and merge only after local and browser validation.
- Commit, push, merge, and Pages deployment are separate operations.

## Validation

- Run the Python site, link, and asset checks before claiming the site is ready.
- Verify all routes in a real browser at mobile, tablet, and desktop widths.
- Confirm keyboard focus, semantic headings, alt text, reduced-motion behavior, and no horizontal overflow.
- Never publish a guessed support email, domain, App Store URL, or legal contact.
