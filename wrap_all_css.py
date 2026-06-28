import sys
import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print("Error: index.html not found")
        sys.exit(1)

    panels = ['gann', 'oil', 'gold', 'darvas', 'valentini']
    
    for panel in panels:
        panel_id = f"article-{panel}-panel"
        
        idx = html.find(f'id="{panel_id}"')
        if idx == -1:
            continue
            
        style_start = html.find('<style>', idx)
        style_end = html.find('</style>', style_start)
        
        if style_start == -1 or style_end == -1:
            continue
            
        style_content = html[style_start + 7:style_end].strip()
        
        # 1. Un-wrap if it's currently completely wrapped (e.g., from our previous script)
        # Check if the entire block is inside #{panel_id} { ... }
        if style_content.startswith(f"#{panel_id} {{") and style_content.endswith("}"):
            # We already fully wrapped valentini and oil! Let's unwrap them so we can re-process safely.
            # Actually, valentini and oil are already 100% perfectly nested. Let's skip them!
            if panel in ['valentini', 'oil']:
                print(f"{panel} is fully and perfectly nested. Skipping.")
                continue
                
        # 2. For the others (gann, gold, darvas), they have scattered #{panel_id} references.
        # We need to replace all #{panel_id} with &
        # Watch out for things like #{panel_id} { --vars: 1; } -> & { --vars: 1; }
        # And #{panel_id}.gann-body -> & .gann-body (or &.gann-body)
        
        # Replace ALL occurrences of #{panel_id} with &
        style_content = style_content.replace(f"#{panel_id}", "&")
        
        # 3. Now wrap the ENTIRE style block in #{panel_id} { ... }
        new_style = f"\n#{panel_id} {{\n{style_content}\n}}\n"
        
        html = html[:style_start + 7] + new_style + html[style_end:]
        print(f"Wrapped and scoped CSS for {panel}")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done wrapping all CSS!")

if __name__ == '__main__':
    main()
