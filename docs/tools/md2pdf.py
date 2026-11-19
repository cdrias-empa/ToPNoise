#!/usr/bin/env python3
"""Build one PDF from the Markdown chapters of the ToPNoise guide.

Pipeline: Markdown --(markdown-it-py)--> one HTML page --(headless Chromium-based browser)--> PDF.

Requirements
------------
- Python 3.8 or later, with the package ``markdown-it-py``   (pip install markdown-it-py)
- A Chromium-based browser: Chromium, Google Chrome or Microsoft Edge.
  Under WSL, the Windows installation of Edge or Chrome is found automatically.

Usage
-----
  python3 docs/tools/md2pdf.py --out ToPNoise-guide.pdf
  python3 docs/tools/md2pdf.py --out ToPNoise-guide-review.pdf --show-notes

Chapters are taken in this order: index.md, the files NN-*.md in numerical order, then appendix-*.md.
Links between chapters become links inside the PDF. Images are embedded in the page.

The notes of the authors are HTML comments in the Markdown files (``<!-- TODO ... -->``).
They are not part of the shared PDF. With ``--show-notes`` they are printed as yellow boxes,
which is useful to review the draft.
"""

import argparse
import base64
import datetime
import html
import mimetypes
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from markdown_it import MarkdownIt
except ImportError:
    sys.exit("The package 'markdown-it-py' is required: pip install markdown-it-py")

CSS = """
@page {
  size: A4;
  margin: 20mm 18mm 22mm 18mm;
  @bottom-center { content: counter(page) " / " counter(pages); font: 9pt "DejaVu Sans", "Segoe UI", sans-serif; color: #666; }
}
@page :first { @bottom-center { content: none; } }
html { font-family: "DejaVu Sans", "Segoe UI", Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #1a1a1a; }
body { margin: 0; }
h1, h2, h3, h4 { color: #0b3d62; line-height: 1.25; break-after: avoid; }
h1 { font-size: 20pt; border-bottom: 2px solid #0b3d62; padding-bottom: 4pt; margin: 0 0 12pt 0; }
h2 { font-size: 14pt; margin: 18pt 0 6pt 0; }
h3 { font-size: 11.5pt; margin: 14pt 0 4pt 0; }
h4 { font-size: 10.5pt; }
p { margin: 5pt 0; orphans: 3; widows: 3; }
a { color: #0b5cad; text-decoration: none; }
section.chapter { break-before: page; }
ul, ol { margin: 4pt 0 4pt 0; padding-left: 20pt; }
li { margin: 2pt 0; }
li.task { list-style: none; position: relative; margin-left: -20pt; padding-left: 20pt; }
li.task .box { position: absolute; left: 0; font-size: 11pt; }
code { font-family: "DejaVu Sans Mono", Consolas, monospace; font-size: 8.8pt; background: #f1f3f5; padding: 0 2pt; border-radius: 2pt; }
pre { background: #f1f3f5; border: 1px solid #d9dde1; border-radius: 3pt; padding: 6pt 8pt; margin: 6pt 0;
      white-space: pre-wrap; word-break: break-word; break-inside: avoid; }
pre { font-size: 8.5pt; }
pre code { background: none; padding: 0; font-size: inherit; }
blockquote { margin: 7pt 0; padding: 4pt 10pt; border-left: 3pt solid #8aa9c4; background: #f4f8fb; }
blockquote p { margin: 3pt 0; }
table { border-collapse: collapse; width: 100%; margin: 7pt 0; font-size: 9pt; }
th, td { border: 1px solid #c8ced4; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #e8eef4; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
img { max-width: 100%; height: auto; display: block; margin: 6pt auto; break-inside: avoid; border: 1px solid #d9dde1; }
em { color: #333; }
hr { border: 0; border-top: 1px solid #c8ced4; }
.note { background: #fff8d6; border: 1px solid #e6d27a; border-left: 4pt solid #d4a900; padding: 4pt 8pt; margin: 6pt 0;
        font-size: 8.5pt; white-space: pre-wrap; break-inside: avoid; }
.note b { color: #8a6d00; }
.cover { height: 235mm; display: flex; flex-direction: column; justify-content: center; }
.cover h1 { font-size: 30pt; border: 0; }
.cover .sub { font-size: 15pt; color: #444; margin-bottom: 30pt; }
.cover .meta { color: #666; font-size: 10pt; }
.toc h2 { margin-top: 0; }
.toc ul { list-style: none; padding-left: 0; }
.toc li.l1 { margin-top: 7pt; font-weight: bold; }
.toc li.l2 { margin-left: 16pt; font-weight: normal; font-size: 9pt; margin-top: 1pt; }
"""


