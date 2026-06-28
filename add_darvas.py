import re
import sys

def process_html():
    file_path = r'd:\Documents\Google Antygravity\file for wed\nicolas-darvas-luoc-su.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}")
        sys.exit(1)

    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''

    # Scope style under panel ID to avoid conflicts with global CSS
    style_content = style_content.replace(':root', '#article-darvas-panel')
    style_content = re.sub(r'\bbody\s*\{', '#article-darvas-panel.darvas-body {', style_content)
    style_content = re.sub(r'\bhtml\s*\{', '#article-darvas-panel.darvas-html {', style_content)

    scoped_style = f"""<style>
#article-darvas-panel {{
{style_content}
}}
</style>"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    panel_html = f"""
<div id="article-darvas-panel" class="sukien-article-panel darvas-body">
    {scoped_style}
    <div style="padding: 16px 20px; background: #0D0F14;">
        <button onclick="openLegendArticle('')" style="background: transparent; border: 1px solid rgba(200,160,74,0.5); color: #C8A04A; padding: 7px 16px; cursor: pointer; font-family: 'DM Mono', monospace; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
            &#8592; Quay lại danh sách
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center; background: #0D0F14;">
        <button onclick="openLegendArticle('')" style="background: transparent; border: 1px solid rgba(200,160,74,0.5); color: #C8A04A; padding: 7px 16px; cursor: pointer; font-family: 'DM Mono', monospace; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
            &#8592; Quay lại danh sách
        </button>
    </div>
</div>
"""
    return panel_html

def main():
    panel_html = process_html()

    # 1. Update index.html
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            index_html = f.read()
    except FileNotFoundError:
        print("Error: Could not find index.html")
        sys.exit(1)

    if 'article-darvas-panel' in index_html:
        print("Panel already exists in index.html")
    else:
        # Add card to the list in Huyền Thoại tab
        card_target = '<div class="news-list">'
        card_new = """<div class="news-list">
                        <a href="/huyen-thoai/nicolas-darvas" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-arrow-trend-up"></i> Giao dịch theo đà</span>
                                <span class="news-time">1920 – 1977</span>
                            </div>
                            <h3 class="news-heading"><span style="font-size:0.75em;color:#6fae6a;font-weight:500;display:block;margin-bottom:2px;letter-spacing:0.04em;">Giao dịch theo đà</span>Nicolas Darvas — Lược Sử Huyền Thoại</h3>
                            <p class="news-excerpt">Vũ công vĩ đại đã biến 36,000 đô la thành 2 triệu đô la với Lý thuyết Hộp nổi tiếng.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
"""
        
        # We need to make sure we replace the first occurrence in the huyen thoai section
        huyen_thoai_start = index_html.find('id="panel-huyen-thoai"')
        if huyen_thoai_start != -1:
            list_start = index_html.find(card_target, huyen_thoai_start)
            if list_start != -1:
                index_html = index_html[:list_start] + card_new + index_html[list_start + len(card_target):]
            else:
                print("Error: Could not find news-list in huyen-thoai panel")
        else:
            print("Error: Could not find panel-huyen-thoai")


        # Insert panel into article-view area for huyen-thoai
        panel_target = '<!-- END OF HUYỀN THOẠI ARTICLE VIEW -->'
        
        huyen_thoai_article_end = index_html.find('</div><!-- /#huyen-thoai-article-view -->')
        if huyen_thoai_article_end != -1:
             index_html = index_html[:huyen_thoai_article_end] + panel_html + '\n                ' + index_html[huyen_thoai_article_end:]
             with open('index.html', 'w', encoding='utf-8') as f:
                f.write(index_html)
             print("Successfully updated index.html")
        else:
             print("Error: Could not find huyen-thoai-article-view end tag")
             

    # 2. Update script.js
    try:
        with open('script.js', 'r', encoding='utf-8') as f:
            script = f.read()
    except FileNotFoundError:
        print("Error: Could not find script.js")
        sys.exit(1)

    if '/nicolas-darvas' in script:
        print("script.js already has routing")
        return

    # Add route in handleRouting for huyen-thoai
    route1 = "        if (subPath === '/wd-gann') {"
    route1_new = "        if (subPath === '/nicolas-darvas') {\n            openLegendArticle('nicolas-darvas', updateUrl);\n        } else if (subPath === '/wd-gann') {"

    # Add handler in openLegendArticle
    route2 = "    if (articleId === 'wd-gann') {"
    route2_new = """    if (articleId === 'nicolas-darvas') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-darvas-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'nicolas-darvas' }, '', '/huyen-thoai/nicolas-darvas');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'wd-gann') {"""

    if route1 in script:
        script = script.replace(route1, route1_new)
    elif "if (subPath === '/rudolf-steiner') {" in script:
        route1_fallback = "if (subPath === '/rudolf-steiner') {"
        route1_new_fallback = "if (subPath === '/nicolas-darvas') {\n            openLegendArticle('nicolas-darvas', updateUrl);\n        } else if (subPath === '/rudolf-steiner') {"
        script = script.replace(route1_fallback, route1_new_fallback)
        
    if route2 in script:
        script = script.replace(route2, route2_new)
    elif "if (articleId === 'rudolf-steiner') {" in script:
        route2_fallback = "if (articleId === 'rudolf-steiner') {"
        route2_new_fallback = """if (articleId === 'nicolas-darvas') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-darvas-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'nicolas-darvas' }, '', '/huyen-thoai/nicolas-darvas');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'rudolf-steiner') {"""
        script = script.replace(route2_fallback, route2_new_fallback)

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print("Successfully updated script.js")
    
    # 3. add font to index.html if not exist
    with open('index.html', 'r', encoding='utf-8') as f:
            index_html = f.read()
    
    font_link = '<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />'
    
    if font_link not in index_html:
         # Need to find the right place to put it
         head_end = index_html.find('</head>')
         if head_end != -1:
              index_html = index_html[:head_end] + "    " + font_link + "\n" + index_html[head_end:]
              with open('index.html', 'w', encoding='utf-8') as f:
                 f.write(index_html)
              print("Added font to index.html")

if __name__ == '__main__':
    main()
