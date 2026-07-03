# Nguyên tắc làm việc (Behavioral Guidelines)

Behavioral guidelines to reduce common LLM coding mistakes.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

# Quy tắc làm việc với dự án tandt-Cloudflare-Pages

## 1. Cấu trúc trang web

- Tất cả nội dung nằm trong một file `index.html` duy nhất (~1.4MB).
- CSS chung nằm trong `style.css` (dark mode theme toàn trang).
- Mỗi bài viết là một `<div id="article-xxx-panel">` nằm thẳng trong `index.html`.
- JavaScript điều khiển hiển thị/ẩn các panel trong `script.js`.

---

## 2. QUY TẮC QUAN TRỌNG NHẤT: CSS của bài viết phải được đóng khung hoàn toàn

**Vấn đề đã gặp nhiều lần:** Khi thêm bài viết mới vào `index.html`, nếu CSS của bài viết không được đóng khung đúng cách, các quy tắc như `* { margin: 0; padding: 0 }` sẽ **áp dụng ra toàn bộ trang web**, làm vỡ layout, thu hẹp trang, và ẩn mất các tab điều hướng (tab Game, v.v.).

**Cách ĐÚNG — Bắt buộc dùng CSS Nesting:**

Tất cả CSS của bài viết phải được bọc hoàn toàn bên trong selector ID của panel đó:

```css
/* ✅ ĐÚNG — mọi quy tắc đều bị nhốt bên trong panel */
#article-empirical-panel {

  & * { box-sizing: border-box; margin: 0; padding: 0; }  /* chỉ ảnh hưởng bên trong */

  & {
    --ink: #1a1a2e;
    --paper: #f5f0e8;
    background: var(--paper);
    color: var(--ink);
  }

  & h1 { font-size: 2rem; }
  & p { line-height: 1.8; }
  & .hero { padding: 4rem 2rem; }
}

/* ❌ SAI — quy tắc này sẽ tràn ra toàn trang */
* { margin: 0; padding: 0; }
h1 { font-size: 2rem; }
.hero { padding: 4rem 2rem; }
```

**Tham khảo các bài viết đã làm đúng:** `article-darvas-panel`, `article-gann-panel`, `article-valentini-panel` — tất cả đều có cấu trúc `#article-xxx-panel { & { ... } }`.

---

## 3. Cách thêm bài viết mới an toàn

Khi thêm một bài viết HTML mới vào `index.html`, dùng script Python theo quy trình sau:

1. **Đọc file HTML gốc** (`file for wed/ten-bai.html`).
2. **Trích xuất `<style>` và `<body>`** bằng regex.
3. **Scope toàn bộ CSS** vào `#article-xxx-panel { ... }` sử dụng CSS nesting.
4. **Chú ý các trường hợp đặc biệt:**
   - `@import` → giữ nguyên, đặt **trước** khối `#article-xxx-panel { }` (không đặt bên trong).
   - `:root { }` → đổi thành `& { }` bên trong panel.
   - `body { }` → đổi thành `& { }` bên trong panel.
   - `html { }` → xóa hoặc comment out.
   - `*, *::before, *::after { }` → đổi thành `& *, & *::before, & *::after { }`.
5. **Dùng script `rebuild_empirical.py` làm template** cho các bài viết tương tự.
6. **Luôn kiểm tra output** bằng `cat index.html | grep -A 20 "id=\"article-xxx-panel\""` trước khi commit.

---

## 4. Git workflow

- Mọi thay đổi đều được commit và push tự động lên GitHub.
- Cloudflare Pages tự động deploy sau mỗi push (~1-2 phút).
- Không cần chạy lệnh Terminal thủ công — agent xử lý toàn bộ.

---

## 5. Thông tin project

- **Repo GitHub:** `https://github.com/tandt1609/dangthanhtan` (redirect từ `tandt-Cloudflare-Pages`)
- **URL live:** `https://dangthanhtan.pages.dev`
- **Nguồn bài viết gốc:** thư mục `../file for wed/` (relative từ `tandt-Cloudflare-Pages/`)

