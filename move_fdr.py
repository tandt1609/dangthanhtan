import re
import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print("Error: Could not find index.html")
        sys.exit(1)

    # 1. Thay thế href trong trang chủ
    # Trang chủ card
    html = html.replace('href="/thu-vien/fdr-luoc-su"', 'href="/huyen-thoai/fdr-luoc-su"')

    # 2. Thay thế onclick trong article panel
    html = html.replace('onclick="openThuVienArticle(\'\')" style="background: transparent; border: 1px solid rgba(160,106,44,0.5); color: #a06a2c; padding: 7px 16px; cursor: pointer; font-family: \'Cormorant SC\', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px; font-weight: 600;">',
                        'onclick="openLegendArticle(\'\')" style="background: transparent; border: 1px solid rgba(160,106,44,0.5); color: #a06a2c; padding: 7px 16px; cursor: pointer; font-family: \'Cormorant SC\', serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px; font-weight: 600;">')

    # 3. Di chuyển panel từ thu-vien-article-view sang huyen-thoai-article-view
    # Mặc dù panel-fdr đang ở cuối thư viện, ta có thể cắt nó ra và nhét vào huyen-thoai-article-view
    panel_start = html.find('<div id="article-fdr-panel"')
    if panel_start != -1:
        # Tìm điểm kết thúc của panel này
        # Nó được đóng bởi </div> ngay trước <!-- PANEL 7: GAME --> hoặc tương tự
        # Tìm </div> tiếp theo mà sau đó là </div> đóng thu-vien-article-view... hơi khó bằng regex.
        # Ta biết nó chứa 2 nút Quay lại. Nút 2:
        btn2_idx = html.find('Quay lại danh sách', panel_start)
        btn2_idx = html.find('Quay lại danh sách', btn2_idx + 10)
        panel_end = html.find('</div>', btn2_idx)
        panel_end = html.find('</div>', panel_end + 6) + 6 # div đóng button wrapper, rồi div đóng article-fdr-panel
        
        panel_content = html[panel_start:panel_end]
        
        # Xóa khỏi vị trí cũ
        html = html[:panel_start] + html[panel_end:]
        
        # Chèn vào huyen-thoai-article-view
        huyen_thoai_end = html.find('<!-- END OF HUYỀN THOẠI ARTICLE VIEW -->')
        if huyen_thoai_end != -1:
            html = html[:huyen_thoai_end] + panel_content + '\n' + html[huyen_thoai_end:]
        else:
            huyen_thoai_end2 = html.find('</div><!-- /#huyen-thoai-article-view -->')
            if huyen_thoai_end2 != -1:
                html = html[:huyen_thoai_end2] + panel_content + '\n' + html[huyen_thoai_end2:]
    
    # 4. Chuyển card từ Thư Viện sang Huyền Thoại
    # Tìm thẻ chứa card trong thư viện
    card_start = html.find('<!-- Post: FDR Luoc Su (Thu Vien) -->')
    if card_start != -1:
        card_end = html.find('</a>', card_start) + 4
        card_content = html[card_start:card_end]
        
        # Xóa khỏi thư viện
        html = html[:card_start] + html[card_end:]
        
        # Chèn vào huyền thoại list view
        ht_list_start = html.find('<div id="huyen-thoai-list-view"')
        ht_news_list = html.find('<div class="news-list">', ht_list_start)
        if ht_news_list != -1:
            insert_pos = ht_news_list + len('<div class="news-list">')
            html = html[:insert_pos] + '\n' + card_content + html[insert_pos:]
            
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated index.html")

    # UPDATE SCRIPT.JS
    try:
        with open('script.js', 'r', encoding='utf-8') as f:
            script = f.read()
    except FileNotFoundError:
        print("Error: Could not find script.js")
        sys.exit(1)

    # A. Rút từ handleRouting thư viện
    route1_old = """        } else if (subPath === '/fdr-luoc-su') {
            openThuVienArticle('fdr-luoc-su', updateUrl);"""
    script = script.replace(route1_old, "")

    # B. Thêm vào handleRouting huyền thoại
    ht_route_target = "        if (subPath === '/mark-douglas') {\n            openLegendArticle('mark-douglas', updateUrl);\n        } else if (subPath === '/fabio-valentini') {"
    ht_route_new = """        if (subPath === '/fdr-luoc-su') {
            openLegendArticle('fdr-luoc-su', updateUrl);
        } else if (subPath === '/mark-douglas') {
            openLegendArticle('mark-douglas', updateUrl);
        } else if (subPath === '/fabio-valentini') {"""
    
    if ht_route_target in script:
        script = script.replace(ht_route_target, ht_route_new)
    else:
        # Fallback if mark-douglas isn't exact
        ht_route_fallback = "        if (subPath === '/fabio-valentini') {"
        ht_route_new_fallback = """        if (subPath === '/fdr-luoc-su') {
            openLegendArticle('fdr-luoc-su', updateUrl);
        } else if (subPath === '/fabio-valentini') {"""
        script = script.replace(ht_route_fallback, ht_route_new_fallback)

    # C. Rút từ openThuVienArticle
    handler_old = """    } else if (articleId === 'fdr-luoc-su') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-fdr-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'fdr-luoc-su' }, '', '/thu-vien/fdr-luoc-su');
        window.scrollTo({ top: 0, behavior: 'smooth' });"""
    script = script.replace(handler_old, "")

    # D. Thêm vào openLegendArticle
    ht_handler_target = """    if (articleId === 'mark-douglas') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-mark-douglas-panel');"""
    
    ht_handler_new = """    if (articleId === 'fdr-luoc-su') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-fdr-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'fdr-luoc-su' }, '', '/huyen-thoai/fdr-luoc-su');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'mark-douglas') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-mark-douglas-panel');"""
        
    if ht_handler_target in script:
        script = script.replace(ht_handler_target, ht_handler_new)
    else:
        ht_handler_fallback = """    if (articleId === 'fabio-valentini') {"""
        ht_handler_new_fallback = """    if (articleId === 'fdr-luoc-su') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-fdr-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'fdr-luoc-su' }, '', '/huyen-thoai/fdr-luoc-su');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'fabio-valentini') {"""
        script = script.replace(ht_handler_fallback, ht_handler_new_fallback)

    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print("Updated script.js")

if __name__ == '__main__':
    main()
