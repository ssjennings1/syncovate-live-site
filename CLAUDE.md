# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**Syncovate** — [syncovatellc.com](https://syncovatellc.com)

An organizational consulting firm offering diagnostics, executive coaching, and speaking/facilitation services. Principal: **Dr. Shannon Jennings, PsyD** ("Dr. J").

**Target audience:** Founders, CEOs, middle managers, and family business leaders at companies with $1M–$50M revenue.

**Tone:** Direct, warm, psychologically grounded. No jargon, no corporate fluff. Write like a trusted advisor who has done the work — not a marketer.

---

## Tech Stack

- **Vanilla HTML, CSS, JavaScript only** — no frameworks, no bundlers, no build step.
- Each page is a **standalone `.html` file** exported directly for upload to Taft Systems hosting.
- No npm, no package.json, no dependencies.

---

## Repository Structure

```
├── CLAUDE.md                       # This file
├── index.html                      # Homepage — service overview + credibility strip
├── organizational-diagnostic.html  # Flagship "Scotoma" diagnostic page
├── coaching-and-advising.html      # Executive coaching & advising
├── speaking.html                   # Speaking & facilitation (live at /speaking)
├── about-dr-j.html                 # Meet Dr. J (nav label is "Meet Dr. J")
├── contact.html                    # Contact info (phone, email, book a call)
├── saturday-seed-blocks.html       # Reference copy of Saturday Seed blocks (not standalone)
├── favicon.svg                     # Site favicon
├── tools/
│   ├── extract_live.py             # Lift a page's code out of a saved live Taft page (undoes Cloudflare email masking)
│   └── launch_check.py             # Mechanical pre-launch checks on a folder of pages
└── .claude/commands/
    ├── check-live.md               # /check-live    — compare repo to the published site (read-only)
    ├── launch-check.md             # /launch-check  — pre-launch checklist for the new site
    └── finish-site.md              # /finish-site   — build the next page of the new site
```

### Source of truth

**Taft is the source of truth, not this repo.** The live site is the Taft website named **"Syncovate"**. As of 2026-10-07 the six pages above were checked against the published site and match it. Before editing, confirm the repo still matches live (fetch `https://syncovatellc.com/<path>` and compare); if Taft has moved ahead, update the repo first.

Live nav: Organizational Diagnostics, Coaching & Advising, Speaking & Facilitation, Meet Dr. J, Field Notes (`https://syncovatellc.com/prism-blog`, a separate Taft blog), and a Book a Call button.

**Direction (2026-10-08): moving away from diagnostic language.** It was tried for about a year and did not land. The Syncovate LLC DRAFT site folds Coaching and the Diagnostic into one **How I Work** page and drops "diagnostic" and "scotoma" as the lead offer. Treat `organizational-diagnostic.html` as a page being retired, not the flagship: do not polish it, and do not write new copy that leads with diagnostics or scotoma. The "flagship" label further down describes the current live site, not the plan.

**Launch plan (2026-10-08):** the **Syncovate LLC DRAFT** site will *replace* the current site; it is not a patch on it. Until then the current pages stay as published. At launch:
- `/organizational-diagnostic` redirects to `/how-i-work` (create the redirect in Taft only when the new site is live, not before).
- The phone number becomes `269-293-4442` everywhere.
- The Scotoma quiz (Scotoma Spotter) becomes its own funnel page *after* the focused site is deployed; until then leave existing links to `spotter.syncovatellc.com` alone.

Not in the repo (live in Taft, intentionally):
- **Saturday Seed** (`/saturday-seed`) is built from separate Taft blocks plus a Taft form. `saturday-seed-blocks.html` is a reference copy only. The live page currently has no `<title>` or meta description.
- **Internal Analysis**, **Trusted Advisor Sales Page**, **Blind Spot Cost Diagram** — work in progress, not published at working URLs. Ignore until told otherwise.
- Sales pages for courses/programs (payment triggers + tracking TBD)

---

## Brand

### Colors

