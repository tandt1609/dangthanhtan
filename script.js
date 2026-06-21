// ====================================================
// FINANCIAL TERMINAL ROUTER & INTERACTIVE CONTROLLER
// ====================================================

// --- 1. THEME SWITCHING (BULL & BEAR) ---
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
        console.log('%c📈 SENTIMENT: BULLISH. Markets trending up.', 'color: #10b981; font-weight: bold;');
    } else {
        body.classList.remove('theme-bull');
        body.classList.add('theme-bear');
        btnBear.classList.add('active');
        btnBull.classList.remove('active');
        
        if (sentimentText) sentimentText.textContent = 'Thị trường Gấu ngủ';
        if (philosophyText) {
            philosophyText.innerHTML = `Khi thị trường bước vào pha <strong>Giảm giá (Bear Market)</strong>, trọng tâm dịch chuyển sang các hệ thống quản trị rủi ro, tối ưu hóa bộ lọc tín hiệu kỹ thuật để phòng vệ danh mục và cảnh báo tự động.`;
        }
        console.log('%c📉 SENTIMENT: BEARISH. Protection mode activated.', 'color: #f43f5e; font-weight: bold;');
    }
}

// --- 2. SINGLE PAGE APPLICATION (SPA) ROUTER ---
const routeToTab = {
    '/': 'trang-chu',
    '/trang-chu': 'trang-chu',
    '/ban-tin': 'trang-chu',
    '/vi-mo': 'vi-mo',
    '/hang-hoa': 'hang-hoa',
    '/su-kien': 'su-kien',
    '/huyen-thoai': 'huyen-thoai',
    '/game': 'game'
};

const tabToRoute = {
    'trang-chu': '/',
    'vi-mo': '/vi-mo',
    'hang-hoa': '/hang-hoa',
    'su-kien': '/su-kien',
    'huyen-thoai': '/huyen-thoai',
    'game': '/game'
};

function switchTab(tabId, updateUrl = true) {
    // Deactivate current tabs and panels
    document.querySelectorAll('.tab-link').forEach(link => link.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));
    
    // Activate target tab link
    const targetLink = document.querySelector(`.tab-link[data-tab="${tabId}"]`);
    if (targetLink) targetLink.classList.add('active');

    // Activate target panel
    const targetPanel = document.getElementById(`panel-${tabId}`);
    if (targetPanel) targetPanel.classList.add('active');

    // Update URL if requested
    if (updateUrl) {
        const route = tabToRoute[tabId] || '/';
        history.pushState({ tabId }, '', route);
    }
    
    console.log(`🧭 Switched to tab: ${tabId}`);
}

function switchSubTab(subTabId) {
    // Deactivate sub-tabs and sub-panels
    document.querySelectorAll('.sub-tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.commodity-sub-panel').forEach(panel => panel.classList.remove('active'));
    
    // Activate target sub-tab button
    const targetBtn = document.querySelector(`.sub-tab-btn[onclick="switchSubTab('${subTabId}')"]`);
    if (targetBtn) targetBtn.classList.add('active');
    
    // Activate target sub-panel
    const targetPanel = document.getElementById(`sub-panel-${subTabId}`);
    if (targetPanel) targetPanel.classList.add('active');
    
    console.log(`📂 Switched commodity sub-tab to: ${subTabId}`);
}


// Initialize router click events
function initRouter() {
    // Intercept click on tab navigation links
    document.querySelectorAll('.tab-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tabId = link.getAttribute('data-tab');
            switchTab(tabId, true);
        });
    });

    // Handle browser Back/Forward navigation
    window.addEventListener('popstate', (e) => {
        const path = window.location.pathname;
        const tabId = routeToTab[path] || 'trang-chu';
        switchTab(tabId, false);
    });

    // Handle initial load routing
    const initialPath = window.location.pathname;
    const initialTab = routeToTab[initialPath] || 'trang-chu';
    switchTab(initialTab, false);
}


// --- 3. INTERACTIVE TRADING SIMULATOR GAME ("TÂN TERMINAL") ---
let gameState = {
    cash: 10000.0,
    shares: 0,
    avgPrice: 0.0,
    stockPrice: 100.0,
    netWorth: 10000.0,
    priceHistory: [100.0, 101.5, 99.2, 100.8, 102.0, 101.0, 103.5]
};

