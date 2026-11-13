"""Exact, immutable admission of original inert instructional SVGs; no file serving."""
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import xml.etree.ElementTree as ET

from .storage import REPOSITORY

SOURCE_ROOT = 'research/mnb2/wiki/player/'
MEDIA_ROOT = SOURCE_ROOT + 'media/'
MAX_BYTES = 128 * 1024
MAX_TOTAL = 2 * 1024 * 1024
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\.svg\Z')
TAGS = {'svg', 'title', 'desc', 'rect', 'circle', 'line', 'polyline', 'polygon', 'text', 'g'}
ATTRIBUTES = {'xmlns', 'viewBox', 'width', 'height', 'x', 'y', 'x1', 'y1', 'x2', 'y2',
              'cx', 'cy', 'r', 'rx', 'ry', 'fill', 'stroke', 'stroke-width',
              'points', 'font-family', 'font-size', 'font-weight', 'text-anchor',
              'stroke-dasharray', 'role'}


@dataclass(frozen=True)
class Media:
    data: bytes
    mimetype: str
    credit: str
    source: str
    sha256: str


def inert_svg(raw):
    """Only a small drawing vocabulary, without references, styles or active XML."""
    if len(raw) > MAX_BYTES or b'<!' in raw or b'<?' in raw:
        raise ValueError('wiki-media-svg-bound')
    try:
        root = ET.fromstring(raw)
    except (ET.ParseError, UnicodeError):
        raise ValueError('wiki-media-svg-invalid') from None
    if root.tag != '{http://www.w3.org/2000/svg}svg' or root.get('viewBox') != '0 0 960 600':
        raise ValueError('wiki-media-svg-root')
    nodes = list(root.iter())
    if len(nodes) > 250:
        raise ValueError('wiki-media-svg-bound')
    for node in nodes:
        if node.tag not in {'{http://www.w3.org/2000/svg}' + tag for tag in TAGS}:
            raise ValueError('wiki-media-svg-tag')
        for key, value in node.attrib.items():
            if key not in ATTRIBUTES or len(value) > 1000 or re.search(r'url|[<>&\\]|[\x00-\x1f]', value, re.I):
                raise ValueError('wiki-media-svg-attribute')
            # No URI, CSS escaping or reference syntax in any admitted value.
            if ':' in value or '(' in value or ')' in value:
                raise ValueError('wiki-media-svg-attribute')
    return raw


class WikiMedia:
    def __init__(self, manifest=None, *, repository=REPOSITORY):
        repository = Path(repository).absolute()
        path = Path(manifest) if manifest is not None else Path(__file__).with_name('wiki_media_manifest.json')
        if path.is_symlink() or path.is_junction() or path.stat().st_size > 64 * 1024:
            raise ValueError('wiki-media-manifest-bound')
        def unique(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError('wiki-media-duplicate-key')
                result[key] = value
            return result
        value = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)
        if (set(value) != {'schema', 'media'} or value['schema'] != 1
                or not isinstance(value['media'], list) or not 1 <= len(value['media']) <= 32):
            raise ValueError('wiki-media-manifest-schema')
        self.items, self.sources = {}, {}
        total = 0
        for entry in value['media']:
            if not isinstance(entry, dict) or set(entry) != {'filename', 'source', 'sha256', 'mimetype', 'credit', 'rights'}:
                raise ValueError('wiki-media-entry-schema')
            name, source, digest = (entry[k] for k in ('filename', 'source', 'sha256'))
            if (not isinstance(name, str) or not NAME.fullmatch(name)
                    or source != MEDIA_ROOT + name or entry['mimetype'] != 'image/svg+xml'
                    or entry['rights'] != 'original-project-diagram'
                    or not isinstance(entry['credit'], str) or not 1 <= len(entry['credit']) <= 500
                    or not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest)
                    or not name.endswith('-' + digest + '.svg')):
                raise ValueError('wiki-media-entry-bound')
            candidate = repository / source
            if any(p.is_symlink() or p.is_junction() for p in (candidate, *candidate.parents)):
                raise ValueError('wiki-media-source-link')
            if not candidate.resolve().is_relative_to(repository.resolve()) or candidate.stat().st_size > MAX_BYTES:
                raise ValueError('wiki-media-source-bound')
            raw = candidate.read_bytes()
            if len(raw) > MAX_BYTES or hashlib.sha256(raw).hexdigest() != digest:
                raise ValueError('wiki-media-source-hash')
            inert_svg(raw)
            total += len(raw)
            if total > MAX_TOTAL:
                raise ValueError('wiki-media-import-bound')
            if name in self.items or source in self.sources:
                raise ValueError('wiki-media-duplicate-source')
            self.items[name] = Media(raw, entry['mimetype'], entry['credit'], source, digest)
            self.sources[source] = name

    def resolve(self, page, href):
        if (not isinstance(href, str) or len(href) > 200 or not href.startswith('media/')
                or PurePosixPath(page.source).parent.as_posix() + '/' != SOURCE_ROOT):
            return None
        name = href[6:]
        if not NAME.fullmatch(name) or name not in self.items:
            return None
        source = str(PurePosixPath(page.source).parent / href)
        return '/wiki-media/' + name if source in self.sources else None
