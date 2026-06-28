import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print("Error: Could not find index.html")
        sys.exit(1)

    # We will replace the previous fix block with an updated one
    old_fix = """
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

    new_fix = """
/* ===== GLOBAL ARTICLE COLOR FIX ===== */
/* Override global colors so they inherit from their specific article scopes */
.sukien-article-panel p,
.sukien-article-panel li,
.sukien-article-panel td,
.sukien-article-panel th,
.sukien-article-panel blockquote,
.sukien-article-panel strong,
.sukien-article-panel em,
.commodity-article-panel p,
.commodity-article-panel li,
.commodity-article-panel td,
.commodity-article-panel th,
.commodity-article-panel blockquote,
.commodity-article-panel strong,
.commodity-article-panel em {
    color: inherit;
}
/* For em, reset font-style to inherit or italic because global CSS set it to normal */
.sukien-article-panel em,
.commodity-article-panel em {
    font-style: italic;
    font-weight: inherit;
}
/* For strong, reset font-weight to inherit or bold */
.sukien-article-panel strong,
.commodity-article-panel strong {
    font-weight: bold;
}
"""

    if old_fix in html:
        html = html.replace(old_fix, new_fix)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Successfully updated global article color fix in index.html")
    else:
        print("Could not find the old fix block to replace.")

if __name__ == '__main__':
    main()
