import urllib.request
import urllib.parse
import json
import os

HEADERS = {'User-Agent': 'FundileBot/1.0 (Educational open source learning platform; princenqaba@gmail.com)'}

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")
os.makedirs(OUT_DIR, exist_ok=True)

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
    ("Male internal reproductive organs.svg", "male_internal_organs.svg"),
    ("Male anatomy.svg", "male_anatomy.svg"),
    ("Male genitalia, internal.svg", "male_genitalia_internal.svg"),
    ("Scheme female reproductive system-en.svg", "female_scheme.svg"),
    ("Chromosomal Crossover.svg", "chromosomal_crossover.svg"),
    ("Synapsis and Crossing Over No Labels.png", "synapsis_crossing_over_nolabels.png"),
]

for wiki_name, local_name in targets:
    url = get_commons_url(wiki_name)
    if url:
        dst = os.path.join(OUT_DIR, local_name)
        try:
            download_file(url, dst)
        except Exception as e:
            print(f"Error downloading {wiki_name}: {e}")
    else:
        print(f"No URL found for {wiki_name}")
