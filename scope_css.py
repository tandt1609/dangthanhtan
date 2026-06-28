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
    
    # We will find the <style> block immediately following <div id="article-{panel}-panel"
    
    for panel in panels:
        panel_id = f"article-{panel}-panel"
        
        # Find the <div id="...">
        idx = html.find(f'id="{panel_id}"')
        if idx == -1:
            continue
            
        style_start = html.find('<style>', idx)
        style_end = html.find('</style>', style_start)
        
        if style_start == -1 or style_end == -1:
            continue
            
        # Extract the style content
        style_content = html[style_start + 7:style_end].strip()
        
        # If it's already wrapped, skip (but we know it's not because we removed it)
        if style_content.startswith(f"#{panel_id} {{"):
            print(f"{panel} is already wrapped. Skipping.")
            continue
            
        # We need to wrap it. BUT we must fix the inner selectors that refer to the panel itself!
        # When I added these panels, I did things like:
        # #article-gold-panel { ... } (from :root)
        # #article-gold-panel.gold-body { ... } (from body)
        # #article-gold-panel.gold-html { ... } (from html)
        
        # So we replace these with '&' (the nesting selector)
        style_content = style_content.replace(f"#{panel_id}.{panel}-body", f"&.{panel}-body")
        style_content = style_content.replace(f"#{panel_id}.{panel}-html", f"&.{panel}-html")
        
        # For Darvas/Valentini etc, they might just be panel-body without the panel prefix in the class?
        # Actually in add_darvas.py I used:
        # f'#{panel_id}.darvas-body'
        
        # What about :root? It became #{panel_id}
        # We replace #{panel_id} { with & {
        # But only if it's followed by a space and {
        style_content = re.sub(rf'#{panel_id}\s*\{{', '& {', style_content)
        
        # For Valentini, it used --maxw: var, which I replaced in expand_widths.py
        # Make sure we don't mess up variables.
        
        # Now wrap it in #{panel_id} { ... }
        new_style = f"\n#{panel_id} {{\n{style_content}\n}}\n"
        
        # Re-insert into html
        html = html[:style_start + 7] + new_style + html[style_end:]
        print(f"Wrapped CSS for {panel}")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done scoping CSS!")

if __name__ == '__main__':
    main()
