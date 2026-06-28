import re
import sys

def process_html():
    file_path = r'd:\Documents\Google Antygravity\file for wed\luoc-su-vang.html'
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
    style_content = style_content.replace(':root', '#article-gold-panel')
    style_content = re.sub(r'\bbody\s*\{', '#article-gold-panel.gold-body {', style_content)
    style_content = re.sub(r'\bhtml\s*\{', '#article-gold-panel.gold-html {', style_content)

    scoped_style = f"""<style>
#article-gold-panel {{
{style_content}
}}
</style>"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    panel_html = f"""
<div id="article-gold-panel" class="commodity-article-panel gold-body">
    {scoped_style}
    <div style="padding: 16px 20px; background: #0A0A0A;">
        <button onclick="openCommodityArticle('')" style="background: transparent; border: 1px solid rgba(212,160,23,0.5); color: #D4A017; padding: 7px 16px; cursor: pointer; font-family: 'Cinzel', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
            &#8592; Quay lại danh sách
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center; background: #0A0A0A;">
        <button onclick="openCommodityArticle('')" style="background: transparent; border: 1px solid rgba(212,160,23,0.5); color: #D4A017; padding: 7px 16px; cursor: pointer; font-family: 'Cinzel', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
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

    if 'article-gold-panel' in index_html:
        print("Panel already exists in index.html")
    else:
        # Add card to the list in Hàng Hóa tab
        card_new = """<a href="/hang-hoa/luoc-su-vang" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-coins"></i> Kim loại quý</span>
                                <span class="news-time">Lược sử vĩ đại</span>
                            </div>
                            <h3 class="news-heading">Lược Sử Vàng — Kim Loại Của Mọi Thời Đại</h3>
                            <p class="news-excerpt">Từ biểu tượng của thần linh, trụ cột của hệ thống tiền tệ, đến công cụ phòng hộ tối thượng trong thời đại bất ổn.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
"""
        
        # We need to insert right after <div class="news-list"> in commodity-list-view
        list_start = index_html.find('<div id="commodity-list-view"')
        if list_start != -1:
            news_list_start = index_html.find('<div class="news-list">', list_start)
            if news_list_start != -1:
                insert_pos = news_list_start + len('<div class="news-list">')
                index_html = index_html[:insert_pos] + '\n                        ' + card_new + index_html[insert_pos:]
            else:
                print("Error: Could not find news-list in commodity-list-view")
        else:
            print("Error: Could not find commodity-list-view")

        # Insert panel into commodity-article-view
        article_view_start = index_html.find('<div id="commodity-article-view"')
        if article_view_start != -1:
            # insert after the opening div
            insert_pos = index_html.find('>', article_view_start) + 1
            index_html = index_html[:insert_pos] + '\n' + panel_html + index_html[insert_pos:]
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(index_html)
            print("Successfully updated index.html")
        else:
             print("Error: Could not find commodity-article-view tag")

    # 2. Update script.js
    try:
        with open('script.js', 'r', encoding='utf-8') as f:
            script = f.read()
    except FileNotFoundError:
        print("Error: Could not find script.js")
        sys.exit(1)

    if '/luoc-su-vang' in script:
        print("script.js already has routing for gold")
    else:
        # Add route in handleRouting for hang-hoa
        route1_target = "if (subPath === '/luoc-su-dau-mo') {"
        if route1_target in script:
             route1_new = "if (subPath === '/luoc-su-vang') {\n            openCommodityArticle('luoc-su-vang', updateUrl);\n        } else " + route1_target
             script = script.replace(route1_target, route1_new)
        
        # Add handler in openCommodityArticle
        route2_target = "if (articleId === 'luoc-su-dau-mo') {"
        if route2_target in script:
             route2_new = """if (articleId === 'luoc-su-vang') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-gold-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'hang-hoa', articleId: 'luoc-su-vang' }, '', '/hang-hoa/luoc-su-vang');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else """ + route2_target
             script = script.replace(route2_target, route2_new)

        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(script)
        print("Successfully updated script.js")
    
    # 3. Add font to index.html if not exist
    with open('index.html', 'r', encoding='utf-8') as f:
            index_html = f.read()
    
    font_link = '<link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&display=swap" rel="stylesheet">'
    
    if 'family=Jost' not in index_html:
         head_end = index_html.find('</head>')
         if head_end != -1:
              index_html = index_html[:head_end] + "    " + font_link + "\n" + index_html[head_end:]
              with open('index.html', 'w', encoding='utf-8') as f:
                 f.write(index_html)
              print("Added font to index.html")

if __name__ == '__main__':
    main()
