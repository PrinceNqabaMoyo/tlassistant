import urllib.request
import urllib.parse
import json

headers = {'User-Agent': 'FundileBot/1.0 (princenqaba@gmail.com)'}

def search_commons(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}%20filetype:drawing&srnamespace=6&format=json&srlimit=15"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        return [item['title'] for item in data['query']['search']]

def p(s):
    print(s.encode('ascii', 'replace').decode())

p("=== Male Reproductive System SVGs ===")
for t in search_commons("male reproductive system"):
    p(t)

p("\n=== Female Reproductive System SVGs ===")
for t in search_commons("female reproductive system"):
    p(t)
