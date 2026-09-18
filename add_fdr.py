import re
import sys

def process_html():
    file_path = '../file for wed/FDR_Luoc_Su.html'
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
    style_content = style_content.replace(':root', '#article-fdr-panel')
    style_content = re.sub(r'\bbody\s*\{', '#article-fdr-panel.fdr-body {', style_content)
    style_content = re.sub(r'\bhtml\s*\{', '#article-fdr-panel.fdr-html {', style_content)

    scoped_style = f"""<style>
#article-fdr-panel {{
{style_content}
}}
</style>"""

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    panel_html = f"""
<div id="article-fdr-panel" class="sukien-article-panel fdr-body">
    {scoped_style}
    <div style="padding: 16px 20px; background: #f3e8d5;">
        <button onclick="openThuVienArticle('')" style="background: transparent; border: 1px solid rgba(160,106,44,0.5); color: #a06a2c; padding: 7px 16px; cursor: pointer; font-family: 'Cormorant SC', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px; font-weight: 600;">
            &#8592; Quay lại danh sách
        </button>
    </div>
    {body_content}
    <div style="padding: 20px; text-align: center; background: #f3e8d5;">
        <button onclick="openThuVienArticle('')" style="background: transparent; border: 1px solid rgba(160,106,44,0.5); color: #a06a2c; padding: 7px 16px; cursor: pointer; font-family: 'Cormorant SC', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px; font-weight: 600;">
            &#8592; Quay lại danh sách
        </button>
    </div>
</div>
"""
    return panel_html


def make_card(href_prefix):
    """Tạo news card HTML cho FDR"""
    return f"""<a href="{href_prefix}/fdr-luoc-su" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-landmark"></i> Lịch sử & Chính trị</span>
                                <span class="news-time">Tháng 9, 2026</span>
                            </div>
                            <h3 class="news-heading">Franklin D. Roosevelt — Người Đàn Ông Không Chân Nhưng Đứng Vững Hơn Cả Nước Mỹ</h3>
                            <p class="news-excerpt">Cậu ấm không biết buộc dây giày, lớn lên thành tổng thống bốn nhiệm kỳ — dẫn dắt nước Mỹ vượt Đại Suy thoái và Thế chiến II bằng đôi chân liệt nhưng ý chí thép.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
"""


