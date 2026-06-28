import re

def process_html():
    with open(r'd:\Documents\Google Antygravity\file for wed\richard-wyckoff-luoc-su.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''

    # Scope style under the panel ID
    style_content = style_content.replace(':root', '#article-wyckoff-panel')
    style_content = re.sub(r'\bbody\s*\{', '#article-wyckoff-panel.wyckoff-body {', style_content)

    scoped_style = f"""
<style>
#article-wyckoff-panel {{
    {style_content}
}}
</style>
"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    panel_html = f"""
<div id="article-wyckoff-panel" class="sukien-article-panel wyckoff-body">
    {scoped_style}
    <div style="padding: 10px 20px;">
        <button class="back-btn" onclick="openLegendArticle('')" style="border: 1px solid #c9b696; padding: 6px 14px; cursor: pointer; background: #f3e9d6; font-family: inherit; color: #2c2316; border-radius: 3px; margin-bottom: 20px;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center;">
        <button class="back-btn" onclick="openLegendArticle('')" style="border: 1px solid #c9b696; padding: 6px 14px; cursor: pointer; background: #f3e9d6; font-family: inherit; color: #2c2316; border-radius: 3px;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
</div>
"""
    return panel_html

def main():
    panel_html = process_html()

    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    # The card for richard-wyckoff already exists in the list, just needs panel inserted
    # Verify panel not already present
    if 'article-wyckoff-panel' in index_html:
        print("Panel already exists in index.html")
    else:
        # Insert panel before closing of huyen-thoai-article-view
        panel_target = """                </div><!-- /#huyen-thoai-article-view -->

            </div><!-- /#panel-huyen-thoai -->"""

        if panel_target in index_html:
            index_html = index_html.replace(panel_target, panel_html + "\n" + panel_target)
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(index_html)
            print("Successfully updated index.html")
        else:
            print("Target not found in index.html")

    # 2. Update script.js
    with open('script.js', 'r', encoding='utf-8') as f:
        script = f.read()

    if 'richard-wyckoff' in script:
        print("script.js already has richard-wyckoff routing")
        return

    route1 = """        } else if (subPath === '/jim-simons') {
            openLegendArticle('jim-simons', updateUrl);"""
    route1_new = """        } else if (subPath === '/richard-wyckoff') {
            openLegendArticle('richard-wyckoff', updateUrl);
        } else if (subPath === '/jim-simons') {
            openLegendArticle('jim-simons', updateUrl);"""

    route2 = """    } else if (articleId === 'jim-simons') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-jimsimons-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'jim-simons' }, '', '/huyen-thoai/jim-simons');
        window.scrollTo({ top: 0, behavior: 'smooth' });"""
    route2_new = """    } else if (articleId === 'richard-wyckoff') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-wyckoff-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'richard-wyckoff' }, '', '/huyen-thoai/richard-wyckoff');
        window.scrollTo({ top: 0, behavior: 'smooth' });\n""" + route2

    script = script.replace(route1, route1_new)
    script = script.replace(route2, route2_new)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print("Successfully updated script.js")

if __name__ == '__main__':
    main()