---

## 6. Thiết kế bài viết — Design System chuẩn

### 6.1 Tông màu chuẩn (palette parchment/vault-green)

Bài viết kiểu **longform nghiên cứu** (lịch sử, phân tích sâu) dùng palette sau — nhất quán giữa các bài:

```css
#article-xxx-panel {
  & {
    --parchment:   #efe6d2;   /* nền giấy cũ */
    --vault-green: #1e4438;   /* xanh rừng đậm — tiêu đề chính */
    --gold:        #b1893a;   /* vàng đồng — nhãn, badge */
    --rust:        #8b3a2a;   /* đỏ gạch — thời kỳ, số liệu */
    --ink:         #1c2c4a;   /* xanh mực — body text */
    --line:        rgba(177,137,58,0.25); /* đường kẻ mờ vàng */
    background: var(--parchment);
    color: var(--ink);
  }
}
```

> Nếu bài viết có tông màu riêng (tối, xanh dương...) thì tự định nghĩa biến riêng — KHÔNG dùng màu cứng (#fff, #000) trong body text.

---

### 6.2 Typography chuẩn

| Vai trò | Font | Style |
|---|---|---|
| Tiêu đề bài (h1) | `Fraunces`, serif | weight 700–900, italic |
| Tiêu đề phần (h2, h3) | `Fraunces` hoặc `EB Garamond` | weight 700 |
| Tên nhân vật / label | `Fraunces`, serif | weight 700 |
| Thời kỳ / nhãn badge | `Courier Prime`, monospace | uppercase, letter-spacing 0.1em |
| Body text | `Literata` hoặc `EB Garamond` | 1.1rem, line-height 1.8 |
| Code / số liệu inline | `JetBrains Mono` hoặc `IBM Plex Mono` | — |

---

### 6.3 Cấu trúc layout bài viết

```
#article-xxx-panel
  └── [back button bar]      — nền vault-green, nút Quay lại
  └── .hero                  — tiêu đề lớn, eyebrow, subtitle
  └── .shell                 — wrapper nội dung, max-width ~780px, margin auto
       └── .intro            — đoạn dẫn nhập nổi bật
       └── .part-title       — tiêu đề phần (số phần + h2 + đường kẻ)
       └── .ledger           — timeline dọc (border-left)
            └── section.era  — từng mốc thời gian
       └── .figures-grid     — danh sách nhân vật (xem 6.4)
       └── .quote            — trích dẫn nổi bật
       └── .cards            — grid các card thể loại
       └── .stamp-wrap       — hộp có con dấu góc
  └── footer                 — chú thích cuối bài
```

---

### 6.4 Pattern: Danh sách nhân vật / bảng so sánh — DÙNG CARD, KHÔNG DÙNG TABLE

**Lý do:** Table HTML bị tràn ngang trên mobile, khó đọc, khó style. Card grid tự responsive.

**CSS pattern `.figures-grid`:**

```css
.figures-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0;
  margin-top: 14px;
  border: 1px solid var(--line);
  border-radius: 12px;
  overflow: hidden;
}
.fig-item {
  display: grid;
  grid-template-columns: 1fr;        /* mobile: 1 cột */
  padding: 20px 22px;
  border-bottom: 1px solid var(--line);
  background: rgba(255,255,255,0.38);
  transition: background 0.18s;
}
.fig-item:last-child  { border-bottom: none; }
.fig-item:nth-child(even) { background: rgba(239,230,210,0.45); }
.fig-item:hover { background: rgba(177,137,58,0.08); }
.fig-name  { font-family:'Fraunces',serif; font-weight:700; font-size:1.05rem; color:var(--vault-green); margin:0 0 4px; }
.fig-era   { font-family:'Courier Prime',monospace; font-size:11.5px; letter-spacing:0.1em; color:var(--rust); text-transform:uppercase; margin-bottom:8px; display:inline-block; }
.fig-desc  { font-size:0.95rem; color:#2c3a5c; margin:0; line-height:1.65; }

/* Desktop (≥560px): 2 cột — tên+thời kỳ bên trái, mô tả bên phải */
@media (min-width:560px) {
  & .fig-item {
    grid-template-columns: 180px 1fr;
    grid-template-rows: auto 1fr;
    gap: 0 18px;
  }
  & .fig-name { grid-column:1; grid-row:1; }
  & .fig-era  { grid-column:1; grid-row:2; align-self:start; }
  & .fig-desc { grid-column:2; grid-row:1 / span 2; padding-top:2px; }
}
```

**HTML pattern:**

```html
<div class="figures-grid">
  <div class="fig-item">
    <div class="fig-name">Tên nhân vật</div>
    <span class="fig-era">Thế kỷ XX</span>
    <p class="fig-desc">Mô tả đóng góp...</p>
  </div>
  <!-- thêm .fig-item cho từng nhân vật -->
</div>
```

> **Quy tắc:** Nếu bài viết gốc dùng `<table>` để liệt kê nhân vật/so sánh, **hãy chủ động chuyển sang `.figures-grid`** khi đăng lên web. Không giữ nguyên `<table>` trừ khi bảng có hơn 4 cột số liệu phức tạp không thể card hóa.

---

## 7. Quy tắc Mobile — BẮT BUỘC

### 7.1 Chặn horizontal scroll

**LUÔN** thêm vào đầu `<style>` trong `index.html` (đã có sẵn — không xóa):

```css
html, body {
  overflow-x: hidden;
  max-width: 100%;
}
.sukien-article-panel,
.commodity-article-panel {
  overflow-x: hidden;
  max-width: 100vw;
  width: 100%;
  box-sizing: border-box;
}
.sukien-article-panel *,
.commodity-article-panel * {
  max-width: 100%;
  box-sizing: border-box;
}
/* Tables/pre vẫn scroll được bên trong */
.sukien-article-panel table,
.commodity-article-panel table,
.sukien-article-panel pre,
.commodity-article-panel pre {
  max-width: 100%;
  overflow-x: auto;
  display: block;
}
```

### 7.2 Breakpoint chuẩn cho bài viết

```css
/* Mobile nhỏ (≤480px) */
@media (max-width:480px) {
  & .shell   { padding: 0 16px 10vh; }
  & .hero    { padding: 5vh 5vw 6vh; }
  & .ledger  { padding-left: 26px; }
  & section.era::before { left: -32px; }
  & .figures-grid { border-radius: 8px; }
  & .fig-item     { padding: 16px 16px; }
  & .stamp { width:72px; height:72px; font-size:10px; top:-12px; right:10px; }
}

/* Desktop 2-cột cho cards */
@media (min-width:640px) {
  & .cards { grid-template-columns: 1fr 1fr; }
}
```

### 7.3 Không dùng white-space: nowrap ở cấp độ toàn bộ cell

Chỉ dùng `white-space: nowrap` cho label nhỏ (badge thời kỳ), không áp cho tên người hoặc đoạn văn.

---

## 8. Checklist trước khi commit bài viết mới

- [ ] CSS hoàn toàn được bọc trong `#article-xxx-panel { }` (CSS nesting)
- [ ] Không có `html {}`, `body {}`, `* {}` ở cấp global
- [ ] `@import` đặt **trước** khối panel, không đặt bên trong
- [ ] Nếu có bảng nhân vật/so sánh → chuyển sang `.figures-grid` card layout
- [ ] Đã kiểm tra breakpoint mobile ≤480px
- [ ] Nút "Quay lại" hoạt động đúng (`openEventArticle('')`)
- [ ] Routing được thêm vào `script.js`
- [ ] Card bài viết được thêm vào danh sách tab tương ứng

