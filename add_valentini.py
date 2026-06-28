import re
import sys

def process_html():
    file_path = r'd:\Documents\Google Antygravity\file for wed\Fabio_Valentini_Luoc_Su.html'
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
    style_content = style_content.replace(':root', '#article-valentini-panel')
    style_content = re.sub(r'\bbody\s*\{', '#article-valentini-panel.valentini-body {', style_content)
    style_content = re.sub(r'\bhtml\s*\{', '#article-valentini-panel.valentini-html {', style_content)

    scoped_style = f"""<style>
#article-valentini-panel {{
{style_content}
}}
</style>"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    panel_html = f"""
<div id="article-valentini-panel" class="sukien-article-panel valentini-body">
    {scoped_style}
    <div style="padding: 16px 20px; background: #f3e9d2;">
        <button onclick="openLegendArticle('')" style="background: transparent; border: 1px solid rgba(160,106,44,0.5); color: #a06a2c; padding: 7px 16px; cursor: pointer; font-family: 'Cormorant SC', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px; font-weight: 600;">
            &#8592; Quay lại danh sách
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center; background: #f3e9d2;">
        <button onclick="openLegendArticle('')" style="background: transparent; border: 1px solid rgba(160,106,44,0.5); color: #a06a2c; padding: 7px 16px; cursor: pointer; font-family: 'Cormorant SC', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px; font-weight: 600;">
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

    if 'article-valentini-panel' in index_html:
        print("Panel already exists in index.html")
    else:
        # Add card to the list in Huyền Thoại tab
        card_target = '<div class="news-list">'
        card_new = """<div class="news-list">
                        <a href="/huyen-thoai/fabio-valentini" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-water"></i> Giao dịch lướt sóng</span>
                                <span class="news-time">Đương đại</span>
                            </div>
                            <h3 class="news-heading"><span style="font-size:0.75em;color:#6fae6a;font-weight:500;display:block;margin-bottom:2px;letter-spacing:0.04em;">Giao dịch lướt sóng</span>Fabio Valentini — Lược Sử Huyền Thoại</h3>
                            <p class="news-excerpt">Từ một trang chiến lược cá nhân ở Italia đến sàn giao dịch quốc tế tại Dubai — hành trình của một người lướt sóng theo đuổi xác suất, kỷ luật và sự minh bạch.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
"""
        
        # Replace the first occurrence in the huyen thoai section
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

    if '/fabio-valentini' in script:
        print("script.js already has routing")
        return

    # Add route in handleRouting for huyen-thoai
    route1 = "        if (subPath === '/nicolas-darvas') {"
    route1_new = "        if (subPath === '/fabio-valentini') {\n            openLegendArticle('fabio-valentini', updateUrl);\n        } else if (subPath === '/nicolas-darvas') {"

    # Add handler in openLegendArticle
    route2 = "    if (articleId === 'nicolas-darvas') {"
    route2_new = """    if (articleId === 'fabio-valentini') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-valentini-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'fabio-valentini' }, '', '/huyen-thoai/fabio-valentini');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'nicolas-darvas') {"""

    if route1 in script:
        script = script.replace(route1, route1_new)
    elif "if (subPath === '/wd-gann') {" in script:
        route1_fallback = "if (subPath === '/wd-gann') {"
        route1_new_fallback = "if (subPath === '/fabio-valentini') {\n            openLegendArticle('fabio-valentini', updateUrl);\n        } else if (subPath === '/wd-gann') {"
        script = script.replace(route1_fallback, route1_new_fallback)
        
    if route2 in script:
        script = script.replace(route2, route2_new)
    elif "if (articleId === 'wd-gann') {" in script:
        route2_fallback = "if (articleId === 'wd-gann') {"
        route2_new_fallback = """if (articleId === 'fabio-valentini') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-valentini-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'fabio-valentini' }, '', '/huyen-thoai/fabio-valentini');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'wd-gann') {"""
        script = script.replace(route2_fallback, route2_new_fallback)

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print("Successfully updated script.js")
    
    # 3. add font to index.html if not exist
    with open('index.html', 'r', encoding='utf-8') as f:
            index_html = f.read()
    
    font_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;600&display=swap" rel="stylesheet" />'
    
    if 'Cormorant+SC' not in index_html:
         head_end = index_html.find('</head>')
         if head_end != -1:
              index_html = index_html[:head_end] + "    " + font_link + "\n" + index_html[head_end:]
              with open('index.html', 'w', encoding='utf-8') as f:
                 f.write(index_html)
              print("Added font to index.html")

if __name__ == '__main__':
    main()
