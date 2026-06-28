import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: index.html not found")
        sys.exit(1)

    original = content

    # ===== GOLD PANEL =====
    # .wrap max-width: 960px -> 1400px
    # hero subtitle max-width: 560px -> 840px
    content = content.replace(
        '#article-gold-panel .wrap {\n  max-width: 960px;',
        '#article-gold-panel .wrap {\n  max-width: 1400px;'
    )
    # hero max-width 560 -> 840 (hero subtitle)
    # We'll do a scoped replacement just in the gold panel area

    # ===== OIL PANEL =====
    # main max-width:740px -> 1100px
    # hero subtitle max-width:620px -> 930px

    # ===== GANN PANEL =====
    # .wrap max-width: 860px -> 1300px
    # hero subtitle max-width: 600px -> 900px

    # ===== DARVAS PANEL =====
    # .container max-width: 860px -> 1300px
    # .container-wide max-width: 1100px -> 1600px
    # hero subtitle max-width: 640px -> 960px

    # ===== VALENTINI PANEL =====
    # --maxw: 760px -> 1140px (defined in :root equivalent block)
    # hero subtitle max-width: 560px -> 840px

    # ===== IMLANGTK PANEL =====
    # .main-content max-width: 860px -> 1300px
    # .article-container max-width: 860px -> 1300px
    # hero subtitle max-width: 640px -> 960px

    # Strategy: use scoped replacements via index positions
    def replace_in_panel(html, panel_id, old, new, occurrence=1):
        start = html.find(f'id="{panel_id}"')
        if start == -1:
            print(f"Panel {panel_id} not found!")
            return html
        count = 0
        pos = start
        while True:
            idx = html.find(old, pos)
            if idx == -1:
                print(f"  '{old}' not found in {panel_id}")
                break
            # Make sure it's within reasonable range (within panel's first 60000 chars)
            if idx - start > 60000:
                print(f"  '{old}' too far from {panel_id}")
                break
            count += 1
            if count == occurrence:
                html = html[:idx] + new + html[idx + len(old):]
                print(f"  Replaced '{old}' -> '{new}' in {panel_id}")
                break
            pos = idx + 1
        return html

    # GOLD PANEL
    content = replace_in_panel(content, 'article-gold-panel', 'max-width: 960px;', 'max-width: 1440px;')   # .wrap
    content = replace_in_panel(content, 'article-gold-panel', 'max-width: 560px;', 'max-width: 840px;')    # hero subtitle

    # OIL PANEL
    content = replace_in_panel(content, 'article-oil-panel', 'max-width:620px;', 'max-width:930px;')       # hero subtitle
    content = replace_in_panel(content, 'article-oil-panel', 'max-width:740px;', 'max-width:1100px;')      # main

    # GANN PANEL
    content = replace_in_panel(content, 'article-gann-panel', 'max-width: 600px;', 'max-width: 900px;')    # hero subtitle
    content = replace_in_panel(content, 'article-gann-panel', 'max-width: 860px;', 'max-width: 1300px;')   # .wrap

    # DARVAS PANEL
    content = replace_in_panel(content, 'article-darvas-panel', 'max-width: 640px;', 'max-width: 960px;')  # hero subtitle
    content = replace_in_panel(content, 'article-darvas-panel', 'max-width: 860px;', 'max-width: 1300px;') # .container
    content = replace_in_panel(content, 'article-darvas-panel', 'max-width: 1100px;', 'max-width: 1650px;')# .container-wide

    # VALENTINI PANEL - uses --maxw CSS var
    content = replace_in_panel(content, 'article-valentini-panel', '--maxw: 760px;', '--maxw: 1140px;')    # var
    content = replace_in_panel(content, 'article-valentini-panel', 'max-width: 560px;', 'max-width: 840px;')# hero subtitle

    # IMLANGTK PANEL
    content = replace_in_panel(content, 'article-imlangtk-panel', 'max-width: 860px;', 'max-width: 1300px;')  # main content (first occurrence)
    content = replace_in_panel(content, 'article-imlangtk-panel', 'max-width: 640px;', 'max-width: 960px;')   # hero subtitle
    content = replace_in_panel(content, 'article-imlangtk-panel', 'max-width: 860px;', 'max-width: 1300px;', occurrence=1)  # second occurrence

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("\nDone! All article panels widths expanded ~1.5x.")

if __name__ == '__main__':
    main()
