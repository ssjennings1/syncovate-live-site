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
├── speaking--facilitation.html     # Speaking & facilitation
├── about-dr-j.html                 # About Dr. J
├── contact.html                    # Contact info (phone, email, book a call)
├── favicon.svg                     # Site favicon
```

Pages under development (not yet created):
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
| Phone | `574-532-3178` |
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

### 5. Dark Opening Section (Bronze Glow, Flexible Structure)
Every page opens with a dark section — `background: #252830` with a radial gradient overlay using a semi-transparent bronze (`rgba(196, 147, 90, 0.15)` or similar) — to keep the moody, grounded feel consistent site-wide.

The *structure* inside that dark opener is not fixed to a single-headline hero. Default to a headline + subhead unless the page's job calls for something else. The real test: a visitor should be able to scan the opener fast and answer "is this the person I'm looking for, and do they have the skills I need" — not just admire it. If a big headline doesn't serve that, don't force it. The homepage's opener (a short sequence of individually-revealed statement lines building to a point, no single H1) is a deliberate departure from the classic hero and is the reference example for when to break the template.

### 6. Section Copy Structure
Every content section follows this eyebrow → headline → body hierarchy:

```html
<span class="eyebrow">Short Label</span>
<h2>Serif Headline Here</h2>
<p>Body copy in DM Sans. Keep it grounded and direct.</p>
```

The eyebrow label is small, uppercase, letter-spaced, in bronze or teal depending on section background.

### 7. Back-to-Top Button
Longer pages include a floating back-to-top button that appears after scrolling down. Present on coaching, speaking, and about pages.

---

## Existing Pages Reference

### `index.html` — Homepage
Entry point for the site. Opens with a "not a hero" sequence of short revealed lines (see pattern 5) instead of a single headline, leading into a "How to Work With Me" section (coaching, speaking, and the diagnostic, each with its own embedded testimonial), a Meet Dr. J section carrying the largest testimonial treatment on the page plus the credential/institution strips, and a closing CTA.

### `organizational-diagnostic.html` — Organizational Diagnostics (flagship)
The most important page. Centers on the "scotoma" metaphor (organizational blind spots). Includes symptoms grid, science section with eye diagram, diagnostic dimensions, case study walkthrough, three-tier pricing grid, and testimonials. Leads to the Scotoma Quiz CTA.

### `coaching-and-advising.html` — Executive Coaching & Advising
1:1 and group coaching for executives and business owners. Includes service tiers (Single Session, Core Retainer, Premium Retainer).

### `speaking--facilitation.html` — Speaking & Facilitation
Keynotes, workshops, and team sessions.

### `about-dr-j.html` — About Dr. J
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

- `main` — production-ready; matches what is live on Taft Systems.
- `feat/<page-or-feature>` — new pages or major features.
- `fix/<description>` — bug/layout fixes.
- `copy/<page>` — copy-only edits.

---

## AI Assistant Guidelines

1. **Read before editing** — always read the full file before making changes.
2. **Match existing patterns exactly** — every page must have the sitewide mechanics (scroll bar, nav scroll state, hamburger, reveal animations) and a dark opening section. Never skip the mechanics. The opener's internal content structure (single headline vs. a short-line sequence, etc.) is a judgment call in service of fast visitor comprehension, not a fixed template — see pattern 5.
3. **Brand consistency** — use only the defined color tokens and fonts. No improvising with new colors or typefaces.
4. **No frameworks** — do not introduce React, Vue, Alpine, Tailwind, or any external library. Pure HTML/CSS/JS only.
5. **Self-contained files** — each `.html` must work when opened standalone in a browser with no local server.
6. **Copy tone** — write in Dr. J's voice: direct, warm, credibility-forward, jargon-free.
7. **Minimal changes** — only change what the task requires. Do not refactor working code.
8. **Update this file** — when new pages are added or conventions evolve, update CLAUDE.md.
