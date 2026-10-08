---
description: Finish building the new Syncovate site (the "Syncovate LLC DRAFT") with minimal time from Shannon.
---

Move the new site forward one page at a time. Shannon's time is the scarce thing: **I draft, she decides and pastes.** Ask only for decisions, in small pieces, one at a time. Plain, warm, direct language. Her clients are founders from trades, manufacturing, retail, and family businesses, so copy is relational and human, never startup jargon.

Rules that never change:
- Git is storage only. Nothing deploys from here. Shannon pastes each page into Taft herself; I never claim a page is live until I have fetched it and checked.
- The TAFT connector cannot read or write a page's code. It lists names and dates only. So the loop is: I give her finished code, she pastes it, I verify.
- Do not touch the old live pages in the repo root (`index.html` etc.). They are a snapshot of the current site, which the new site replaces. Work in a separate folder: `new-site/`.
- Ignore the work-in-progress pages (Internal Analysis, Trusted Advisor Sales Page, Blind Spot Cost Diagram).

Decisions already made (do not re-ask): bronze `#BF8756` / hover `#A3703E`; phone `269-293-4442`; email `Shannon@SyncovateLLC.com`; Coaching and Diagnostic fold into one **How I Work** page; moving away from diagnostic language; `/organizational-diagnostic` redirects to `/how-i-work` at launch; the Scotoma quiz becomes its own funnel page after launch.

Steps:
1. **Status.** Read the draft's source (`ssjennings1/syncovateseptember2026`, clone read-only into `/home/user/ssjennings1/syncovateseptember2026` if missing; its pages are `index`, `how-i-work`, `meet-dr-j`, `speaking`, `contact`, `saturday-seed`, built from `partials/`). Use the TAFT connector (`getFunnels`, `getPagesByFunnelId`, limit 20) on the "Syncovate LLC DRAFT" site (`uaG3AcvLc35TKkPcGT1J`) to see which pages exist in Taft. Report in a short table: page, exists in repo, exists in Taft. Last known: Taft had only Home and How I Work.
2. **Pick the next page** (suggest one; Shannon can override). Order: Meet Dr. J, Speaking, Contact, Saturday Seed.
3. **Draft it** into `new-site/<page>.html` on a branch named `feat/new-site-<page>`. Reuse the draft's partials and existing live copy; change as little as possible. Run `python3 -I tools/launch_check.py new-site/` and fix any FAIL before showing her.
4. **Decisions.** Show her only what needs a decision, one at a time ("keep this section or cut it?"). Do not ask her to read the whole page.
5. **Hand off.** Give her the finished code and say exactly which Taft page and which block to paste it into. Offer the page as a file she can open.
6. **Verify.** After she says she pasted it, fetch the published page and confirm the key content is there (same approach as `/check-live`). Report plainly: it took, or here is what is off.
7. Save to the branch, commit (Conventional Commits, `feat(<page>): ...`), push the branch. Never open a pull request unless asked. Never push to `main`.
8. Stop after each page and say what is left. When every page exists in Taft, tell her it is time to run `/launch-check`.
