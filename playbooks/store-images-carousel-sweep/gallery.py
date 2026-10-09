"""Capture a PDP's gallery + full page for image-format classification.
Usage: python3 -I gallery.py tasks.tsv   (lines: name<TAB>pdp_url)
Per brand:
  - _hero.png : first viewport (hero carousel slide 1)
  - slide image FILES downloaded from the gallery DOM (high-res, all slides where present), g00..
  - full_page.png sliced into tiles tile00.. (<=1500px each) so agents can Read the whole page
  - index.txt : slide alt text + tile list
"""
import sys, os, asyncio, urllib.request, ssl, math
from playwright.async_api import async_playwright
OUT='/tmp/claude-0/pw/gallery/'
proxy = os.environ.get('HTTPS_PROXY') or os.environ.get('https_proxy')
UA='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'

# Gallery slide <img> only: images high on the page, wide, inside a media/gallery/carousel container. Exclude tiny thumbs/swatches.
GAL_JS = r"""() => {
  const abs=u=>{try{return new URL(u,location.href).href}catch(e){return u}};
  const base=s=>s?s.split('?')[0].replace(/_\d+x\d*(\.(jpg|jpeg|png|webp))/i,'$2'):s;
  const pick=img=>{ let s=img.currentSrc||img.getAttribute('src')||'';
    const ss=img.getAttribute('srcset')||img.getAttribute('data-srcset')||'';
    if(ss){const ps=ss.split(',').map(x=>x.trim().split(/\s+/));let best=null,bw=0;for(const p of ps){const w=parseInt((p[1]||'').replace('w',''))||0;if(w>=bw){bw=w;best=p[0]}}if(best)s=best;}
    s=img.getAttribute('data-zoom')||img.getAttribute('data-large')||s; return abs(s); };
  const inGallery=el=>{ let p=el; for(let i=0;i<8&&p;i++){ const c=(p.className&&p.className.baseVal!==undefined?p.className.baseVal:(''+(p.className||''))).toLowerCase();
    const id=(p.id||'').toLowerCase(); const lbl=c+' '+id;
    if(/gallery|product__media|product-media|media-gallery|carousel|swiper|flickity|slick|slideshow|product-single__photo|product-image-main|hero/.test(lbl)) return true;
    if(/thumbnail|thumb|swatch|variant|footer|recommend|related|upsell|cross/.test(lbl)) return false; p=p.parentElement; } return false; };
  const out=[]; const seen=new Set();
  for(const img of document.querySelectorAll('img')){ const r=img.getBoundingClientRect(); const y=r.top+scrollY;
    const big = r.width>=window.innerWidth*0.55 && r.height>=200 && y<1300;
    if(!(inGallery(img)|| big)) continue;
    const s=pick(img); if(!s||s.startsWith('data:')) continue; const k=base(s); if(seen.has(k))continue; seen.add(k);
    out.push({src:s, alt:(img.getAttribute('alt')||'').trim().slice(0,160), w:Math.round(r.width), h:Math.round(r.height), y:Math.round(y)}); }
  out.sort((a,b)=>a.y-b.y); return out.slice(0,16);
}"""

def dl(url, path):
    try:
        ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        op=urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':UA}), timeout=40, context=ctx)
        data=op.read()
        if len(data)<1500: return False
        open(path,'wb').write(data); return True
    except Exception as e: return False

async def one(b, name, url):
    d=OUT+name+'/'; os.makedirs(d,exist_ok=True)
    ctx=await b.new_context(viewport={'width':430,'height':932}, user_agent=UA, is_mobile=True, has_touch=True, device_scale_factor=2)
    pg=await ctx.new_page()
    try:
        await pg.goto(url, wait_until='domcontentloaded', timeout=60000)
        await pg.wait_for_timeout(5000)
        try: await pg.wait_for_load_state('load', timeout=12000)
        except: pass
        for sel in ['button[aria-label*="lose" i]','button:has-text("No thanks")','button:has-text("Close")','[aria-label="Close dialog"]','button:has-text("Accept")','button:has-text("ACCEPT")']:
            try: await pg.locator(sel).first.click(timeout=700)
            except: pass
        await pg.keyboard.press('Escape'); await pg.wait_for_timeout(500)
        await pg.mouse.wheel(0,500); await pg.wait_for_timeout(700); await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(600)
        await pg.screenshot(path=d+'_hero.png')
        gal=await pg.evaluate(GAL_JS); slides=[]
        for i,g in enumerate(gal):
            ext='.jpg'
            for e in ('.png','.webp','.jpeg','.jpg'):
                if e in g['src'].lower().split('?')[0]: ext=e; break
            fp=d+f"g{i:02d}{ext}"
            if dl(g['src'],fp): slides.append({**g,'file':os.path.basename(fp)})
        # full page, then slice into <=1500px tiles
        fpng=d+'full_page.png'; await pg.screenshot(path=fpng, full_page=True)
        tiles=slice_png(fpng, d)
        open(d+'index.txt','w').write(
            f"{name}\nURL {pg.url}\nTITLE {await pg.title()}\nGALLERY SLIDE FILES ({len(slides)}):\n"
            + '\n'.join(f"  {s['file']} {s['w']}x{s['h']} y{s['y']} alt={s['alt']}" for s in slides)
            + f"\nFULL-PAGE TILES ({len(tiles)}): "+' '.join(tiles))
        print('OK', name, len(slides),'slides', len(tiles),'tiles', pg.url)
    except Exception as e:
        print('FAIL', name, url, str(e)[:160]); open(d+'index.txt','w').write(f"{name}\nFAIL {str(e)[:160]}\n")
    await ctx.close()

def slice_png(path, d):
    try:
        from PIL import Image
    except Exception:
        return []
    im=Image.open(path); W,H=im.size; step=1500; tiles=[]
    n=math.ceil(H/step)
    for i in range(min(n,20)):
        top=i*step; bot=min(top+step,H)
        t=im.crop((0,top,W,bot)); fp=d+f"tile{i:02d}.png"; t.save(fp); tiles.append(os.path.basename(fp))
    return tiles

async def main():
    rows=[l.rstrip('\n').split('\t') for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
    async with async_playwright() as p:
        kw=dict(headless=True, executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--ssl-version-max=tls1.2','--disable-blink-features=AutomationControlled'])
        if proxy: kw['proxy']={'server':proxy}
        b=await p.chromium.launch(**kw)
        for r in rows:
            if len(r)>=2: await one(b, r[0], r[1])
        await b.close()
asyncio.run(main())
