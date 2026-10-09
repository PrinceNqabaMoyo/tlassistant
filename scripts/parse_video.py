import re
from pathlib import Path

content_file = Path(r"C:\Users\princ\.gemini\antigravity\brain\1d15265b-8900-4d95-a91c-abc8a7730424\.system_generated\steps\24990\content.md")
text = content_file.read_text(encoding="utf-8", errors="ignore")

for pattern in [
    r"<title>(.*?)</title>",
    r'name="title"\s+content="(.*?)"',
    r'property="og:title"\s+content="(.*?)"',
    r'property="og:description"\s+content="(.*?)"',
    r'name="description"\s+content="(.*?)"',
    r'"title":\{"simpleText":"(.*?)"\}',
    r'"videoDetails":\{"videoId":".*?","title":"(.*?)"',
]:
    matches = re.findall(pattern, text)
    if matches:
        print(f"Pattern {pattern} -> {matches[0]}")
