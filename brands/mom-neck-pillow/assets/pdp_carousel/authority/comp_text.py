from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
SRC, OUT = sys.argv[1], sys.argv[2]
F='/usr/share/fonts/opentype/inter/'
def f(n,s): return ImageFont.truetype(F+n,s)
PLUM=(46,35,64); ROSE=(184,71,106); BODY=(70,58,80); MILK=(251,244,238)
im=Image.open(SRC).convert('RGBA')
def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def card(im,box,alpha=242):
    x0,y0,x1,y1=box
    sh=Image.new('RGBA',im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    sd.rounded_rectangle((x0+6,y0+18,x1+6,y1+18),40,fill=(40,20,50,70)); sh=sh.filter(ImageFilter.GaussianBlur(28))
    im=Image.alpha_composite(im,sh)
    c=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(c).rounded_rectangle(box,40,fill=MILK+(alpha,))
    return Image.alpha_composite(im,c)
d0=ImageDraw.Draw(im)
lab=f('Inter-Bold.otf',30); qf=f('InterDisplay-Bold.otf',58); nf=f('Inter-Bold.otf',42); cf=f('Inter-Medium.otf',30); tf=f('Inter-SemiBold.otf',34)
pad=54
# CARD 1 quote
x0,y0,x1=1300,90,1985; cw=x1-x0-2*pad
quote="Most new moms I see aren’t stiff from feeding. They’re stiff from the 8 hours after it."
ql=wrap(d0,quote,qf,cw)
h1=pad+30+34+80+len(ql)*72+34+4+34+52+40+pad-10
im=card(im,(x0,y0,x1,y0+h1)); d=ImageDraw.Draw(im)
x=x0+pad; y=y0+pad
d.text((x,y),"WHAT A POSTPARTUM PT LOOKS FOR",font=lab,fill=ROSE); y+=30+34
d.text((x-4,y-34),"“",font=f('InterDisplay-Black.otf',140),fill=ROSE); y+=80
for l in ql: d.text((x,y),l,font=qf,fill=PLUM); y+=72
y+=34; d.line((x,y,x+120,y),fill=ROSE,width=4); y+=34
d.text((x,y),"Jenna Holt, DPT",font=nf,fill=PLUM); y+=52
d.text((x,y),"Postpartum physical therapist · 12 years",font=cf,fill=BODY)
print('card1 bottom',y0+h1)
# CARD 2 ticks (bottom right, below pillow)
ticks=["Fits back and side sleep","Arm cutouts, no dead arm","Holds its shape at 3am"]
X0,X1=1390,1990; cw2=X1-X0-2*pad-60
tl=[wrap(d,t,tf,cw2) for t in ticks]
h2=pad+sum(len(x)*46+24 for x in tl)-24+pad
Y1=1985; Y0=Y1-h2
im=card(im,(X0,Y0,X1,Y1)); d=ImageDraw.Draw(im)
y=Y0+pad; x=X0+pad
for lines in tl:
    cy=y+22; r=19
    d.ellipse((x,cy-r,x+2*r,cy+r),fill=ROSE)
    d.line([(x+11,cy+1),(x+17,cy+8),(x+28,cy-7)],fill=(255,255,255),width=5,joint='curve')
    yy=y
    for l in lines: d.text((x+60,yy),l,font=tf,fill=PLUM); yy+=46
    y=yy+24
print('card2 top',Y0)
im.convert('RGB').save(OUT,quality=95)