| Token | Hex | Usage |
|-------|-----|-------|
| Bronze | `#BF8756` | Primary CTA buttons, accents, hover states |
| Bronze Hover | `#A3703E` | Button hover / active state |
| Bronze Subtle | `rgba(196,147,90,0.07)` | Light bronze tint for backgrounds |
| Teal | `#56ADBF` | Secondary accent, highlights |
| Charcoal Deep | `#252830` | Dark hero backgrounds, footer |
| Charcoal | `#3D4148` | Secondary dark backgrounds |
| Charcoal Mid | `#5C6170` | Mid-tone dark text/accents |
| Cream | `#FAF8F5` | Light section backgrounds |
| Warm Gray | `#F0EDE8` | Alternate light section backgrounds |
| Text | `#3A3530` | Primary body text color |
| Text Muted | `#7A736B` | Secondary/subdued text |
| Border | `rgba(196,147,90,0.18)` | Subtle bronze-tinted borders |

> **Decision (2026-10-08): `#BF8756` is the brand bronze, hover `#A3703E`.** Homepage, About, and Coaching already use it. Organizational Diagnostic, Speaking, and Contact are still live with the older `#C4935A` (hover `#A87840`) and need updating in Taft. Until they are, the repo copies match live (old bronze) on purpose. The Diagnostic page also uses white button text where the other pages use charcoal; that is still undecided. The `rgba(196,147,90,…)` tints and borders are shared by every page and are not part of this change.

> **Decision (2026-10-08): leave `574-532-3178` on the current live site for now.** When the new site replaces it, use `269-293-4442`, the number connected to the CRM. The Syncovate LLC DRAFT site already uses it. The repo copies match live on purpose.

### Typography

| Role | Font | Notes |
|------|------|-------|
| Headings (h1–h3) | Cormorant Garamond | Serif, loaded from Google Fonts |
| Body / UI | DM Sans | Sans-serif, loaded from Google Fonts |

### Key External Links

| Purpose | URL |
|---------|-----|
| Book a Call (Calendly widget) | `https://link.syncovatellc.com/widget/booking/29K6RwPvCIc2xOxgUVKo` |
| Scotoma Quiz (lead capture) | `https://spotter.syncovatellc.com/` |
| Phone | Live site today: `574-532-3178`. **At launch of the new site: `269-293-4442`** (the number connected to the CRM; tel `tel:2692934442`, schema `+12692934442`) |
| Email | `Shannon@SyncovateLLC.com` |
| LinkedIn | `https://www.linkedin.com/in/shannonsjennings/` |

---

## Page Structure & Design Patterns

Every page **must** implement all of the following. Do not omit any pattern on new pages.

### 1. Scroll Progress Bar
A thin bar fixed at the very top of the viewport (height 2px, bronze-to-teal gradient) that fills left-to-right as the user scrolls.

```html
<div class="scroll-progress"></div>
```

```js
var prog = document.querySelector('.scroll-progress');
window.addEventListener('scroll', () => {
  const pct = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
  prog.style.width = pct + '%';
});
```

### 2. Fixed Nav with Blur / Scroll State
The `<nav>` starts transparent and gains a `scrolled` class (backdrop blur + shadow) once the user scrolls past ~50px.

```js
window.addEventListener('scroll', () => {
  document.querySelector('nav').classList.toggle('scrolled', window.scrollY > 50);
});
```

### 3. Mobile Hamburger Menu
Full-screen overlay menu triggered by a hamburger button. Nav links close the menu on click.

### 4. Scroll Reveal Animations
Elements animate in as they enter the viewport using an `IntersectionObserver`.

- `.reveal` — fade + slide up
- `.reveal-scale` — fade + scale up

Apply these classes to section containers, cards, and content blocks. Never add them to the `<nav>` or `<footer>`.

### 5. Dark Hero with Radial Bronze Glow
All hero sections use `background: #252830` with a radial gradient overlay centered behind the headline, using a semi-transparent bronze (`rgba(196, 147, 90, 0.15)` or similar).

### 6. Section Copy Structure
Every content section follows this eyebrow → headline → body hierarchy:

```html
<span class="eyebrow">Short Label</span>
<h2>Serif Headline Here</h2>
<p>Body copy in DM Sans. Keep it grounded and direct.</p>
```

The eyebrow label is small, uppercase, letter-spaced, in bronze or teal depending on section background.

### 7. Back-to-Top Button
Longer pages include a floating back-to-top button that appears after scrolling down. Currently on the coaching and speaking pages (the live About page does not have one).

---

## Existing Pages Reference

### `index.html` — Homepage
Service overview with three-card grid (Diagnostics, Coaching, Speaking), credibility strip, about snapshot, and quotes. Entry point for the site.