function updateGameDOM() {
    const cashEl = document.getElementById('game-cash');
    const sharesEl = document.getElementById('game-shares');
    const avgPriceEl = document.getElementById('game-avg-price');
    const networthEl = document.getElementById('game-networth');
    const chartPriceEl = document.getElementById('chart-price');
    const chartChangeEl = document.getElementById('chart-change');

    if (!cashEl) return; // Game tab is not loaded yet or elements missing

    // Format currencies
    cashEl.textContent = `$${gameState.cash.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    sharesEl.textContent = `${gameState.shares} TNT`;
    avgPriceEl.textContent = `$${gameState.avgPrice.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    
    // Calculate net worth
    gameState.netWorth = gameState.cash + (gameState.shares * gameState.stockPrice);
    networthEl.textContent = `$${gameState.netWorth.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    
    // Networth color indicators
    if (gameState.netWorth >= 10000.0) {
        networthEl.className = 'value text-bull';
    } else {
        networthEl.className = 'value text-bear';
    }

    // Chart Price
    chartPriceEl.textContent = `$${gameState.stockPrice.toFixed(2)}`;
    
    // Daily Change calculation based on initial $100 price
    const changePct = ((gameState.stockPrice - 100) / 100) * 100;
    chartChangeEl.textContent = `${changePct >= 0 ? '+' : ''}${changePct.toFixed(2)}%`;
    chartChangeEl.className = `chart-change ${changePct >= 0 ? 'text-bull' : 'text-bear'}`;
}

function gameAction(action) {
    if (action === 'buy') {
        if (gameState.cash <= 0) return;
        
        // Buy all-in
        const sharesToBuy = Math.floor(gameState.cash / gameState.stockPrice);
        if (sharesToBuy > 0) {
            const cost = sharesToBuy * gameState.stockPrice;
            
            // Recalculate average price
            const oldTotalCost = gameState.shares * gameState.avgPrice;
            const newTotalCost = oldTotalCost + cost;
            
            gameState.shares += sharesToBuy;
            gameState.cash -= cost;
            gameState.avgPrice = newTotalCost / gameState.shares;
            
            console.log(`🛒 Bought ${sharesToBuy} TNT shares at $${gameState.stockPrice.toFixed(2)}`);
        }
    } 
    else if (action === 'sell') {
        if (gameState.shares <= 0) return;
        
        // Sell all-in
        const proceeds = gameState.shares * gameState.stockPrice;
        console.log(`💰 Sold ${gameState.shares} TNT shares at $${gameState.stockPrice.toFixed(2)}`);
        
        gameState.cash += proceeds;
        gameState.shares = 0;
        gameState.avgPrice = 0.0;
    } 
    else if (action === 'reset') {
        gameState = {
            cash: 10000.0,
            shares: 0,
            avgPrice: 0.0,
            stockPrice: 100.0,
            netWorth: 10000.0,
            priceHistory: [100.0, 101.5, 99.2, 100.8, 102.0, 101.0, 103.5]
        };
        console.log('🔄 Game reset successfully.');
    }
    
    updateGameDOM();
    renderGameChart();
}

function renderGameChart() {
    const polyline = document.getElementById('chart-line');
    const svg = document.getElementById('game-svg-chart');
    if (!polyline || !svg) return;

    // Get actual width and height of SVG container
    const width = svg.clientWidth || 500;
    const height = 150;

    const history = gameState.priceHistory;
    const maxVal = Math.max(...history) * 1.01;
    const minVal = Math.min(...history) * 0.99;
    const range = maxVal - minVal;

    const points = history.map((price, index) => {
        const x = (index / (history.length - 1)) * width;
        // SVG coordinates start at 0,0 top-left, so we subtract scaled height from overall height
        const y = height - ((price - minVal) / range) * (height - 30) - 15;
        return `${x},${y}`;
    }).join(' ');

    polyline.setAttribute('points', points);
    
    // Change chart color dynamically based on recent price change
    const isUp = history[history.length - 1] >= history[history.length - 2];
    polyline.setAttribute('stroke', isUp ? '#10b981' : '#f43f5e');
}

function startTradingSimulator() {
    // Tick price every 1 second
    setInterval(() => {
        // Skew price direction based on active site theme (Bull or Bear)
        const isBullTheme = document.body.classList.contains('theme-bull');
        
        // Random change percent
        // Bull theme gives slightly positive drift, Bear theme gives negative drift
        const bias = isBullTheme ? -0.45 : -0.55; 
        const changePercent = (Math.random() + bias) * 4; // range [-2%, +2%] roughly

        const newPrice = gameState.stockPrice * (1 + changePercent / 100);
        gameState.stockPrice = Math.max(1.0, newPrice); // Price can't fall below $1.00

        gameState.priceHistory.push(gameState.stockPrice);
        
        // Keep history size to max 30 ticks
        if (gameState.priceHistory.length > 30) {
            gameState.priceHistory.shift();
        }

        updateGameDOM();
        renderGameChart();
    }, 1200);

    // Initial renders
    updateGameDOM();
    setTimeout(() => {
        renderGameChart();
    }, 500);

    // Handle resizing of the SVG chart
    window.addEventListener('resize', renderGameChart);
}


// --- 4. INITIALIZATION ---
document.addEventListener('DOMContentLoaded', () => {
    console.log('%c📊 Đặng Thanh Tân Terminal Initialized.', 'color: #ffd200; font-size: 14px; font-weight: bold;');
    
    setTheme('bull');
    initRouter();
    startTradingSimulator();
});
