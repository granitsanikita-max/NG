from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageChops, ImageEnhance
F='/tmp/claude-0/-home-user-NG/92cd2168-7086-5de0-bc34-0c2243670dd7/scratchpad/fonts/'
CREAM=(245,237,230); CLARET=(163,49,84); INK=(35,16,23)
src=Image.open('g2.png').convert('RGB')
# key out white bg: alpha from darkness
g=src.convert('L')
a=g.point(lambda v: 255 if v<200 else (0 if v>245 else int((245-v)/45*255)))
a=a.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
cut=src.copy(); cut.putalpha(a)
cut=cut.crop(cut.getbbox())
cut.save('brief-cut.png')

def layer(canvas, im, xy, shadow=True):
    if shadow:
        sh=Image.new('RGBA',im.size,(0,0,0,0)); sh.putalpha(im.getchannel('A').point(lambda v:int(v*0.35)))
        sh=sh.filter(ImageFilter.GaussianBlur(10))
        canvas.alpha_composite(sh,(xy[0]+6,xy[1]+12))
    canvas.alpha_composite(im,xy)

def edge(im):
    # thin light rim so stacked black layers separate
    al=im.getchannel('A')
    rim=al.filter(ImageFilter.MaxFilter(7))
    r=Image.new('RGBA',im.size,(245,237,230,0)); r.putalpha(rim)
    out=Image.new('RGBA',im.size,(0,0,0,0)); out.alpha_composite(r); out.alpha_composite(im)
    return out

def stack(n, w, step):
    b=cut.copy(); b.thumbnail((w,w)); b=edge(b)
    W=b.width+abs(step[0])*(n-1)+40; H=b.height+abs(step[1])*(n-1)+40
    c=Image.new('RGBA',(W,H),(0,0,0,0))
    for i in range(n):
        k=n-1-i
        layer(c,b,(20+step[0]*k, 20+(-step[1])*(n-1)+step[1]*k))
    return c

def badge(c, text, sub=None):
    d=ImageDraw.Draw(c)
    f=ImageFont.truetype(F+'hk700.ttf',92)
    tw=d.textlength(text,font=f)
    x,y=48,48; pad=34
    d.rectangle([x,y,x+tw+pad*2,y+138],fill=CLARET)
    d.text((x+pad,y+16),text,font=f,fill=(255,255,255))

def pack(n, out):
    S=1000; c=Image.new('RGBA',(S,S),CREAM+(255,))
    if n<=5:
        st=stack(n, 660 if n==3 else 620, (46,-44) if n==3 else (34,-32))
        st.thumbnail((860,760))
        c.alpha_composite(st,((S-st.width)//2,(S-st.height)//2+60))
    else:
        st=stack(5,420,(26,-25)); st.thumbnail((480,480))
        c.alpha_composite(st,(25,(S-st.height)//2+70))
        c.alpha_composite(st,(S-st.width-25,(S-st.height)//2+70))
    badge(c, f'{n} PAIRS')
    c.convert('RGB').save(out,quality=92)

pack(3,'leapproof-3-pairs.jpg'); pack(5,'leapproof-5-pairs.jpg'); pack(10,'leapproof-10-pairs.jpg')

# single for offer page
S=1000; c=Image.new('RGBA',(S,S),CREAM+(255,)); b=cut.copy(); b.thumbnail((820,820)); layer(c,b,((S-b.width)//2,(S-b.height)//2)); c.convert('RGB').save('leapproof-brief-single.jpg',quality=92)

def gift(src, box, out, label):
    im=Image.open(src).convert('RGB').crop(box)
    S=1000; c=im.resize((S,S),Image.LANCZOS)
    d=ImageDraw.Draw(c); f=ImageFont.truetype(F+'hk700.ttf',64)
    tw=d.textlength(label,font=f); x,y=48,48
    d.rectangle([x,y,x+tw+56,y+100],fill=CLARET); d.text((x+28,y+14),label,font=f,fill=(255,255,255))
    c.save(out,quality=92)
gift('bag-big.jpg',(0,0,800,800),'leapproof-free-wash-bag.jpg','FREE GIFT')
gift('sheets-big.jpg',(0,0,800,800),'leapproof-free-wash-sheets.jpg','FREE GIFT')
s=Image.new('RGB',(2000,800),'white')
for i,f in enumerate(['leapproof-3-pairs.jpg','leapproof-5-pairs.jpg','leapproof-10-pairs.jpg','leapproof-free-wash-bag.jpg','leapproof-free-wash-sheets.jpg','leapproof-brief-single.jpg']):
    im=Image.open(f); im.thumbnail((400,400)); s.paste(im,((i%5)*400,(i//5)*400))
s.save('packs-sheet.jpg')
