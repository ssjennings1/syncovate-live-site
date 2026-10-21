# Paste runbook — moving the sandbox into Taft

The new site lives in `sandbox/`. Taft is the source of truth once pasted. Git is storage only.
Target Taft site: **"Syncovate LLC DRAFT"** (funnel id `uaG3AcvLc35TKkPcGT1J`). It replaces the live
"Syncovate Website" at launch; until then nothing here is public.

## 0. Before any page
- [ ] Portrait: the connector can't upload media. At paste time the portrait path in `meet-dr-j.html` was swapped for a base64 data URI of `sandbox/assets/dr-j-porch-portrait.jpg` (the repo file is unchanged). Optional later: upload the JPG to the Taft media library and swap in the hosted URL.
- [ ] Upload `sandbox/assets/favicon.svg` as the site favicon (Taft site settings → favicon). The pages reference `favicon.svg` by relative path; Taft's site-level favicon setting covers it.
- [ ] Confirm the two product links still resolve: Single Session booking `…/widget/booking/qPTZ7uQpwZfnM4X74qqK`, Team Session payment `…/payment-link/6ac7d2c0c0e70c7fefb7355e`, Trusted Advisor payment `…/payment-link/68b849c521970953fbe18f26`.

## 1. Per page (same steps each time)
Order: Home → How I Work → Workshops → Meet Dr. J → Contact → Saturday Seed.

1. In Taft, open the DRAFT site. Pages Home and How I Work already exist; create the others with these paths:
   `/how-i-work`, `/workshops`, `/meet-dr-j`, `/contact`, `/saturday-seed` (Home is `/`).
2. Each page is ONE custom-code element (Section > 1 Column Row > Code). Add the new Code element first (Taft refuses to save an empty page), then delete the old sections. The old global header ("Nav Bar Syncovate") and Footer are site-level and sync across pages; delete them once (each page carries its own nav and footer) and save through the "Section Changes Made / Global Sections" dialog.
3. Paste by clipboard: in the Taft tab run `fetch('https://raw.githubusercontent.com/ssjennings1/syncovate-live-site/feat/sandbox-pages/sandbox/<page>.html')` then `navigator.clipboard.writeText(...)`. Click the Code element > Open Code Editor > cmd+a, cmd+v > Save, then save the page. (This needs the repo to be public; if it goes private, paste from a local copy instead.)
4. Meet Dr. J only: use the data-URI portrait described in step 0.
5. SEO: set Title and Description in Taft's SEO panel (toolbar icon, document with magnifier > Content). Head tags inside a custom-code element land in the page body and do not count. Text is in each page's `<title>` and meta description. Do not set noindex.
6. Save, then open the Taft preview on a phone. Check: nav opens, buttons go to the booking widget, the logo shows. The footer Seed form is a placeholder until the GHL form is swapped in.
7. Tell Claude "pasted <page>"; it fetches the preview and diffs against the repo (`/check-live` logic).

## 2. Launch (only when all six pages are pasted and checked)
- [ ] Run `python3 -I tools/launch_check.py sandbox/` → must read `0 FAIL, 0 WARN`.
- [ ] Point the domain at the DRAFT site (Taft → Sites → Domains). The old site stays as a fallback for a week.
- [ ] Redirects (Claude can create these through the TAFT connector, each needs one approval):
  `/organizational-diagnostic` → `/how-i-work`, `/speaking` → `/workshops`, `/coaching-and-advising` → `/how-i-work`, `/about-dr-j` → `/meet-dr-j`.
- [ ] Google Business Profile: phone to 269-293-4442, description to the new footer line ("Business psychology for founders and owner-operators of growing, privately held companies"), appointment link to the 15-minute call.
- [ ] Email signature phone: still 574 (her main line). Leave it.

## 3. After launch (first 30-day loop)
- Photos: see `sandbox/PHOTO-SHOT-LIST.md`.
- The No Man's Land / two-curve graphic for Home ("Hard to see from the inside").
- Teal t-shirt recolor on the studio originals, if still wanted (Canva brush tool).
- Scotoma quiz gets its own funnel page; footer stays without it.
