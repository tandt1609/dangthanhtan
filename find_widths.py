import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: index.html not found")
        sys.exit(1)

    panels = ['gold', 'gann', 'oil', 'darvas', 'valentini', 'imlangtk']
    for panel in panels:
        pid = f'article-{panel}-panel'
        start = None
        end = None
        for i, l in enumerate(lines):
            if f'<div id="{pid}"' in l:
                start = i
            if start and '</style>' in l and i > start:
                end = i
                break
        if start and end:
            print(f'--- {pid}: lines {start+1} to {end+1} ---')
            for j in range(start, min(end+1, start+600)):
                if 'max-width' in lines[j] or '.wrap' in lines[j] or '.container' in lines[j] or '.page {' in lines[j] or 'main{' in lines[j] or 'main {' in lines[j] or '.prose {' in lines[j]:
                    print(f'  {j+1}: {lines[j].strip()}')
        else:
            print(f"Could not find panel: {pid}")

if __name__ == '__main__':
    main()
