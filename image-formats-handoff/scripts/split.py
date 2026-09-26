import re,sys,json,os
# usage: cd <WORK>/board2_<kind> && python3 ../split.py <frame_key> <cards_per_chunk>
key=sys.argv[1]; per=int(sys.argv[2])
s=open(f'frame_{key}.svg').read()
lines=s.split('\n')
head=lines[:2]  # svg, g
body=lines[2:-1]
frame_rect=body[0]
starts=[i for i,l in enumerate(body) if 'width="1964" height="938"' in l]
pre=body[1:starts[0]]
cards=[body[a:b] for a,b in zip(starts,starts[1:]+[len(body)])]
chunks=[]
for i in range(0,len(cards),per):
    part=sum(cards[i:i+per],[])
    if i==0: chunks.append('\n'.join(head+[frame_rect]+pre+part+['</g></svg>']))
    else: chunks.append('\n'.join(['<svg xmlns="http://www.w3.org/2000/svg">', head[1].replace(f'id="{key}"','data-miro-id="FRAMEID"'), frame_rect]+part+['</g></svg>']))
for n,c in enumerate(chunks): open(f'chunk_{key}_{n}.svg','w').write(c)
print(key,[len(c) for c in chunks])
