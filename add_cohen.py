import re

def process_html():
    with open(r'd:\Documents\Google Antygravity\file for wed\steven-cohen-luoc-su.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''

    # Scope style
    style_content = style_content.replace(':root', '#article-cohen-panel')
    style_content = style_content.replace('body{', '#article-cohen-panel.cohen-body {')
    style_content = style_content.replace('body {', '#article-cohen-panel.cohen-body {')
    
    scoped_style = f"""
<style>
#article-cohen-panel {{
    {style_content.replace(':root', '&').replace('body', '&')}
}}
</style>
"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''
    
    panel_html = f"""
<div id="article-cohen-panel" class="sukien-article-panel cohen-body">
    {scoped_style}
    <div style="padding: 10px 20px; background: var(--bg);">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: var(--text); border: 1px solid var(--rule); padding: 5px 10px; cursor: pointer; background: var(--bg-panel); font-family: inherit; margin-bottom: 20px;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center; background: var(--bg);">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: var(--text); border: 1px solid var(--rule); padding: 5px 10px; cursor: pointer; background: var(--bg-panel); font-family: inherit;">
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

    card_target = """                        <a href="/huyen-thoai/jim-simons" class="news-card clickable-card">"""
    
    card_new = """                        <a href="/huyen-thoai/steven-cohen" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-crown"></i> Hồ sơ Huyền thoại</span>
                                <span class="news-time">11/06/1956 – nay</span>
                            </div>
                            <h3 class="news-heading">Steven A. Cohen — Lược Sử, Triết Lý và Phương Pháp</h3>
                            <p class="news-excerpt">Từ một thiếu niên mê bài poker đến người sáng lập quỹ đầu cơ có tỷ suất sinh lời cao nhất lịch sử và vụ phạt giao dịch nội gián khét tiếng.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>

                        <a href="/huyen-thoai/jim-simons" class="news-card clickable-card">"""

    if 'steven-cohen' not in index_html:
        index_html = index_html.replace(card_target, card_new)

    panel_target = """                </div><!-- /#huyen-thoai-article-view -->

            </div><!-- /#panel-huyen-thoai -->"""
            
    if panel_target in index_html and 'article-cohen-panel' not in index_html:
        index_html = index_html.replace(panel_target, panel_html + "\n" + panel_target)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
            print("Successfully updated index.html")
    else:
        print("Target not found or already inserted in index.html")
        
    # 2. Update script.js
    with open('script.js', 'r', encoding='utf-8') as f:
        script = f.read()
        
    route1 = """        } else if (subPath === '/jim-simons') {
            openLegendArticle('jim-simons', updateUrl);"""
    route1_new = """        } else if (subPath === '/steven-cohen') {
            openLegendArticle('steven-cohen', updateUrl);
        } else if (subPath === '/jim-simons') {
            openLegendArticle('jim-simons', updateUrl);"""
            
    route2 = """    } else if (articleId === 'jim-simons') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-jimsimons-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'jim-simons' }, '', '/huyen-thoai/jim-simons');
        window.scrollTo({ top: 0, behavior: 'smooth' });"""
    route2_new = """    } else if (articleId === 'steven-cohen') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-cohen-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'steven-cohen' }, '', '/huyen-thoai/steven-cohen');
        window.scrollTo({ top: 0, behavior: 'smooth' });\n""" + route2
        
    if 'steven-cohen' not in script:
        script = script.replace(route1, route1_new)
        script = script.replace(route2, route2_new)
        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(script)
            print("Successfully updated script.js")
    else:
        print("script.js already contains steven-cohen")

if __name__ == '__main__':
    main()