def chapter_files(docs):
    """Return the Markdown files of the guide, in reading order."""
    files = []
    if (docs / "index.md").is_file():
        files.append(docs / "index.md")
    files += sorted(p for p in docs.glob("[0-9][0-9]-*.md"))
    files += sorted(docs.glob("appendix-*.md"))
    return files


def chapter_id(path):
    return "ch-" + path.stem


def embed_image(src, base_dir, warnings):
    """Return a data URI for a local image, or the original src if it cannot be read."""
    if re.match(r"^(https?:|data:)", src):
        return src
    image = (base_dir / src).resolve()
    if not image.is_file():
        warnings.append(f"image not found: {src} (in {base_dir})")
        return src
    mime = mimetypes.guess_type(image.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(image.read_bytes()).decode("ascii")


CODE_FIT_CHARS = 90      # characters per line that fit at the normal size (8.5 pt)
CODE_MIN_PT = 6.8        # below this size the text is too small: the lines are wrapped instead


def fit_code_block(match):
    """Reduce the font size of a code block whose longest line is wider than the page."""
    longest = max(len(line) for line in html.unescape(match.group(2)).split("\n"))
    if longest > CODE_FIT_CHARS:
        size = 8.5 * CODE_FIT_CHARS / longest
        if size >= CODE_MIN_PT:
            return f'<pre style="font-size:{size:.1f}pt; white-space:pre"><code{match.group(1)}>{match.group(2)}</code></pre>'
    return match.group(0)


def render_chapter(path, md, show_notes, known_ids, warnings):
    """Render one Markdown file to HTML. Returns (html, [(level, title, id), ...])."""
    source = path.read_text(encoding="utf-8")
    body = md.render(source)

    # The list "Contents" of the first page is replaced, in the PDF, by the generated table of contents.
    if path.name == "index.md":
        body = re.sub(r"<h2>Contents</h2>.*?(?=<h2>|\Z)", "", body, flags=re.S)

    # Author's notes: HTML comments are kept by the Markdown renderer.
    def note(match):
        if not show_notes:
            return ""
        raw = re.sub(r"[ \t]*\n[ \t]*", "\n", match.group(1)).strip()
        label = "Note"
        tag = re.match(r"(TODO|REVIEW)(\([^)]*\))?:?\s*", raw)
        if tag:  # a leading TODO/REVIEW becomes the label of the box
            label = tag.group(1) + (" " + tag.group(2) if tag.group(2) else "")
            raw = raw[tag.end():]
        text = html.escape(raw)
        return f'<div class="note"><b>{html.escape(label)}</b> {text}</div>'

    body = re.sub(r"<!--(.*?)-->", note, body, flags=re.S)

    # Task list items: "- [ ] text"
    body = re.sub(r"<li>(\s*<p>)?\[ \] ", lambda m: '<li class="task">' + (m.group(1) or "") + '<span class="box">☐</span>', body)
    body = re.sub(r"<li>(\s*<p>)?\[[xX]\] ", lambda m: '<li class="task">' + (m.group(1) or "") + '<span class="box">☑</span>', body)

    # Links between chapters: "04-track.md" -> "#ch-04-track"
    def link(match):
        target = match.group(1)
        stem = Path(target.split("#")[0]).stem
        if f"ch-{stem}" in known_ids:
            return f'href="#ch-{stem}"'
        warnings.append(f"link to a file that is not in the guide: {target} (in {path.name})")
        return match.group(0)

    body = re.sub(r'href="([^"#:]+\.md(?:#[^"]*)?)"', link, body)

    # Wide code blocks (folder trees, diagrams) keep their layout: the font is reduced to fit the page.
    body = re.sub(r"<pre><code([^>]*)>(.*?)</code></pre>", fit_code_block, body, flags=re.S)

    # Embed images
    body = re.sub(r'<img src="([^"]+)"', lambda m: '<img src="' + embed_image(m.group(1), path.parent, warnings) + '"', body)

    # Anchors on headings, and the list of headings for the table of contents
    headings = []
    counter = {"n": 0}

    def heading(match):
        level, attrs, text = int(match.group(1)), match.group(2), match.group(3)
        if level > 2:
            return match.group(0)
        counter["n"] += 1
        hid = chapter_id(path) if level == 1 else f"{chapter_id(path)}-s{counter['n']}"
        headings.append((level, re.sub(r"<[^>]+>", "", html.unescape(text)), hid))
        return f'<h{level} id="{hid}"{attrs}>{text}</h{level}>'

    body = re.sub(r"<h([1-6])([^>]*)>(.*?)</h\1>", heading, body, flags=re.S)
    return f'<section class="chapter">{body}</section>', headings


def find_browser():
    """Find a Chromium-based browser. Returns (command, is_windows_exe) or (None, False)."""
    for name in ("microsoft-edge", "msedge", "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found, False
    for candidate in (
        "/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
        "/mnt/c/Program Files/Microsoft/Edge/Application/msedge.exe",
        "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe",
        "/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    ):
        if os.path.isfile(candidate):
            return candidate, True
    return None, False


def print_pdf(browser, windows_exe, html_file, pdf_file):
    """Print an HTML file to PDF with a headless browser."""
    if windows_exe:
        # A Windows program needs Windows paths. wslpath converts them.
        html_url = "file:///" + subprocess.check_output(["wslpath", "-m", str(html_file)], text=True).strip()
        pdf_arg = subprocess.check_output(["wslpath", "-w", str(pdf_file)], text=True).strip()
    else:
        html_url = html_file.resolve().as_uri()
        pdf_arg = str(pdf_file.resolve())
    command = [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf_arg}", html_url]
    if pdf_file.exists():
        pdf_file.unlink()
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)


def main():
    parser = argparse.ArgumentParser(description="Build one PDF from the Markdown chapters of the ToPNoise guide.")
    parser.add_argument("--docs", type=Path, default=Path(__file__).resolve().parent.parent, help="folder with the Markdown files (default: the folder docs/)")
    parser.add_argument("--out", type=Path, default=Path("ToPNoise-guide.pdf"), help="PDF file to write")
    parser.add_argument("--show-notes", action="store_true", help="print the notes of the authors (HTML comments) as yellow boxes")
    parser.add_argument("--status", default="Draft", help="text shown on the cover, e.g. 'Draft' or 'Version 1.0'")
    parser.add_argument("--keep-html", action="store_true", help="keep the intermediate HTML file next to the PDF")
    args = parser.parse_args()

    docs = args.docs.resolve()
    files = chapter_files(docs)
    if not files:
        sys.exit(f"No chapter found in {docs}")
    known_ids = {chapter_id(p) for p in files}

    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    warnings, chapters, toc = [], [], []
    for path in files:
        chapter_html, headings = render_chapter(path, md, args.show_notes, known_ids, warnings)
        chapters.append(chapter_html)
        for level, title, hid in headings:
            toc.append(f'<li class="l{level}"><a href="#{hid}">{html.escape(title)}</a></li>')

    today = datetime.date.today().isoformat()
    cover = (
        '<section class="cover"><h1>ToPNoise</h1><div class="sub">Step-by-step guide</div>'
        f'<div class="meta">{html.escape(args.status)} &middot; {today}</div></section>'
    )
    toc_html = '<section class="chapter toc"><h2>Contents</h2><ul>' + "".join(toc) + "</ul></section>"
    document = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>ToPNoise - step-by-step guide</title>'
        f"<style>{CSS}</style></head><body>{cover}{toc_html}{''.join(chapters)}</body></html>"
    )

    out = args.out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    html_file = out.with_suffix(".html")
    html_file.write_text(document, encoding="utf-8")

    browser, windows_exe = find_browser()
    if browser is None:
        sys.exit(f"No Chromium-based browser found (Chromium, Google Chrome or Microsoft Edge).\nThe HTML page is in {html_file}: open it in a browser and print it to PDF.")

    print_pdf(browser, windows_exe, html_file, out)
    if not out.is_file() or out.stat().st_size == 0:
        sys.exit(f"The browser did not write the PDF. The HTML page is in {html_file}")
    if not args.keep_html:
        html_file.unlink()

    pages = len(re.findall(rb"/Type\s*/Page[^s]", out.read_bytes()))
    print(f"{out}  ({out.stat().st_size // 1024} KiB, about {pages} pages, {len(files)} chapters, browser: {Path(browser).name})")
    for message in warnings:
        print("warning:", message)


if __name__ == "__main__":
    main()
