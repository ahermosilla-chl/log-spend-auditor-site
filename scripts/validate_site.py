"""Static-site validation (stdlib only): python scripts/validate_site.py"""
import re, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMUNITY = "https://logspendauditor.lemonsqueezy.com/checkout/buy/523549b0-405d-4bcf-a2f1-47c3e58e5934"
PRO = "https://logspendauditor.lemonsqueezy.com/checkout/buy/294c335c-f859-4297-9a2c-e9415ec3e669?checkout[discount_code]=LAUNCH69"
PAGES = ["index.html", "privacy/index.html", "terms/index.html"]
CANONICAL = {
    "index.html": "https://logspendauditor.com/",
    "privacy/index.html": "https://logspendauditor.com/privacy/",
    "terms/index.html": "https://logspendauditor.com/terms/",
}
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
        if tag in ("img", "link", "source", "video", "audio", "use"):
            ref = a.get("src") or a.get("href") or ""
            if tag == "link" and a.get("rel") == "canonical":
                if ref != CANONICAL[page]:
                    err(f"{page}: canonical is {ref!r}, expected {CANONICAL[page]!r}")
            elif re.match(r"(https?:)?//", ref):
                err(f"{page}: external resource {ref}")
            elif tag == "use" and not ref.startswith("#"):
                err(f"{page}: <use> must reference an inline symbol, got {ref}")
        if any(k.startswith("on") for k in a):
            err(f"{page}: inline event handler")
    if re.search(r"@import|url\(\s*['\"]?https?:", raw):
        err(f"{page}: external CSS import")

    if not any(t == "link" and a.get("rel") == "canonical" for t, a in p.tags):
        err(f"{page}: missing canonical link")
    if f'content="{CANONICAL[page]}"' not in raw:
        err(f"{page}: og:url does not match canonical")
    if "github.io" in raw:
        err(f"{page}: github.io must not appear")

    # heading hierarchy: exactly one h1, no skipped levels
    levels = [int(t[1]) for t, _a in p.tags if re.fullmatch(r"h[1-6]", t)]
    if levels.count(1) != 1:
        err(f"{page}: expected exactly one h1, found {levels.count(1)}")
    for prev, cur in zip(levels, levels[1:]):
        if cur > prev + 1:
            err(f"{page}: heading level skips from h{prev} to h{cur}")
    for tag, a in p.tags:
        if tag == "svg" and a.get("aria-hidden") != "true" and "role" not in a and a.get("width") != "0":
            err(f"{page}: <svg> without aria-hidden or role")
        if tag == "img" and "alt" not in a:
            err(f"{page}: <img> without alt")

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
for label, url in (("Download Community — Free", COMMUNITY), ("Buy Pro — $69", PRO)):
    found = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>\s*' + re.escape(label) + r"\s*</a>", raw)
    if len(found) < 3 or any(f != url for f in found):
        err(f"CTA {label!r}: expected >=3 links, all exactly {url}; got {found}")
for k in ("Regular price $99", "One-time purchase", "Built and tested on Ubuntu 22.04 LTS", "Requires glibc 2.35 or newer",
          "Launch price limited to the first 10 redemptions.", "No license required", "1 active installation", "License does not expire",
          "Start with Community. Upgrade to Pro in the same application — no reinstall required.",
          "Available now", "Coming later", "no reinstall required", "Community discovers the problem. Pro explains the problem.",
          "Find where your Splunk ingest budget is going — without sending your data anywhere."):
    if k not in raw:
        err(f"index.html: missing copy {k!r}")
if hrefs.count(COMMUNITY) + hrefs.count(PRO) != sum(1 for h in hrefs if h and "lemonsqueezy" in h):
    err("index.html: unexpected lemonsqueezy link")
if re.search(r"(?i)subscri", raw):
    err("subscription mentioned")

# css has no external references
css = (ROOT / "site-v2.css").read_text(encoding="utf-8")
if re.search(r"https?://|@import", css):
    err("site-v2.css: external reference")

# every page must load the current stylesheet (stale cached CSS broke production once)
for page in PAGES:
    if 'href="' + ("../" if "/" in page else "") + 'site-v2.css"' not in parsed[page][0]:
        err(f"{page}: does not link site-v2.css")
if (ROOT / "style.css").exists():
    err("old style.css still present")

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
