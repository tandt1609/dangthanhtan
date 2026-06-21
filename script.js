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
        if (btnBull) btnBull.classList.add('active');
        if (btnBear) btnBear.classList.remove('active');

        if (sentimentText) sentimentText.textContent = 'Thị trường Bò tót';
        if (philosophyText) {
            philosophyText.innerHTML = `Khi thị trường trong pha <strong>Tăng giá (Bull Market)</strong>, chúng tôi tập trung phát triển các bảng Dashboard tối ưu hóa hiệu năng, xử lý luồng dữ liệu thời gian thực (Websockets) để nắm bắt nhanh các cơ hội dòng tiền lớn.`;
        }
    } else {
        body.classList.remove('theme-bull');
        body.classList.add('theme-bear');
        if (btnBear) btnBear.classList.add('active');
        if (btnBull) btnBull.classList.remove('active');

        if (sentimentText) sentimentText.textContent = 'Thị trường Gấu ngủ';
        if (philosophyText) {
            philosophyText.innerHTML = `Khi thị trường bước vào pha <strong>Giảm giá (Bear Market)</strong>, trọng tâm dịch chuyển sang các hệ thống quản trị rủi ro, tối ưu hóa bộ lọc tín hiệu kỹ thuật để phòng vệ danh mục và cảnh báo tự động.`;
        }
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

    // If switching to a main tab, default the commodity sub-views to list if it's updateUrl
    if (tabId === 'hang-hoa' && updateUrl) {
        openCommodityArticle('', true);
    } else if (updateUrl) {
        const route = tabToRoute[tabId] || '/';
        history.pushState({ tabId }, '', route);
    }
    
    console.log(`🧭 Switched to tab: ${tabId}`);
}

function openCommodityArticle(articleId, updateUrl = true) {
    const listView = document.getElementById('commodity-list-view');
    const articleView = document.getElementById('commodity-article-view');
    
    if (!listView || !articleView) return;
    
    // Deactivate all article panels
    document.querySelectorAll('.commodity-article-panel').forEach(panel => panel.classList.remove('active'));
    
    if (articleId === 'tien-si-dong') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const targetPanel = document.getElementById('article-tiensidong-panel');
        if (targetPanel) targetPanel.classList.add('active');
        
        if (updateUrl) {
            history.pushState({ tabId: 'hang-hoa', articleId: 'tien-si-dong' }, '', '/hang-hoa/tien-si-dong');
        }
    } else if (articleId === 'luoc-su-dong') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const targetPanel = document.getElementById('article-luocsudong-panel');
        if (targetPanel) targetPanel.classList.add('active');
        
        if (updateUrl) {
            history.pushState({ tabId: 'hang-hoa', articleId: 'luoc-su-dong' }, '', '/hang-hoa/luoc-su-dong');
        }
    } else {
        // Go back to list view
        articleView.classList.remove('active');
        listView.classList.add('active');
        
        if (updateUrl) {
            history.pushState({ tabId: 'hang-hoa', articleId: '' }, '', '/hang-hoa');
        }
    }
}
function openHomeArticle(articleId) {
    // Switch to Commodities tab without updating the URL yet
    switchTab('hang-hoa', false);
    // Open the commodity article and update the URL to its nested path
    openCommodityArticle(articleId, true);
}

function openHomeEventArticle(articleId) {
    switchTab('su-kien', false);
    openEventArticle(articleId, true);
}


// Router matching logic for paths
function handleRouting(path) {
    if (path.startsWith('/hang-hoa')) {
        switchTab('hang-hoa', false);
        const subPath = path.substring('/hang-hoa'.length);
        if (subPath === '/tien-si-dong') {
            openCommodityArticle('tien-si-dong', false);
        } else if (subPath === '/luoc-su-dong') {
            openCommodityArticle('luoc-su-dong', false);
        } else {
            openCommodityArticle('', false);
        }
    } else if (path.startsWith('/huyen-thoai')) {
        switchTab('huyen-thoai', false);
        const subPath = path.substring('/huyen-thoai'.length);
        if (subPath === '/jim-simons') {
            openLegendArticle('jim-simons', false);
        } else {
            openLegendArticle('', false);
        }
    } else if (path.startsWith('/su-kien')) {
        switchTab('su-kien', false);
        const subPath = path.substring('/su-kien'.length);
        if (subPath === '/chicxulub') {
            openEventArticle('chicxulub', false);
        } else {
            openEventArticle('', false);
        }
    } else {
        const tabId = routeToTab[path] || 'trang-chu';
        switchTab(tabId, false);
    }
}

