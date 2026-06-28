import re

def main():
    # 1. Update script.js
    with open('script.js', 'r', encoding='utf-8') as f:
        script_content = f.read()
        
    route1 = """        } else if (subPath === '/luoc-su-kinh-dich') {
            openThuVienArticle('luoc-su-kinh-dich', updateUrl);"""
    route1_new = """        } else if (subPath === '/luoc-su-kinh-dich') {
            openThuVienArticle('luoc-su-kinh-dich', updateUrl);
        } else if (subPath === '/luoc-su-tu-vi') {
            openThuVienArticle('luoc-su-tu-vi', updateUrl);"""
            
    route2 = """    } else if (articleId === 'luoc-su-kinh-dich') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-kinhdich-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'luoc-su-kinh-dich' }, '', '/thu-vien/luoc-su-kinh-dich');
        window.scrollTo({ top: 0, behavior: 'smooth' });"""
    route2_new = route2 + """
    } else if (articleId === 'luoc-su-tu-vi') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-tuvi-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'thu-vien', articleId: 'luoc-su-tu-vi' }, '', '/thu-vien/luoc-su-tu-vi');
        window.scrollTo({ top: 0, behavior: 'smooth' });"""

    if 'luoc-su-tu-vi' not in script_content:
        script_content = script_content.replace(route1, route1_new)
        script_content = script_content.replace(route2, route2_new)
        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(script_content)

    # 2. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    card_target = """                    <div class="news-list">
                        <a href="/thu-vien/luoc-su-kinh-dich" class="news-card clickable-card">"""
    
    card_new = """                    <div class="news-list">
                        <a href="/thu-vien/luoc-su-tu-vi" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-star"></i> Chiêm tinh & Mệnh lý</span>
                                <span class="news-time">Tháng 6, 2026</span>
                            </div>
                            <h3 class="news-heading">Lược Sử Tử Vi Đẩu Số: Nguồn Gốc, Triết Lý & Ứng Dụng</h3>
                            <p class="news-excerpt">Từ nguồn gốc – quá trình phát triển – triết lý cốt lõi đến ý nghĩa và cách áp dụng trong đời sống hiện đại.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc tài liệu</span>
                            </div>
                        </a>

                        <a href="/thu-vien/luoc-su-kinh-dich" class="news-card clickable-card">"""

    panel_html = """
