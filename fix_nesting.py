import sys
import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print("Error: Could not find index.html")
        sys.exit(1)

    panels = ['gann', 'oil', 'gold', 'darvas', 'valentini']
    
    for panel in panels:
        # Pattern to find the start of the buggy wrapper
        # <style>\n#article-{panel}-panel {
        start_pattern = f"<style>\n#article-{panel}-panel {{"
        if start_pattern in html:
            html = html.replace(start_pattern, "<style>")
            
            # Now we need to remove the closing '}' that matches this wrapper
            # It's located right before </style> for that panel.
            # We can use regex to find }\n</style> that immediately follows the panel's content
            # Wait, the closing wrapper is just:
            # }
            # </style>
            # Let's replace "}\n</style>" with "</style>" BUT only for the ones we fixed.
            # To be safe, we can do a targeted regex replace for the end of the style block of this panel.
            
            # Find the index of <div id="article-{panel}-panel"
            panel_div = f'<div id="article-{panel}-panel"'
            idx = html.find(panel_div)
            if idx != -1:
                # Find the </style> that belongs to this panel
                style_end = html.find('</style>', idx)
                if style_end != -1:
                    # Look backwards from </style> to find the '}'
                    before_style = html[:style_end]
                    last_brace = before_style.rfind('}')
                    if last_brace != -1:
                        # Remove that '}'
                        html = html[:last_brace] + html[last_brace+1:]
                        print(f"Fixed nesting for {panel}")
        else:
            print(f"Did not find buggy wrapper for {panel}")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done fixing CSS nesting.")

if __name__ == '__main__':
    main()
