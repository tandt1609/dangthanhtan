import re

def process_steiner():
    with open(r'd:\Documents\Google Antygravity\file for wed\rudolf-steiner-luoc-su.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''

    # Scope style
    style_content = style_content.replace(':root', '#article-steiner-panel')
    style_content = style_content.replace('body{', '#article-steiner-panel.steiner-body {')
    style_content = style_content.replace('body {', '#article-steiner-panel.steiner-body {')
    
    scoped_style = f"""
<style>
#article-steiner-panel {{
    {style_content.replace(':root', '&').replace('body', '&')}
}}
</style>
"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''
    
    panel_html = f"""
<div id="article-steiner-panel" class="sukien-article-panel steiner-body">
    {scoped_style}
    <div style="padding: 10px 20px; background: var(--parch);">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: var(--ink); border: 1px solid var(--ink); padding: 5px 10px; cursor: pointer; background: transparent; font-family: inherit; margin-bottom: 20px;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center; background: var(--parch);">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: var(--ink); border: 1px solid var(--ink); padding: 5px 10px; cursor: pointer; background: transparent; font-family: inherit;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
</div>
"""
    return panel_html

def main():
    panel_html = process_steiner()
    
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    target = """                </div><!-- /#huyen-thoai-article-view -->

            </div><!-- /#panel-huyen-thoai -->"""
            
    if target in index_html and 'article-steiner-panel' not in index_html:
        index_html = index_html.replace(target, panel_html + "\n" + target)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
            print("Successfully inserted panel")
    else:
        print("Target not found or already inserted")

if __name__ == '__main__':
    main()
