# Visual Hooks Library (Miro: https://miro.com/app/board/uXjVHhmCPn0=/)
155 visual hook formats for the first 3 seconds of a video ad, in Kallaway's 5 categories (all 47 from his Short-Form Lego Bricks FigJam included).
Examples are proven only: TikTok 50k+ likes, or Meta ad live 30+ days at scale. Each example is shown as a 7-frame strip (0.0s to 3.0s).

- taxonomy.json: the 155 formats (what you see, why it works, how to shoot, aliases, source)
- hooks_data.json: formats plus their verified examples (after filters, exclusions and cross-format dedupe)
- cls_*_all.json: first-3s classification of ~1,450 ads; hunts/K*.json: targeted example hunts
- gen_hooks.py -> hooks_data.json + composite images; gen_hooks_board.py -> Miro SVG frames + plan
- board/: frame ids, image ids and push instructions for the live board
