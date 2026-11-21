#!/usr/bin/env python3
"""Fetch a logo for each software entry and normalize it to a 96x96 PNG.

Usage: python scripts/fetch_logos.py [id ...] [--force]

Needs Pillow. SVG logos are rendered with cairosvg if installed, otherwise with
Playwright through Node. Entries without a logo fall back to their Lucide icon.

Sources, in order: the entry's optional `logo` field (an image URL or
`github:<owner>`), icons declared on the entry's access and docs pages, then the
GitHub avatar of the repository owner when the owner name matches the project.
Logos are trademarks of their owners and appear only to identify the software.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets" / "logos"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
SIZE, PAD, MIN_SRC = 96, 8, 48
# sha1 of normalized PNGs for generic icons: GitHub octocat, MkDocs Material, OSM wiki, WordPress
BLOCK = {"669755d34856694a7dc96d09e9ccd8a7cbd3e735", "60f99567ea6f357f40def1401657a116b21292bd",
         "26407e1e58d73fcf2712e6b66ba3ddb84fe5b224", "6d5cac663313ead62e13e86b288efd0e96478658"}
COMMON = ["man/figures/logo.png", "man/figures/logo.svg", "docs/_static/logo.png", "docs/_static/logo.svg",
          "docs/source/_static/logo.png", "docs/source/_static/logo.svg", "doc/_static/logo.png", "docs/img/logo.png",
          "docs/images/logo.png", "docs/assets/logo.png", "docs/assets/logo.svg", "assets/logo.png", "assets/logo.svg",
          "logo.png", "logo.svg", ".github/logo.png", "pkgdown/favicon/apple-touch-icon.png", "pkgdown/assets/logo.png",
          "doc/logo.png", "images/logo.png", "img/logo.png", "docs/logo.png", "docs/logo.svg", "docs/_static/img/logo.png"]


def curl(url, binary=False, timeout=20):
    r = subprocess.run(["curl", "-sL", "--max-time", str(timeout), "-A", UA, "-w", "\n%{http_code}\n%{url_effective}", url],
                       capture_output=True)
    body, _, tail = r.stdout.rpartition(b"\n")
    body, _, code = body.rpartition(b"\n")
    final = tail.decode(errors="ignore")
    return (int(code or 0), body if binary else body.decode("utf-8", "ignore"), final)


class Icons(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []
        self.imgs = []
        self.og = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img" and a.get("src") and not a["src"].startswith("data:"):
            blob = " ".join([a.get("src", ""), a.get("alt") or "", a.get("class") or "", a.get("id") or ""]).lower()
            if "logo" in blob and not re.search(r"badge|shields|travis|codecov", blob):
                self.imgs.append(a["src"])
        if tag == "meta" and (a.get("property") or "").lower() == "og:image" and a.get("content"):
            self.og = a["content"]
        if tag == "link" and a.get("href") and "icon" in (a.get("rel") or "").lower():
            self.found.append((a["href"], a.get("sizes") or "", (a.get("type") or "").lower(), a.get("rel").lower()))


def page_icons(url):
    code, html, final = curl(url)
    if code != 200:
        return []
    p = Icons()
    try:
        p.feed(html[:200000])
    except Exception:
        pass
    out = []
    for href, sizes, typ, rel in p.found:
        if href.startswith("data:"):
            continue
        m = re.findall(r"(\d+)x\d+", sizes)
        px = max(map(int, m)) if m else (180 if "apple" in rel else 32)
        score = 1000 if (href.split("?")[0].endswith(".svg") or "svg" in typ) else px
        out.append((score, urljoin(final, href)))
    root = f"{urlparse(final).scheme}://{urlparse(final).netloc}"
    out.append((16, root + "/favicon.ico"))
    ordered = [u for _, u in sorted(out, key=lambda x: -x[0])]
    imgs = [urljoin(final, s) for s in p.imgs[:3]]
    return imgs + ordered


def render_svg(data):
    try:
        import cairosvg
        return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=data, output_width=256, output_height=256)))
    except ImportError:
        pass
    with tempfile.TemporaryDirectory() as d:
        src, dst = Path(d, "in.svg"), Path(d, "out.png")
        src.write_bytes(data)
        js = ("const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();"
              "const p=await b.newPage({viewport:{width:256,height:256}});const s=fs.readFileSync(process.argv[2]);"
              "await p.setContent(`<body style=\"margin:0;background:transparent\"><img src=\"data:image/svg+xml;base64,${s.toString('base64')}\" "
              "style=\"width:256px;height:256px;object-fit:contain\"></body>`);await p.waitForTimeout(150);"
              "await p.screenshot({path:process.argv[3],omitBackground:true});await b.close();})()")
        env = dict(os.environ)
        npm = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        env["NODE_PATH"] = npm
        r = subprocess.run(["node", "-e", js, str(src), str(dst)], capture_output=True, env=env, timeout=60)
        if r.returncode or not dst.exists():
            return None
        return Image.open(io.BytesIO(dst.read_bytes())).convert("RGBA")


def decode(data):
    head = data[:300].lstrip().lower()
    if head.startswith(b"<svg") or b"<svg" in head or head.startswith(b"<?xml"):
        return render_svg(data)
    img = Image.open(io.BytesIO(data))
    if img.format == "ICO":
        best = max(img.ico.sizes(), key=lambda s: s[0])
        img.size = best
        img = img.ico.getimage(best)
    return img.convert("RGBA")


def usable(img):
    if img is None or min(img.size) < MIN_SRC and max(img.size) < MIN_SRC:
        return False
    a = img.getchannel("A")
    if a.getextrema()[1] == 0:
        return False
    rgb = img.convert("RGB").resize((16, 16))
    colors = rgb.getcolors(256)
    return colors is None or len(colors) > 3 or a.getextrema()[0] < 250


def normalize(img):
    a = img.getchannel("A")
    box = a.point(lambda v: 255 if v > 8 else 0).getbbox()
    if box and (box[2] - box[0]) * (box[3] - box[1]) < img.size[0] * img.size[1]:
        img = img.crop(box)
    if max(img.size) / max(1, min(img.size)) > 2.2:
        return None
    inner = SIZE - 2 * PAD
    img.thumbnail((inner, inner), Image.LANCZOS)
    canvas = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    canvas.paste(img, ((SIZE - img.size[0]) // 2, (SIZE - img.size[1]) // 2), img)
    return canvas


def repo_logos(e):
    m = re.match(r"https://github.com/([^/]+)/([^/#]+)", e.get("repo", ""))
    if not m:
        return
    o, r = m.groups()
    base = f"https://raw.githubusercontent.com/{o}/{r}/HEAD/"
    for name in ("README.md", "README.rst", "readme.md", "README.markdown"):
        code, txt, _ = curl(base + name)
        if code != 200:
            continue
        refs = (re.findall(r"!\[[^\]]*\]\(([^)\s]+)", txt) + re.findall(r"<img[^>]+src=[\"']([^\"']+)", txt)
                + re.findall(r"\.\. (?:image|figure):: (\S+)", txt))
        for u in refs:
            u = u.split("#")[0].split("?")[0]
            if "logo" not in u.lower() or re.search(r"shields\.io|badge|img\.shields|travis|codecov", u.lower()):
                continue
            g = re.match(r"https://github.com/([^/]+/[^/]+)/(?:blob|raw)/(.+)", u)
            if g:
                u = f"https://raw.githubusercontent.com/{g.group(1)}/{g.group(2)}"
            elif not u.startswith("http"):
                u = base + u.lstrip("./")
            yield u
        break
    for p in COMMON:
        yield base + p


def candidates(e):
    logo = e.get("logo")
    if logo == "none":
        return
    if logo:
        yield f"https://avatars.githubusercontent.com/{logo[7:]}?s=256" if logo.startswith("github:") else logo
        return
    seen = set()
    for key in ("access", "docs"):
        for u in page_icons(e[key]):
            if u not in seen:
                seen.add(u)
                yield u
    yield from repo_logos(e)
    m = re.match(r"https://github.com/([^/]+)/", e.get("repo", ""))
    if m:
        owner = m.group(1).lower()
        words = re.sub(r"[^a-z0-9]", "", e["id"] + e["title"].lower())
        if owner in words or re.sub(r"[^a-z0-9]", "", e["id"]) in owner:
            yield f"https://avatars.githubusercontent.com/{m.group(1)}?s=256"


def fetch(e, force=False):
    dst = OUT / f"{e['id']}.png"
    if dst.exists() and not force:
        return "kept"
    for url in candidates(e):
        code, data, _ = curl(url, binary=True)
        if code != 200 or not data:
            continue
        try:
            img = decode(data)
        except Exception:
            continue
        if not usable(img):
            continue
        if "avatars.githubusercontent.com" in url and img.convert("RGB").getpixel((2, 2)) == (240, 240, 240):
            continue
        out = normalize(img)
        if out is None:
            continue
        buf = io.BytesIO()
        out.save(buf, "PNG", optimize=True)
        if hashlib.sha1(buf.getvalue()).hexdigest() in BLOCK:
            continue
        dst.write_bytes(buf.getvalue())
        return url
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    OUT.mkdir(parents=True, exist_ok=True)
    entries = [e for f in sorted((ROOT / "data" / "software").glob("*.yml")) for e in yaml.safe_load(f.read_text("utf-8"))]
    if args:
        entries = [e for e in entries if e["id"] in args]
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(12) as ex:
        results = list(ex.map(lambda e: (e["id"], fetch(e, force)), entries))
    miss = [i for i, r in results if r is None]
    for i, r in results:
        if r not in (None, "kept"):
            print(f"ok   {i:32} {r}")
    print(f"{len(results) - len(miss)} logos, {len(miss)} missing")
    for i in miss:
        print("miss", i)


if __name__ == "__main__":
    main()
