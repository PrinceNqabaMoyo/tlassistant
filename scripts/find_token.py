import os, re

def search(token):
    for root, dirs, files in os.walk('src'):
        for f in files:
            if f.endswith(('.jsx', '.js')):
                path = os.path.join(root, f)
                content = open(path, encoding='utf-8', errors='ignore').read()
                matches = re.findall(rf'[^\'\"]*{re.escape(token)}[^\'\"]*', content)
                if matches:
                    print(f"{path}: {matches[:5]}")

if __name__ == '__main__':
    search('topic-card')
