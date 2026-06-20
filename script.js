// Financial Terminal Theme & Sentiment Controller

function setTheme(theme) {
    const body = document.body;
    const btnBull = document.getElementById('btn-bull');
    const btnBear = document.getElementById('btn-bear');
    const sentimentText = document.getElementById('current-sentiment-text');
    const philosophyText = document.getElementById('sentiment-philosophy');

    if (theme === 'bull') {
        body.classList.remove('theme-bear');
        body.classList.add('theme-bull');
        
        btnBull.classList.add('active');
        btnBear.classList.remove('active');
        
        if (sentimentText) sentimentText.textContent = 'Thị trường Bò tót';
        if (philosophyText) {
            philosophyText.innerHTML = `Khi thị trường trong pha <strong>Tăng giá (Bull Market)</strong>, chúng tôi tập trung phát triển các bảng Dashboard tối ưu hóa hiệu năng, xử lý luồng dữ liệu thời gian thực (Websockets) để nắm bắt nhanh các cơ hội dòng tiền lớn.`;
        }
        
        console.log('%c📈 SENTIMENT UPDATE: BULLISH. Focus on momentum, volume streaming & real-time analytics.', 'color: #10b981; font-weight: bold;');
    } else {
        body.classList.remove('theme-bull');
        body.classList.add('theme-bear');
        
        btnBear.classList.add('active');
        btnBull.classList.remove('active');
        
        if (sentimentText) sentimentText.textContent = 'Thị trường Gấu ngủ';
        if (philosophyText) {
            philosophyText.innerHTML = `Khi thị trường bước vào pha <strong>Giảm giá (Bear Market)</strong>, trọng tâm dịch chuyển sang các hệ thống quản trị rủi ro, tối ưu hóa bộ lọc tín hiệu kỹ thuật để phòng vệ danh mục và cảnh báo tự động.`;
        }
        
        console.log('%c📉 SENTIMENT UPDATE: BEARISH. Focus on risk management, hedging algorithms & alert triggers.', 'color: #f43f5e; font-weight: bold;');
    }
}

// Entry animations & interactions
document.addEventListener('DOMContentLoaded', () => {
    console.log('%c📊 T&T Financial Hub Terminal Active.', 'color: #6366f1; font-size: 14px; font-weight: bold;');
    
    // Set default theme to Bull
    setTheme('bull');

    // Smooth entrance for cards
    const cards = document.querySelectorAll('.project-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(15px)';
        card.style.transition = 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 + index * 80);
    });
});
