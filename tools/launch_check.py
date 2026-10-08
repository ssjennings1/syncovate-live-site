#!/usr/bin/env python3
"""Mechanical pre-launch checks for a folder of page files.

Usage:  python3 -I tools/launch_check.py <folder> [--phone NEW] [--bronze HEX] [--legacy-patterns]
--legacy-patterns also requires the OLD site's five design patterns (scroll bar, nav scroll state,
hamburger, reveal, mobile menu). The streamlined draft does not use them, so they are off by default.
Exit code 1 if any FAIL. WARN = look at it, not necessarily wrong.
Judgment calls (copy, tone, whether a section should exist) are NOT checked here.
"""
import os, re, sys, glob

args = sys.argv[1:]
if not args:
    raise SystemExit(__doc__)
folder = args[0]
opt = lambda k, d: args[args.index(k) + 1] if k in args else d
GOOD_PHONE = opt('--phone', '269-293-4442')
GOOD_BRONZE = opt('--bronze', '#BF8756').upper()
OLD_PHONES = ['574-532-3178', '5745323178']
OLD_BRONZES = ['#C4935A', '#A87840']
EMAIL = 'Shannon@SyncovateLLC.com'

files = sorted(f for f in glob.glob(os.path.join(folder, '*.html')))
if not files:
    raise SystemExit('No .html files in %s' % folder)
names = {os.path.splitext(os.path.basename(f))[0] for f in files}
fails = warns = 0

def say(level, page, msg):
    global fails, warns
    if level == 'FAIL': fails += 1
    if level == 'WARN': warns += 1
    print('  %-4s %s' % (level, msg))

for f in files:
    page = os.path.basename(f)
    raw = open(f, encoding='utf8', errors='ignore').read()
    s = re.sub(r'<!--.*?-->', '', raw, flags=re.S)   # ignore comments (e.g. "Never #C4935A")
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)       # ignore CSS comments
    print('\n%s' % page)
    low = s.lower()
    # head basics
    t = re.search(r'<title>([^<]*)</title>', s)
    if not t or not t.group(1).strip(): say('FAIL', page, 'no <title>')
    if not re.search(r'<meta name="description" content="[^"]{20,}', s): say('FAIL', page, 'no meta description (20+ chars)')
    if 'rel="canonical"' not in s: say('WARN', page, 'no canonical link')
    if 'name="viewport"' not in s: say('FAIL', page, 'no viewport meta')
    if 'property="og:title"' not in s: say('WARN', page, 'no Open Graph title')
    # brand color
    root = re.search(r':root\s*\{(.*?)\}', s, re.S)
    rootcss = root.group(1) if root else ''
    m = re.search(r'--bronze:\s*(#[0-9a-fA-F]{6})', rootcss)
    if m and m.group(1).upper() != GOOD_BRONZE: say('FAIL', page, '--bronze is %s, expected %s' % (m.group(1), GOOD_BRONZE))
    if not m and GOOD_BRONZE.lower() not in low: say('WARN', page, 'brand bronze %s not found on this page' % GOOD_BRONZE)
    for ob in OLD_BRONZES:
        if ob.lower() in low: say('FAIL', page, 'old color %s still present' % ob)
    # phone / email
    for op in OLD_PHONES:
        if op in s: say('FAIL', page, 'old phone %s present (%d)' % (op, s.count(op)))
    if GOOD_PHONE not in s and GOOD_PHONE.replace('-', '') not in s: say('WARN', page, 'new phone %s not on this page' % GOOD_PHONE)
    if re.search(r'[a-z0-9._-]+@syncovatellc\.com', s, re.I) and EMAIL not in s: say('FAIL', page, 'email present but not exactly %s' % EMAIL)
    if 'email&#160;protected' in s or 'cdn-cgi' in s: say('FAIL', page, 'Cloudflare email masking left in file')
    # site patterns (CLAUDE.md)
    for label, needle in ([] if '--legacy-patterns' not in args else [('scroll progress bar', 'scroll-progress'), ('nav scrolled state', "'scrolled'"), ('hamburger menu', 'hamburger'),
                          ('scroll reveal', 'IntersectionObserver'), ('mobile menu', 'mobile-menu')]):
        if needle not in s: say('FAIL', page, 'missing pattern: %s' % label)
    if 'console.log' in s: say('FAIL', page, 'console.log left in code')
    if re.search(r'lorem ipsum', low) or re.search(r'\b(TODO|FIXME|TBD|XXX)\b', s):
        say('WARN', page, 'placeholder text found (lorem ipsum / TODO / FIXME / TBD / XXX)')
    # images need alt
    for img in re.findall(r'<img\b[^>]*>', s):
        if 'alt=' not in img: say('FAIL', page, 'image without alt text')
    # internal links must point at a real page in this folder
    for href in sorted(set(re.findall(r'href="(/[^"#?]*)"', s))):
        slug = href.strip('/')
        if slug in ('', 'homepage', 'home', 'favicon.svg'): continue
        if slug not in names and slug.replace('-', '') not in {n.replace('-', '') for n in names}:
            say('WARN', page, 'link %s has no matching file in folder (fine if it lives in Taft)' % href)
    # old offer language
    d = len(re.findall(r'diagnostic', low)); sc = len(re.findall(r'scotoma', low))
    if d or sc: say('WARN', page, 'diagnostic x%d, scotoma x%d (direction: moving away; the quiz link is the only thing that may stay)' % (d, sc))

print('\n== %d FAIL, %d WARN across %d pages ==' % (fails, warns, len(files)))
sys.exit(1 if fails else 0)
