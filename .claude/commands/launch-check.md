---
description: Pre-launch checklist for the new Syncovate site (the "Syncovate LLC DRAFT"). Run before switching the domain.
---

Run the pre-launch check on the new site. **Nothing is published by this command.** Shannon switches the site in Taft herself, and only after she says go.

Decisions already made (do not re-ask):
- The "Syncovate LLC DRAFT" site **replaces** the current site.
- Brand bronze is `#BF8756` (hover `#A3703E`). The old `#C4935A` / `#A87840` must not appear.
- Phone at launch is `269-293-4442` (the CRM number). The old `574-532-3178` must not appear anywhere, including `tel:` links and structured data.
- Email is `Shannon@SyncovateLLC.com`.
- Direction is away from "diagnostic" language. The Scotoma quiz becomes its own funnel page *after* launch; existing links to `spotter.syncovatellc.com` may stay until then.
- `/organizational-diagnostic` must redirect to `/how-i-work` at launch.

Steps:
1. **Get the draft's code.** The draft's source repo is `ssjennings1/syncovateseptember2026` (public). Clone it read-only if `/home/user/ssjennings1/syncovateseptember2026` does not exist: `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/ssjennings1/syncovateseptember2026 /home/user/ssjennings1/syncovateseptember2026`. Warn Shannon if the repo is older than what is in Taft (compare the Taft draft's last-edited date from the TAFT connector with the repo's last commit). If she gives a draft preview URL, fetch the pages from it and use `tools/extract_live.py` too.
2. **Mechanical checks:** `python3 -I tools/launch_check.py <folder>`. Any FAIL is a blocker; explain each in plain language. WARNs get a short look: fix them or say why they are fine.
3. **Judgment checks the script cannot do** (read the pages):
   - Every nav and footer link goes somewhere that exists; nav and footer are the same on every page.
   - Page titles and descriptions read well and are different on each page.
   - No leftover "diagnostic" or "scotoma" as the lead offer; pricing and offers match what Shannon says she sells now.
   - Testimonial names, companies, and spellings are consistent across pages (e.g. "Mid-City Supply").
   - The booking link `https://link.syncovatellc.com/widget/booking/29K6RwPvCIc2xOxgUVKo` is on every call-to-action.
4. **Redirects (TAFT connector, read first):** list current redirects with `fetch-redirects-list` (limit 20). Report whether `/organizational-diagnostic` already redirects. **Do not create or change a redirect until Shannon says the new site is live**, and then only with her approval of the exact operation.
5. **Report** as a short go / no-go: what is clear, what blocks launch, and what is her call. Plain language, no jargon.
6. After launch (only when she says it is live): run `/check-live`-style verification against the new site and confirm the redirect works by requesting `/organizational-diagnostic`.

Never open a pull request unless asked. Never push to `main`.
