"""usage: python3 tt_patch.py in.svg out.svg  -- adds '🎬 Video' mp4 link after each TikTok ▶ Watch link in examples textAreas (idempotent)."""
import sys, json, re
H='/tmp/claude-0/-home-user-NG/12cf501e-e1e4-51cb-a9e4-da29e659b5ef/scratchpad/hooks'
vid={e['id']:e['video_url'] for x in json.load(open(H+'/hooks_data.json')) for e in x['examples'] if e['platform']=='tiktok' and 'media.winninghunter.com' in (e.get('video_url') or '')}
s=open(sys.argv[1]).read()
n=0
def rep(m):
    global n
    i=m.group(1); u=vid.get(i)
    if not u: return m.group(0)
    n+=1
    return m.group(0)+f' · &lt;a href="{u}"&gt;🎬 Video&lt;/a&gt;'
s=re.sub(r'&lt;a href="https://app\.winninghunter\.com/ad/(\d+)\?platform=tiktok"&gt;▶ Watch&lt;/a&gt;(?! · &lt;a href="https://media)',rep,s)
# keep only textArea elements that changed + wrapper
open(sys.argv[2],'w').write(s); print('links added',n)
