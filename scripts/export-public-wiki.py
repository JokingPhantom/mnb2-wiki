"""Export only admitted player wiki content as a public, server-free /wiki/ site.

Run with a Python environment containing scripts/wiki-requirements.txt. No server,
database, account, or remote service is opened. The output directory must be new.
"""
import argparse
import hashlib
from html import escape, unescape
import json
from pathlib import Path
import re
import sys

REPOSITORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY))

from orchestration.combined_host.wiki import Wiki, expanded_details, inline_text, parser
from orchestration.combined_host import wiki as wiki_renderer, wiki_media as wiki_media_renderer, storage as wiki_storage

# Prepared interpreters may also admit another checkout in their fixed sys.path.
# Never attribute that checkout's content to this exporter's source revision.
for module in (wiki_renderer, wiki_media_renderer, wiki_storage):
    if Path(module.__file__).resolve().parent != REPOSITORY / 'orchestration' / 'combined_host':
        raise ImportError('public-wiki-renderer-origin-mismatch')


STYLE = """html{color-scheme:dark}*{box-sizing:border-box}body{margin:0;background:#151b18;color:#e4e8dd;font:17px/1.65 system-ui,sans-serif}header,main,footer{max-width:1100px;margin:auto;padding:1rem 1.5rem}header{border-bottom:1px solid #637057}nav{display:flex;flex-wrap:wrap;gap:1rem}a{color:#c4dc94}a:focus-visible,input:focus-visible{outline:3px solid #e4c96f;outline-offset:3px}.edition{color:#c8cabc;font-size:.9rem}article{overflow-wrap:anywhere}h1,h2,h3{line-height:1.25;scroll-margin-top:1rem}table{display:block;max-width:100%;overflow-x:auto;border-collapse:collapse}td,th{padding:.5rem;border:1px solid #637057;text-align:left}pre{overflow:auto;padding:1rem;background:#202923}img{max-width:100%;height:auto}input{display:block;width:100%;max-width:40rem;padding:.7rem;font:inherit;background:#202923;color:inherit;border:1px solid #88967c}#results li{margin:.8rem 0}footer{border-top:1px solid #637057;font-size:.85rem}details{margin:1rem 0}.skip{position:absolute;left:-10000px}.skip:focus{position:static}code{overflow-wrap:anywhere}
"""

SEARCH = """'use strict';
const input = document.querySelector('#search');
const output = document.querySelector('#results');
const status = document.querySelector('#search-status');
let entries;
async function search() {
  const query = input.value.trim().toLocaleLowerCase();
  output.replaceChildren();
  if (!query) { status.textContent = ''; return; }
  try {
    entries ??= await fetch('/wiki/search.json').then(response => {
      if (!response.ok) throw Error('Search unavailable');
      return response.json();
    });
    if (query !== input.value.trim().toLocaleLowerCase()) return;
    const words = query.split(/\\s+/);
    const matches = entries.filter(entry => words.every(word =>
      (entry.title + ' ' + entry.text).toLocaleLowerCase().includes(word)));
    matches.sort((a,b) => Number(b.title.toLocaleLowerCase().includes(query)) - Number(a.title.toLocaleLowerCase().includes(query)) || a.title.localeCompare(b.title));
    for (const entry of matches.slice(0,50)) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.href = entry.url; link.textContent = entry.title;
      const summary = document.createElement('p');
      const position = entry.text.toLocaleLowerCase().indexOf(words[0]);
      summary.textContent = entry.text.slice(Math.max(0,position-50),Math.max(0,position-50)+220);
      item.append(link,summary); output.append(item);
    }
    status.textContent = matches.length + ' matching articles' + (matches.length > 50 ? '; showing the first 50.' : '.');
  } catch { status.textContent = 'Search could not load. Use All articles below.'; }
}
input.addEventListener('input', search);
"""


def public_url(page, base='/wiki/'):
    return base if page.slug == 'index' else f'{base}{page.slug}/'


