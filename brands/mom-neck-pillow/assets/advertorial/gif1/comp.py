import numpy as np, subprocess, math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
G='/home/user/NG/brands/mom-neck-pillow/assets/advertorial/gif1/'
C=G+'clips/'
S=720; FPS=24; SCN=3.2; NS=int(SCN*FPS)
F=lambda w,s: ImageFont.truetype(f'/usr/share/fonts/opentype/inter/Inter-{w}.otf',s)
fB=F('Bold',26); fM=F('SemiBold',22); fX=F('ExtraBold',34)
def frames(path,start,dur,speed=1.0):
    out=[]
    cmd=['ffmpeg','-v','error','-ss',str(start),'-t',str(dur*speed),'-i',path,'-vf',f'setpts=PTS/{speed},fps={FPS},scale={S}:{S}','-f','rawvideo','-pix_fmt','rgb24','-']
    raw=subprocess.run(cmd,capture_output=True,check=True).stdout
    n=len(raw)//(S*S*3)
    a=np.frombuffer(raw,np.uint8)[:n*S*S*3].reshape(n,S,S,3)
    out=[Image.fromarray(x) for x in a]
    while len(out)<NS: out.append(out[-1])
    return out[:NS]
def still(p): return Image.open(G+p).convert('RGB').resize((S,S),Image.LANCZOS)
def ease(x): x=max(0,min(1,x)); return x*x*(3-2*x)
def badge(im,mark,col):
    d=ImageDraw.Draw(im); r=27; cx=cy=18+r
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=col,outline='white',width=3)
    if mark=='✕':
        k=10; d.line([cx-k,cy-k,cx+k,cy+k],fill='white',width=6); d.line([cx-k,cy+k,cx+k,cy-k],fill='white',width=6)
    else:
        d.line([(cx-12,cy+1),(cx-3,cy+10),(cx+13,cy-9)],fill='white',width=6,joint='curve')
def callout(im,text,anchor,label_xy,t,col=(255,255,255)):
    # line grows from anchor to label, then text fades in
    if t<=0: return im
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    ax,ay=anchor; lx,ly=label_xy
    p=ease(t/0.35)
    ex,ey=ax+(lx-ax)*p, ay+(ly-ay)*p
    d.line([ax,ay,ex,ey],fill=col+(255,),width=3)
    d.ellipse([ax-7,ay-7,ax+7,ay+7],fill=col+(255,))
    if t>0.3:
        al=int(255*ease((t-0.3)/0.25))
        tw=d.textlength(text,font=fB)
        tx=lx-tw-10 if lx<ax else lx+10
        d.rounded_rectangle([tx-10,ly-20,tx+tw+10,ly+18],radius=8,fill=(0,0,0,int(al*0.55)))
        d.text((tx,ly-16),text,font=fB,fill=(255,255,255,al))
    return Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
def pill(im,text,col,t,y=None):
    if t<=0: return im
    al=ease(t/0.25)
    ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    tw=d.textlength(text,font=fM); y=y or S-70
    d.rounded_rectangle([(S-tw)/2-18,y,(S+tw)/2+18,y+42],radius=21,fill=col+(int(235*al),))
    d.text(((S-tw)/2,y+8),text,font=fM,fill=(255,255,255,int(255*al)))
    return Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
RED=(217,48,37); GRN=(30,142,62); BLU=(40,110,240)
out=[]
# ---------- Scene 1 ----------
L=frames(C+'v1_anat_red.mp4',0.4,SCN); R=frames(C+'v2_stretch.mp4',0.3,SCN)
for i in range(NS):
    t=i/FPS; l=L[i].copy(); r=R[i].copy()
    l=callout(l,'Neck bent all night',(440,330),(250,150),t-0.5)
    l=callout(l,'Squeezed',(300,430),(170,560),t-1.2)
    badge(l,'✕',RED); badge(r,'✓',GRN)
    r=pill(r,'Wakes up loose',GRN,t-1.4)
    out.append((l,r))