<div id="article-tuvi-panel" class="sukien-article-panel">
    <div class="article-phathoc">
        <button class="back-btn" onclick="openThuVienArticle('')">
            <i class="fa-solid fa-arrow-left"></i> Quay lại Thư viện
        </button>
        
        <div class="ph-header">
            <div class="ph-dharma-wheel"><i class="fa-solid fa-star"></i></div>
            <h1>LƯỢC SỬ TỬ VI ĐẨU SỐ</h1>
            <p class="subtitle">Từ nguồn gốc – quá trình phát triển – triết lý cốt lõi đến ý nghĩa và cách áp dụng trong đời sống</p>
            <div class="ph-quote">"Tử Vi không định đoạt số phận. Nó là tấm bản đồ giúp con người thấu hiểu chính mình, từ đó chọn hướng đi phù hợp giữa muôn nẻo cuộc đời."</div>
            <p>Tổng hợp từ nhiều nguồn chính thống<br>Tài liệu nghiên cứu – Tham khảo cá nhân</p>
        </div>
        
        <div class="ph-content">
            <h2>LỜI MỞ ĐẦU</h2>
            <p>Tử Vi Đẩu Số là một trong những di sản tinh thần quý giá bậc nhất của văn hóa phương Đông. Trải qua hơn một nghìn năm hình thành và phát triển, từ vùng Hoa Hạ cổ đại cho đến những cuộc bàn luận sôi nổi trên các diễn đàn đương đại, Tử Vi đã chứng tỏ sức sống mãnh liệt và giá trị thực tiễn không ngừng được khai thác. Đây không đơn thuần là một môn bói toán hay tiên đoán vận mệnh, mà là một hệ thống tri thức tổng hòa giữa thiên văn học, triết học, tâm lý học và đạo đức học cổ đại.</p>
            <p>Tài liệu này được biên soạn nhằm cung cấp một cái nhìn toàn cảnh, có hệ thống về Tử Vi: từ nguồn gốc lịch sử, quá trình phát triển qua các thời kỳ, những triết lý nền tảng, cho đến ý nghĩa và cách thức ứng dụng thiết thực trong đời sống hôm nay. Nội dung được tổng hợp từ các nguồn chính thống — bao gồm các bộ kinh điển như Tử Vi Đẩu Số Toàn Thư của Hi Di Trần Đoàn, các nghiên cứu của Vũ Tài Lục, Nguyễn Mạnh Bảo, các học giả Việt Nam như Nguyễn Bỉnh Khiêm, Lê Quý Đôn, cùng nhiều công trình hiện đại — với tinh thần trân trọng cội nguồn nhưng cũng giữ thái độ phê phán và lý tính.</p>
            <p>Người viết tin rằng Tử Vi, khi được tiếp cận đúng đắn, không phải là tấm bùa định mệnh khiến con người bị động chấp nhận số phận, mà là tấm gương soi giúp mỗi cá nhân hiểu rõ tính cách, tiềm năng, thử thách và nhịp điệu thời vận của bản thân — từ đó chủ động định hướng cuộc đời theo chiều kích sâu sắc hơn, có ý thức hơn.</p>
            
            <h2>PHẦN I. NGUỒN GỐC VÀ SỰ RA ĐỜI CỦA TỬ VI</h2>
            <h3>1. Khái niệm và ý nghĩa tên gọi</h3>
            <p><strong>Tử Vi Đẩu Số (紫微斗數)</strong> là một hệ thống dự trắc về vận mệnh con người được xây dựng trên cơ sở triết lý Kinh Dịch, kết hợp các học thuyết Âm Dương, Ngũ Hành và Thiên Can – Địa Chi. Người xem lập một <strong>lá số</strong> dựa trên giờ, ngày, tháng, năm sinh theo âm lịch và giới tính, sau đó căn cứ vào vị trí các sao trong 12 cung để luận giải về tính cách, sự nghiệp, hôn nhân, sức khỏe, tài lộc và những biến cố lớn trong đời người.</p>
            <p>Về tên gọi, có hai cách giải thích phổ biến và đều có cơ sở:</p>
            <ul>
                <li><strong>Cách thứ nhất:</strong> "Tử" nghĩa là màu tím, "Vi" là loài hoa tường vi. Hoa tử vi (tường vi tím) từ ngàn xưa được các nhà chiêm tinh, tướng số phương Đông dùng làm vật chiêm bốc. Có giai thoại kể rằng Quỷ Cốc tiên sinh từng dùng cành hoa tử vi để đoán trước vận mệnh hai học trò Tôn Tẫn và Bàng Quyên khi họ xuống núi.</li>
                <li><strong>Cách thứ hai:</strong> "Tử Vi" là tên một ngôi sao quan trọng nhất trong khoa này — sao Đế tinh, đứng đầu trong 14 chính tinh. Các nhà nghiên cứu hiện đại nghiêng về cách giải thích này, vì toàn bộ hệ thống xoay quanh việc an định và luận giải vị trí của các sao.</li>
            </ul>
            <p>Còn "Đẩu Số" có nghĩa là phép tính các vì sao trong chòm Bắc Đẩu và Nam Đẩu. Như vậy, "Tử Vi Đẩu Số" có thể hiểu là "phép tính vận mệnh dựa trên ngôi sao Tử Vi và các sao thuộc Bắc Nam đẩu".</p>
            
            <h3>2. Bối cảnh lịch sử ra đời</h3>
            <p>Sử sách Trung Hoa cổ đại không ghi chính thức ai là người khai sáng ra Tử Vi, vì theo quy định của chế độ phong kiến tập quyền, các môn thuộc "tạp thư" — bao gồm Tử Vi, Địa Lý, Nhâm Độn, Bói Dịch — không được đưa vào chính sử. Tuy nhiên, qua các thư tịch lưu truyền và dã sử, giới nghiên cứu thừa nhận rằng Tử Vi không phải đột nhiên xuất hiện, mà là kết tinh của một dòng tri thức lâu đời.</p>
            <p>Trước khi Tử Vi được hệ thống hóa, các nhà thiên văn và mệnh lý cổ đại đã tích lũy nhiều quan sát về sự vận hành của tinh tú và mối tương quan với vận mệnh con người. Các bộ phận tri thức nền tảng bao gồm:</p>
            <ul>
                <li><strong>Dịch lý</strong> — học thuyết về biến hóa của vũ trụ, lấy 64 quẻ làm khung tham chiếu, là nền tảng triết học gốc rễ;</li>
                <li><strong>Thiên văn học</strong> — quan sát chuyển động của các vì sao và quy luật tuần hoàn của nhật nguyệt;</li>
                <li><strong>Hình tượng học</strong> — nghiên cứu hình dáng vũ trụ, con người, thú vật;</li>
                <li><strong>Lịch số</strong> — tính toán ngày, tháng, năm và chu kỳ tuần hoàn;</li>
                <li><strong>Địa lý (Phong Thủy)</strong> — nghiên cứu tương ứng giữa con người với địa khí, phương hướng, môi trường sống.</li>
            </ul>
            <p>Tất cả các khoa này đều có liên hệ mật thiết với số mệnh nhân sinh, và việc tổng hợp chúng thành một hệ thống nhất quán là công lao lịch sử của Hi Di Trần Đoàn vào cuối thời Đường, đầu thời Tống — giai đoạn chuyển tiếp từ loạn lạc sang thái bình.</p>
            
            <h3>3. Hi Di Trần Đoàn — Lão tổ của khoa Tử Vi</h3>
            <p>Hi Di Trần Đoàn (陳摶), còn được tôn xưng là <strong>Trần Đoàn lão tổ</strong> hay <strong>Hi Di lão tổ</strong>, là vị đạo sĩ lỗi lạc bậc nhất trong lịch sử Đạo giáo Trung Hoa. Theo bộ <em>Triệu thị Minh thuyết Tử Vi kinh</em>, ông sinh khoảng năm 888–893 (cuối đời Đường Hy Tông đến Đường Chiêu Tông) tại Chân Nguyên, Hào Châu, và mất vào thời Tống — tương truyền thọ 118 tuổi.</p>
            <p>Truyền thuyết kể rằng khi mới sinh, Trần Đoàn không thể nói được. Đến năm bốn tuổi, ông gặp một bà lão áo xanh bên dòng nước xoáy, được bà cho bú, từ đó mở miệng nói và càng lớn càng thông tuệ phi thường — đọc kinh sử bách gia một lần là thuộc. Cha ông là một nhà thiên văn lịch số đại tài, đã sớm phát hiện thiên tư của con và truyền dạy thiên văn từ năm tám tuổi.</p>
            <p><strong>Giai thoại nổi tiếng nhất</strong> về Trần Đoàn là việc ông dùng thiên văn và Tử Vi đoán trước hai đứa trẻ ăn xin sẽ làm vua. Một ngày, ông cùng đệ tử lên núi xem thiên văn, chợt thấy sao Tử Vi và Thiên Phủ đi vào địa phận sao Phá Quân và Hóa Kỵ, ánh sáng chiếu xuống núi Hoa Sơn. Hôm sau, gặp một thiếu phụ gánh hai đứa trẻ chạy loạn, ông hỏi giờ sinh và lập số, nhận ra đây chính là hai chân long thiên tử tương lai — đó chính là <strong>Triệu Khuông Dẫn</strong> (Tống Thái Tổ) và <strong>Triệu Khuông Nghĩa</strong> (Tống Thái Tông), những người sau này thống nhất thiên hạ, lập nên triều Tống.</p>
            <p>Khi Tống Thái Tổ lên ngôi và mời Trần Đoàn ra làm quan, ông từ chối, xin về tu ẩn ở <strong>núi Hoa Sơn</strong> tỉnh Thiểm Tây — ngọn núi được mệnh danh là "kỳ hiểm thiên hạ đệ nhất sơn". Tại đây, ông tổng hợp tinh hoa các khoa Dịch lý, Thiên văn, Hình tượng, Lịch số, Địa lý và viết nên bộ <em>Tử Vi kinh</em> (còn gọi là <em>Tử Vi Chính Nghĩa</em>) dâng lên Tống Thái Tổ.</p>
            <div class="ph-quote-block" style="background:#f9f9f9; padding:15px; border-left:4px solid #8b3a1a; margin-bottom:20px; font-style:italic;">
                Trong lời tựa, Trần Đoàn khiêm nhường tự nhận:<br>
                "Bần đạo không phải là người đặt ra khoa này. Nhân người trước đã nói về Tử Vi, bần đạo nhận thấy Dịch lý, Hình tượng, Thiên văn, Lịch số, Địa lý đều có uyên nguyên với nhau, mới tước bỏ những rườm rà của người xưa, họp thành khoa Tử Vi."
            </div>
            <p>Lời tự thuật này cho thấy Trần Đoàn không xem mình là người sáng lập, mà là người <strong>tổng hợp và hệ thống hóa</strong> — biến những mảnh tri thức rời rạc thành một khoa học có cấu trúc rõ ràng. Đây cũng là điểm khiến Tử Vi được tôn trọng như một di sản tập thể của trí tuệ Đông phương.</p>
            
            <h3>4. Bộ Tử Vi Đẩu Số Toàn Thư</h3>
            <p><strong>Tử Vi Đẩu Số Toàn Thư (紫微斗數全書)</strong> là bộ sách kinh điển nhất, được coi là "chính thư" của khoa Tử Vi. Tác giả gốc là Hi Di Trần Đoàn, sau được tiến sĩ <strong>La Hồng Tiên</strong> đời Minh (niên hiệu Gia Tĩnh, vua Minh Thế Tông) biên soạn lại, chỉnh lý và phổ biến rộng rãi.</p>
            <p>Theo lời tựa của La Hồng Tiên: <em>"Tôi vì muốn biết về số mệnh nên đã đến tận núi Hoa Sơn, chỗ ông Hi Di Trần Đoàn đắc đạo, để chiêm bái nơi thờ tự bậc đại hiền. Lúc ra về, có một vị cao niên thái độ ung dung đưa cho tôi cuốn sách và bảo: 'Đây là Tử Vi Đẩu Số tập của Hi Di tiên sinh.'"</em> Câu chuyện mang màu sắc huyền thoại, nhưng nó cho thấy giá trị tinh thần mà người xưa gán cho bộ sách này.</p>
            <p>Ngoài bộ Toàn Thư, các thư tịch Tử Vi quan trọng khác bao gồm:</p>
            <ul>
                <li><em>Tử Vi Chính Nghĩa</em> — bản truyền cho Tống Thái Tổ Triệu Khuông Dẫn;</li>
                <li><em>Triệu thị Minh Thuyết Tử Vi Kinh</em> — do Cẩm Chướng thư cục Thượng Hải ấn hành năm 1921;</li>
                <li><em>Tử Vi Thiển Thuyết</em> — bộ tổng luận do Lưu Bá Ôn (đại thần khai quốc nhà Minh) biên soạn;</li>
                <li><em>Lịch Số Tử Vi Toàn Thư</em> — do Hứa Quang Chi đời Minh biên soạn;</li>
                <li><em>Tử Vi Đẩu Số Toàn Thư bản Nam Tông</em> — do Ma Y biên soạn đời Tống, sau được các Tử Vi gia phái Nam bổ túc, khắc bản in vào thời Thanh Khang Hy.</li>
            </ul>
            
            <h2>PHẦN II. QUÁ TRÌNH PHÁT TRIỂN</h2>
            <h3>1. Tại Trung Hoa qua các triều đại</h3>
            <p>Sau khi Hi Di Trần Đoàn dâng <em>Tử Vi kinh</em> lên Tống Thái Tổ, môn này ban đầu chỉ lưu truyền trong hoàng thất. Vì vua Tống họ Triệu nên giai đoạn này còn được gọi là <strong>phái Triệu gia</strong> — phái thừa hưởng trực tiếp và nguyên gốc từ tổ sư Hi Di. Theo <em>Triệu thị Minh Thuyết Tử Vi Kinh</em>, vua chúa và đại thần học Tử Vi để "biết kẻ trung người nịnh mà phân biệt dùng người".</p>
            <p>Qua các triều Tống – Nguyên – Minh – Thanh, Tử Vi được bổ sung và phân hóa thành nhiều phái khác nhau. Đến đời Minh, La Hồng Tiên hệ thống lại thành <em>Tử Vi Đẩu Số Toàn Thư</em>; Lưu Bá Ôn — vị quân sư khai quốc — viết <em>Tử Vi Thiển Thuyết</em>; Hứa Quang Chi soạn <em>Lịch Số Tử Vi Toàn Thư</em>. Ở phương Nam, phái <strong>Nam Tông</strong> hình thành với phong cách luận giải riêng, bổ sung và hiệu đính bộ sách của Ma Y.</p>
            <p>Đáng chú ý, dù xuất phát từ Trung Hoa, Tử Vi không phải là môn dự trắc nổi bật nhất ở quê hương của nó. Trong nền văn hóa thuật số Trung Hoa, các môn như Bát Tự (Tứ Trụ), Kỳ Môn Độn Giáp, Thái Ất, Lục Nhâm thường được giới học giả coi trọng hơn. Phải đến khi du nhập vào Việt Nam, Tử Vi mới thực sự được nâng tầm thành môn học hàng đầu trong kho tàng huyền học Đông phương.</p>
            
            <h3>2. Du nhập và phát triển tại Việt Nam</h3>
            <h4>a. Thời nhà Trần — phái Đông A</h4>
            <p>Tử Vi du nhập Việt Nam vào thời nhà Trần thông qua một sự kiện lịch sử đặc biệt. <strong>Hoàng Bính</strong>, một viên quan nhà Tống, dự đoán được vận nước Tống sẽ rơi vào tay quân Mông Cổ, đã bỏ sang Đại Việt xin cư ngụ và làm tôi cho nhà Trần. Ông mang theo hai bộ tài liệu vô cùng quý giá: <em>Triệu thị Minh Thuyết Tử Vi Kinh</em> và <em>Tử Vi Tinh Nghĩa</em>.</p>
            <p>Trên cơ sở hai bộ này, hoàng tộc nhà Trần biên soạn thêm và cho ra đời bộ <em>Đông A Di Sự</em> — không hẳn là sách nghiên cứu Tử Vi, mà là tập chép các học thuyết đời Trần, trong đó có phần về Tử Vi. Bộ sách này được ba người liên tiếp ghi chép: <strong>Huệ Túc phu nhân</strong> (vợ vua Trần Thái Tông), <strong>Đoàn Nhữ Hài</strong> (vị tể tướng đời Trần, học trò của Huệ Túc), và <strong>Trần Nguyên Đán</strong>. Từ đây, <strong>phái Tử Vi Đông A</strong> ra đời. Tên gọi Đông A xuất phát từ việc chữ "Trần" (陳) ghép từ chữ Đông (東) và chữ A (阿) — nên họ Trần còn được gọi là họ Đông A, gắn liền với "hào khí Đông A" của thời đại oanh liệt ấy.</p>
            
            <h4>b. Thời Lê – Trịnh — Trạng Trình Nguyễn Bỉnh Khiêm</h4>
            <p>Đầu thời Lê – Trịnh, <strong>Trạng Trình Nguyễn Bỉnh Khiêm</strong> (1491–1585) — học giả nổi tiếng "trên thông thiên văn, dưới tường địa lý" — đã có những đóng góp quan trọng cho việc nghiên cứu Tử Vi tại Việt Nam. Ông được biết đến với khả năng tiên đoán phi thường, để lại bộ <em>Sấm Trạng Trình</em> nổi tiếng. Ông từng đưa ra những lời khuyên có tầm chiến lược cho các thế lực lớn — khuyên Trịnh Kiểm "giữ chùa thờ Phật thì ăn oản" (làm thực quyền sau lưng vua Lê) và khuyên Nguyễn Hoàng "Hoành Sơn nhất đái, vạn đại dung thân" — định hình cục diện Đàng Trong Đàng Ngoài kéo dài hơn hai thế kỷ.</p>
            <p>Đáng tiếc, các trước tác về Tử Vi của Nguyễn Bỉnh Khiêm phần lớn bị thất lạc, không còn lưu giữ được nguyên vẹn. Nhưng ảnh hưởng của ông đã đặt nền móng cho truyền thống Tử Vi Việt Nam mang đậm tính ứng dụng và gắn với vận nước.</p>
            
            <h4>c. Cuối thời Lê – đầu thời Tây Sơn — Lê Quý Đôn</h4>
            <p><strong>Lê Quý Đôn</strong> (1726–1784) — bác học hàng đầu của Việt Nam — đã nâng Tử Vi lên một tầm cao mới. Ông để lại hai công trình vĩ đại còn lưu truyền đến nay:</p>
            <ul>
                <li><em>Thần Khê Định Số</em> — bộ phú văn vần luận giải rất tinh tế các cách cục Tử Vi, đặc biệt là quan hệ giữa tướng mạo và sao trên lá số. Câu phú nổi tiếng: <em>"Sát Phá Liêm Tham — người nào Sát, Phá, Liêm, Tham, phải uy nghi, phải hiên ngang mới hùng"</em> cho thấy Lê Quý Đôn nhấn mạnh <strong>tướng mệnh phải phù hợp mới ăn được sao</strong> — một quan điểm rất sâu sắc về sự thống nhất giữa hình và khí.</li>
                <li><em>Phú Tử Vi của Lê Quý Đôn</em> — tập hợp các câu phú nôm bổ túc cho Tử Vi Đẩu Số Toàn Thư.</li>
            </ul>
            
            <h4>d. Thời cận – hiện đại</h4>
            <p>Trong thế kỷ XX, Tử Vi tiếp tục được nghiên cứu và phổ biến rộng rãi. Các tên tuổi lớn bao gồm: <strong>Vũ Tài Lục</strong> (dịch giả của <em>Tử Vi Đẩu Số Toàn Thư</em> từ bản Đài Loan, có những bình chú sâu sắc), <strong>Nguyễn Mạnh Bảo</strong> (tác giả <em>Tử Vi Đẩu Số</em>), <strong>Thiên Lương</strong> — vị thầy có ảnh hưởng lớn ở miền Nam trước 1975 với học phái mang tên ông.</p>
            <p>Đến đầu thế kỷ XXI, Tử Vi bùng nổ trên Internet với nhiều diễn đàn nổi tiếng (tuvilyso.org, lyso.vn), các phần mềm an sao tự động, các kênh YouTube giảng dạy. Tử Vi cũng đi vào học thuật chính quy: tiến sĩ triết học <strong>Mai K. Đa</strong> đã giảng dạy môn "Triết học phương Đông ứng dụng — Tử Vi" như một bộ môn nghiêm túc về tri thức Đông phương.</p>
            
            <h4>đ. Những khác biệt giữa Tử Vi Việt Nam và Trung Hoa</h4>
            <p>Sau quá trình tiếp thu và phát triển độc lập, Tử Vi Việt Nam đã hình thành những đặc điểm riêng biệt so với Tử Vi nguyên thủy của Trung Hoa:</p>
            <table style="width:100%; border-collapse:collapse; margin-bottom:20px;">
                <thead>
                    <tr style="background:#8b3a1a; color:white;">
                        <th style="padding:10px; border:1px solid #ddd;">Tiêu chí</th>
                        <th style="padding:10px; border:1px solid #ddd;">Tử Vi Trung Hoa</th>
                        <th style="padding:10px; border:1px solid #ddd;">Tử Vi Việt Nam</th>
                    </tr>
                </thead>
                <tbody style="text-align:left;">
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold;">Khởi cung an Mệnh</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắt đầu từ cung Sửu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắt đầu từ cung Dần</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold;">Cách tính tuế hạn</td>
                        <td style="padding:10px; border:1px solid #ddd;">Cố định</td>
                        <td style="padding:10px; border:1px solid #ddd;">Tùy thuộc cầm tinh của người xem</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold;">Sao Thiên Không</td>
                        <td style="padding:10px; border:1px solid #ddd;">An liền sau Thái Tuế, đồng cung Thiếu Dương</td>
                        <td style="padding:10px; border:1px solid #ddd;">Vị trí thay bằng Địa Không (một số phái)</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold;">Phong cách luận giải</td>
                        <td style="padding:10px; border:1px solid #ddd;">Thiên về lý thuyết, bám sát kinh điển</td>
                        <td style="padding:10px; border:1px solid #ddd;">Linh hoạt, thực dụng, gắn với tâm linh dân gian</td>
                    </tr>
                </tbody>
            </table>
            <p style="text-align:center; font-style:italic; margin-top:-10px;">Bảng 1. So sánh một số đặc điểm giữa Tử Vi Trung Hoa và Tử Vi Việt Nam.</p>
            
            <h3>3. Các trường phái lớn</h3>
            <p>Trong dòng chảy phát triển hơn nghìn năm, Tử Vi đã phân hóa thành nhiều trường phái với phong cách luận giải khác nhau. Một số trường phái tiêu biểu:</p>
            <ul>
                <li><strong>Phái Triệu gia (Bắc tông):</strong> Nguyên gốc từ Hi Di Trần Đoàn, lưu truyền trong hoàng thất nhà Tống. Bộ kinh điển là <em>Tử Vi Chính Nghĩa</em>.</li>
                <li><strong>Phái Nam tông (Trung Châu phái):</strong> Phát triển ở miền Nam Trung Hoa, do Ma Y khởi xướng và được các Tử Vi gia bổ túc qua nhiều đời. Đặc trưng là chú trọng tính thực dụng và phong cách luận giải gần gũi đời sống.</li>
                <li><strong>Phái Đông A (Việt Nam):</strong> Thuộc dòng dõi nhà Trần, kế thừa từ Hoàng Bính, được hoàng tộc nhà Trần phát triển và biên soạn thành <em>Đông A Di Sự</em>.</li>
                <li><strong>Phái Thiên Lương:</strong> Trường phái có ảnh hưởng lớn ở miền Nam Việt Nam thế kỷ XX, do thầy Thiên Lương sáng lập, nhấn mạnh khía cạnh nhân văn và đạo đức trong luận giải.</li>
                <li><strong>Phái Tứ Hóa (Phi Tinh):</strong> Phái hiện đại của Đài Loan, đặc biệt chú trọng vai trò của bốn sao Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ và kỹ thuật "phi tinh" (chuyển hóa sao giữa các cung).</li>
            </ul>
            <p>Các phái không loại trừ nhau, mà bổ sung những góc nhìn khác nhau cho cùng một hệ thống. Người học Tử Vi nghiêm túc thường tham khảo nhiều phái để có cái nhìn đa chiều và thấu đáo.</p>
            
            <h2>PHẦN III. TRIẾT LÝ CỐT LÕI</h2>
            <h3>1. Nền tảng triết học Đông phương</h3>
            <p>Tử Vi không phải là một môn bói toán đơn lẻ, mà đứng trên nền tảng tổng hợp của bốn trụ cột triết học Đông phương:</p>
            <h4>a. Học thuyết Âm Dương</h4>
            <p>Âm Dương là cặp phạm trù gốc rễ của triết học phương Đông, thể hiện hai mặt đối lập nhưng bổ sung lẫn nhau trong vạn vật: Âm (tĩnh, lạnh, tối, mềm, hấp thụ) và Dương (động, nóng, sáng, cứng, phát tán). Trong Tử Vi, mỗi tuổi, mỗi cung, mỗi sao đều mang thuộc tính âm hoặc dương. Sự <strong>thuận lý hay nghịch lý</strong> giữa âm dương của tuổi và cung Mệnh là một yếu tố quan trọng trong luận đoán — người âm dương thuận lý thường có cuộc đời hài hòa hơn, còn nghịch lý thường có nội tâm phức tạp, "nghĩ một đằng làm một nẻo".</p>
            <h4>b. Học thuyết Ngũ Hành</h4>
            <p>Ngũ Hành — Kim, Mộc, Thủy, Hỏa, Thổ — là năm yếu tố biến đổi của vũ trụ. Chúng vận hành theo hai quy luật: <strong>tương sinh</strong> (Kim sinh Thủy, Thủy sinh Mộc, Mộc sinh Hỏa, Hỏa sinh Thổ, Thổ sinh Kim) và <strong>tương khắc</strong> (Kim khắc Mộc, Mộc khắc Thổ, Thổ khắc Thủy, Thủy khắc Hỏa, Hỏa khắc Kim). Trong Tử Vi, ngũ hành xuất hiện ở ba cấp độ: ngũ hành nạp âm của <strong>bản mệnh</strong> (theo năm sinh), ngũ hành của <strong>cục</strong> (Thủy nhị cục, Mộc tam cục, Kim tứ cục, Thổ ngũ cục, Hỏa lục cục) và ngũ hành của từng <strong>sao</strong>. Sự tương sinh tương khắc giữa ba cấp độ này quyết định nhiều khía cạnh của vận mệnh.</p>
            <h4>c. Hệ thống Thiên Can – Địa Chi</h4>
            <p>Mười Thiên Can (Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý) kết hợp với mười hai Địa Chi (Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi) tạo thành chu kỳ 60 năm — <strong>Lục thập hoa giáp</strong>. Đây là hệ thống tọa độ thời gian cổ đại để định vị mọi biến cố. Mỗi tổ hợp can chi mang một ngũ hành nạp âm riêng (ví dụ: Giáp Tý — Hải Trung Kim, Bính Dần — Lư Trung Hỏa) và là cơ sở để tính tuổi, lập lá số.</p>
            <h4>d. Triết lý Kinh Dịch</h4>
            <p>Kinh Dịch — bộ kinh cổ nhất của Trung Hoa — là gốc rễ tư tưởng cho toàn bộ thuật số phương Đông. Tinh thần cốt lõi của Dịch là <strong>biến hóa</strong>: không có gì đứng yên, mọi vật đều vận động theo quy luật. Vận mệnh con người không phải tấm bản đồ tĩnh, mà là dòng chảy động — có lúc thịnh, lúc suy, lúc cát, lúc hung. Tử Vi kế thừa tinh thần này qua hệ thống <strong>đại hạn</strong> (10 năm) và <strong>tiểu hạn</strong> (1 năm), giúp người học nhận ra nhịp điệu vận động của cuộc đời.</p>
            
            <h3>2. Cấu trúc lá số: Thiên – Nhân – Địa bàn</h3>
            <p>Lá số Tử Vi là một sơ đồ thu nhỏ của vũ trụ vào khoảnh khắc một người chào đời. Nó được chia thành 12 ô tương ứng với 12 cung, trong đó an khoảng 120 sao theo các quy tắc nghiêm ngặt. Lá số được phân thành ba bàn:</p>
            <ul>
                <li><strong>Thiên bàn:</strong> Sơ đồ sao Tử Vi sắp xếp căn cứ vào ngũ hành nạp âm của cung Mệnh. Đây là loại lá số chủ yếu, thể hiện thông tin về tính cách, dung mạo, sự nghiệp, tài vận, hôn nhân, phú quý, họa phúc, yểu thọ trong một đời người, cùng các điềm triệu tiên thiên về lục thân (cha mẹ, anh em, vợ chồng, con cái…).</li>
                <li><strong>Nhân bàn:</strong> Sơ đồ động về sự biến hóa của các vận hạn — đại hạn, tiểu hạn, lưu niên, lưu nguyệt, lưu nhật. Phản ánh các thăng trầm trong từng giai đoạn cuộc đời.</li>
                <li><strong>Địa bàn:</strong> Sơ đồ bố cục sao theo ngũ hành nạp âm của cung Thân, thể hiện thông tin tiên thiên và phản ánh căn khí, tính tình ngầm ẩn của con người. Đây là lý do có người địa vị cao nhưng hành vi đê tiện (Thiên bàn tốt, Địa bàn xấu), hay có người nghèo khổ mà nhân cách cao thượng (Thiên bàn xấu, Địa bàn tốt).</li>
            </ul>
            
            <h3>3. Mười hai cung</h3>
            <p>Mười hai cung là phần linh hồn của lá số, mỗi cung đại diện cho một phương diện cốt yếu của đời người. Cung Mệnh là trung tâm — "phần đầu não" — chỉ huy 11 cung còn lại, vốn được ví như tứ chi và xương cốt:</p>
            <table style="width:100%; border-collapse:collapse; margin-bottom:20px;">
                <thead>
                    <tr style="background:#8b3a1a; color:white;">
                        <th style="padding:10px; border:1px solid #ddd;">Cung</th>
                        <th style="padding:10px; border:1px solid #ddd;">Ý nghĩa chính</th>
                        <th style="padding:10px; border:1px solid #ddd;">Cung đối/tam hợp</th>
                    </tr>
                </thead>
                <tbody style="text-align:left;">
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Mệnh</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bản mệnh, tính cách tiên thiên, tài năng, dung mạo, thành tựu một đời</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Thiên Di<br>Tam hợp: Tài, Quan</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Thân</td>
                        <td style="padding:10px; border:1px solid #ddd;">Vận thế hậu thiên, hành vi, môi trường sống, khả năng thực hiện</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đồng cung với 1 trong 6: Mệnh, Phu, Tài, Quan, Di, Phúc</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Phụ Mẫu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Tướng mạo, tính cách, sức khỏe cha mẹ; tình cảm cha mẹ – con cái</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Tật Ách</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Phúc Đức</td>
                        <td style="padding:10px; border:1px solid #ddd;">Phúc phận, đời sống tinh thần, tâm hồn, dòng tộc, phước đức tổ tiên</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Tài Bạch</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Điền Trạch</td>
                        <td style="padding:10px; border:1px solid #ddd;">Nhà cửa, đất đai, bất động sản, tài sản kế thừa</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Tử Tức</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Quan Lộc</td>
                        <td style="padding:10px; border:1px solid #ddd;">Sự nghiệp, công danh, học vấn, thăng tiến, chức vụ</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Phu Thê<br>Tam hợp: Mệnh, Tài</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Nô Bộc</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đồng nghiệp, cấp dưới, bạn bè, quý nhân – tiểu nhân trong xã hội</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Huynh Đệ</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Thiên Di</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đi xa, xuất ngoại, ngoại giao, môi trường bên ngoài, định cư</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Mệnh</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Tật Ách</td>
                        <td style="padding:10px; border:1px solid #ddd;">Sức khỏe, bệnh tật, tai nạn, các bộ phận dễ tổn thương</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Phụ Mẫu</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Tài Bạch</td>
                        <td style="padding:10px; border:1px solid #ddd;">Tiền bạc, thu nhập, dòng tiền, năng lực kiếm và quản lý tài chính</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Phúc Đức<br>Tam hợp: Mệnh, Quan</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Tử Tức</td>
                        <td style="padding:10px; border:1px solid #ddd;">Con cái, học trò, sản phẩm sáng tạo, di sản</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Điền Trạch</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Phu Thê</td>
                        <td style="padding:10px; border:1px solid #ddd;">Hôn nhân, tình yêu, bạn đời, tính cách người phối ngẫu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Quan Lộc</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#8b3a1a;">Huynh Đệ</td>
                        <td style="padding:10px; border:1px solid #ddd;">Anh chị em, đồng đội, người thân ngang hàng</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đối: Nô Bộc</td>
                    </tr>
                </tbody>
            </table>
            <p style="text-align:center; font-style:italic; margin-top:-10px;">Bảng 2. Mười hai cung trong lá số Tử Vi và ý nghĩa cốt lõi.</p>
            <p>Một nguyên tắc quan trọng: <strong>không bao giờ luận một cung đơn lẻ</strong>. Cung Mệnh phải xem cùng cung Thiên Di (đối cung) và cung Tài, Quan (tam hợp). Cung Tài cần xem cùng Phúc Đức (đối) và Mệnh, Quan. Người luận Tử Vi giỏi luôn nhìn lá số như một mạng lưới chỉnh thể, không tách rời.</p>
            
            <h3>4. Mười bốn chính tinh</h3>
            <p>Trong khoảng 120 sao trên lá số, có 14 ngôi sao chủ chốt được gọi là <strong>chính tinh</strong>. Chúng được chia thành hai hệ:</p>
            <ul>
                <li><strong>Bắc Đẩu Tinh hệ (vòng Tử Vi, 6 sao):</strong> Tử Vi, Thiên Cơ, Thái Dương, Vũ Khúc, Thiên Đồng, Liêm Trinh — thiên về dương, chủ về sự khai sáng, vận động, quyền lực và sự nghiệp.</li>
                <li><strong>Nam Đẩu Tinh hệ (vòng Thiên Phủ, 8 sao):</strong> Thiên Phủ, Thái Âm, Tham Lang, Cự Môn, Thiên Tướng, Thiên Lương, Thất Sát, Phá Quân — thiên về âm, chủ về sự ổn định, tài sản, các mối quan hệ và đời sống nội tâm.</li>
            </ul>
            <p>Trong đó, <strong>Thái Dương</strong> và <strong>Thái Âm</strong> được coi là hai sao Trung Thiên, đại diện cho hai thái cực âm dương lớn nhất.</p>
            <table style="width:100%; border-collapse:collapse; margin-bottom:20px;">
                <thead>
                    <tr style="background:#8b3a1a; color:white;">
                        <th style="padding:10px; border:1px solid #ddd;">Sao</th>
                        <th style="padding:10px; border:1px solid #ddd;">Hệ</th>
                        <th style="padding:10px; border:1px solid #ddd;">Tính chất chủ đạo</th>
                    </tr>
                </thead>
                <tbody style="text-align:left;">
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Tử Vi</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắc Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đế tinh – quân chủ tối cao, lãnh đạo, danh tiếng, uy nghi</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thiên Cơ</td>
                        <td style="padding:10px; border:1px solid #ddd;">Nam Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Thiện tinh – trí tuệ, mưu lược, linh hoạt, hướng thiện</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thái Dương</td>
                        <td style="padding:10px; border:1px solid #ddd;">Trung Thiên</td>
                        <td style="padding:10px; border:1px solid #ddd;">Quý tinh – cha, chồng, con trai cả; quang minh, sự nghiệp, công danh</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Vũ Khúc</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắc Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Tài tinh – kinh tế, tài chính, tài lộc, cương nghị, độc lập</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thiên Đồng</td>
                        <td style="padding:10px; border:1px solid #ddd;">Nam Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Phúc tinh – phúc thọ, hiền hòa, hưởng thụ, may mắn</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Liêm Trinh</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắc Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Tù tinh / Quyền tinh – công danh, liêm khiết, kỷ luật; cẩn thận đào hoa và thị phi</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thiên Phủ</td>
                        <td style="padding:10px; border:1px solid #ddd;">Nam Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Tài tinh / Quyền tinh – kho tàng, ổn định, nhân hậu, quản lý</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thái Âm</td>
                        <td style="padding:10px; border:1px solid #ddd;">Trung Thiên</td>
                        <td style="padding:10px; border:1px solid #ddd;">Mẹ, vợ, con gái; tài sản ngầm, nội tâm, văn hóa, mỹ cảm</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Tham Lang</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắc Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Đào hoa tinh – tham vọng, đam mê, biến hóa, giao tế, dục vọng</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Cự Môn</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắc Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Ám tinh – ngôn từ, tranh biện, nghi ngờ, thị phi, khả năng phân tích</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thiên Tướng</td>
                        <td style="padding:10px; border:1px solid #ddd;">Nam Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Quyền tinh – tướng tài, công bằng, trung tín, phò tá</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thiên Lương</td>
                        <td style="padding:10px; border:1px solid #ddd;">Nam Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Phúc tinh – nhân hậu, hóa giải, thầy thuốc, người dẫn đường</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Thất Sát</td>
                        <td style="padding:10px; border:1px solid #ddd;">Nam Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Quyền tinh / Sát tinh – uy lực, dũng mãnh, sát phạt, quyết đoán</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid #ddd; font-weight:bold; color:#d9534f;">Phá Quân</td>
                        <td style="padding:10px; border:1px solid #ddd;">Bắc Đẩu</td>
                        <td style="padding:10px; border:1px solid #ddd;">Hao tinh – phá cũ lập mới, biến động, hiếu thắng, tiên phong</td>
                    </tr>
                </tbody>
            </table>
            <p style="text-align:center; font-style:italic; margin-top:-10px;">Bảng 3. Mười bốn chính tinh và tính chất chủ đạo.</p>
            <p>Mười bốn chính tinh được chia thành bốn nhóm cách cục lớn:</p>
            <ul>
                <li><strong>Tử Phủ Vũ Tướng (Liêm):</strong> Nhóm điều hành, đại diện cho lực lượng chính danh, quyền lực nhà nước, sự ổn định và lãnh đạo.</li>
                <li><strong>Sát Phá Tham (Liêm):</strong> Nhóm thực hành, đại diện cho biến động, tham vọng, sát phạt và khả năng thích nghi cao.</li>
                <li><strong>Cơ Nguyệt Đồng Lương:</strong> Nhóm lý thuyết, đại diện cho trí tuệ, tình cảm, sự bình an, hợp với nghề văn chức, học thuật.</li>
                <li><strong>Cự Nhật:</strong> Nhóm ngoại giao, đại diện cho ngôn ngữ, sáng tạo, năng lượng và khả năng truyền đạt.</li>
            </ul>
            <p>Bên cạnh chính tinh còn có hàng chục <strong>phụ tinh</strong> quan trọng: <em>Lục Cát Tinh</em> (Tả Phù, Hữu Bật, Văn Xương, Văn Khúc, Thiên Khôi, Thiên Việt) — những sao trợ giúp; <em>Lục Sát Tinh</em> (Kình Dương, Đà La, Hỏa Tinh, Linh Tinh, Địa Không, Địa Kiếp) — những sao cản trở; và <em>Tứ Hóa</em> (Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ) — bốn sao biến hóa quyết định sự khác biệt giữa các tuổi cùng cách cục.</p>
            
            <h2>PHẦN IV. Ý NGHĨA THỰC TIỄN</h2>
            <p>Tử Vi không chỉ có giá trị về mặt tri thức cổ truyền, mà còn mang lại nhiều ý nghĩa thiết thực cho đời sống đương đại. Khi được tiếp cận đúng đắn, nó có thể trở thành một công cụ tự nhận thức và phát triển bản thân rất hữu ích.</p>
            
            <h3>1. Công cụ tự hiểu mình</h3>
            <p>Đây là ý nghĩa quan trọng nhất. Cung Mệnh và các sao tọa thủ giúp người xem nhận diện rõ hơn về <strong>tính cách tiên thiên</strong>: ưu điểm, nhược điểm, khuynh hướng phản ứng trước sự việc, kiểu năng lượng đặc trưng. Nhiều người sau khi nghiên cứu lá số của mình đã "giật mình" vì những đặc điểm trên giấy phản ánh chính xác đến lạ những gì họ vẫn cảm nhận về bản thân nhưng chưa từng gọi tên.</p>
            <div class="ph-quote-block" style="background:#f9f9f9; padding:15px; border-left:4px solid #8b3a1a; margin-bottom:20px; font-style:italic;">
                Nói như một học giả: "Học Tử Vi đơn giản là để hiểu mình. Ai chưa hiểu mình thì tốt nhất không nên khuyên bảo người khác."
            </div>
            
            <h3>2. Định hướng nghề nghiệp</h3>
            <p>Cha ông có câu: "Con gái sợ chọn nhầm chồng, con trai sợ làm nhầm nghề". Tử Vi qua các cung Mệnh – Thân – Quan – Tài có thể chỉ ra <strong>ưu cách nghề nghiệp</strong> phù hợp với từng người. Một số liên hệ phổ biến:</p>
            <ul>
                <li>Mệnh có Thái Dương, Thái Âm sáng sủa: hợp lãnh đạo, chính trị, giáo dục, truyền thông;</li>
                <li>Mệnh có Vũ Khúc, Thiên Phủ: hợp kinh doanh, tài chính, ngân hàng;</li>
                <li>Mệnh có Thiên Cơ, Cự Môn: hợp công nghệ, nghiên cứu, phân tích, sáng tạo;</li>
                <li>Mệnh có Cơ Nguyệt Đồng Lương: hợp văn chức, hành chính, văn hóa nghệ thuật;</li>
                <li>Mệnh có Sát Phá Tham: hợp các nghề có biến động, đột phá, khởi nghiệp, võ nghiệp, kinh doanh rủi ro cao.</li>
            </ul>
            
            <h3>3. Phòng và bảo vệ sức khỏe</h3>
            <p>Cung Tật Ách kết hợp với Mệnh và Thân giúp dự đoán các bộ phận cơ thể dễ bị tổn thương, các loại bệnh có khuynh hướng mắc phải. Người luận Tử Vi có kinh nghiệm thậm chí có thể đoán chính xác mức độ và thời gian phát bệnh, từ đó chủ động xây dựng chế độ ăn uống, tập luyện và thăm khám y tế phù hợp.</p>
            
            <h3>4. Hiểu các mối quan hệ</h3>
            <p>Cung Phu Thê cho biết tính cách bạn đời, thời điểm hôn nhân thuận lợi, những thử thách trong gia đạo. Cung Phụ Mẫu, Huynh Đệ, Tử Tức giúp hiểu mối quan hệ với cha mẹ, anh em, con cái. Cung Nô Bộc cho thấy cách bạn kết nối với đồng nghiệp và xã hội. Hiểu sâu các cung này không phải để phán xét người thân, mà để có ứng xử khéo léo, vị tha và xây dựng quan hệ bền vững hơn.</p>
            
            <h3>5. Nắm bắt nhịp điệu vận hạn</h3>
            <p>Vận mệnh không phải đường thẳng mà là đường cong có sóng. Đại hạn 10 năm và tiểu hạn 1 năm cho biết khi nào là <strong>thời thịnh vượng</strong> để dốc sức tiến công, khi nào là <strong>thời khó khăn</strong> nên thủ thế, tu dưỡng. Nhiều người nắm được vận thịnh đã đạt thành công rực rỡ; ngược lại, biết trước thời suy thì giữ mình cẩn trọng, tránh được tai họa.</p>
            
            <h3>6. Tu dưỡng bản thân — ý nghĩa cao nhất</h3>
            <p>Trên lá số luôn có cát tinh và hung tinh đan xen — như một xã hội thu nhỏ có người tốt và kẻ gian. Người trí tuệ hiểu rằng <strong>không thể đổi vận mệnh, nhưng có thể đổi cách phản ứng</strong>. Tu dưỡng đạo đức, làm việc thiện, không ngừng học hỏi sẽ tăng cường ảnh hưởng của cát tinh; ngược lại, buông thả sẽ để hung tinh trỗi dậy. Đây chính là tinh thần "Đức năng thắng số" mà người xưa đã đúc kết.</p>
            <p>Lê Quý Đôn trong <em>Thần Khê Định Số</em> nhấn mạnh: <em>tướng mệnh phải phù hợp mới ăn được sao</em>. Nghĩa là dù lá số đẹp đến đâu, nếu hành động trái với cốt cách, thì cũng không hưởng được phúc trọn vẹn. Đây là một thông điệp đạo đức sâu sắc: số mệnh không phải món quà cho không, mà là tiềm năng cần được nuôi dưỡng bằng nhân cách.</p>
            
            <h2>PHẦN V. CÁCH ÁP DỤNG VÀO ĐỜI SỐNG</h2>
            <p>Sau khi hiểu lý thuyết, câu hỏi đặt ra là: <strong>làm sao đưa Tử Vi vào thực hành đời sống một cách lành mạnh?</strong> Dưới đây là những nguyên tắc và phương pháp được đúc kết từ kinh nghiệm của các bậc tiền bối.</p>
            
            <h3>1. Lập lá số chính xác</h3>
            <p>Bước đầu tiên là có một lá số đúng. Cần ba thông tin: <strong>giờ – ngày – tháng – năm sinh theo âm lịch và giới tính</strong>. Trong đó, <strong>giờ sinh</strong> là yếu tố dễ sai nhất và quan trọng nhất — sai một giờ có thể làm thay đổi cả cung Mệnh, Thân, Phúc Đức. Ngày nay có nhiều phần mềm và website lập lá số tự động (lyso.vn, tuvi.cohoc.net, kabala.vn…), giúp việc an sao trở nên thuận tiện. Người mới học không cần thuộc lòng quy tắc an sao, mà nên tập trung vào <strong>kỹ năng luận giải</strong>.</p>
            
            <h3>2. Đọc lá số theo trình tự</h3>
            <p>Một lộ trình luận giải hợp lý cho người tự xem:</p>
            <ul>
                <li><strong>Bước 1</strong> — Xem cung Mệnh để hiểu tính cách, cốt cách, ưu nhược điểm tiên thiên.</li>
                <li><strong>Bước 2</strong> — Xem cung Thân để hiểu môi trường hậu thiên, cách hành xử thực tế.</li>
                <li><strong>Bước 3</strong> — Xem cung Quan Lộc và Tài Bạch (tam hợp với Mệnh) để hiểu sự nghiệp và tài lộc.</li>
                <li><strong>Bước 4</strong> — Xem cung Phu Thê và Tử Tức để hiểu gia đạo.</li>
                <li><strong>Bước 5</strong> — Xem cung Tật Ách để hiểu sức khỏe, cung Phúc Đức để hiểu nội tâm và phúc phận.</li>
                <li><strong>Bước 6</strong> — Xem đại hạn và tiểu hạn năm hiện tại để biết đang ở giai đoạn nào của vận trình.</li>
            </ul>
            
            <h3>3. Những nguyên tắc quan trọng khi luận</h3>
            <ul>
                <li><strong>Không bao giờ luận một cung đơn lẻ</strong>. Luôn xem cung đối và tam hợp. Cung Mệnh tốt nhưng Quan Lộc yếu thì sự nghiệp vẫn có khó khăn; Tài Bạch tốt nhưng Điền Trạch xấu thì kiếm tiền giỏi nhưng khó giữ của.</li>
                <li><strong>Cân nhắc bối cảnh sinh ra</strong>. Cùng một cách Tử Phủ Vũ Tướng, sinh trong nhà chúa thì phát huy hết tác dụng, sinh trong gia đình nghèo khó chỉ an phận thủ thường. Bối cảnh xã hội, gia đình, lá số cha mẹ đều ảnh hưởng đến việc "ăn sao".</li>
                <li><strong>Đừng bỏ qua cung phụ trợ</strong>. Phúc Đức, Nô Bộc, Tật Ách tưởng nhỏ nhưng ảnh hưởng sâu xa đến tổng thể vận mệnh. Người mới học hay chỉ chú trọng Mệnh – Quan – Tài là chưa đủ.</li>
                <li><strong>Hiểu rằng dự đoán chỉ tương đối</strong>. Vận mệnh chịu ảnh hưởng cả yếu tố chủ quan (ý chí, nỗ lực, đạo đức) và khách quan (môi trường, thời đại, may rủi). Tử Vi cho thấy xu hướng, không phải định mệnh tuyệt đối.</li>
                <li><strong>Không tự kỷ ám thị</strong>. Đừng vì thấy một sao xấu mà sống trong lo lắng, hoặc thấy một cách đẹp mà chủ quan buông thả. Tử Vi là tham khảo, đời sống thực tế mới là sân chơi của bạn.</li>
            </ul>
            
            <h3>4. Ứng dụng cụ thể trong các quyết định lớn</h3>
            <ul>
                <li><strong>Chọn nghề và phát triển sự nghiệp:</strong> Đối chiếu cung Quan Lộc và Tài Bạch với khả năng thực tế. Nếu lá số ưu cách kinh doanh nhưng bạn đang làm văn chức, có thể đó là lý do bạn cảm thấy bí bách. Hoặc ngược lại — biết mình hợp công việc ổn định mà cứ đua theo bạn bè khởi nghiệp thì rủi ro tâm lý rất lớn.</li>
                <li><strong>Hôn nhân và lựa chọn bạn đời:</strong> Cung Phu Thê cho biết kiểu người phù hợp với mình về tính cách. Tuy nhiên, đừng dùng Tử Vi để loại trừ ai đó chỉ vì vài câu phú không tốt — quan trọng là hai người có thực sự hiểu và tôn trọng nhau hay không.</li>
                <li><strong>Chọn ngày giờ tốt cho việc đại sự:</strong> Khán nhật hạn Tử Vi cho phép chọn ngày tốt dựa trên chính lá số của đương sự, có độ chính xác cao hơn các phương pháp chọn ngày chung chung. Phù hợp khi cưới hỏi, khai trương, ký hợp đồng quan trọng, xuất hành xa.</li>
                <li><strong>Đầu tư và tài chính:</strong> Đại hạn và lưu niên có thể chỉ ra giai đoạn thuận lợi cho việc mở rộng đầu tư hay năm cần thận trọng giảm rủi ro. Tuy nhiên, Tử Vi không thay thế phân tích cơ bản và kỹ thuật — nó là một biến số tham khảo trong tổ hợp ra quyết định.</li>
            </ul>
            
            <h3>5. Thái độ đúng đắn của người học Tử Vi</h3>
            <p>Cuối cùng, điều quan trọng nhất không phải là kỹ thuật luận giải mà là <strong>thái độ tinh thần</strong>. Dưới đây là những phẩm chất mà người học Tử Vi nghiêm túc cần nuôi dưỡng:</p>
            <ul>
                <li><strong>Khiêm nhường:</strong> Tri thức Tử Vi mênh mông, các bậc thầy hàng chục năm vẫn chưa dám tự nhận thông thạo. Người mới học càng cần khiêm tốn.</li>
                <li><strong>Lý tính:</strong> Phân biệt rõ giữa khoa học dự trắc với mê tín dị đoan. Không sa đà vào bùa chú, lễ lạt giải hạn không có cơ sở.</li>
                <li><strong>Tự lực:</strong> Tử Vi giúp hiểu mình, nhưng hành động và quyết định phải do chính mình. Không ỷ lại vào thầy bói thay mình ra quyết định lớn của cuộc đời.</li>
                <li><strong>Tu thân tích đức:</strong> Đây là tinh thần xuyên suốt của Tử Vi và toàn bộ huyền học Đông phương. Đức năng thắng số — phẩm hạnh có thể chuyển hóa vận mệnh.</li>
                <li><strong>Cân bằng:</strong> Không lệ thuộc Tử Vi đến mức bỏ bê chuyên môn nghề nghiệp, kỹ năng sống thực tế. Tử Vi là chiếc la bàn, không phải con thuyền — bạn vẫn phải tự chèo.</li>
            </ul>
            
            <h2>LỜI KẾT</h2>
            <p>Tử Vi Đẩu Số đã đồng hành cùng người Á Đông hơn một nghìn năm, từ những ngày Hi Di Trần Đoàn ngồi tu ẩn trên đỉnh Hoa Sơn cho đến những ứng dụng smartphone an sao tự động trong tay người trẻ thế kỷ XXI. Sức sống bền bỉ ấy không phải vì nó là môn bói toán hay phép màu, mà vì nó chạm đến những câu hỏi căn bản nhất của đời người: <em>Tôi là ai? Tôi nên đi về đâu? Tôi đang ở đoạn nào của hành trình?</em></p>
            <p>Khi đặt Tử Vi vào đúng vị trí của nó — không phải tấm bùa định mệnh, không phải bản án không thể kháng cáo, mà là tấm gương soi giúp con người tự nhận thức — thì giá trị thực sự của nó hiện ra: một <strong>công cụ tu thân và phát triển bản thân</strong> rất tinh tế. Người hiểu Tử Vi thấu đáo không trở nên bị động, mà ngược lại, càng chủ động hơn trong lựa chọn, càng khoan dung hơn trong ứng xử, và càng kính cẩn hơn trước nhịp điệu lớn của vũ trụ.</p>
            <p>Cụ Lê Quý Đôn từng dạy: tướng mệnh phải phù hợp mới ăn được sao. Hi Di Trần Đoàn từng nói: học Tử Vi không phải để đoán định, mà để "biết kẻ trung người nịnh, cứu kẻ bị nạn, trị kẻ làm ác". Ở mức cao nhất, Tử Vi là khoa học của <strong>nhân – nghĩa – trí – tín</strong>, không phải khoa học của may rủi.</p>
            <p>Hy vọng tài liệu nhỏ này góp phần đem lại một góc nhìn cân bằng và trân trọng về di sản tinh thần quý giá của tiền nhân — để mỗi người có thể tiếp cận Tử Vi như một người bạn đồng hành tỉnh thức, không phải như một vị thần phán xử.</p>
            <div class="ph-quote-block" style="text-align:center; padding:15px; border:1px solid #ddd; margin:20px 0; font-style:italic;">
                "Hành trình vĩ đại của một người chính là hành trình thấu hiểu bản thân và chinh phục cái Tôi to lớn — và đó cũng là con đường để đạt được Hạnh Phúc."
            </div>
            
            <p style="text-align:center; margin-top:40px; font-style:italic;">— HẾT —</p>
            
            <hr class="ph-divider">
            <h3>TÀI LIỆU THAM KHẢO</h3>
            <h4>Sách kinh điển</h4>
            <ul>
                <li>Hi Di Trần Đoàn, Tử Vi Đẩu Số Toàn Thư, La Hồng Tiên biên soạn (đời Minh, niên hiệu Gia Tĩnh), Trúc Lâm An Thư Cục ấn hành tại Đài Loan; Vũ Tài Lục dịch, 1973.</li>
                <li>Hi Di Trần Đoàn, Tử Vi Chính Nghĩa (truyền cho Tống Thái Tổ Triệu Khuông Dẫn).</li>
                <li>Triệu thị Minh Thuyết Tử Vi Kinh, Cẩm Chướng thư cục Thượng Hải, 1921.</li>
                <li>Lưu Bá Ôn, Tử Vi Thiển Thuyết.</li>
                <li>Hứa Quang Chi, Lịch Số Tử Vi Toàn Thư (đời Minh).</li>
                <li>Lê Quý Đôn, Thần Khê Định Số và Phú Tử Vi của Lê Quý Đôn (Việt Nam, thế kỷ XVIII).</li>
                <li>Đông A Di Sự — chép bởi Huệ Túc phu nhân, Đoàn Nhữ Hài và Trần Nguyên Đán (đời Trần).</li>
            </ul>
            <h4>Sách hiện đại</h4>
            <ul>
                <li>Vũ Tài Lục, Tử Vi Đẩu Số Toàn Thư (bản dịch và bình chú), 1973.</li>
                <li>Nguyễn Mạnh Bảo, Tử Vi Đẩu Số.</li>
                <li>Lê Quang Lăng, Tử Vi Nam Phái (sưu tầm di sản Trạng Trình Nguyễn Bỉnh Khiêm).</li>
                <li>Mai K. Đa (TS. Triết học), giáo trình Tử Vi ứng dụng — Hiểu số mệnh, làm chủ cuộc đời, TUVI.SCHOOL.</li>
            </ul>
            <h4>Nguồn trực tuyến tham khảo</h4>
            <ul>
                <li>Lý số Việt Nam — lyso.vn: bài "Lịch sử Tử Vi", "Ý nghĩa 12 cung trong Tử Vi", "Tính nhân quả trong lá số Tử Vi".</li>
                <li>Tử Vi Cổ Học — tuvi.cohoc.net: bài "Tổng quan về 14 chính tinh".</li>
                <li>Xemtuong.net — xemtuong.net: bài "Tử vi đẩu số — Bản đồ giải mã vận mệnh bậc nhất".</li>
                <li>Nghiencuulichsu.com: bài "Giới thiệu Tử Vi Đẩu Số Toàn Thư của Trần Đoàn".</li>
                <li>Tủ Sách Xưa — tusachxua.com: bài "Hi Di Trần Đoàn — Lão tổ của khoa Tử Vi Đẩu Số".</li>
                <li>Tùy phong đáo thử — tuyphongdaothu.wordpress.com: bài "Hy Di Trần Đoàn và nguồn gốc khoa Tử vi".</li>
                <li>Spiderum: bài "Tử vi và những chặng đường phát triển" (lịch sử Tử Vi tại Việt Nam).</li>
                <li>Tracuutuvi.com, Maihoadichso.com, Tuvi666.com, Tracuulasotuvi.com: các bài về 14 chính tinh và phụ tinh.</li>
                <li>Wikipedia tiếng Việt — bài "Tử vi", "Nguyễn Bỉnh Khiêm", "Lê Quý Đôn".</li>
            </ul>
            <p style="font-size:0.9em; color:#666; font-style:italic;">Lưu ý: Tài liệu này được biên soạn nhằm mục đích giáo dục, tham khảo và bảo tồn di sản văn hóa. Các nội dung được tổng hợp, đối chiếu và trình bày lại bằng ngôn ngữ riêng của người biên soạn, không sao chép nguyên văn từ bất kỳ nguồn nào. Mọi sai sót còn tồn tại là trách nhiệm của người biên soạn.</p>
        </div>
        
        <div class="ph-footer-buttons">
            <button class="back-btn" onclick="openThuVienArticle('')">
                <i class="fa-solid fa-arrow-left"></i> Quay lại Thư viện
            </button>
        </div>
    </div>
</div>
"""
    
    panel_target = """                </div>
            </div>

            <!-- PANEL 7: GAME -->"""
    
    panel_new = panel_html + """
                </div>
            </div>

            <!-- PANEL 7: GAME -->"""

    if 'id="article-tuvi-panel"' not in html_content:
        html_content = html_content.replace(card_target, card_new)
        html_content = html_content.replace(panel_target, panel_new)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)

if __name__ == '__main__':
    main()