def public_render(wiki, page, base='/wiki/'):
    """Rewrite only attributes emitted by the existing sanitized renderer."""
    routes = {value.url: public_url(value, base) for value in wiki.pages.values()}

    def rewrite(match):
        attr, url = match[1], unescape(match[2])
        path, marker, fragment = url.partition('#')
        if path in routes:
            url = routes[path] + (marker + fragment if marker else '')
        elif path.startswith('/wiki-media/'):
            url = base + 'media/' + path.removeprefix('/wiki-media/')
        return f'{attr}="{escape(url, quote=True)}"'

    return re.sub(r'(href|src)="([^"]*)"', rewrite, wiki.render(page))


def shell(title, body, edition='', base='/wiki/'):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · Mud and Blood 2 Wiki</title><link rel="stylesheet" href="{base}assets/style.css"></head>
<body><a class="skip" href="#content">Skip to article</a><header><nav aria-label="Main"><a href="/">Games</a><a href="{base}">Wiki home</a><a href="{base}all/">All articles and search</a></nav></header>
<main id="content"><p class="edition">{escape(edition)}</p>{body}</main>
<footer>Community reconstruction reference. Read each article's edition and evidence qualifications. Saves remain in your browser.</footer></body></html>'''


def fresh_output(output):
    output = Path(output).absolute()
    if output.exists() or any(part.is_symlink() or part.is_junction() for part in (output, *output.parents)):
        raise ValueError('wiki-output-must-be-new-and-unlinked')
    return output


def export_wiki(output, *, wiki=None, base='/wiki/', source_output=None):
    output = fresh_output(output)
    if not re.fullmatch(r'/(?:[a-zA-Z0-9][a-zA-Z0-9._-]*/)+', base):
        raise ValueError('wiki-base-must-be-an-absolute-directory-url')
    if source_output is not None:
        source_output = fresh_output(source_output)
        if source_output.is_relative_to(output) or output.is_relative_to(source_output):
            raise ValueError('wiki-source-output-must-be-separate')
    wiki = wiki or Wiki()
    # The hosted import also admits developer documents. They are deliberately
    # excluded here, including link resolution, before any rendering occurs.
    wiki.pages = {key: value for key, value in wiki.pages.items() if key[0] == 'player'}
    wiki.sources = {source: page for source, page in wiki.sources.items() if page.wiki == 'player'}
    if ('player', 'index') not in wiki.pages or any(page.slug in ('all', 'assets', 'media') for page in wiki.pages.values()):
        raise ValueError('wiki-public-route-collision')
    pages = sorted(wiki.pages.values(), key=lambda page: page.slug)
    files = {'assets/style.css': STYLE.encode(), 'assets/search.js': SEARCH.replace("'/wiki/search.json'", json.dumps(base + 'search.json')).encode()}
    search_entries, identities = [], []
    for page in pages:
        path = 'index.html' if page.slug == 'index' else f'{page.slug}/index.html'
        sections = page.sections()
        contents = ''.join(f'<li><a href="#{escape(section["id"])}">{escape(section["title"])}</a></li>' for section in sections)
        toc = f'<details><summary>On this page</summary><ul>{contents}</ul></details>' if sections else ''
        body = toc + '<article>' + public_render(wiki, page, base) + '</article>'
        files[path] = shell(page.title, body, page.edition, base).encode()
        text = ' '.join(inline_text(token.children) for token in parser().parse(expanded_details(page.markdown)) if token.type == 'inline')
        search_entries.append(dict(title=page.title, url=public_url(page, base), text=text, edition=page.edition))
        identities.append(dict(slug=page.slug, sha256=page.source_hash, qualification=page.label))
    directory = ''.join(f'<li><a href="{public_url(page, base)}">{escape(page.title)}</a></li>' for page in sorted(pages, key=lambda page: page.title.casefold()))
    body = f'''<h1>All articles and search</h1><label for="search">Search the player wiki</label><input id="search" type="search" maxlength="100" autocomplete="off"><p id="search-status" role="status"></p><ul id="results"></ul><h2>All articles</h2><ul>{directory}</ul><script src="{base}assets/search.js" defer></script>'''
    files['all/index.html'] = shell('All articles and search', body, base=base).encode()
    files['search.json'] = json.dumps(search_entries, ensure_ascii=False, separators=(',', ':')).encode()
    media_records = []
    for name, media in sorted(wiki.media.items.items()):
        files['media/' + name] = media.data
        media_records.append(dict(filename=name, sha256=media.sha256, credit=media.credit, rights='original-project-diagram'))
    manifest = dict(schema='mnb2-public-wiki-v1', pages=identities, media=media_records,
                    files=[dict(path=path, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest()) for path, raw in sorted(files.items())])
    files['public-wiki.json'] = (json.dumps(manifest, indent=2, ensure_ascii=False) + '\n').encode()
    # Build and validate every byte before creating output; never overwrite a
    # previous release or copy arbitrary repository files into the public tree.
    source_files = public_sources(wiki) if source_output is not None else None
    write_files(output, files)
    if source_files is not None:
        write_files(source_output, source_files)
    return dict(pages=len(pages), files=len(files), bytes=sum(map(len, files.values())))


