import urllib.request
import urllib.parse
import json
import os

HEADERS = {'User-Agent': 'FundileBot/1.0 (Educational open source learning platform; princenqaba@gmail.com)'}

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

def download_file(url, target_path):
    print(f"Downloading {url} to {target_path}...")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp, open(target_path, 'wb') as f:
        f.write(resp.read())
    print(f"Saved {target_path} ({os.path.getsize(target_path)} bytes)")

def get_commons_url(filename):
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles=File:{urllib.parse.quote(filename)}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data['query']['pages']
        for page_id in pages:
            if 'imageinfo' in pages[page_id]:
                return pages[page_id]['imageinfo'][0]['url']
    return None

targets = [
    ("Figure 27 01 01ab.jpg", "openstax_male_27_01_01.jpg"),
    ("Figure 27 01 02.jpg", "openstax_male_27_01_02.jpg"),
    ("Figure 27 02 01.png", "openstax_female_27_02_01.png"),
    ("Figure 28 02 01.JPG", "openstax_female_28_02_01.jpg"),
    ("Figure 28 02 06.JPG", "openstax_female_28_02_06.jpg"),
]

for wiki_name, local_name in targets:
    url = get_commons_url(wiki_name)
    if url:
        dst = os.path.join(OUT_DIR, local_name)
        try:
            download_file(url, dst)
        except Exception as e:
            print(f"Error {wiki_name}: {e}")
    else:
        print(f"No URL for {wiki_name}")
