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
    '/thu-vien': 'thu-vien',
    '/game': 'game'
};

const tabToRoute = {
    'trang-chu': '/',
    'vi-mo': '/vi-mo',
    'hang-hoa': '/hang-hoa',
    'su-kien': '/su-kien',
    'huyen-thoai': '/huyen-thoai',
    'thu-vien': '/thu-vien',
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

    // Handle sub-view routing per tab
    if (tabId === 'hang-hoa' && updateUrl) {
        // Hang hoa: reset to list view and push URL
        openCommodityArticle('', true);
    } else if (tabId === 'su-kien' && updateUrl) {
        // Su kien: reset to list view and push URL
        openEventArticle('', true);
    } else if (tabId === 'huyen-thoai' && updateUrl) {
        // Huyen thoai: reset to list view and push URL
        openLegendArticle('', true);
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
function handleRouting(path, updateUrl = false) {
    if (path.startsWith('/hang-hoa')) {
        switchTab('hang-hoa', false);
        const subPath = path.substring('/hang-hoa'.length);
        if (subPath === '/tien-si-dong') {
            openCommodityArticle('tien-si-dong', updateUrl);
        } else if (subPath === '/luoc-su-dong') {
            openCommodityArticle('luoc-su-dong', updateUrl);
        } else {
            openCommodityArticle('', updateUrl);
        }
    } else if (path.startsWith('/huyen-thoai')) {
        switchTab('huyen-thoai', false);
        const subPath = path.substring('/huyen-thoai'.length);
        if (subPath === '/jim-simons') {
            openLegendArticle('jim-simons', updateUrl);
        } else if (subPath === '/richard-wyckoff') {
            openLegendArticle('richard-wyckoff', updateUrl);
        } else if (subPath === '/warren-buffett') {
            openLegendArticle('warren-buffett', updateUrl);
        } else {
            openLegendArticle('', updateUrl);
        }
    } else if (path.startsWith('/su-kien')) {
        switchTab('su-kien', false);
        const subPath = path.substring('/su-kien'.length);
        if (subPath === '/chicxulub') {
            openEventArticle('chicxulub', updateUrl);
        } else {
            openEventArticle('', updateUrl);
        }
    } else {
        const tabId = routeToTab[path] || 'trang-chu';
        switchTab(tabId, updateUrl);
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

    // Intercept click on all article cards — route via SPA (keeps href for right-click → new tab)
    document.querySelectorAll('.clickable-card').forEach(card => {
        card.addEventListener('click', (e) => {
            // Allow modifier-key clicks (Ctrl/Cmd/middle-click) to open in new tab natively
            if (e.ctrlKey || e.metaKey || e.shiftKey || e.button === 1) return;
            e.preventDefault();
            const path = card.getAttribute('href');
            if (path) handleRouting(path, true);
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
// RETRO HANDHELD TETRIS GAME ENGINE
// ============================================================
const TETRIS = {
    state: 'start', // start | playing | paused | gameOver
    board: [],
    current: null,
    nextType_: null,
    score: 0,
    level: 1,
    lines: 0,
    gravityAcc: 0,
    softDropping: false,
    audioCtx: null,
    muted: false,
    lastTs: 0,
    
    // Board config
    COLS: 10,
    ROWS: 20,
    CELL: 24,
    NEXT_CELL: 14,
    
    SHAPES: {
        I: [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
        O: [[1,1],[1,1]],
        T: [[0,1,0],[1,1,1],[0,0,0]],
        S: [[0,1,1],[1,1,0],[0,0,0]],
        Z: [[1,1,0],[0,1,1],[0,0,0]],
        J: [[1,0,0],[1,1,1],[0,0,0]],
        L: [[0,0,1],[1,1,1],[0,0,0]],
    },
    PIECE_TYPES: ['I','O','T','S','Z','J','L'],
    LINES_PER_LEVEL: 10,
    SOFT_DROP_INTERVAL: 45,
    DAS_DELAY: 170,
    DAS_REPEAT: 50,
    
    heldKeys: {},
    repeatTimers: {},
    bag: [],

    init() {
        this.boardCanvas = document.getElementById('boardCanvas');
        if (!this.boardCanvas) return;
        this.bctx = this.boardCanvas.getContext('2d');
        this.nextCanvas = document.getElementById('nextCanvas');
        this.nctx = this.nextCanvas.getContext('2d');

        this.scoreValueEl = document.getElementById('scoreValue');
        this.levelValueEl = document.getElementById('levelValue');
        this.linesValueEl = document.getElementById('linesValue');
        this.powerLed = document.getElementById('powerLed');

        this.overlay = document.getElementById('overlay');
        this.overlayMsg = document.getElementById('overlayMsg');
        this.overlaySub = document.getElementById('overlaySub');

        this.btnStartPause = document.getElementById('btnStartPause');
        this.btnMute = document.getElementById('btnMute');
        this.btnUp = document.getElementById('btnUp');
        this.btnLeft = document.getElementById('btnLeft');
        this.btnRight = document.getElementById('btnRight');
        this.btnDown = document.getElementById('btnDown');
        this.btnRotate = document.getElementById('btnRotate');
        this.btnDrop = document.getElementById('btnDrop');

        const isTouchDevice = window.matchMedia('(hover: none) and (pointer: coarse)').matches;
        const hintEl = document.getElementById('controlsHint');
        if (hintEl) {
            hintEl.innerHTML = isTouchDevice
                ? 'Chạm các nút trên máy để chơi — <b>▲</b> xoay, <b>▼</b> rơi nhanh.'
                : 'Dùng <b>phím mũi tên</b> để di chuyển/xoay, <b>Space</b> để thả nhanh, <b>P</b> tạm dừng.';
        }

        // Set up canvas resize and retina scaling
        this.fitCanvases();
        window.addEventListener('resize', () => this.fitCanvases());

        // Bind UI actions
        this.bindEvents();

        this.newGame();
        this.draw();

        // Start game loop
        this.lastTs = 0;
        const loop = (ts) => {
            this.tick(ts);
            requestAnimationFrame(loop);
        };
        requestAnimationFrame(loop);
        
        // Fullscreen listener
        const handleFullscreenChange = () => {
            const el = document.getElementById('tetris-wrapper');
            if (!el) return;
            const isFS = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement);
            if (!isFS) {
                el.classList.remove('is-fullscreen');
                document.body.style.overflow = '';
            } else {
                el.classList.add('is-fullscreen');
            }
        };
        document.addEventListener('fullscreenchange', handleFullscreenChange);
        document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
        document.addEventListener('mozfullscreenchange', handleFullscreenChange);
    },

    fitCanvases() {
        if (!this.boardCanvas || !this.nextCanvas) return;
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        this.boardCanvas.width = this.COLS * this.CELL * dpr;
        this.boardCanvas.height = this.ROWS * this.CELL * dpr;
        this.bctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        this.nextCanvas.width = 4 * this.NEXT_CELL * dpr;
        this.nextCanvas.height = 4 * this.NEXT_CELL * dpr;
        this.nctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    },

    // 8-bit Sound effects
    ensureAudio() {
        if (!this.audioCtx) {
            try {
                this.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            } catch (e) {
                this.audioCtx = null;
            }
        } else if (this.audioCtx.state === 'suspended') {
            this.audioCtx.resume();
        }
    },

    beep(freq, duration, gainPeak, delay) {
        if (!this.audioCtx || this.muted) return;
        const t0 = this.audioCtx.currentTime + (delay || 0);
        const osc = this.audioCtx.createOscillator();
        const gain = this.audioCtx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(freq, t0);
        gain.gain.setValueAtTime(0, t0);
        gain.gain.linearRampToValueAtTime(gainPeak || 0.12, t0 + 0.01);
        gain.gain.exponentialRampToValueAtTime(0.001, t0 + duration);
        osc.connect(gain).connect(this.audioCtx.destination);
        osc.start(t0);
        osc.stop(t0 + duration + 0.02);
    },

    sfxMove() { this.beep(220, 0.04, 0.07); },
    sfxRotate() { this.beep(380, 0.05, 0.08); },
    sfxLock() { this.beep(140, 0.06, 0.10); },
    sfxLineClear(n) {
        const base = 500;
        for (let i = 0; i < n; i++) this.beep(base + i * 160, 0.10, 0.14, i * 0.06);
    },
    sfxLevelUp() { [0, 0.08, 0.16].forEach((d, i) => this.beep(440 + i * 220, 0.12, 0.13, d)); },
    sfxGameOver() {
        this.beep(200, 0.25, 0.15);
        this.beep(140, 0.35, 0.14, 0.18);
        this.beep(90, 0.45, 0.13, 0.36);
    },
    sfxHardDrop() { this.beep(110, 0.08, 0.14); },

    // Utils
    rotateMatrix(m) {
        const n = m.length;
        const res = Array.from({length: n}, () => Array(n).fill(0));
        for (let y = 0; y < n; y++) {
            for (let x = 0; x < n; x++) {
                res[x][n - 1 - y] = m[y][x];
            }
        }
        return res;
    },

    cloneMatrix(m) {
        return m.map(row => row.slice());
    },

    pad(n, len) {
        return String(n).padStart(len, '0');
    },

    nextType() {
        if (this.bag.length === 0) {
            this.bag = this.PIECE_TYPES.slice();
            for (let i = this.bag.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [this.bag[i], this.bag[j]] = [this.bag[j], this.bag[i]];
            }
        }
        return this.bag.pop();
    },

    createEmptyBoard() {
        return Array.from({length: this.ROWS}, () => Array(this.COLS).fill(0));
    },

    spawnPiece(type) {
        const matrix = this.cloneMatrix(this.SHAPES[type]);
        const col = Math.floor((this.COLS - matrix.length) / 2);
        return { type, matrix, row: 0, col };
    },

    newGame() {
        this.board = this.createEmptyBoard();
        this.score = 0;
        this.level = 1;
        this.lines = 0;
        this.gravityAcc = 0;
        this.bag = [];
        this.current = this.spawnPiece(this.nextType());
        this.nextType_ = this.nextType();
        this.updateHUD();
    },

    spawnNext() {
        this.current = this.spawnPiece(this.nextType_);
        this.nextType_ = this.nextType();
        if (this.collides(this.current.matrix, this.current.row, this.current.col)) {
            this.enterGameOver();
        }
    },

    collides(matrix, row, col) {
        for (let y = 0; y < matrix.length; y++) {
            for (let x = 0; x < matrix.length; x++) {
                if (!matrix[y][x]) continue;
                const r = row + y, c = col + x;
                if (c < 0 || c >= this.COLS || r >= this.ROWS) return true;
                if (r >= 0 && this.board[r][c]) return true;
            }
        }
        return false;
    },

    tryMove(dx) {
        if (this.state !== 'playing') return;
        const col = this.current.col + dx;
        if (!this.collides(this.current.matrix, this.current.row, col)) {
            this.current.col = col;
            this.sfxMove();
        }
    },

    tryRotate() {
        if (this.state !== 'playing') return;
        const rotated = this.rotateMatrix(this.current.matrix);
        const kicks = [0, -1, 1, -2, 2];
        for (const k of kicks) {
            if (!this.collides(rotated, this.current.row, this.current.col + k)) {
                this.current.matrix = rotated;
                this.current.col += k;
                this.sfxRotate();
                return;
            }
        }
    },

    softDropStep() {
        if (this.state !== 'playing') return;
        const row = this.current.row + 1;
        if (!this.collides(this.current.matrix, row, this.current.col)) {
            this.current.row = row;
            if (this.softDropping) this.score += 1;
        } else {
            this.lockPiece();
        }
        this.updateHUD();
    },

    hardDrop() {
        if (this.state !== 'playing') return;
        let cells = 0;
        while (!this.collides(this.current.matrix, this.current.row + 1, this.current.col)) {
            this.current.row += 1;
            cells += 1;
        }
        this.score += cells * 2;
        this.sfxHardDrop();
        this.lockPiece();
        this.updateHUD();
    },

    lockPiece() {
        const m = this.current.matrix;
        for (let y = 0; y < m.length; y++) {
            for (let x = 0; x < m.length; x++) {
                if (!m[y][x]) continue;
                const r = this.current.row + y, c = this.current.col + x;
                if (r >= 0 && r < this.ROWS && c >= 0 && c < this.COLS) this.board[r][c] = 1;
            }
        }
        this.sfxLock();
        this.clearLines();
        this.spawnNext();
    },

    clearLines() {
        let cleared = 0;
        for (let r = this.ROWS - 1; r >= 0; r--) {
            if (this.board[r].every(cell => cell)) {
                this.board.splice(r, 1);
                this.board.unshift(Array(this.COLS).fill(0));
                cleared++;
                r++;
            }
        }
        if (cleared > 0) {
            const table = {1: 100, 2: 300, 3: 500, 4: 800};
            this.score += (table[cleared] || 800) * this.level;
            this.lines += cleared;
            const newLevel = Math.floor(this.lines / this.LINES_PER_LEVEL) + 1;
            if (newLevel > this.level) {
                this.level = newLevel;
                this.sfxLevelUp();
            }
            this.sfxLineClear(cleared);
        }
        this.updateHUD();
    },

    ghostRow() {
        let r = this.current.row;
        while (!this.collides(this.current.matrix, r + 1, this.current.col)) r++;
        return r;
    },

    updateHUD() {
        if (this.scoreValueEl) this.scoreValueEl.textContent = this.pad(Math.min(this.score, 999999), 6);
        if (this.levelValueEl) this.levelValueEl.textContent = this.pad(this.level, 2);
        if (this.linesValueEl) this.linesValueEl.textContent = this.pad(Math.min(this.lines, 999), 3);
    },

    showOverlay(msg, sub, blink) {
        if (!this.overlay) return;
        this.overlayMsg.textContent = msg;
        this.overlayMsg.classList.toggle('blink', !!blink);
        this.overlaySub.innerHTML = sub || '';
        this.overlay.classList.remove('hidden');
    },

    hideOverlay() {
        if (this.overlay) this.overlay.classList.add('hidden');
    },

    startGame() {
        this.ensureAudio();
        this.newGame();
        this.state = 'playing';
        this.hideOverlay();
        if (this.powerLed) this.powerLed.classList.add('on');
        if (this.btnStartPause) this.btnStartPause.textContent = 'PAUSE';
        this.lastTs = 0;
    },

    togglePause() {
        if (this.state === 'playing') {
            this.state = 'paused';
            this.showOverlay('TẠM DỪNG', 'NHẤN START<br>ĐỂ TIẾP TỤC');
            if (this.powerLed) this.powerLed.classList.remove('on');
            if (this.btnStartPause) this.btnStartPause.textContent = 'START';
        } else if (this.state === 'paused') {
            this.state = 'playing';
            this.hideOverlay();
            if (this.powerLed) this.powerLed.classList.add('on');
            if (this.btnStartPause) this.btnStartPause.textContent = 'PAUSE';
            this.lastTs = 0;
        }
    },

    enterGameOver() {
        this.state = 'gameOver';
        this.sfxGameOver();
        if (this.powerLed) this.powerLed.classList.remove('on');
        this.showOverlay('GAME OVER', 'ĐIỂM: ' + this.pad(this.score, 6) + '<br>NHẤN START<br>ĐỂ CHƠI LẠI');
        if (this.btnStartPause) this.btnStartPause.textContent = 'START';
    },

    // Keyboard and tap repeat logic
    startRepeat(key, fn) {
        if (this.heldKeys[key]) return;
        this.heldKeys[key] = true;
        fn();
        this.repeatTimers[key] = setTimeout(() => {
            const rep = () => {
                if (!this.heldKeys[key]) return;
                fn();
                this.repeatTimers[key] = setTimeout(rep, this.DAS_REPEAT);
            };
            rep();
        }, this.DAS_DELAY);
    },

    stopRepeat(key) {
        this.heldKeys[key] = false;
        clearTimeout(this.repeatTimers[key]);
    },

    bindEvents() {
        // Mute button
        if (this.btnMute) {
            this.btnMute.onclick = () => {
                this.muted = !this.muted;
                this.btnMute.textContent = this.muted ? '🔇' : '🔊';
            };
        }

        // Start/Pause Button
        if (this.btnStartPause) {
            this.btnStartPause.onclick = () => {
                this.ensureAudio();
                if (this.state === 'start' || this.state === 'gameOver') {
                    this.startGame();
                } else {
                    this.togglePause();
                }
            };
        }

        // Controls binding function
        const bindHoldButton = (el, key, fn) => {
            if (!el) return;
            el.addEventListener('pointerdown', (e) => {
                this.ensureAudio();
                e.preventDefault();
                this.startRepeat(key, fn);
            });
            ['pointerup', 'pointerleave', 'pointercancel'].forEach(ev => {
                el.addEventListener(ev, () => this.stopRepeat(key));
            });
        };

        const bindTapButton = (el, fn) => {
            if (!el) return;
            el.addEventListener('pointerdown', (e) => {
                this.ensureAudio();
                e.preventDefault();
                fn();
            });
        };

        // Pointer controls
        bindHoldButton(this.btnLeft, 'left', () => this.tryMove(-1));
        bindHoldButton(this.btnRight, 'right', () => this.tryMove(1));
        bindTapButton(this.btnUp, () => this.tryRotate());
        bindTapButton(this.btnRotate, () => this.tryRotate());
        bindTapButton(this.btnDrop, () => this.hardDrop());

        if (this.btnDown) {
            this.btnDown.addEventListener('pointerdown', (e) => {
                this.ensureAudio();
                e.preventDefault();
                this.softDropping = true;
            });
            ['pointerup', 'pointerleave', 'pointercancel'].forEach(ev => {
                this.btnDown.addEventListener(ev, () => {
                    this.softDropping = false;
                });
            });
        }

        // Keyboard bindings
        window.addEventListener('keydown', (e) => {
            const gamePanel = document.getElementById('panel-game');
            if (!gamePanel || !gamePanel.classList.contains('active')) return;
            
            this.ensureAudio();
            const k = e.key;
            if (k === 'Enter') {
                if (this.state === 'start' || this.state === 'gameOver') this.startGame();
                return;
            }
            if (k === 'p' || k === 'P' || k === 'Escape') {
                if (this.state === 'playing' || this.state === 'paused') this.togglePause();
                return;
            }
            if (this.state !== 'playing') return;
            if (k === 'ArrowLeft') { this.startRepeat('left', () => this.tryMove(-1)); e.preventDefault(); }
            else if (k === 'ArrowRight') { this.startRepeat('right', () => this.tryMove(1)); e.preventDefault(); }
            else if (k === 'ArrowUp') { if (!this.heldKeys['up']) { this.heldKeys['up'] = true; this.tryRotate(); } e.preventDefault(); }
            else if (k === 'ArrowDown') { this.softDropping = true; e.preventDefault(); }
            else if (k === ' ') { this.hardDrop(); e.preventDefault(); }
        });

        window.addEventListener('keyup', (e) => {
            const k = e.key;
            if (k === 'ArrowLeft') this.stopRepeat('left');
            else if (k === 'ArrowRight') this.stopRepeat('right');
            else if (k === 'ArrowUp') this.heldKeys['up'] = false;
            else if (k === 'ArrowDown') this.softDropping = false;
        });
    },

    gravityIntervalMs() {
        return Math.max(90, 800 - (this.level - 1) * 60);
    },

    tick(ts) {
        if (!this.lastTs) this.lastTs = ts;
        const dt = Math.min(ts - this.lastTs, 50);
        this.lastTs = ts;

        if (this.state === 'playing') {
            const interval = this.softDropping ? this.SOFT_DROP_INTERVAL : this.gravityIntervalMs();
            this.gravityAcc += dt;
            while (this.gravityAcc >= interval) {
                this.gravityAcc -= interval;
                this.softDropStep();
                if (this.state !== 'playing') break;
            }
        }

        this.draw();
    },

    // Retro LCD dot-matrix rendering
    INK_ACTIVE: '#232b18',
    INK_LOCKED: '#3c4a2c',
    INK_OFF: 'rgba(60,74,44,0.14)',
    INK_GHOST: 'rgba(60,74,44,0.32)',

    paintCell(c, col, row, size, fill) {
        const pad = size * 0.07;
        const x = col * size, y = row * size;
        c.fillStyle = fill;
        c.beginPath();
        const r = size * 0.18;
        c.moveTo(x + pad + r, y + pad);
        c.arcTo(x + size - pad, y + pad, x + size - pad, y + size - pad, r);
        c.arcTo(x + size - pad, y + size - pad, x + pad, y + size - pad, r);
        c.arcTo(x + pad, y + size - pad, x + pad, y + pad, r);
        c.arcTo(x + pad, y + pad, x + size - pad, y + pad, r);
        c.closePath();
        c.fill();
    },

    draw() {
        if (!this.bctx || !this.nctx) return;
        
        // Clear and draw board background
        this.bctx.clearRect(0, 0, this.COLS * this.CELL, this.ROWS * this.CELL);
        for (let r = 0; r < this.ROWS; r++) {
            for (let c = 0; c < this.COLS; c++) {
                this.paintCell(this.bctx, c, r, this.CELL, this.board[r][c] ? this.INK_LOCKED : this.INK_OFF);
            }
        }

        if (this.current && (this.state === 'playing' || this.state === 'paused')) {
            // Draw ghost piece
            const gRow = this.ghostRow();
            const m = this.current.matrix;
            for (let y = 0; y < m.length; y++) {
                for (let x = 0; x < m.length; x++) {
                    if (!m[y][x]) continue;
                    const r = gRow + y, c = this.current.col + x;
                    if (r >= 0 && r < this.ROWS && c >= 0 && c < this.COLS && r !== this.current.row + y) {
                        this.paintCell(this.bctx, c, r, this.CELL, this.INK_GHOST);
                    }
                }
            }

            // Draw active piece
            for (let y = 0; y < m.length; y++) {
                for (let x = 0; x < m.length; x++) {
                    if (!m[y][x]) continue;
                    const r = this.current.row + y, c = this.current.col + x;
                    if (r >= 0 && r < this.ROWS && c >= 0 && c < this.COLS) {
                        this.paintCell(this.bctx, c, r, this.CELL, this.INK_ACTIVE);
                    }
                }
            }
        }

        // Draw next piece preview
        this.nctx.clearRect(0, 0, 4 * this.NEXT_CELL, 4 * this.NEXT_CELL);
        for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 4; c++) {
                this.paintCell(this.nctx, c, r, this.NEXT_CELL, this.INK_OFF);
            }
        }
        if (this.nextType_) {
            const m = this.SHAPES[this.nextType_];
            const offset = Math.floor((4 - m.length) / 2);
            for (let y = 0; y < m.length; y++) {
                for (let x = 0; x < m.length; x++) {
                    if (!m[y][x]) continue;
                    this.paintCell(this.nctx, x + offset, y + offset, this.NEXT_CELL, this.INK_LOCKED);
                }
            }
        }
    },

    toggleFullscreen() {
        const el = document.getElementById('tetris-wrapper');
        if (!el) return;
        const fsEl = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement;
        
        const req = el.requestFullscreen || el.webkitRequestFullscreen || el.mozRequestFullScreen;
        const exit = document.exitFullscreen || document.webkitExitFullscreen || document.mozCancelFullScreen;

        if (req) {
            if (!fsEl) {
                req.call(el).then(() => {
                    el.classList.add('is-fullscreen');
                }).catch(err => {
                    el.classList.toggle('is-fullscreen');
                    document.body.style.overflow = el.classList.contains('is-fullscreen') ? 'hidden' : '';
                });
            } else {
                if (exit) {
                    exit.call(document);
                    el.classList.remove('is-fullscreen');
                    document.body.style.overflow = '';
                }
            }
        } else {
            el.classList.toggle('is-fullscreen');
            document.body.style.overflow = el.classList.contains('is-fullscreen') ? 'hidden' : '';
            if (el.classList.contains('is-fullscreen')) {
                window.scrollTo(0, 0);
            }
        }
    }
};

function tetrisInit()             { TETRIS.init(); }
function tetrisToggleFullscreen() { TETRIS.toggleFullscreen(); }
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
    } else if (articleId === 'richard-wyckoff') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-richard-wyckoff-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'richard-wyckoff' }, '', '/huyen-thoai/richard-wyckoff');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (articleId === 'warren-buffett') {
        listView.classList.remove('active');
        articleView.classList.add('active');
        const panel = document.getElementById('article-warren-buffett-panel');
        if (panel) panel.classList.add('active');
        if (updateUrl) history.pushState({ tabId: 'huyen-thoai', articleId: 'warren-buffett' }, '', '/huyen-thoai/warren-buffett');
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
