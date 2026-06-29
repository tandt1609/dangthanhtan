import re

def main():
    # 1. Read the empirical science file
    with open('../file for wed/empirical-science.html', 'r', encoding='utf-8') as f:
        html = f.read()

    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    # Modify CSS to be scoped
    lines = style_content.split('\n')
    scoped_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(':root'):
            scoped_lines.append(line.replace(':root', '#article-empirical-panel'))
        elif stripped.startswith('body') and '{' in stripped:
            scoped_lines.append(line.replace('body', '#article-empirical-panel'))
        elif stripped.startswith('html') and '{' in stripped:
            scoped_lines.append('/* html rule removed */')
        elif stripped.startswith('*, *::'):
            scoped_lines.append(line)
        else:
            scoped_lines.append(line)
    
    scoped_style_content = '\n'.join(scoped_lines)

    # Build the panel
    panel_html = f"""
<div id="article-empirical-panel" class="sukien-article-panel empirical-body">
    <style>
#article-empirical-panel {{
{scoped_style_content}
}}
    </style>
    <div style="padding: 14px 20px; background: #1a1a2e;">
        <button onclick="openThuVienArticle('')" style="background: transparent; border: 1px solid rgba(255,255,255,0.5); color: #fff; padding: 7px 16px; cursor: pointer; font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
            &#8592; Quay lại Thư viện
        </button>
    </div>
    {body_content}
    <div style="padding: 20px 20px 30px; text-align: center; background: #fffdf7;">
        <button onclick="openThuVienArticle('')" style="background: transparent; border: 1px solid rgba(26,26,46,0.3); color: #1a1a2e; padding: 7px 16px; cursor: pointer; font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
            &#8592; Quay lại Thư viện
        </button>
    </div>
</div>
"""

    card_html = """
                        <a href="/thu-vien/khoa-hoc-thuc-nghiem" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-flask"></i> Khoa học & Thực nghiệm</span>
                                <span class="news-time">Tháng 6, 2026</span>
                            </div>
                            <h3 class="news-heading">Khoa Học Thực Nghiệm — Ánh Sáng Giữa Đống Hỗn Độn</h3>
                            <p class="news-excerpt">Khi nhân loại quyết định ngừng tin vào ông trời và bắt đầu đo đạc mọi thứ — thế giới thay đổi mãi mãi.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc tài liệu</span>
                            </div>
                        </a>
"""

    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Insert card into the list view
    if card_html not in index_content:
        list_marker = '<div id="thu-vien-list-view" class="sukien-view active">\n                    <div class="news-list">'
        if list_marker in index_content:
            index_content = index_content.replace(list_marker, list_marker + card_html)
            print("Card injected.")
        else:
            print("Card marker not found.")
    
    # Insert panel into the article view
    if 'id="article-empirical-panel"' not in index_content:
        panel_marker = '<div id="thu-vien-article-view" class="sukien-view">'
        if panel_marker in index_content:
            index_content = index_content.replace(panel_marker, panel_marker + '\n' + panel_html)
            print("Panel injected.")
        else:
            print("Panel marker not found.")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)

    # 2. Update script.js
    with open('script.js', 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    if "openThuVienArticle('khoa-hoc-thuc-nghiem'" not in script_content:
        # Add to popstate event listener
        js_marker1 = "openThuVienArticle('dai-bang-tai-sinh', updateUrl);"
        js_insert1 = "            openThuVienArticle('khoa-hoc-thuc-nghiem', updateUrl);\n"
        script_content = script_content.replace(js_marker1, js_insert1 + js_marker1)
        
        # Add to openThuVienArticle function
        js_marker2 = "document.getElementById('article-phathoc-panel').style.display = 'none';"
        js_insert2 = "    const empiricalPanel = document.getElementById('article-empirical-panel');\n    if(empiricalPanel) empiricalPanel.style.display = 'none';\n"
        script_content = script_content.replace(js_marker2, js_marker2 + '\n' + js_insert2)
        
        js_marker3 = "document.getElementById('article-phathoc-panel').style.display = 'block';"
        js_insert3 = """
        } else if (articleId === 'khoa-hoc-thuc-nghiem') {
            const panel = document.getElementById('article-empirical-panel');
            if (panel) panel.style.display = 'block';
            if (updateUrl) history.pushState({ tab: 'thu-vien', article: 'khoa-hoc-thuc-nghiem' }, '', '/thu-vien/khoa-hoc-thuc-nghiem');
"""
        script_content = script_content.replace(js_marker3, js_marker3 + js_insert3)
        print("script.js updated.")

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script_content)

if __name__ == '__main__':
    main()
