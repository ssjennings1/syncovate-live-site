---
description: Compare what is published on syncovatellc.com with this repo and report drift. Read-only.
---

Check whether this repo still matches the live Syncovate site. **Read-only: change nothing.**

Background: git here is storage only. Nothing deploys from it. Taft is the source of truth. Shannon pastes pages into Taft herself.

1. Confirm `https://syncovatellc.com/` is reachable from this environment (`curl -sS -o /dev/null -w "%{http_code}" -L https://syncovatellc.com/`). If it is blocked, stop and tell Shannon to allow `syncovatellc.com` in the environment's Network access settings (cloud environment menu, then Edit). Do not work around it.
2. For each page file in the repo root (`index`, `about-dr-j`, `coaching-and-advising`, `organizational-diagnostic`, `speaking`, `contact`): save the live page (`curl -sS -L https://syncovatellc.com/<name> -o <scratchpad>/<name>.html`; `index` is `/`). Put saved copies in the scratchpad directory, never in the repo.
3. Turn each saved page into its custom code: `python3 -I tools/extract_live.py <saved> <scratchpad>/<name>.out.html`, then `cmp` it with the repo file.
4. Report in plain language, one line per page: **same** or **drifted**. For a drifted page, show a short readable summary of what changed (use visible text, not raw HTML), and say which side looks newer. Taft is usually the newer side.
5. Also use the TAFT connector (read-only: `getFunnels`, `getPagesByFunnelId`, both limited to 20 per call) to list the "Syncovate" website's pages and last-edited dates, and flag any page edited in Taft that is not in the repo. Site IDs: live "Syncovate" `nW6pe4jDehtx0qg496bk`; "Syncovate LLC DRAFT" `uaG3AcvLc35TKkPcGT1J`; location `yCTzggMS1VT4xrqF3lML`. The connector returns names and dates only, never page code.
6. Ignore the work-in-progress pages (Internal Analysis, Trusted Advisor Sales Page, Blind Spot Cost Diagram) unless Shannon says otherwise.
7. If anything drifted, offer one next step: save the live version into the repo on a branch named `chore/sync-live-site-YYYY-MM-DD`. Do not do it without a yes. Never open a pull request unless asked.

Style: plain, warm, direct. Lead with the answer ("Everything matches" or "2 pages have changed in Taft").
