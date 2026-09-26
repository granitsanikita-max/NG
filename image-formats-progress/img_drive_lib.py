import json, re
from concurrent.futures import ThreadPoolExecutor
ROOT = '1tInAm82OP8ceeJdDCcbEA_i5-RrZR2lm'  # Drive folder "Image Ad Formats - Winning References"
def _px(method, url, **kw):
    r = proxy_execute(method, url, toolkit='googledrive', **kw)
    return r[0] if isinstance(r, tuple) else r
def _list(q):
    out, tok = [], None
    while True:
        qp = {'q': q, 'fields': 'nextPageToken,files(id,name,size)', 'pageSize': '1000'}
        if tok: qp['pageToken'] = tok
        d = _px('GET', 'https://www.googleapis.com/drive/v3/files', query_params=qp)
        out += d.get('files', []); tok = d.get('nextPageToken')
        if not tok: return out
def drive_state():
    """Rebuild state from Drive itself (survives sandbox resets): folders + done files keyed by ad id."""
    folders = {f['name']: f['id'] for f in _list(f"'{ROOT}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false")}
    done = {}
    def scan(item):
        name, fid = item
        return [(name, f) for f in _list(f"'{fid}' in parents and trashed=false")]
    with ThreadPoolExecutor(8) as ex:
        for res in ex.map(scan, folders.items()):
            for folder, f in res:
                m = re.search(r'- (\d+)\.jpg$', f['name'])
                if m: done[m.group(1)] = {'id': f['id'], 'link': 'https://drive.google.com/file/d/%s/view' % f['id'], 'size': f.get('size'), 'folder': folder}
    return folders, done
def _folder(folders, name):
    if name not in folders:
        d = _px('POST', 'https://www.googleapis.com/drive/v3/files', body={'name': name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [ROOT]})
        folders[name] = d['id']
    return folders[name]
def _up(job, fid):
    folder, name, src, aid = job
    r, e = run_composio_tool('GOOGLEDRIVE_UPLOAD_FROM_URL', {'source_url': src, 'name': name, 'parent_folder_id': fid, 'mime_type': 'image/jpeg'})
    f = (r or {}).get('data') or {}
    if e or not f.get('id'): return aid, None, str(e or r)[:160]
    return aid, {'id': f['id'], 'link': 'https://drive.google.com/file/d/%s/view' % f['id'], 'size': f.get('size'), 'folder': folder}, None
def run_img(jobs):
    folders, done = drive_state()
    todo = [j for j in jobs if j[3] not in done]
    fids = {j[0]: _folder(folders, j[0]) for j in todo}
    fails = {}
    with ThreadPoolExecutor(6) as ex:
        for aid, res, err in ex.map(lambda j: _up(j, fids[j[0]]), todo):
            if res: done[aid] = res
            else: fails[aid] = err
    small = [k for k, v in done.items() if v.get('size') and int(v['size']) < 15000]
    return {'uploaded': len(todo) - len(fails), 'skipped_already_in_drive': len(jobs) - len(todo), 'fails': fails, 'done_total': len(done), 'small': small}
def links():
    return {k: v['link'] for k, v in drive_state()[1].items()}
