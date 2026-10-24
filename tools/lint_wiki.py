#!/usr/bin/env python3
"""Lint для вики an-info (операция Lint из CLAUDE.md).

Проверяет: каждый факт из raw/*_facts.json присутствует на своей домашней странице ровно
один раз в виде пункта «- **[Fxxx]** <значок>»; значки на всех страницах совпадают с raw/;
относительные ссылки ведут на существующие файлы; ID не повторяются между файлами raw/.
Домашняя страница определяется по полю angle через карту HOME ниже, дополненную полем
верхнего уровня "home_pages" каждого файла raw/. Запуск: python3 -I tools/lint_wiki.py
"""
import glob, json, os, re, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
W = os.path.join(REPO, 'wiki')
HOME = {
    'official-text': 'announcement-text.md', 'mechanism-deep': 'fund-mechanism.md',
    'finance-ipo': 'finance-and-ipo.md', 'comparisons': 'comparisons.md', 'reactions': 'reactions.md',
    'anthropic-context': 'anthropic-context.md', 'russian-coverage': 'media-coverage.md',
}
MARKS = '✅|⚠️|🔴|🟢|🟡|🟠|⚪'
facts, ok = {}, True
raw_files = sorted(glob.glob(os.path.join(REPO, 'raw', '*_facts.json')))
for rf in raw_files:
    d = json.load(open(rf))
    HOME.update(d.get('home_pages', {}))
    for f in d['facts']:
        if f['id'] in facts:
            print(f'[DUPLICATE ID ACROSS RAW] {f["id"]} in {os.path.basename(rf)}'); ok = False
        facts[f['id']] = f
print('raw files:', ', '.join(os.path.basename(r) for r in raw_files), '| facts:', len(facts))
pages = {p: open(os.path.join(W, p)).read() for p in sorted(os.listdir(W)) if p.endswith('.md')}
print('pages:', ', '.join(f'{p} ({len(t)//1000}k)' for p, t in pages.items()))
bullet = re.compile(r'^\s*[-*]\s+\*\*\[(F\d{3,})\]\*\*\s*(' + MARKS + ')', re.M)
angles = sorted({f['angle'] for f in facts.values()})
for angle in angles:
    page = HOME.get(angle)
    if not page or page not in pages:
        print(f'[MISSING PAGE] angle {angle} -> {page}'); ok = False; continue
    found = bullet.findall(pages[page]); ids = [i for i, _ in found]
    expected = [i for i, f in facts.items() if f['angle'] == angle]
    missing = [i for i in expected if i not in ids]
    dups = sorted({i for i in ids if ids.count(i) > 1})
    foreign = [i for i in ids if i not in expected]
    badmark = [(i, m, facts[i]['status_mark']) for i, m in found if i in facts and facts[i]['status_mark'] != m]
    print(f'{page}: {len(found)} bullets / {len(expected)} expected; missing={missing} dups={dups} foreign={foreign} badmark={badmark}')
    if missing or dups or badmark: ok = False
for p, t in pages.items():
    for m in re.finditer(r'\]\(([^)#\s]+\.md)(#[^)]*)?\)', t):
        tgt = m.group(1)
        if tgt.startswith(('http://', 'https://')): continue
        if not os.path.exists(os.path.normpath(os.path.join(W, tgt))):
            print(f'[BROKEN LINK] {p} -> {tgt}'); ok = False
    for m in re.finditer(r'(F\d{3,})\]?\*?\*?\s*(' + MARKS + ')', t):
        i, mk = m.group(1), m.group(2)
        if i not in facts: print(f'[NO SUCH ID] {p}: {i}'); ok = False
        elif facts[i]['status_mark'] != mk: print(f'[MARK] {p}: {i} page {mk} raw {facts[i]["status_mark"]}'); ok = False
print('LINT OK' if ok else 'LINT FAILED')
sys.exit(0 if ok else 1)
