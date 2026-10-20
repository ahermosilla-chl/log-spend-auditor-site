#!/usr/bin/env bash
# Single source of truth for what gets published. Used by the GitHub Pages
# workflow and by the Cloudflare Pages build command (output dir: _site).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/validate_site.py
rm -rf _site && mkdir _site
cp -r index.html 404.html privacy terms sample-report site-v2.css favicon.svg robots.txt sitemap.xml _headers _site/
echo "Built _site/:"; find _site -type f | sort
