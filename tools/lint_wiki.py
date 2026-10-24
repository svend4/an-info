#!/usr/bin/env python3
"""Lint для вики an-info (операция Lint из CLAUDE.md).

Проверяет: каждый факт из raw/ присутствует на своей домашней странице ровно один раз
в виде пункта «- **[Fxxx]** <значок>»; значки на всех страницах совпадают с raw/;
относительные ссылки ведут на существующие файлы. Запуск: python3 -I tools/lint_wiki.py
"""
import json, re, os, sys
REPO=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); W=os.path.join(REPO,'wiki')
d=json.load(open(os.path.join(REPO,'raw/2026-10-24_public-benefit-fund_facts.json')))
HOME={'official-text':'announcement-text.md','mechanism-deep':'fund-mechanism.md','finance-ipo':'finance-and-ipo.md','comparisons':'comparisons.md','reactions':'reactions.md','anthropic-context':'anthropic-context.md','russian-coverage':'media-coverage.md'}
facts={f['id']:f for f in d['facts']}
pages={p:open(os.path.join(W,p)).read() for p in sorted(os.listdir(W)) if p.endswith('.md')}
print('pages:', ', '.join(f"{p} ({len(t)//1000}k)" for p,t in pages.items()))
bullet=re.compile(r'^\s*[-*]\s+\*\*\[(F\d{3})\]\*\*\s*(✅|⚠️|🔴|🟢|🟡|🟠|⚪)', re.M)
ok=True
for angle,page in HOME.items():
    if page not in pages: print(f'[MISSING PAGE] {page}'); ok=False; continue
    found=bullet.findall(pages[page])
    ids=[f for f,_ in found]
    expected=[f['id'] for f in d['facts'] if f['angle']==angle]
    missing=[i for i in expected if i not in ids]
    dups=sorted({i for i in ids if ids.count(i)>1})
    foreign=[i for i in ids if i not in expected]
    badmark=[(i,m,facts[i]['status_mark']) for i,m in found if i in facts and facts[i]['status_mark']!=m]
    print(f'{page}: {len(found)} bullets / {len(expected)} expected; missing={missing} dups={dups} foreign={foreign} badmark={badmark}')
    if missing or dups or badmark: ok=False
# links
for p,t in pages.items():
    for m in re.finditer(r'\]\(([^)#\s]+\.md)(#[^)]*)?\)', t):
        tgt=m.group(1)
        if tgt.startswith(('http://','https://')): continue
        path=os.path.normpath(os.path.join(W,tgt))
        if not os.path.exists(path): print(f'[BROKEN LINK] {p} -> {tgt}'); ok=False
# marks anywhere vs raw
for p,t in pages.items():
    for m in re.finditer(r'(F\d{3})\]?\*?\*?\s*(✅|⚠️|🔴|🟢|🟡|🟠|⚪)', t):
        i,mk=m.group(1),m.group(2)
        if i in facts and facts[i]['status_mark']!=mk: print(f'[MARK] {p}: {i} page {mk} raw {facts[i]["status_mark"]}'); ok=False
        if i not in facts: print(f'[NO SUCH ID] {p}: {i}'); ok=False
print('LINT OK' if ok else 'LINT FAILED')
