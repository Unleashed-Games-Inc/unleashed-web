#!/usr/bin/env python3
"""Fetch the latest videos from the Unleashed Games YouTube channel and write videos.json.

Uses YouTube's public per-channel RSS feed — no API key required. Run locally or via
the youtube-feed GitHub Action (.github/workflows/youtube-feed.yml).
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

CHANNEL_ID = os.environ.get("YT_CHANNEL_ID", "UC2Oql-KGdR_DFOON-tVIPBQ")  # @UnleashedGG
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
MAX_VIDEOS = int(os.environ.get("YT_MAX_VIDEOS", "12"))
OUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "videos.json")

NS = {
    "a": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "unleashed-web-feed/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main() -> int:
    root = ET.fromstring(fetch(FEED_URL))
    videos = []
    for entry in root.findall("a:entry", NS)[:MAX_VIDEOS]:
        vid = entry.find("yt:videoId", NS).text
        title = entry.find("a:title", NS).text
        published = entry.find("a:published", NS).text  # ISO 8601
        videos.append({
            "id": vid,
            "title": title,
            "published": published,
            "thumb": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
            "url": f"https://www.youtube.com/watch?v={vid}",
        })

    if not videos:
        print("No videos parsed from feed; leaving videos.json untouched.", file=sys.stderr)
        return 1

    payload = {
        "channel": CHANNEL_ID,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(videos),
        "videos": videos,
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {len(videos)} videos to {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
