#!/usr/bin/env python3
"""Split the finished sandbox pages into shared blocks plus a middle for each page.

Why: every page (except Field Notes) is built as
    [ header block ]  +  [ page middle ]  +  [ footer block ]
so the menu and footer are edited once, in Taft's global header and footer.

Reads  sandbox/<page>.html
Writes sandbox/blocks/header-block.html   (menu, from index.html)
       sandbox/blocks/footer-block.html   (footer, from index.html)
       sandbox/middles/<page>.html        (page body only, styles scoped to .sy-block)

Run:  python3 -I tools/make_blocks.py
All CSS is scoped under `.sy-block` so nothing leaks into the surrounding Taft page.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "sandbox"
PAGES = ["index", "how-i-work", "workshops", "meet-dr-j", "contact", "saturday-seed"]

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500'
    '&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&display=swap" rel="stylesheet">\n'
)

# Neutralises whatever global CSS the surrounding page has (element rules, resets).
ISOLATE = (
    ".sy-block :where(h1,h2,h3,h4,p,ul,ol,li,a,div,span,form,label,button,input,b,strong,em,figure,header,footer,nav,"
    "section,blockquote,cite,textarea,small,svg){font-size:inherit;line-height:inherit;letter-spacing:inherit;"
    "text-transform:none;text-decoration:none;color:inherit;font-style:normal;font-weight:inherit;text-align:inherit}\n"
    ".sy-block *,.sy-block *::before,.sy-block *::after{margin:0;padding:0;box-sizing:border-box}\n"
    ".sy-block{font-family:var(--sy-sans);font-weight:400;font-size:17px;line-height:1.75;color:var(--sy-ink);"
    "-webkit-text-size-adjust:100%}\n"
    ".sy-block a{color:inherit;text-decoration:none}\n"
    ".sy-block img,.sy-block svg{max-width:100%}\n"
    ".sy-block ul,.sy-block ol{list-style:none}\n"
)

CHROME_SEL = re.compile(r"^(\.nav|\.brand|\.footer|\.seed-form|\.seed-name|\.seed(?![\w-])|\.sr\b|\.seed-top|\.seed-foot|\.back)")
HEADER_KEEP = re.compile(r"^(:root|\.wrap|\.btn|\.nav|\.brand|\.footer|\.seed-form|\.seed-name|\.seed(?![\w-])|\.sr\b)")


def split_rules(text):
    out, i, n = [], 0, len(text)
    while i < n:
        m = re.match(r"\s+", text[i:])
        if m:
            i += m.end()
            continue
        if text.startswith("/*", i):
            i = text.index("*/", i) + 2
            continue
        j = text.index("{", i)
        sel = text[i:j].strip()
        depth, k = 1, j + 1
        while depth and k < n:
            depth += (text[k] == "{") - (text[k] == "}")
            k += 1
        out.append((sel, text[j + 1:k - 1]))
        i = k
    return out


def prefix(sel):
    sel = sel.strip()
    if sel == ":root":
        return ".sy-block"
    if sel in ("html", "body"):
        return ".sy-block"
    if sel == "*":
        return ".sy-block *"
    if sel.startswith("html "):
        sel = sel[5:]
    if sel.startswith("body "):
        sel = sel[5:]
    return ".sy-block " + sel


def build(rules, keep):
    out = []
    for sel, body in rules:
        if sel.startswith("@media"):
            inner = build(split_rules(body), keep)
            if inner.strip():
                out.append(sel + "{" + inner + "}")
        elif sel.startswith("@keyframes") or sel.startswith("@font-face"):
            out.append(sel + "{" + body + "}")
        elif sel.startswith("@"):
            continue
        else:
            parts = [p.strip() for p in sel.split(",")]
            kept = [p for p in parts if keep(p)]
            if kept:
                out.append(",".join(prefix(p) for p in kept) + "{" + body.strip() + "}")
    return "\n".join(out)


def page_css(src):
    return "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(f"  wrote {path.relative_to(ROOT.parent)}  ({len(text)//1024} KB)")


NAV_JS = """<script>
(function(){
  var nav=document.getElementById('nav'),t=document.getElementById('navToggle');
  if(t&&nav){t.addEventListener('click',function(){
    var open=nav.classList.toggle('open');
    t.setAttribute('aria-expanded',open?'true':'false');
    t.setAttribute('aria-label',open?'Close menu':'Open menu');
  });}
  try{
    var p=location.pathname.replace(/\\/+$/,'')||'/';
    document.querySelectorAll('#nav .nav-links a').forEach(function(a){
      var u=new URL(a.href,location.href),q=u.pathname.replace(/\\/+$/,'')||'/';
      if(q===p){a.setAttribute('aria-current','page');}else{a.removeAttribute('aria-current');}
    });
  }catch(e){}
})();
</script>"""


def main():
    home = (ROOT / "index.html").read_text()
    shared = build(split_rules(page_css(home)), lambda p: bool(HEADER_KEEP.match(p)) or p == "*")
    header = re.search(r'<header class="nav" id="nav">.*?</header>', home, re.S).group(0)
    footer = re.search(r'<footer class="footer">.*?</footer>', home, re.S).group(0)
    note = ("<!-- SYNCOVATE {n} BLOCK. Paste into ONE Custom Code element ({where}). Self-contained: fonts, styles "
            "(scoped to .sy-block, nothing leaks into the rest of the page){extra}. Generated by tools/make_blocks.py "
            "from sandbox/index.html. Do not edit by hand; change the source page and regenerate. -->\n")
    style = "<style>\n" + ISOLATE + shared + "\n</style>\n"
    write(ROOT / "blocks" / "header-block.html",
          note.format(n="HEADER", where="the site's global header", extra=" and the menu script")
          + FONTS + style + '<div class="sy-block">\n' + header + "\n</div>\n" + NAV_JS + "\n")
    write(ROOT / "blocks" / "footer-block.html",
          note.format(n="FOOTER", where="the site's global footer", extra="")
          + FONTS + style + '<div class="sy-block">\n' + footer + "\n</div>\n")

    for name in PAGES:
        src = (ROOT / f"{name}.html").read_text()
        css = build(split_rules(page_css(src)), lambda p: not CHROME_SEL.match(p))
        main = re.search(r"<main>.*?</main>", src, re.S)
        if not main:
            print(f"  !! {name}: no <main> found", file=sys.stderr)
            continue
        # keep page scripts that sit after </main> (scroll reveal), drop the nav toggle part by leaving it null-safe
        tail = src[main.end():]
        scripts = "".join(re.findall(r"<script>.*?</script>", tail, re.S))
        mid_note = (f"<!-- SYNCOVATE PAGE MIDDLE: {name}. Paste into ONE Custom Code element between the header and footer "
                    "blocks. Styles are scoped to .sy-block. Generated by tools/make_blocks.py. -->\n")
        write(ROOT / "middles" / f"{name}.html",
              mid_note + FONTS + "<style>\n" + ISOLATE + css + "\n</style>\n"
              + '<div class="sy-block">\n' + main.group(0) + "\n</div>\n" + scripts + "\n")


if __name__ == "__main__":
    main()