def main():
    panel_html = process_html()

    # 1. Update index.html
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            index_html = f.read()
    except FileNotFoundError:
        print("Error: Could not find index.html")
        sys.exit(1)

    if 'article-fdr-panel' in index_html:
        print("Panel already exists in index.html")
    else:
        # ── A. Thêm card vào TRANG CHỦ ──────────────────────────────────────
        # Chèn trước card đầu tiên trong panel-trang-chu
        trangchu_target = '<div id="panel-trang-chu" class="tab-panel active">'
        trangchu_news_list = '<div class="news-list">'

        trangchu_start = index_html.find(trangchu_target)
        if trangchu_start != -1:
            news_list_start = index_html.find(trangchu_news_list, trangchu_start)
            if news_list_start != -1:
                # Chèn card FDR ngay sau thẻ <div class="news-list"> đầu tiên của trang chủ
                insert_pos = news_list_start + len(trangchu_news_list)
                fdr_card_home = '\n                        <!-- Post: FDR (Thu Vien) -->\n                        ' + make_card('/thu-vien')
                index_html = index_html[:insert_pos] + fdr_card_home + index_html[insert_pos:]
                print("Added FDR card to trang-chu")
            else:
                print("Warning: Could not find news-list in panel-trang-chu")
        else:
            print("Warning: Could not find panel-trang-chu")

        # ── B. Thêm card vào THƯ VIỆN list-view ─────────────────────────────
        thu_vien_list_target = '<div id="thu-vien-list-view" class="sukien-view active">'
        tv_news_list = '<div class="news-list">'

        tv_start = index_html.find(thu_vien_list_target)
        if tv_start != -1:
            tv_news_list_start = index_html.find(tv_news_list, tv_start)
            if tv_news_list_start != -1:
                insert_pos2 = tv_news_list_start + len(tv_news_list)
                fdr_card_tv = '\n                        <!-- Post: FDR Luoc Su (Thu Vien) -->\n                        ' + make_card('/thu-vien')
                index_html = index_html[:insert_pos2] + fdr_card_tv + index_html[insert_pos2:]
                print("Added FDR card to thu-vien list-view")
            else:
                print("Warning: Could not find news-list in thu-vien-list-view")
        else:
            print("Warning: Could not find thu-vien-list-view")

        # ── C. Chèn article panel vào thu-vien-article-view ──────────────────
        # Anchor: panel-game luôn đứng ngay sau phần kết thúc panel-thu-vien
        game_anchor = '<!-- PANEL 7: GAME -->'
        game_pos = index_html.find(game_anchor)
        if game_pos != -1:
            # Lùi về trước để tìm dòng </div> đóng thu-vien-article-view
            # Cấu trúc: </div>\n             </div>\n\n             <!-- PANEL 7: GAME -->
            insert_pos = index_html.rfind('\n', 0, game_pos)  # cuối dòng trước game_anchor
            insert_pos = index_html.rfind('\n', 0, insert_pos)  # lên thêm một dòng
            index_html = index_html[:insert_pos] + '\n' + panel_html + index_html[insert_pos:]
            print("Inserted FDR panel into thu-vien-article-view (game anchor)")
        else:
            print("Error: Could not find '<!-- PANEL 7: GAME -->' anchor")
            sys.exit(1)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
        print("Successfully updated index.html")

    # 2. Update script.js
    try:
        with open('script.js', 'r', encoding='utf-8') as f:
            script = f.read()
    except FileNotFoundError:
        print("Error: Could not find script.js")
        sys.exit(1)

    if '/fdr-luoc-su' in script:
        print("script.js already has FDR routing")
        return

    # ── Thêm route trong handleRouting ───────────────────────────────────────
    route1_target = "        } else {\n            openThuVienArticle('', updateUrl);\n        }\n    } else if (path.startsWith('/vi-mo'))"
    route1_new = """        } else if (subPath === '/fdr-luoc-su') {
            openThuVienArticle('fdr-luoc-su', updateUrl);
        } else {
            openThuVienArticle('', updateUrl);
        }
    } else if (path.startsWith('/vi-mo'))"""

    if route1_target in script:
        script = script.replace(route1_target, route1_new)
        print("Added route in handleRouting")
    else:
        # fallback: chèn trước } else { ... openThuVienArticle('', updateUrl)
        fallback1 = "        } else {\r\n            openThuVienArticle('', updateUrl);\r\n        }\r\n    } else if (path.startsWith('/vi-mo'))"
        fallback1_new = """        } else if (subPath === '/fdr-luoc-su') {
            openThuVienArticle('fdr-luoc-su', updateUrl);
        } else {
            openThuVienArticle('', updateUrl);
        }
    } else if (path.startsWith('/vi-mo'))"""
        if fallback1 in script:
            script = script.replace(fallback1, fallback1_new)
            print("Added route in handleRouting (CRLF fallback)")
        else:
            print("Warning: Could not find routing target, trying last resort")
            # last resort: chèn trước dòng "} else {" trong khối thu-vien
            old_snoopy = "        } else if (subPath === '/snoopy') {\n            openThuVienArticle('snoopy', updateUrl);\n        } else {"
            new_snoopy = """        } else if (subPath === '/snoopy') {
            openThuVienArticle('snoopy', updateUrl);
        } else if (subPath === '/fdr-luoc-su') {
            openThuVienArticle('fdr-luoc-su', updateUrl);
        } else {"""
            if old_snoopy in script:
                script = script.replace(old_snoopy, new_snoopy)
                print("Added route in handleRouting (snoopy anchor)")

    # ── Thêm handler trong openThuVienArticle ────────────────────────────────
    route2_target = "    } else {\n        articleView.classList.remove('active');\n        listView.classList.add('active');\n        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: '' }, '', '/thu-vien');\n    }\n}"
    route2_new = """    } else if (articleId === 'fdr-luoc-su') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-fdr-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'fdr-luoc-su' }, '', '/thu-vien/fdr-luoc-su');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        articleView.classList.remove('active');
        listView.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: '' }, '', '/thu-vien');
    }
}"""

    if route2_target in script:
        script = script.replace(route2_target, route2_new)
        print("Added FDR handler in openThuVienArticle")
    else:
        # CRLF fallback
        fallback2 = "    } else {\r\n        articleView.classList.remove('active');\r\n        listView.classList.add('active');\r\n        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: '' }, '', '/thu-vien');\r\n    }\r\n}"
        fallback2_new = """    } else if (articleId === 'fdr-luoc-su') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-fdr-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'fdr-luoc-su' }, '', '/thu-vien/fdr-luoc-su');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        articleView.classList.remove('active');
        listView.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: '' }, '', '/thu-vien');
    }
}"""
        if fallback2 in script:
            script = script.replace(fallback2, fallback2_new)
            print("Added FDR handler in openThuVienArticle (CRLF fallback)")
        else:
            # anchor on snoopy handler
            old_snoopy_handler = "    } else if (articleId === 'snoopy') {\n        listView.classList.remove('active');\n        articleView.classList.add('active');\n        const panel = document.getElementById('article-snoopy-panel');\n        if (panel) panel.classList.add('active');\n        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'snoopy' }, '', '/thu-vien/snoopy');\n        window.scrollTo({ top: 0, behavior: 'smooth' });\n    } else {"
            new_snoopy_handler = """    } else if (articleId === 'snoopy') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-snoopy-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'snoopy' }, '', '/thu-vien/snoopy');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'fdr-luoc-su') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-fdr-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'fdr-luoc-su' }, '', '/thu-vien/fdr-luoc-su');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {"""
            if old_snoopy_handler in script:
                script = script.replace(old_snoopy_handler, new_snoopy_handler)
                print("Added FDR handler (snoopy anchor)")
            else:
                print("Warning: Could not find snoopy handler anchor either")

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print("Successfully updated script.js")

    # 3. Thêm font Cormorant SC vào index.html nếu chưa có
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    font_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;600&display=swap" rel="stylesheet" />'

    if 'Cormorant+SC' not in index_html:
        head_end = index_html.find('</head>')
        if head_end != -1:
            index_html = index_html[:head_end] + "    " + font_link + "\n" + index_html[head_end:]
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(index_html)
            print("Added Cormorant SC font to index.html")
    else:
        print("Cormorant SC font already present")


if __name__ == '__main__':
    main()
