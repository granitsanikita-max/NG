#!/usr/bin/env python3
"""Convert final/*.md to Google-Docs-friendly HTML (tables, clickable links)."""
import glob, re, markdown, html
for f in sorted(glob.glob('final/*.md')):
    t=open(f).read()
    L=t.split('\n'); t='\n'.join(('\n'+l) if l.startswith('|') and i and L[i-1].strip() and not L[i-1].startswith('|') else l for i,l in enumerate(L))
    # make bare URLs clickable (skip ones already inside markdown links / angle brackets)
    t=re.sub(r'(?<![\(<\[="])\b(https?://[^\s\)\]>|`"]+[^\s\)\]>|`".,;:])', r'<\1>', t)
    body=markdown.markdown(t, extensions=['tables','sane_lists','fenced_code'])
    title=html.escape(t.splitlines()[0].lstrip('# ').strip())
    css='body{font-family:Arial;font-size:11pt}table{border-collapse:collapse}th,td{border:1px solid #999;padding:4px;vertical-align:top}th{background:#eeeeee}'
    out=f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>{body}</body></html>'
    open(f[:-3]+'.html','w').write(out); print(f[:-3]+'.html', len(out), body.count('<table'), body.count('<a href'))
