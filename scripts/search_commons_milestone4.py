import urllib.request
import urllib.parse
import json

headers = {'User-Agent': 'FundileBot/1.0 (princenqaba@gmail.com)'}

def search_commons(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json&srlimit=8"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return [item['title'] for item in data['query']['search']]

def safe_print(s):
    print(s.encode('ascii', 'replace').decode())

safe_print("Male search:")
for t in search_commons("Scheme male reproductive system"):
    safe_print(t)
for t in search_commons("Male internal reproductive organs"):
    safe_print(t)
for t in search_commons("Male anatomy"):
    safe_print(t)

safe_print("\nFemale search:")
for t in search_commons("Scheme female reproductive system"):
    safe_print(t)

safe_print("\nCrossing over search:")
for t in search_commons("Chromosomal Crossover"):
    safe_print(t)
for t in search_commons("Crossing over"):
    safe_print(t)