# ---------- Scene 2 ----------
L=frames(C+'v3_lying_down.mp4',0.6,SCN); R=frames(C+'v4_anat_red_to_green.mp4',0.0,SCN,speed=5.0/SCN)
for i in range(NS):
    t=i/FPS; l=L[i].copy(); r=R[i].copy()
    # green glow under pillow
    g=Image.new('RGBA',(S,S),(0,0,0,0)); gd=ImageDraw.Draw(g)
    a=int(235*ease((t-0.6)/0.6)*(0.7+0.3*math.sin(t*6)))
    gd.ellipse([150,610,720,705],fill=(70,255,100,a))
    gd.ellipse([230,630,640,690],fill=(0,0,0,0))
    g=g.filter(ImageFilter.GaussianBlur(14))
    l=Image.alpha_composite(l.convert('RGBA'),g).convert('RGB')
    r=callout(r,'Back in line',(470,300),(260,150),t-2.2)
    out.append((l,r))
# ---------- Scene 3 ----------
B=still('before_xray_v1.png'); A=still('after_xray_v2.png')
R=frames(C+'v5_laugh.mp4',0.0,SCN)
for i in range(NS):
    t=i/FPS
    m=ease((t-1.3)/0.5)
    l=Image.blend(B,A,m); r=R[i].copy()
    d=ImageDraw.Draw(l)
    col=tuple(int(RED[k]*(1-m)+GRN[k]*m) for k in range(3))
    rr=95+6*math.sin(t*7)
    cx,cy=420,300
    d.ellipse([cx-rr,cy-rr,cx+rr,cy+rr],outline=col,width=6)
    tag='FLAT PILLOW' if m<0.5 else 'NIGHT SHIFT'
    tw=d.textlength(tag,font=fM)
    d.rounded_rectangle([18,18,18+tw+28,60],radius=8,fill=col); d.text((32,26),tag,font=fM,fill='white')
    l=pill(l,'Neck hanging' if m<0.5 else 'Neck held level',col,1.0)
    out.append((l,r))
# ---------- compose with arrow in scene 2 ----------
W=S*2+8
os.makedirs('/tmp/claude-0/-home-user-NG/6edd7bb5-0b0a-52f0-8ea6-071ef359b0e6/scratchpad/anim/final',exist_ok=True)
for i,(l,r) in enumerate(out):
    c=Image.new('RGB',(W,S),'white'); c.paste(l,(0,0)); c.paste(r,(S+8,0))
    if NS<=i<2*NS:
        t=(i-NS)/FPS; p=ease((t-0.9)/0.7)
        if p>0:
            ov=Image.new('RGBA',(W,S),(0,0,0,0)); d=ImageDraw.Draw(ov)
            pts=[]
            for k in range(41):
                u=k/40*p
                x=(1-u)**2*470+2*(1-u)*u*730+u*u*1040
                y=(1-u)**2*360+2*(1-u)*u*160+u*u*300
                pts.append((x,y))
            d.line(pts,fill=BLU+(255,),width=10,joint='curve')
            if p>0.98:
                x2,y2=pts[-1]; x1,y1=pts[-3]; ang=math.atan2(y2-y1,x2-x1)
                hd=[(x2+14*math.cos(ang),y2+14*math.sin(ang)),(x2-22*math.cos(ang)+18*math.sin(ang),y2-22*math.sin(ang)-18*math.cos(ang)),(x2-22*math.cos(ang)-18*math.sin(ang),y2-22*math.sin(ang)+18*math.cos(ang))]
                d.polygon(hd,fill=BLU+(255,))
            c=Image.alpha_composite(c.convert('RGBA'),ov).convert('RGB')
    c.save(f'/tmp/claude-0/-home-user-NG/6edd7bb5-0b0a-52f0-8ea6-071ef359b0e6/scratchpad/anim/final/{i:04d}.jpg',quality=92)
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i','/tmp/claude-0/-home-user-NG/6edd7bb5-0b0a-52f0-8ea6-071ef359b0e6/scratchpad/anim/final/%04d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-crf','25','-preset','slow','-movflags','+faststart','-an',G+'gif1_hero_final.mp4'],check=True)
print('ok',len(out))
