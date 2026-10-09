"""Static-site validation (stdlib only): python scripts/validate_site.py"""
import re, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMUNITY = "https://logspendauditor.lemonsqueezy.com/checkout/buy/523549b0-405d-4bcf-a2f1-47c3e58e5934"
PRO = "https://logspendauditor.lemonsqueezy.com/checkout/buy/294c335c-f859-4297-9a2c-e9415ec3e669?checkout[discount_code]=LAUNCH69"
PAGES = ["index.html", "privacy/index.html", "terms/index.html"]
VOID = {"meta", "link", "br", "img", "hr", "input"}
errors: list[str] = []


def err(msg):
    errors.append(msg)


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.links, self.ids, self.tags, self.text = [], [], set(), [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a))
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a":
            self.links.append(a)
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            err(f"unbalanced </{tag}> (open: {self.stack[-3:]})")
        else:
            self.stack.pop()

    def handle_data(self, d):
        self.text.append(d)


parsed = {}
for page in PAGES:
    raw = (ROOT / page).read_text(encoding="utf-8")
    p = P()
    p.feed(raw)
    if p.stack:
        err(f"{page}: unclosed tags {p.stack}")
    parsed[page] = (raw, p)

    # no JS, no external resources other than deliberate checkout links
    for tag, a in p.tags:
        if tag in ("script", "iframe", "object", "embed", "form", "input"):
            err(f"{page}: forbidden <{tag}>")
        if tag in ("img", "link", "source", "video", "audio") :
            ref = a.get("src") or a.get("href") or ""
            if re.match(r"(https?:)?//", ref):
                err(f"{page}: external resource {ref}")
        if any(k.startswith("on") for k in a):
            err(f"{page}: inline event handler")
    if re.search(r"@import|url\(\s*['\"]?https?:", raw):
        err(f"{page}: external CSS import")

    # links
    for a in p.links:
        href = a.get("href", "")
        if href.startswith("#"):
            if href[1:] not in p.ids:
                err(f"{page}: broken anchor {href}")
        elif href.startswith("mailto:"):
            pass
        elif href.startswith("https://"):
            if href not in (COMMUNITY, PRO):
                err(f"{page}: unexpected external link {href}")
            if "noopener" not in a.get("rel", ""):
                err(f"{page}: external link without rel=noopener {href}")
        elif re.match(r"[a-z]+:", href):
            err(f"{page}: unexpected scheme {href}")
        else:
            target = (ROOT / page).parent / href.split("#")[0]
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                err(f"{page}: broken internal link {href}")

    text = " ".join(p.text)
    for pat, why in [
        (r"/checkout/\?cart=", "cart URL"),
        (r"test[ -]?mode|/test/|sandbox", "test mode"),
        (r"sales (are )?(coming|will)|when commercial sales|go live|coming soon", "old 'sales later' wording"),
        (r"subscription", "subscription wording"),
        (r"prepared for macOS", "old platform statement"),
        (r"\$(?!69\b|99\b)\d+", "unexpected price"),
        (r"(?i)download[^<]{0,40}(windows|macos)|buy[^<]{0,40}(windows|macos)", "Windows/macOS CTA"),
        (r"(?i)google-analytics|gtag|plausible|fonts\.googleapis", "tracking/external font"),
        (r"(?i)(variant|product)[ _-]?id|\b\d{6,7}\b", "possible product/variant id"),
        (r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", None),
    ]:
        scan = raw if why is None else raw
        for m in re.finditer(pat, scan, re.I if why else 0):
            val = m.group(0)
            if why is None:  # UUIDs only allowed inside the two checkout URLs
                if val in COMMUNITY or val in PRO:
                    continue
                why_ = "uuid outside checkout URLs"
            else:
                why_ = why
            err(f"{page}: {why_}: {val!r}")
    for needle in ("not affiliated with or endorsed by Splunk Inc",):
        if needle not in raw:
            err(f"{page}: missing trademark disclaimer")
    if "Last updated" in raw and "2026-10-09" not in raw:
        err(f"{page}: Last updated not 2026-10-09")

# checkout CTAs on landing
raw, p = parsed["index.html"]
hrefs = [a.get("href") for a in p.links]
for label, url in (("Download Community — Free", COMMUNITY), ("Buy Pro — $69 Launch Price", PRO)):
    found = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>\s*' + re.escape(label) + r"\s*</a>", raw)
    if len(found) < 2 or any(f != url for f in found):
        err(f"CTA {label!r}: expected >=2 links, all exactly {url}; got {found}")
for k in ("Regular price $99", "One-time purchase", "Linux x86_64. Built and tested on Ubuntu 22.04 LTS. Requires glibc 2.35 or newer.",
          "Available now", "Coming later", "no reinstall required", "Community discovers the problem. Pro explains the problem.",
          "Find where your Splunk ingest budget is going — without sending your data anywhere."):
    if k not in raw:
        err(f"index.html: missing copy {k!r}")
if hrefs.count(COMMUNITY) + hrefs.count(PRO) != sum(1 for h in hrefs if h and "lemonsqueezy" in h):
    err("index.html: unexpected lemonsqueezy link")
if re.search(r"(?i)subscri", raw):
    err("subscription mentioned")

# css has no external references
css = (ROOT / "style.css").read_text(encoding="utf-8")
if re.search(r"https?://|@import", css):
    err("style.css: external reference")

# secrets in any tracked file
for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and f.suffix in {".html", ".css", ".txt", ".yml", ".py", ".svg"}:
        if re.search(r"ghp_[0-9A-Za-z]{20}|sk_(live|test)_|BEGIN [A-Z ]*PRIVATE KEY|hermosilla2|dxc\.com|eyJ[A-Za-z0-9_-]{10,}\.eyJ", f.read_text(encoding="utf-8")) and f.name != "validate_site.py":
            err(f"{f.relative_to(ROOT)}: sensitive pattern")

if errors:
    print("\n".join(errors))
    print(f"SITE VALIDATION FAILED: {len(errors)} problem(s)")
    sys.exit(1)
print("SITE VALIDATION OK")