def write_files(output, files):
    output.mkdir(parents=True)
    for name, data in sorted(files.items()):
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def public_sources(wiki):
    """A portable public repository seed; no developer docs or host state."""
    pages = [page for page in wiki.pages.values() if page.wiki == 'player']
    files = {page.source: page.markdown.encode() for page in pages}
    # Both levels must be regular packages. Namespace packages can otherwise lose
    # to a different checkout's regular package later on an isolated sys.path.
    files['orchestration/__init__.py'] = b'"""Public player wiki tooling."""\n'
    files['orchestration/combined_host/__init__.py'] = b'"""Portable read-only wiki renderer."""\n'
    manifest = [dict(wiki=page.wiki, slug=page.slug, source=page.source, sha256=page.source_hash, label=page.label) for page in pages]
    # Wiki validates both indexes; the portable bundle substitutes a newly authored
    # inert placeholder instead of distributing the project's developer index.
    placeholder = b'# Developer index\n\nThis public repository contains the player wiki only.\n'
    placeholder_source = 'orchestration/combined_host/wiki_sources/dev-index.md'
    files[placeholder_source] = placeholder
    manifest.append(dict(wiki='dev', slug='index', source=placeholder_source,
                         sha256=hashlib.sha256(placeholder).hexdigest(), label='Public bundle placeholder; no developer documents are distributed.'))
    files['orchestration/combined_host/wiki_manifest.json'] = (json.dumps(dict(schema=1, pages=manifest), indent=2) + '\n').encode()
    for name, media in wiki.media.items.items():
        files[media.source] = media.data
    files['orchestration/combined_host/wiki_media_manifest.json'] = (REPOSITORY / 'orchestration/combined_host/wiki_media_manifest.json').read_bytes()
    for name in ('wiki.py', 'wiki_media.py'):
        files['orchestration/combined_host/' + name] = (REPOSITORY / 'orchestration/combined_host' / name).read_bytes()
    files['orchestration/combined_host/storage.py'] = b'"""Public wiki source root; no server storage."""\nfrom pathlib import Path\nREPOSITORY = Path(__file__).resolve().parents[2]\n'
    files['scripts/export-public-wiki.py'] = Path(__file__).read_bytes()
    files['requirements.txt'] = b'markdown-it-py==4.2.0\nnh3==0.3.7\nmdurl==0.1.2\n'
    files['.gitignore'] = b'.venv/\nsite/\n__pycache__/\n*.pyc\n.env*\n'
    files['README.md'] = b'''# Mud and Blood 2 player wiki

Curated project-authored player reference and original instructional diagrams.
Preserve the edition, evidence and source qualifications in every article.
Only the exact admitted diagrams are included; original game media is excluded.

Use Python 3.14 or newer. Install requirements.txt into a local virtual environment.
Build with `python scripts/export-public-wiki.py --output site --base /wiki/`.
The output directory must be new. Serve the resulting directory at /wiki/.

Edit Markdown under research/mnb2/wiki/player/. The source manifest pins each
article's SHA-256; update its hash when approving an edit. Content commits do not
publish the live site. A human requests a release and the publishing agent builds
and deploys that selected committed revision.
'''
    return files


def main():
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument('--output', required=True, type=Path)
    arguments.add_argument('--base', default='/wiki/')
    arguments.add_argument('--source-output', type=Path)
    options = arguments.parse_args()
    try:
        print(json.dumps(export_wiki(options.output, base=options.base, source_output=options.source_output)))
    except (OSError, ValueError) as error:
        arguments.exit(1, f'Wiki export refused: {error}\n')


if __name__ == '__main__':
    main()
