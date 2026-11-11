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
    ("Male genital system - Sagittal view.svg", "male_sagittal_vector.svg"),
    ("Human male reproductive system en.svg", "male_human_repro_vector.svg"),
    ("Female genital system - Front view 1.svg", "female_front_1_vector.svg"),
    ("Female genital system - Front view 2.svg", "female_front_2_vector.svg"),
    ("Female internal genitalia unlabeled.svg", "female_internal_unlabeled.svg"),
    ("Sexual organs - female (no description).svg", "female_no_description.svg"),
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
