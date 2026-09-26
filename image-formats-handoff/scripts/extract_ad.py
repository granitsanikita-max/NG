#!/usr/bin/env python3
"""usage: extract_ad.py <rawhtml_file> <ad_id>  -> prints JSON {video, poster, images} for the deeplinked ad"""
import sys, re, json
s = open(sys.argv[1]).read()
for _ in range(3): s = s.replace('\\\\', '\\').replace('\\"', '"').replace('\\/', '/')
ad = sys.argv[2]
i = s.find('"deeplink_ad_archive":{"ad_archive_id":"%s"' % ad)
if i < 0:
    i = s.find('"ad_archive_id":"%s"' % ad)
if i < 0:
    print(json.dumps({"error": "ad not found"})); sys.exit(2)
seg = s[i:i + 60000]
def g(k):
    m = re.search('"%s":"([^"]+)"' % k, seg); return m.group(1).replace('\\u0025', '%') if m else None
imgs = re.findall('"original_image_url":"([^"]+)"', seg)[:3]
print(json.dumps({"video": g("video_hd_url") or g("video_sd_url"), "poster": g("video_preview_image_url"), "images": imgs, "display_format": g("display_format")}))
