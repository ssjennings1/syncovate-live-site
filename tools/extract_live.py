#!/usr/bin/env python3
"""Pull a page's custom code out of a saved copy of a live Taft page.

Taft wraps each page's custom code in its own HTML shell. The page's own
document is the SECOND "<!DOCTYPE html>" in the file. Cloudflare also masks
email addresses on the way out; this puts the real address back.

Usage:
  curl -sS -L https://syncovatellc.com/<path> -o saved.html
  python3 -I tools/extract_live.py saved.html out.html
"""
import re, sys

def decode(h):
    k = int(h[:2], 16)
    return ''.join(chr(int(h[i:i+2], 16) ^ k) for i in range(2, len(h), 2))

def extract(s):
    a = s.find('<!DOCTYPE html>', 100)
    if a < 0:
        raise SystemExit('No embedded document found (page may be unpublished or not custom code).')
    b = s.find('</html>', a) + len('</html>')
    d = s[a:b]
    # <a href="/cdn-cgi/l/email-protection#HEX"><span class="__cf_email__" data-cfemail="HEX">[email protected]</span></a>
    d = re.sub(r'<a href="/cdn-cgi/l/email-protection#[0-9a-f]+"([^>]*)>\s*<span class="__cf_email__" data-cfemail="([0-9a-f]+)">\[email&#160;protected\]</span>\s*</a>',
               lambda m: '<a href="mailto:%s"%s>%s</a>' % (decode(m.group(2)), m.group(1), decode(m.group(2))), d)
    # <a href="/cdn-cgi/l/email-protection#HEX"> (mailto link whose text is something else)
    d = re.sub(r'<a href="/cdn-cgi/l/email-protection#([0-9a-f]+)"([^>]*)>',
               lambda m: '<a href="mailto:%s"%s>' % (decode(m.group(1)), m.group(2)), d)
    # <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="HEX">[email protected]</a>  (plain-text email)
    d = re.sub(r'<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="([0-9a-f]+)">\[email&#160;protected\]</a>',
               lambda m: decode(m.group(1)), d)
    d = re.sub(r'<span class="__cf_email__" data-cfemail="([0-9a-f]+)">\[email&#160;protected\]</span>',
               lambda m: decode(m.group(1)), d)
    d = re.sub(r'<script data-cfasync="false" src="/cdn-cgi/scripts/[^"]+"></script>', '', d)
    return d.rstrip() + '\n'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    src = open(sys.argv[1], encoding='utf8', errors='surrogateescape').read()
    out = extract(src)
    open(sys.argv[2], 'w', encoding='utf8', errors='surrogateescape').write(out)
    left = sum(out.count(x) for x in ('cdn-cgi', 'cfemail', 'email&#160;protected'))
    print('%s: %d bytes, Cloudflare leftovers: %d' % (sys.argv[2], len(out), left))
    if left:
        raise SystemExit('Leftover Cloudflare masking; check the output by hand.')
