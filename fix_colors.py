import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print("Error: Could not find index.html")
        sys.exit(1)

    # CSS to force inheritance in all article panels
    fix_css = """
/* ===== GLOBAL ARTICLE COLOR FIX ===== */
/* Override global p, li, td colors so they inherit from their specific article scopes */
.sukien-article-panel p,
.sukien-article-panel li,
.sukien-article-panel td,
.sukien-article-panel th,
.sukien-article-panel blockquote,
.commodity-article-panel p,
.commodity-article-panel li,
.commodity-article-panel td,
.commodity-article-panel th,
.commodity-article-panel blockquote {
    color: inherit;
}
"""

    if 'GLOBAL ARTICLE COLOR FIX' in html:
        print("Fix already applied.")
        return

    # Insert right before </style> or right after <link rel="stylesheet">
    insert_marker = '<!-- Remove preload class after CSS loads'
    idx = html.find(insert_marker)
    
    if idx != -1:
        # Wrap the fix in a <style> tag
        style_block = f"<style>{fix_css}</style>\n    "
        html = html[:idx] + style_block + html[idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Successfully applied global article color fix to index.html")
    else:
        print("Could not find insertion marker")

if __name__ == '__main__':
    main()
