import re

def process_html():
    with open(r'd:\Documents\Google Antygravity\file for wed\su-im-lang-va-tai-tao-than-kinh.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''

    # Scope style under panel ID to avoid conflicts with global CSS
    style_content = style_content.replace(':root', '#article-imlangtk-panel')
    style_content = re.sub(r'\bbody\s*\{', '#article-imlangtk-panel.imlangtk-body {', style_content)
    style_content = re.sub(r'\bhtml\s*\{', '#article-imlangtk-panel.imlangtk-html {', style_content)

    scoped_style = f"""<style>
#article-imlangtk-panel {{
{style_content}
}}
</style>"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    panel_html = f"""
<div id="article-imlangtk-panel" class="sukien-article-panel imlangtk-body">
    {scoped_style}
    <div style="padding: 16px 20px; background: #1a1a2e;">
        <button onclick="openThuVienArticle('')" style="background: transparent; border: 1px solid rgba(92,124,250,0.5); color: #5c7cfa; padding: 7px 16px; cursor: pointer; font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
            &#8592; Quay lại Thư viện
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center; background: #fffdf7;">
        <button onclick="openThuVienArticle('')" style="background: transparent; border: 1px solid rgba(26,26,46,0.3); color: #1a1a2e; padding: 7px 16px; cursor: pointer; font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
            &#8592; Quay lại Thư viện
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

    if 'article-imlangtk-panel' in index_html:
        print("Panel already exists in index.html")
    else:
        # Add card to the list
        card_target = '<a href="/thu-vien/luoc-su-tu-vi" class="news-card clickable-card">'
        card_new = """<a href="/thu-vien/su-im-lang-va-tai-tao-than-kinh" class="news-card clickable-card">
<div class="news-meta">
<span class="news-source"><i class="fa-solid fa-brain"></i> Khoa học & Tâm lý</span>
<span class="news-time">Tháng 6, 2026</span>
</div>
<h3 class="news-heading">Sự Im Lặng và Khả Năng Tái Tạo Thần Kinh — Phân Tích Khoa Học Toàn Diện</h3>
<p class="news-excerpt">Từ khoa học thần kinh đến thiền định — những phát hiện mới nhất về cách sự im lặng và nghỉ ngơi định hướng lại não bộ, phục hồi tâm trí và tái tạo năng lượng.</p>
<div class="news-footer">
<span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc tài liệu</span>
</div>
</a>

""" + card_target
        index_html = index_html.replace(card_target, card_new)

        # Insert panel into article-view area — insert before first panel in thu-vien-article-view
        panel_target = '\n<div id="article-phathoc-panel" class="sukien-article-panel">'
        panel_new = '\n' + panel_html + '\n<div id="article-phathoc-panel" class="sukien-article-panel">'
        index_html = index_html.replace(panel_target, panel_new)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
        print("Successfully updated index.html")

    # 2. Update script.js
    with open('script.js', 'r', encoding='utf-8') as f:
        script = f.read()

    if 'su-im-lang-va-tai-tao-than-kinh' in script:
        print("script.js already has routing")
        return

    # Add route in handleRouting
    route1 = "        } else if (subPath === '/luoc-su-tu-vi') {\n            openThuVienArticle('luoc-su-tu-vi', updateUrl);"
    route1_new = "        } else if (subPath === '/su-im-lang-va-tai-tao-than-kinh') {\n            openThuVienArticle('su-im-lang-va-tai-tao-than-kinh', updateUrl);\n" + route1

    # Add handler in openThuVienArticle
    route2 = "    } else if (articleId === 'luoc-su-tu-vi') {"
    route2_new = """    } else if (articleId === 'su-im-lang-va-tai-tao-than-kinh') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-imlangtk-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'su-im-lang-va-tai-tao-than-kinh' }, '', '/thu-vien/su-im-lang-va-tai-tao-than-kinh');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'luoc-su-tu-vi') {"""

    script = script.replace(route1, route1_new)
    script = script.replace(route2, route2_new)

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print("Successfully updated script.js")

if __name__ == '__main__':
    main()
