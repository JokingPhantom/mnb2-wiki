"""Explicit immutable text imports and HTML-disabled wiki rendering. No file writes."""
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import unicodedata
from urllib.parse import quote, unquote, urlsplit

from markdown_it import MarkdownIt
import nh3

from .storage import REPOSITORY

MAX_BYTES = 256 * 1024
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
ROOTS = ('research/mnb2/wiki/player/', 'orchestration/combined_host/wiki_sources/', 'docs/')
DEV_SOURCES = {'docs/ARCHITECTURE_TARGET.md', 'docs/SIMULATION_M1.md', 'docs/TOOLING_M6.md',
               'orchestration/combined_host/wiki_sources/dev-index.md'}
TAGS = {'p', 'br', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'em', 'strong',
        's', 'blockquote', 'ul', 'ol', 'li', 'pre', 'code', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'img'}
ATTRS = {'a': {'href'}, 'img': {'src', 'alt', 'width', 'height', 'loading'},
         'table': {'tabindex', 'aria-label'}, **{f'h{i}': {'id'} for i in range(1, 7)}}


def parser():
    return MarkdownIt('js-default', {'html': False, 'maxNesting': 20}).enable('table')


def bounded_text(text):
    if not isinstance(text, str) or len(text.encode('utf-8')) > MAX_BYTES or '\x00' in text:
        raise ValueError('wiki-text-bound')
    return text


def expanded_details(text):
    """Only exact standalone wrappers become expanded text; arbitrary HTML stays escaped.

    Avoid touching code fences. Summary content still passes through HTML-disabled
    Markdown and the sanitizer, so this never admits HTML attributes or raw tags.
    """
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            result.append(line)
            continue
        stripped = line.strip()
        if fence is None and stripped in ('<details>', '</details>'):
            result.append('')
        elif fence is None and (summary := re.fullmatch(r'<summary>([^<>]{1,500})</summary>', stripped)):
            result.append('\n' + summary[1] + '\n')
        else:
            result.append(line)
    return '\n'.join(result)


def inline_text(tokens):
    return ''.join(token.content for token in (tokens or []) if token.type in
                   ('text', 'code_inline', 'softbreak', 'hardbreak', 'image'))


def fragment_name(text):
    text = unicodedata.normalize('NFC', text).lower()
    return ''.join(c for c in text if c.isalnum() or c in ('_', '-', ' ')).replace(' ', '-')


def heading_map(tokens, prefix):
    fragments, used = {}, set()
    for index, token in enumerate(tokens):
        if token.type != 'heading_open':
            continue
        original = fragment_name(inline_text(tokens[index + 1].children))
        fragment, count = original, 0
        while fragment in used:
            count += 1
            fragment = f'{original}-{count}'
        used.add(fragment)
        # ASCII prefix and digest keep arbitrary authored strings out of HTML IDs.
        identifier = prefix + hashlib.sha256(fragment.encode()).hexdigest()[:20]
        fragments[fragment] = identifier
        token.attrSet('id', identifier)
    return fragments


@dataclass(frozen=True)
class Page:
    wiki: str
    slug: str
    source: str
    source_hash: str
    label: str
    markdown: str

    @property
    def url(self):
        return f'/wiki/{self.wiki}/' + ('' if self.slug == 'index' else self.slug)

    @property
    def title(self):
        tokens = parser().parse(expanded_details(self.markdown))
        for i, token in enumerate(tokens):
            if token.type == 'heading_open':
                return inline_text(tokens[i + 1].children).strip()[:160] or self.slug
        return self.slug

    @property
    def edition(self):
        if self.wiki != 'player':
            return 'Project developer reference'
        if self.source.startswith('wiki-created/'):
            return 'Edition not declared — check the article before applying advice'
        if self.slug in ('combat-results', 'combat-issues', 'rifle-skill'):
            return 'Modern reconstruction — check the dated build and corrections'
        if self.slug in ('sniper', 'weapon-comparison', 'grenades', 'unit-lifecycle',
                         'grease-gun', 'm1-garand', 'mortar', 'officer', 'regular-soldier',
                         'shotgun', 'editions', 'index', 'topic-index', 'whats-new', 'evidence-and-method'):
            return 'Historical 2.3.1g and explicitly marked modern sections'
        return 'Historical Mud and Blood 2 — selected publisher-associated 2.3.1g'

    def sections(self, markdown=None):
        tokens = parser().parse(expanded_details(self.markdown if markdown is None else markdown))
        heading_map(tokens, f'w-{self.wiki}-{self.slug}-')
        return [dict(title=inline_text(tokens[i + 1].children), id=token.attrGet('id'), level=token.tag)
                for i, token in enumerate(tokens) if token.type == 'heading_open' and token.tag in ('h2', 'h3')]


