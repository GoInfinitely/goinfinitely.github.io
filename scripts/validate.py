"""Validate publishable assets, anchors, metadata, and local references."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'docs'

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.images, self.labels = [], [], [], []
        self.language = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for name in ('href', 'src'):
            if name in attrs:
                self.refs.append(attrs[name])
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'html':
            self.language = attrs.get('lang')

for file in ROOT.glob('*.html'):
    html = file.read_text()
    page = Document()
    page.feed(html)
    assert page.language == 'en', f'Missing language in {file}'
    assert len(page.ids) == len(set(page.ids)), f'Duplicate IDs in {file}'
    for image in page.images:
        assert image.get('alt'), f'Missing image alternative in {file}'
        assert image.get('width') and image.get('height'), 'Image needs dimensions'
    for ref in page.refs:
        parts = urlsplit(ref)
        if parts.scheme or parts.netloc:
            assert parts.scheme in ('https', 'mailto'), f'Unexpected external scheme: {ref}'
            continue
        if not parts.path:
            assert parts.fragment in page.ids, f'Broken fragment: {ref}'
            continue
        target = ROOT / unquote(parts.path).lstrip('/')
        assert target.exists(), f'Missing local asset: {ref}'
    assert '<title>' in html and 'name="viewport"' in html
    for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        json.loads(data)
    print(f'OK: {file.name} ({len(page.refs)} links/assets)')

for url in re.findall(r"url\(['\"]?([^)'\"]+)", (ROOT / 'styles.css').read_text()):
    assert (ROOT / url).is_file(), f'Missing CSS asset: {url}'
assert (ROOT / 'assets/jose-cabral-resume.pdf').read_bytes().startswith(b'%PDF')
assert (ROOT / 'assets/inter-latin.woff2').read_bytes().startswith(b'wOF2')
assert (ROOT / '.nojekyll').exists()
ET.parse(ROOT / 'sitemap.xml')
for file in (ROOT / 'assets').glob('*.svg'):
    ET.parse(file)
print('OK: font, PDF, SVGs, sitemap, CSS references, and Pages configuration')
