# LucenWell — AI avatar / start-scene workflow (locked decision)

**Avatar realism: use Nano Banana Pro (higgsfield model `nano_banana_pro`), NOT GPT Image 2.5 or Seedream, for on-camera human avatars.**
- GPT Image 2.5 and Seedream render faces too plastic / "AI-y" for believable UGC.
- Nano Banana Pro, given a real reference photo as `image_references`, locks the person's face/hair/build cleanly and keeps authentic skin texture.
- Flow: upload the real reference → generate one master lock (front-facing UGC kitchen selfie) → reference that master (by media_id or prior job_id) for every subsequent shot so the face stays consistent.
- Resolution: 2K for start scenes (they get animated into video, which downscales). 4K only for large static stills.
- Product shots: feed the real product image (`product_inhand.png`) as an additional `image_references` so the bottle/label matches.

**V2 (Product Comparison Video) avatar = fresh face "Rachael v2"** — locked from user-supplied reference (curvy ~41 blonde). Distinct from Dana (V1/V3). Fresh face does NOT break the advertorial handoff; cold traffic still → advertorial, warm/retargeting → PDP.
