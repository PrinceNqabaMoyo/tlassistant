import urllib.request
import json
import os

HEADERS = {
    'User-Agent': 'FundileBot/1.0 (Educational open source learning platform; princenqaba@gmail.com)'
}

PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams")

def download_file(url, target_path):
    print(f"Downloading {url} to {target_path}...")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp, open(target_path, 'wb') as f:
        f.write(resp.read())
    print(f"Downloaded {target_path} ({os.path.getsize(target_path)} bytes)")

def get_commons_url(filename):
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles=File:{urllib.parse.quote(filename)}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data['query']['pages']
        for page_id in pages:
            return pages[page_id]['imageinfo'][0]['url']

def main():
    targets = [
        ("Diagram_of_human_eye_without_labels.svg", "human_eye_wikimedia.svg"),
        ("Anatomy_of_the_Human_Ear_blank.svg", "human_ear_wikimedia.svg"),
        ("Human_endocrine_male_&_female_svg_no_labels.svg", "endocrine_system_wikimedia.svg"),
    ]
    for wiki_name, local_name in targets:
        dst = os.path.join(PUBLIC_DIR, local_name)
        try:
            url = get_commons_url(wiki_name)
            print(f"Direct URL for {wiki_name}: {url}")
            download_file(url, dst)
        except Exception as e:
            print(f"Failed to fetch {wiki_name}: {e}")

if __name__ == "__main__":
    main()
