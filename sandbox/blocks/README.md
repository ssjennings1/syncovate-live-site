# Header and footer blocks, plus a middle for every page

Every page except Field Notes is built the same way:

    [ header block ]   one Custom Code element, in Taft's GLOBAL header
    [ page middle  ]   one Custom Code element on each page (sandbox/middles/<page>.html)
    [ footer block ]   one Custom Code element, in Taft's GLOBAL footer

Change the menu or the footer once (in the two global blocks) and every page picks it up.

## Files
- `sandbox/blocks/header-block.html` — menu, logo, Let's Talk button, mobile menu script. Marks the current page in the menu automatically.
- `sandbox/blocks/footer-block.html` — Saturday Seed email band, logo, link columns, copyright.
- `sandbox/middles/index.html` (Home), `how-i-work.html`, `workshops.html`, `meet-dr-j.html`, `contact.html`, `saturday-seed.html`.

All of them are generated from the finished pages by `python3 -I tools/make_blocks.py`. Edit the page in `sandbox/`, re-run the script, and re-paste the block or middle that changed. Do not edit the generated files by hand.

## How they stay clean inside Taft
Every style is scoped under `.sy-block`, and each block resets the element styles around it, so nothing leaks into (or out of) the rest of the Taft page. Tested against a page with deliberately hostile global CSS. Header + middle + footer reassemble to within 0.1% of the original full pages (pixel comparison, desktop).

## Notes
- The footer's Saturday Seed email band also shows on the Saturday Seed page itself, next to its own form. Harmless, but it can be hidden on that page if you prefer.
- The Contact middle embeds the Taft form "Drop us a message" (id `ZF0441qk1h4lSpjDf9dH`). Fields, notifications and bot protection are set in Taft's form builder.
- Page titles and descriptions are set in Taft's SEO panel for each page (head tags inside a Custom Code element do not count).
- The header is `position: sticky`; in Taft's header section, turn on the section's own "sticky" setting if you want it to stay at the top while scrolling.
- Images: Home middle uses `assets/dr-j-home-portrait.jpg`, Meet Dr. J middle uses `assets/dr-j-porch-portrait.jpg`. Swap each path for a data URI or a Taft media-library URL when pasting.