class Wiki:
    def __init__(self, manifest=None, *, repository=REPOSITORY):
        from .wiki_media import WikiMedia
        self.media = WikiMedia()
        self.pages, self.sources, self.fragments = {}, {}, {}
        total_bytes = 0
        repository = Path(repository).absolute()
        path = Path(manifest) if manifest is not None else Path(__file__).with_name('wiki_manifest.json')
        if path.stat().st_size > 2 * 1024 * 1024 or path.is_symlink() or path.is_junction():
            raise ValueError('wiki-manifest-bound')
        def unique(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError('wiki-duplicate-key')
                result[key] = value
            return result
        data = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)
        if (set(data) != {'schema', 'pages'} or data['schema'] != 1
                or not isinstance(data['pages'], list) or not 2 <= len(data['pages']) <= 1000):
            raise ValueError('wiki-manifest-schema')
        for entry in data['pages']:
            if set(entry) != {'wiki', 'slug', 'source', 'sha256', 'label'}:
                raise ValueError('wiki-entry-schema')
            wiki, slug, source, digest, label = (entry[k] for k in ('wiki', 'slug', 'source', 'sha256', 'label'))
            if (wiki not in ('player', 'dev') or not isinstance(slug, str) or not SLUG.fullmatch(slug)
                    or len(slug) > 100 or not isinstance(source, str) or not source.isascii()
                    or '\\' in source or not source.endswith('.md') or source.startswith('/')
                    or any(p in ('', '.', '..') or p.startswith('.') for p in source.split('/'))
                    or not isinstance(digest, str) or not re.fullmatch('[0-9a-f]{64}', digest)
                    or not isinstance(label, str) or not 1 <= len(label) <= 300):
                raise ValueError('wiki-entry-bound')
            if (wiki == 'player' and not source.startswith(ROOTS[0])) or (wiki == 'dev' and source not in DEV_SOURCES):
                raise ValueError('wiki-source-not-admitted')
            candidate = repository / source
            if any(p.is_symlink() or p.is_junction() for p in (candidate, *candidate.parents)):
                raise ValueError('wiki-source-link')
            if not candidate.resolve().is_relative_to(repository.resolve()) or candidate.stat().st_size > MAX_BYTES:
                raise ValueError('wiki-source-bound')
            raw = candidate.read_bytes()
            if len(raw) > MAX_BYTES or hashlib.sha256(raw).hexdigest() != digest:
                raise ValueError('wiki-source-hash')
            total_bytes += len(raw)
            if total_bytes > 16 * 1024 * 1024:
                raise ValueError('wiki-import-bound')
            text = bounded_text(raw.decode('utf-8'))
            key = (wiki, slug)
            if key in self.pages or source.casefold() in self.sources:
                raise ValueError('wiki-duplicate-page')
            page = Page(wiki, slug, source, digest, label, text)
            self.pages[key] = page
            self.sources[source.casefold()] = page
            self.fragments[key] = heading_map(parser().parse(expanded_details(text)), f'w-{wiki}-{slug}-')
        if any((wiki, 'index') not in self.pages for wiki in ('player', 'dev')):
            raise ValueError('wiki-index-required')

    def page(self, wiki, slug='index'):
        if slug in ('README.md', 'index.md'):
            slug = 'index'
        elif slug.endswith('.md'):
            slug = slug[:-3]
        return self.pages.get((wiki, slug))

    def link(self, page, href):
        """Resolve identifiers, never request-controlled disk paths. None means labelled text."""
        if (not isinstance(href, str) or len(href) > 2048 or '\\' in href
                or any(ord(c) < 33 or ord(c) == 127 or unicodedata.category(c).startswith('C') for c in href)
                or re.search(r'%(?![0-9a-fA-F]{2})', href)):
            return None
        try:
            decoded = unquote(href, errors='strict')
            if ('%' in decoded or '\\' in decoded or decoded.startswith('//')
                    or any(unicodedata.category(c).startswith('C') for c in decoded)):
                return None
            url = urlsplit(decoded)
            if url.scheme:
                if url.scheme not in ('http', 'https') or not url.hostname or url.username or url.password:
                    return None
                original = urlsplit(href)
                if original.scheme != url.scheme or original.netloc != url.netloc:
                    return None
                # Explicit loopback/private operator targets are unavailable remotely.
                host = url.hostname.lower().rstrip('.')
                import ipaddress
                try:
                    address = ipaddress.ip_address(host)
                    if not address.is_global:
                        return None
                except ValueError:
                    # Browsers parse shortened, decimal and hexadecimal IPv4
                    # spellings that ipaddress intentionally rejects. Numeric
                    # final labels are not admitted as fallback DNS hostnames.
                    if (host == 'localhost' or host.endswith(('.localhost', '.local'))
                            or re.fullmatch(r'(?:[0-9]+|0x[0-9a-f]+)', host.split('.')[-1])):
                        return None
                return href
            if url.netloc or url.query:
                return None
            if not url.fragment and (media_url := self.media.resolve(page, url.path)):
                return media_url
            if url.path.startswith('/wiki/'):
                parts = url.path.split('/')
                target = self.page(parts[2], parts[3] or 'index') if len(parts) == 4 else None
            elif url.path.startswith('/'):
                return None
            else:
                parts = list(PurePosixPath(page.source).parent.parts) if url.path else list(PurePosixPath(page.source).parts)
                if url.path:
                    for part in url.path.split('/'):
                        if part == '..':
                            if not parts:
                                return None
                            parts.pop()
                        elif part not in ('', '.'):
                            parts.append(part)
                target = self.sources.get('/'.join(parts).casefold())
                if target is None and url.path and '/' not in url.path:
                    target = self.page(page.wiki, url.path)
            if target is None:
                return None
            if not url.fragment:
                return target.url
            identifier = self.fragments[(target.wiki, target.slug)].get(unicodedata.normalize('NFC', url.fragment))
            return target.url + '#' + quote(identifier) if identifier else None
        except (ValueError, UnicodeError):
            return None

    def render(self, page, markdown=None):
        text = page.markdown if markdown is None else bounded_text(markdown)
        md = parser()
        tokens = md.parse(expanded_details(text))
        local_fragments = heading_map(tokens, f'w-{page.wiki}-{page.slug}-')
        def visit(children):
            for token in children:
                if token.type == 'table_open':
                    token.attrSet('tabindex', '0')
                    token.attrSet('aria-label', 'Comparison table; scroll horizontally for more columns')
                if token.type == 'image':
                    source = self.media.resolve(page, token.attrGet('src'))
                    if source and token.content.strip():
                        token.attrs = {'src': source, 'alt': token.content[:1000], 'width': '960', 'height': '600', 'loading': 'lazy'}
                        # markdown-it derives alt text from inline children at render
                        # time. Keep those inert tokens so the description survives.
                    else:
                        token.type, token.tag, token.nesting = 'text', '', 0
                        token.content = f'[Image unavailable: {token.content}]'
                        token.children = None
                        token.attrs = {}
                elif token.type == 'link_open':
                    href = token.attrGet('href') or ''
                    if href.startswith('#'):
                        try:
                            identifier = local_fragments.get(unquote(href[1:], errors='strict'))
                        except UnicodeError:
                            identifier = None
                        resolved = '#' + identifier if identifier else None
                    else:
                        resolved = self.link(page, href)
                    if resolved:
                        token.attrSet('href', resolved)
                        token.attrSet('rel', 'noreferrer noopener')
                    else:
                        token.tag = 'span'
                        token.attrs = {}
                        # Closing token is paired below; no original href is rendered.
                        token.meta['unavailable'] = True
                if token.children:
                    visit(token.children)
            stack = []
            for token in children:
                if token.type == 'link_open':
                    stack.append(token.meta.get('unavailable', False))
                    if stack[-1]:
                        token.type, token.tag, token.nesting, token.content = 'text', '', 0, '[Unavailable reference: '
                elif token.type == 'link_close' and stack:
                    if stack.pop():
                        token.type, token.tag, token.nesting, token.content = 'text', '', 0, ']'
        visit(tokens)
        rendered = md.renderer.render(tokens, md.options, {})
        return nh3.clean(rendered, tags=TAGS, attributes=ATTRS, url_schemes={'http', 'https'},
                         link_rel='noreferrer noopener', strip_comments=True)

    def search(self, name, query):
        """Bounded current admitted text only; snippets are plain text, never HTML."""
        aliases = {"won't shoot": ('why-soldiers-stop-shooting', 'shoot'),
                   'wont shoot': ('why-soldiers-stop-shooting', 'shoot'),
                   'invisible enemies': ('concealment', 'hidden'),
                   'money': ('tactical-points', 'tactical points'),
                   'tp': ('tactical-points', 'tp'), 'reload': ('weapon-comparison', 'refill'),
                   'mg': ('machine-gunner', 'machine gunner'), 'at': ('anti-tank-options', 'anti-tank')}
        folded = query.casefold().replace('’', "'")
        preferred, needle = aliases.get(folded, ('', folded))
        entries = []
        for page in self.pages.values():
            if page.wiki != name:
                continue
            tokens = parser().parse(expanded_details(page.markdown))
            text = ' '.join(inline_text(t.children) for t in tokens if t.type == 'inline')
            haystack = (page.slug + ' ' + page.title + ' ' + text).casefold()
            if needle and not all(word in haystack for word in needle.split()):
                continue
            position = text.casefold().find(needle)
            start = max(0, position - 65)
            snippet = ('…' if start else '') + text[start:start + 230] + ('…' if len(text) > start + 230 else '')
            score = (100 if page.slug == preferred else 0) + (20 if needle and needle in page.title.casefold() else 0)
            entries.append(dict(url=page.url, title=page.title, slug=page.slug, snippet=snippet,
                                edition=page.edition, score=score))
        return sorted(entries, key=lambda e: (-e['score'], e['slug']))