### `organizational-diagnostic.html` — Organizational Diagnostics (flagship)
The most important page. Centers on the "scotoma" metaphor (organizational blind spots). Includes symptoms grid, science section with eye diagram, diagnostic dimensions, case study walkthrough, three-tier pricing grid, and testimonials. Leads to the Scotoma Quiz CTA.

### `coaching-and-advising.html` — Executive Coaching & Advising
1:1 and group coaching for executives and business owners. Includes service tiers (Single Session, Core Retainer, Premium Retainer).

### `speaking.html` — Speaking & Facilitation
Keynotes, workshops, and team sessions.

### `about-dr-j.html` — Meet Dr. J
Background, credentials, and story of Dr. Shannon Jennings. Two-column hero, origin story, "This Is / This Isn't" comparison grid, credentials grid, and how-I-work section.

### `contact.html` — Contact
Minimal page with three-column contact card grid (phone, email, book a call).

---

## Hosting & Deployment

- Files are uploaded **manually** to Taft Systems as standalone HTML files.
- Each `.html` file must be fully self-contained (inline `<style>` blocks acceptable; external CSS files are fine if also uploaded).
- No server-side rendering, no routing, no APIs.
- Nav links use **extensionless paths** (e.g., `/organizational-diagnostic` not `/organizational-diagnostic.html`) — Taft Systems handles the resolution.
- Google Fonts are loaded via `<link>` tags in `<head>` — always include both Cormorant Garamond and DM Sans.

---

## Writing & Copy Guidelines

- **Voice:** Confident, direct, warm. Dr. J speaks plainly — avoid consultant-speak.
- **Headlines:** Lead with the problem or transformation, not credentials.
- **CTAs:** Specific and action-forward. Prefer "Take the Scotoma Quiz" or "Book a Call" over "Learn More."
- **Length:** Body copy should be scannable. Short paragraphs (2–4 lines). Use `<ul>` for lists of 3+ items.
- **Psychology references:** Appropriate when grounded — this audience expects intellectual credibility, not pop-psych platitudes.

---

## Code Conventions

### HTML
- Use semantic elements (`<section>`, `<article>`, `<nav>`, `<main>`, `<footer>`).
- All interactive elements must be keyboard accessible.
- `alt` text required on all images.

### CSS
- Use CSS custom properties (`--var`) for all brand colors and repeated values.
- Mobile-first media queries.
- Avoid `!important` except to override third-party embed styles.

### JavaScript
- Vanilla ES6+. No libraries.
- All JS at the bottom of `<body>` or in a `<script>` block before `</body>`.
- Use `DOMContentLoaded` or place scripts after the elements they reference.
- No `console.log` left in production code.

### File Naming
- All page files: `kebab-case.html`
- Images/assets: `kebab-case.ext`

---

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <short summary>
```

| Type | When to use |
|------|-------------|
| `feat` | New page or significant new section |
| `fix` | Bug fix, broken link, layout issue |
| `copy` | Copy/content changes only |
| `style` | Visual/CSS-only changes |
| `chore` | Housekeeping, file renames |
| `docs` | CLAUDE.md or other documentation |

Scope examples: `scotoma`, `coaching`, `speaking`, `about`, `nav`, `global`

---

## Branch Strategy

- Git is **storage and history only**. Nothing is published from here; the site goes live only when pages are pasted or uploaded in Taft. `main` is the latest saved copy of the live site, not a deploy trigger.
- `main` — latest saved copy of what is live on Taft Systems.
- `feat/<page-or-feature>` — new pages or major features.
- `fix/<description>` — bug/layout fixes.
- `copy/<page>` — copy-only edits.

---

## AI Assistant Guidelines

1. **Read before editing** — always read the full file before making changes.
2. **Match existing patterns exactly** — every page must have all five design patterns (scroll bar, nav scroll state, hamburger, reveal animations, dark hero). Never skip one.
3. **Brand consistency** — use only the defined color tokens and fonts. No improvising with new colors or typefaces.
4. **No frameworks** — do not introduce React, Vue, Alpine, Tailwind, or any external library. Pure HTML/CSS/JS only.
5. **Self-contained files** — each `.html` must work when opened standalone in a browser with no local server.
6. **Copy tone** — write in Dr. J's voice: direct, warm, credibility-forward, jargon-free.
7. **Minimal changes** — only change what the task requires. Do not refactor working code.
8. **Update this file** — when new pages are added or conventions evolve, update CLAUDE.md.