function openEventArticle(articleId, updateUrl = true) {
    const listView   = document.getElementById('sukien-list-view');
    const articleView = document.getElementById('sukien-article-view');
    if (!listView || !articleView) return;

    document.querySelectorAll('.sukien-article-panel').forEach(p => p.classList.remove('active'));

    if (articleId === 'chicxulub') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-chicxulub-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'su-kien', articleId: 'chicxulub' }, '', '/su-kien/chicxulub');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        articleView.classList.remove('active');
        listView.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'su-kien', articleId: '' }, '', '/su-kien');
    }
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
        handleRouting(path);
    });

    // Handle initial load routing
    const initialPath = window.location.pathname;
    handleRouting(initialPath);
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
    tetrisInit();
});


// ============================================================
// TETRIS TÂN — GAME ENGINE
// ============================================================
const TETRIS = {
    // Board dimensions
    COLS: 10,
    ROWS: 20,
    // Difficulty: { label, dropInterval (ms), levelSpeedup (ms per level) }
    DIFFICULTIES: {
        easy:   { dropInterval: 700,  levelMs: 55  },
        medium: { dropInterval: 450,  levelMs: 38  },
        hard:   { dropInterval: 250,  levelMs: 22  },
        expert: { dropInterval: 120,  levelMs: 10  }
    },
    // Tetromino shapes [rotations][rows][cols], 4 rotations each
    PIECES: {
        I: { color: '#22d3ee', cells: [
            [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
            [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],
            [[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],
            [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]
        ]},
        O: { color: '#facc15', cells: [
            [[1,1],[1,1]],[[1,1],[1,1]],[[1,1],[1,1]],[[1,1],[1,1]]
        ]},
        T: { color: '#a855f7', cells: [
            [[0,1,0],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,1],[0,1,0]],
            [[0,0,0],[1,1,1],[0,1,0]],
            [[0,1,0],[1,1,0],[0,1,0]]
        ]},
        S: { color: '#4ade80', cells: [
            [[0,1,1],[1,1,0],[0,0,0]],
            [[0,1,0],[0,1,1],[0,0,1]],
            [[0,0,0],[0,1,1],[1,1,0]],
            [[1,0,0],[1,1,0],[0,1,0]]
        ]},
        Z: { color: '#f43f5e', cells: [
            [[1,1,0],[0,1,1],[0,0,0]],
            [[0,0,1],[0,1,1],[0,1,0]],
            [[0,0,0],[1,1,0],[0,1,1]],
            [[0,1,0],[1,1,0],[1,0,0]]
        ]},
        J: { color: '#6366f1', cells: [
            [[1,0,0],[1,1,1],[0,0,0]],
            [[0,1,1],[0,1,0],[0,1,0]],
            [[0,0,0],[1,1,1],[0,0,1]],
            [[0,1,0],[0,1,0],[1,1,0]]
        ]},
        L: { color: '#f97316', cells: [
            [[0,0,1],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,0],[0,1,1]],
            [[0,0,0],[1,1,1],[1,0,0]],
            [[1,1,0],[0,1,0],[0,1,0]]
        ]}
    },

    // --- State ---
    board: [],
    current: null,       // { type, rotation, x, y }
    next: null,
    held: null,
    canHold: true,
    score: 0,
    lines: 0,
    level: 1,
    best: 0,
    running: false,
    paused: false,
    difficulty: 'easy',
    dropTimer: null,
    dropInterval: 700,
    lastTime: 0,
    animFrameId: null,
    flashRows: [],

    // Canvas references
    canvas: null, ctx: null,
    nextCanvas: null, nextCtx: null,
    holdCanvas: null, holdCtx: null,

    // Piece bag for 7-bag randomizer
    bag: [],

    init() {
        this.canvas     = document.getElementById('tetris-canvas');
        this.nextCanvas = document.getElementById('tetris-next-canvas');
        this.holdCanvas = document.getElementById('tetris-hold-canvas');
        if (!this.canvas) return;
        this.ctx      = this.canvas.getContext('2d');
        this.nextCtx  = this.nextCanvas.getContext('2d');
        this.holdCtx  = this.holdCanvas.getContext('2d');
        this.best = parseInt(localStorage.getItem('tetris_best') || '0');
        this.updateDOM();
        this.drawBoard();
        this.setDifficulty(this.difficulty, false);
    },

    setDifficulty(diff, restart = true) {
        this.difficulty   = diff;
        this.dropInterval = this.DIFFICULTIES[diff].dropInterval;
        document.querySelectorAll('.diff-btn').forEach(b => b.classList.remove('active'));
        const btn = document.getElementById('diff-' + diff);
        if (btn) btn.classList.add('active');
        if (restart && this.running) this.start();
    },

    resetBoard() {
        this.board = Array.from({length: this.ROWS}, () => Array(this.COLS).fill(0));
        this.score = 0; this.lines = 0; this.level = 1;
        this.held = null; this.canHold = true;
        this.bag = [];
        this.current = this.spawnPiece();
        this.next    = this.spawnPiece();
        this.flashRows = [];
    },

    // 7-bag randomizer
    nextBag() {
        if (this.bag.length === 0) {
            this.bag = Object.keys(this.PIECES).sort(() => Math.random() - 0.5);
        }
        return this.bag.pop();
    },

    spawnPiece() {
        const type = this.nextBag();
        const piece = this.PIECES[type];
        const cells = piece.cells[0];
        const cols  = cells[0].length;
        return {
            type, rotation: 0,
            x: Math.floor((this.COLS - cols) / 2),
            y: 0
        };
    },

    getCells(piece) {
        return this.PIECES[piece.type].cells[piece.rotation];
    },
    getColor(type) {
        return this.PIECES[type].color;
    },

    // Check if a piece at (px,py) with given cells is valid
    isValid(cells, px, py) {
        for (let r = 0; r < cells.length; r++) {
            for (let c = 0; c < cells[r].length; c++) {
                if (!cells[r][c]) continue;
                const nx = px + c, ny = py + r;
                if (nx < 0 || nx >= this.COLS || ny >= this.ROWS) return false;
                if (ny >= 0 && this.board[ny][nx]) return false;
            }
        }
        return true;
    },

    // SRS wall kick data (J,L,S,T,Z and I share different tables)
    KICKS_JLSTZ: [
        [[0,0],[-1,0],[-1,1],[0,-2],[-1,-2]],
        [[0,0],[1,0],[1,-1],[0,2],[1,2]],
        [[0,0],[1,0],[1,1],[0,-2],[1,-2]],
        [[0,0],[-1,0],[-1,-1],[0,2],[-1,2]]
    ],
    KICKS_I: [
        [[0,0],[-2,0],[1,0],[-2,-1],[1,2]],
        [[0,0],[-1,0],[2,0],[-1,2],[2,-1]],
        [[0,0],[2,0],[-1,0],[2,1],[-1,-2]],
        [[0,0],[1,0],[-2,0],[1,-2],[-2,1]]
    ],

    tryRotate(dir) {
        if (!this.current || !this.running || this.paused) return;
        const p = this.current;
        const newRot = ((p.rotation + dir) + 4) % 4;
        const newCells = this.PIECES[p.type].cells[newRot];
        const kicks = p.type === 'I' ? this.KICKS_I : this.KICKS_JLSTZ;
        const table = kicks[p.rotation];

        for (const [kx, ky] of table) {
            const nx = p.x + kx, ny = p.y - ky;
            if (this.isValid(newCells, nx, ny)) {
                p.rotation = newRot;
                p.x = nx; p.y = ny;
                this.draw();
                return;
            }
        }
    },

    move(dx) {
        if (!this.current || !this.running || this.paused) return;
        const p = this.current;
        const cells = this.getCells(p);
        if (this.isValid(cells, p.x + dx, p.y)) {
            p.x += dx;
            this.draw();
        }
    },

    softDrop() {
        if (!this.current || !this.running || this.paused) return;
        this.drop(true);
    },

    hardDrop() {
        if (!this.current || !this.running || this.paused) return;
        const p = this.current;
        const cells = this.getCells(p);
        let dropY = p.y;
        while (this.isValid(cells, p.x, dropY + 1)) dropY++;
        const dropped = dropY - p.y;
        p.y = dropY;
        this.score += dropped * 2;
        this.lock();
    },

    ghostY() {
        if (!this.current) return this.current.y;
        const p = this.current;
        const cells = this.getCells(p);
        let gy = p.y;
        while (this.isValid(cells, p.x, gy + 1)) gy++;
        return gy;
    },

    hold() {
        if (!this.canHold || !this.current || !this.running || this.paused) return;
        const type = this.current.type;
        if (this.held) {
            // Swap
            const heldType = this.held;
            this.held = type;
            this.current = { type: heldType, rotation: 0, x: Math.floor((this.COLS - this.PIECES[heldType].cells[0][0].length) / 2), y: 0 };
        } else {
            this.held = type;
            this.current = this.next;
            this.next = this.spawnPiece();
        }
        this.canHold = false;
        this.draw();
    },

    drop(soft = false) {
        if (!this.current) return;
        const p = this.current;
        const cells = this.getCells(p);
        if (this.isValid(cells, p.x, p.y + 1)) {
            p.y++;
            if (soft) this.score += 1;
            this.draw();
        } else {
            this.lock();
        }
    },

    lock() {
        const p = this.current;
        const cells = this.getCells(p);
        // Place on board
        for (let r = 0; r < cells.length; r++) {
            for (let c = 0; c < cells[r].length; c++) {
                if (!cells[r][c]) continue;
                const ny = p.y + r, nx = p.x + c;
                if (ny < 0) { this.gameOver(); return; }
                this.board[ny][nx] = p.type;
            }
        }
        this.clearLines();
        this.canHold = true;
        this.current = this.next;
        this.next = this.spawnPiece();
        // Check game over
        const newCells = this.getCells(this.current);
        if (!this.isValid(newCells, this.current.x, this.current.y)) {
            this.gameOver(); return;
        }
        this.draw();
    },

    clearLines() {
        const full = [];
        for (let r = 0; r < this.ROWS; r++) {
            if (this.board[r].every(c => c !== 0)) full.push(r);
        }
        if (!full.length) return;

        // Scoring: 1=100, 2=300, 3=500, 4=800 (× level)
        const pts = [0, 100, 300, 500, 800];
        this.score += (pts[full.length] || 800) * this.level;
        this.lines += full.length;
        this.level = Math.floor(this.lines / 10) + 1;

        // Speed up per level
        const cfg = this.DIFFICULTIES[this.difficulty];
        this.dropInterval = Math.max(50, cfg.dropInterval - (this.level - 1) * cfg.levelMs);

        // Remove full rows and add empty ones at top
        for (const r of full) this.board.splice(r, 1);
        while (this.board.length < this.ROWS) this.board.unshift(Array(this.COLS).fill(0));

        this.updateDOM();

        // Flash animation
        this.flashRows = full;
        setTimeout(() => { this.flashRows = []; this.draw(); }, 120);
    },

    gameOver() {
        this.running = false;
        cancelAnimationFrame(this.animFrameId);
        if (this.score > this.best) {
            this.best = this.score;
            localStorage.setItem('tetris_best', this.best);
            document.getElementById('tetris-best').textContent = this.best.toLocaleString();
        }
        // Show overlay
        const overlay = document.getElementById('tetris-overlay');
        const msg = document.getElementById('tetris-overlay-msg');
        const scoreEl = document.getElementById('tetris-overlay-score');
        const btn = document.getElementById('tetris-play-btn');
        if (overlay) {
            msg.textContent = 'Game Over!';
            scoreEl.style.display = 'block';
            scoreEl.textContent = `Điểm: ${this.score.toLocaleString()} | Hàng: ${this.lines}`;
            btn.innerHTML = '<i class="fa-solid fa-rotate-right"></i> CHƠI LẠI';
            overlay.classList.add('active');
        }
        const pauseBtn = document.getElementById('tetris-pause-btn');
        if (pauseBtn) pauseBtn.style.display = 'none';
    },

    start() {
        this.running = false;
        cancelAnimationFrame(this.animFrameId);
        this.resetBoard();
        this.running = true;
        this.paused  = false;
        this.lastTime = performance.now();

        // Hide overlay
        const overlay = document.getElementById('tetris-overlay');
        if (overlay) overlay.classList.remove('active');

        // Show pause btn
        const pauseBtn = document.getElementById('tetris-pause-btn');
        if (pauseBtn) pauseBtn.style.display = 'flex';

        this.updateDOM();
        this.loop(performance.now());
    },

    loop(now) {
        if (!this.running) return;
        const delta = now - this.lastTime;
        if (!this.paused && delta >= this.dropInterval) {
            this.drop();
            this.lastTime = now;
        }
        this.draw();
        this.animFrameId = requestAnimationFrame(ts => this.loop(ts));
    },

    pause() {
        if (!this.running) return;
        this.paused = !this.paused;
        const icon  = document.getElementById('tetris-pause-icon');
        const label = document.getElementById('tetris-pause-label');
        if (this.paused) {
            if (icon) icon.className = 'fa-solid fa-play';
            if (label) label.textContent = 'Tiếp tục';
        } else {
            if (icon) icon.className = 'fa-solid fa-pause';
            if (label) label.textContent = 'Tạm dừng';
            this.lastTime = performance.now();
        }
        this.draw();
    },

    updateDOM() {
        const fmt = n => n.toLocaleString();
        const el = id => document.getElementById(id);
        if (el('tetris-score')) el('tetris-score').textContent = fmt(this.score);
        if (el('tetris-level')) el('tetris-level').textContent = this.level;
        if (el('tetris-lines')) el('tetris-lines').textContent = this.lines;
        if (el('tetris-best'))  el('tetris-best').textContent  = fmt(this.best);
    },

    // --- DRAWING ---
    cellSize() {
        return this.canvas.width / this.COLS; // canvas logical width = 300, COLS=10 → 30px
    },

    drawBoard() {
        const ctx = this.ctx;
        const cs  = this.cellSize();
        ctx.fillStyle = '#050810';
        ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Grid lines
        ctx.strokeStyle = 'rgba(255,255,255,0.04)';
        ctx.lineWidth = 0.5;
        for (let c = 0; c <= this.COLS; c++) {
            ctx.beginPath(); ctx.moveTo(c * cs, 0); ctx.lineTo(c * cs, this.canvas.height); ctx.stroke();
        }
        for (let r = 0; r <= this.ROWS; r++) {
            ctx.beginPath(); ctx.moveTo(0, r * cs); ctx.lineTo(this.canvas.width, r * cs); ctx.stroke();
        }

        // Locked cells
        for (let r = 0; r < this.ROWS; r++) {
            for (let c = 0; c < this.COLS; c++) {
                if (this.board[r][c]) {
                    const flash = this.flashRows.includes(r);
                    this.drawCell(ctx, c, r, this.getColor(this.board[r][c]), cs, flash);
                }
            }
        }
    },

    drawCell(ctx, cx, cy, color, cs, flash = false) {
        const x = cx * cs, y = cy * cs;
        if (flash) {
            ctx.fillStyle = '#ffffff';
            ctx.fillRect(x, y, cs, cs);
            return;
        }
        // Cell fill
        ctx.fillStyle = color;
        ctx.fillRect(x + 1, y + 1, cs - 2, cs - 2);
        // Highlight (top-left)
        ctx.fillStyle = 'rgba(255,255,255,0.28)';
        ctx.fillRect(x + 1, y + 1, cs - 2, 3);
        ctx.fillRect(x + 1, y + 1, 3, cs - 2);
        // Shadow (bottom-right)
        ctx.fillStyle = 'rgba(0,0,0,0.3)';
        ctx.fillRect(x + 1, y + cs - 4, cs - 2, 3);
        ctx.fillRect(x + cs - 4, y + 1, 3, cs - 2);
    },

    draw() {
        this.drawBoard();
        const ctx = this.ctx;
        const cs  = this.cellSize();

        if (this.paused) {
            ctx.fillStyle = 'rgba(5,8,16,0.7)';
            ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
            ctx.fillStyle = '#f8fafc';
            ctx.font = `bold ${cs * 1.4}px monospace`;
            ctx.textAlign = 'center';
            ctx.fillText('⏸ TẠM DỪNG', this.canvas.width / 2, this.canvas.height / 2);
            return;
        }

        if (!this.current) return;

        // Ghost piece
        const gy = this.ghostY();
        const gCells = this.getCells(this.current);
        const gColor = this.getColor(this.current.type);
        for (let r = 0; r < gCells.length; r++) {
            for (let c = 0; c < gCells[r].length; c++) {
                if (!gCells[r][c]) continue;
                const gx = (this.current.x + c) * cs;
                const gcy = (gy + r) * cs;
                ctx.strokeStyle = gColor;
                ctx.lineWidth = 1;
                ctx.globalAlpha = 0.35;
                ctx.strokeRect(gx + 1, gcy + 1, cs - 2, cs - 2);
                ctx.globalAlpha = 1;
            }
        }

        // Active piece
        const cells = this.getCells(this.current);
        const color = this.getColor(this.current.type);
        for (let r = 0; r < cells.length; r++) {
            for (let c = 0; c < cells[r].length; c++) {
                if (!cells[r][c]) continue;
                this.drawCell(ctx, this.current.x + c, this.current.y + r, color, cs);
            }
        }

        // Draw preview canvases
        this.drawPreview(this.nextCtx, this.nextCanvas, this.next ? this.next.type : null);
        this.drawPreview(this.holdCtx, this.holdCanvas, this.held);
    },

    drawPreview(ctx, canvas, type) {
        ctx.fillStyle = '#050810';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        if (!type) return;
        const cells = this.PIECES[type].cells[0];
        const color = this.getColor(type);
        const rows = cells.length, cols = cells[0].length;
        const cs = Math.min(Math.floor(canvas.width / (cols + 1)), Math.floor(canvas.height / (rows + 1)));
        const ox = Math.floor((canvas.width  - cols * cs) / 2);
        const oy = Math.floor((canvas.height - rows * cs) / 2);
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (!cells[r][c]) continue;
                ctx.fillStyle = color;
                ctx.fillRect(ox + c * cs + 1, oy + r * cs + 1, cs - 2, cs - 2);
                ctx.fillStyle = 'rgba(255,255,255,0.28)';
                ctx.fillRect(ox + c * cs + 1, oy + r * cs + 1, cs - 2, 3);
                ctx.fillRect(ox + c * cs + 1, oy + r * cs + 1, 3, cs - 2);
            }
        }
    },

    // Input handler
    handleInput(action) {
        switch (action) {
            case 'left':   this.move(-1);      break;
            case 'right':  this.move(1);       break;
            case 'down':   this.softDrop();    break;
            case 'drop':   this.hardDrop();    break;
            case 'rotate': this.tryRotate(1);  break;
            case 'hold':   this.hold();        break;
            case 'pause':  this.pause();       break;
        }
    },

    toggleFullscreen() {
        const el = document.getElementById('tetris-wrapper');
        if (!el) return;
        const fsEl = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement;
        if (!fsEl) {
            const req = el.requestFullscreen || el.webkitRequestFullscreen || el.mozRequestFullScreen;
            if (req) req.call(el);
        } else {
            const exit = document.exitFullscreen || document.webkitExitFullscreen || document.mozCancelFullScreen;
            if (exit) exit.call(document);
        }
    },

    bindKeys() {
        document.addEventListener('keydown', (e) => {
            // Only intercept when game tab is active
            const gamePanel = document.getElementById('panel-game');
            if (!gamePanel || !gamePanel.classList.contains('active')) return;
            if (!this.running) return;

            switch (e.key) {
                case 'ArrowLeft':  e.preventDefault(); this.move(-1);     break;
                case 'ArrowRight': e.preventDefault(); this.move(1);      break;
                case 'ArrowDown':  e.preventDefault(); this.softDrop();   break;
                case 'ArrowUp':    e.preventDefault(); this.tryRotate(1); break;
                case ' ':          e.preventDefault(); this.hardDrop();   break;
                case 'c': case 'C': this.hold();   break;
                case 'p': case 'P': this.pause();  break;
            }
        });
    }
};

// --- Global wrappers for HTML onclick / external calls ---
function tetrisInit()             { TETRIS.init(); TETRIS.bindKeys(); }
function tetrisStart()            { TETRIS.start(); }
function tetrisPause()            { TETRIS.pause(); }
function tetrisInput(action)      { TETRIS.handleInput(action); }
function tetrisToggleFullscreen() { TETRIS.toggleFullscreen(); }
function tetrisSetDifficulty(d)   { TETRIS.setDifficulty(d, false); }

function openLegendArticle(articleId, updateUrl = true) {
    const listView = document.getElementById('huyen-thoai-list-view');
    const articleView = document.getElementById('huyen-thoai-article-view');
    if (!listView || !articleView) return;

    document.querySelectorAll('.sukien-article-panel').forEach(p => p.classList.remove('active'));

    if (articleId === 'jim-simons') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-jimsimons-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'jim-simons' }, '', '/huyen-thoai/jim-simons');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        articleView.classList.remove('active');
        listView.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: '' }, '', '/huyen-thoai');
    }
}

function openHomeLegendArticle(articleId) {
    switchTab('huyen-thoai', false);
    openLegendArticle(articleId, true);
}