def register_wiki(app, wiki, *, store=None):
    from flask import Response, abort, g, jsonify, render_template, request
    from markupsafe import Markup
    from .auth import COOKIE
    from .wiki_store import WikiError

    @app.errorhandler(WikiError)
    def wiki_error(error):
        return jsonify(error=str(error)), error.status

    @app.context_processor
    def available_gameplay():
        return dict(wiki_gameplay_available='gameplay_index' in app.view_functions)

    @app.after_request
    def reading_media_policy(response):
        # Admit same-origin images only on wiki reading/editor documents. Keep
        # login's restrictive policy and the media response's sandbox intact.
        if request.endpoint in ('wiki_page', 'wiki_directory', 'wiki_history', 'wiki_editor') and response.status_code == 200:
            response.headers['Content-Security-Policy'] = "default-src 'none'; script-src 'self'; connect-src 'self'; style-src 'self'; img-src 'self'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'"
        return response

    def current():
        return store.view() if store else wiki

    def editable(name):
        return bool(store and store.allowed(request.cookies.get(COOKIE), name, g.identity['csrf_secret']))

    def navigation(view):
        # A code deployment does not import a new source edition. Existing stores
        # can retain older admitted page sets, so never promise absent guides.
        return {slug: page.url for slug in ('editions', 'topic-index', 'starting-checklist',
                                           'evidence-and-method', 'instructional-visuals')
                if (page := view.page('player', slug)) is not None}

    def require_edit(name):
        if store is None:
            abort(404)
        if not editable(name):
            raise WikiError('wiki-edit-forbidden', 403)

    def data(fields):
        if not request.is_json:
            raise WikiError('json-required')
        value = request.get_json()
        if not isinstance(value, dict) or set(value) - set(fields):
            raise WikiError('invalid-request')
        return value

    @app.get('/static/wiki.css')
    def wiki_css():
        return Response(Path(__file__).with_name('static').joinpath('wiki.css').read_bytes(), mimetype='text/css')

    @app.get('/static/wiki.js')
    def wiki_js():
        return Response(Path(__file__).with_name('static').joinpath('wiki.js').read_bytes(), mimetype='text/javascript')

    @app.get('/wiki-media/<filename>')
    def wiki_media(filename):
        media = current().media.items.get(filename)
        if media is None:
            abort(404)
        response = Response(media.data, mimetype=media.mimetype)
        response.headers['Content-Security-Policy'] = "default-src 'none'; style-src 'none'; sandbox"
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response

    @app.get('/wiki/<name>/')
    @app.get('/wiki/<name>/<slug>')
    def wiki_page(name, slug='index'):
        view = current()
        page = view.page(name, slug)
        if page is None:
            abort(404)
        return render_template('wiki.html', page=page, body=Markup(view.render(page)),
                               editable=editable(name), history=store is not None, navigation=navigation(view))

    @app.get('/wiki/<name>/_pages')
    def wiki_directory(name):
        if name not in ('player', 'dev'):
            abort(404)
        query = request.args.get('q', '').strip()
        number = request.args.get('page', '1')
        if (len(query) > 100 or any(unicodedata.category(c).startswith('C') for c in query)
                or not re.fullmatch(r'[1-9][0-9]{0,5}', number)):
            abort(400)
        view = current()
        entries = view.search(name, query)
        number = int(number)
        pages = max(1, (len(entries) + 49) // 50)
        if number > pages:
            abort(404)
        return render_template('wiki_directory.html', wiki=name, query=query,
                               entries=entries[(number - 1) * 50:number * 50],
                               total=len(entries), number=number, pages=pages,
                               editable=editable(name))

    @app.get('/api/wiki/<name>/<slug>')
    def wiki_source(name, slug):
        page = current().page(name, slug)
        if page is None:
            abort(404)
        if store:
            value = store.read(page.wiki, page.slug)
            response = jsonify(value)
            response.headers['ETag'] = value['etag']
            return response
        return jsonify(wiki=page.wiki, slug=page.slug, markdown=page.markdown, sourceHash=page.source_hash, qualification=page.label)

    @app.get('/wiki/<name>/_new')
    @app.get('/wiki/<name>/<slug>/edit')
    def wiki_editor(name, slug=None):
        require_edit(name)
        view = current()
        page = view.page(name, slug or 'index')
        if page is None:
            abort(404)
        return render_template('wiki_editor.html', page=page, creating=slug is None)

    @app.get('/wiki/<name>/<slug>/history')
    @app.get('/wiki/<name>/<slug>/history/<revision>')
    def wiki_history(name, slug, revision=None):
        if store is None:
            abort(404)
        view = current()
        page = view.page(name, slug)
        if page is None:
            abort(404)
        if revision:
            from dataclasses import replace
            text = store.revision(name, page.slug, revision)
            historical = replace(page, markdown=text)
            return render_template('wiki.html', page=historical, body=Markup(view.render(historical)),
                                   historical_revision=revision, history=True, navigation=navigation(view))
        return render_template('wiki_history.html', page=page, revisions=store.history(name, page.slug))

    @app.get('/wiki/<name>/<slug>/export')
    def wiki_export(name, slug):
        if store is None:
            abort(404)
        page = current().page(name, slug)
        if page is None:
            abort(404)
        value = store.read(name, page.slug)
        response = Response(value['markdown'], mimetype='text/plain')
        response.headers['Content-Disposition'] = f'attachment; filename="{page.slug}.md"'
        response.headers['X-Wiki-Source'] = value['sourceHash']
        response.headers['X-Wiki-Revision'] = value['revision'] or 'source'
        return response

    @app.get('/api/wiki/<name>/<slug>/revisions')
    def wiki_revisions(name, slug):
        if store is None:
            abort(404)
        before = request.args.get('before')
        try:
            before = int(before) if before is not None else None
        except ValueError:
            raise WikiError('invalid-history-cursor') from None
        return jsonify(revisions=store.history(name, slug, before=before))

    @app.post('/api/wiki/<name>/<slug>/preview')
    def wiki_preview(name, slug):
        require_edit(name)
        store.key(name, slug)
        value = data(('markdown',))
        view = current()
        page = view.page(name, slug) or Page(name, slug, f'wiki-created/{name}/{slug}.md', '', '', '')
        try:
            return jsonify(html=view.render(page, bounded_text(value.get('markdown'))))
        except (ValueError, UnicodeError):
            raise WikiError('invalid-markdown') from None

    @app.put('/api/wiki/<name>/<slug>')
    def wiki_save(name, slug):
        if store is None:
            abort(405)
        value = data(('markdown', 'sourceHash', 'resolveSource'))
        expected = request.headers.get('If-Match')
        if expected is None:
            raise WikiError('revision-precondition-required', 428)
        result = store.save(name, slug, value.get('markdown'), expected, value.get('sourceHash'),
                            request.cookies.get(COOKIE), g.identity['csrf_secret'], resolve=value.get('resolveSource'))
        response = jsonify(result)
        response.headers['ETag'] = result['etag']
        return response

    @app.post('/api/wiki/<name>/pages')
    def wiki_create(name):
        if store is None:
            abort(404)
        value = data(('slug', 'markdown'))
        return jsonify(store.save(name, value.get('slug'), value.get('markdown'), None, None,
                                  request.cookies.get(COOKIE), g.identity['csrf_secret'], create=True)), 201
