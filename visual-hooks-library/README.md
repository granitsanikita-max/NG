# Visual Hooks Library (Miro: https://miro.com/app/board/uXjVHhmCPn0=/)
141 visual hook formats for the first 3 seconds of a video ad, in Kallaway's 5 categories (all 47 from his Short-Form Lego Bricks FigJam, with his definitions and reference stills in kallaway_refs/). Every format has at least one real reference; 14 formats with none were dropped.
References are proven: TikTok ads 50k+ likes, Meta ads live 30+ days at scale, or viral organic TikToks (50k+ likes or 1M+ views).

- taxonomy.json: the 155 formats (what you see, why it works, how to shoot, aliases, source)
- hooks_data.json: formats plus their verified examples (after filters, exclusions and cross-format dedupe)
- cls_*_all.json: first-3s classification of ~1,450 ads; hunts/K*.json: targeted example hunts
- gen_hooks.py -> hooks_data.json + composite images; gen_hooks_board.py -> Miro SVG frames + plan
- board/: frame ids, image ids and push instructions for the live board
