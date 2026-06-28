import re

def process_html():
    with open(r'd:\Documents\Google Antygravity\file for wed\su-im-lang-va-tai-tao-than-kinh.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_match.group(1) if body_match else ''

    # Build properly scoped CSS:
    # 1. CSS variables: keep :root as is but wrap all rules under #article-imlangtk-panel
    # 2. Prepend #article-imlangtk-panel to every selector line

    lines = style_content.split('\n')
    scoped_lines = []
    
    for line in lines:
        stripped = line.strip()
        # Skip :root, body, html special handling
        if stripped.startswith(':root'):
            scoped_lines.append(line.replace(':root', '#article-imlangtk-panel'))
        elif stripped.startswith('body') and '{' in stripped:
            scoped_lines.append(line.replace('body', '#article-imlangtk-panel'))
        elif stripped.startswith('html') and '{' in stripped:
            # skip html rule
            scoped_lines.append('/* html rule removed */')
        elif stripped.startswith('*, *::'):
            scoped_lines.append(line)
        else:
            scoped_lines.append(line)
    
    scoped_style_content = '\n'.join(scoped_lines)

    # Now wrap all CSS selectors with scope using a Python regex approach
    # The cleanest way: wrap the whole block in a @scope or just use direct injection
    # Since @scope is not widely supported, we use a "prefix all selectors" approach
    
    # Better approach: add explicit overrides for the problematic areas
    fix_css = """
/* ===== PANEL FIX: ensure proper background and text colors ===== */
#article-imlangtk-panel {
    background: #fffdf7;
    color: #1a1a2e;
    --ink: #1a1a2e;
    --mid: #2d3561;
    --accent: #5c7cfa;
    --warm: #c9b99a;
    --parchment: #f5f0e8;
    --paper: #fffdf7;
    --rule: rgba(26,26,46,0.12);
    --rule-warm: rgba(201,185,154,0.45);
    --ghost: rgba(92,124,250,0.08);
    --type-display: 'EB Garamond', Georgia, serif;
    --type-body: 'Inter', system-ui, sans-serif;
    --type-label: 'Space Grotesk', system-ui, sans-serif;
    --max: 860px;
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 17px;
    line-height: 1.75;
}
#article-imlangtk-panel .masthead {
    background: #1a1a2e;
    color: #f5f0e8;
    padding: 0 0 5rem;
    position: relative;
    overflow: hidden;
}
#article-imlangtk-panel .masthead::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 60% 80% at 70% 40%, rgba(92,124,250,0.18) 0%, transparent 65%),
        radial-gradient(ellipse 40% 60% at 20% 80%, rgba(201,185,154,0.10) 0%, transparent 60%);
    pointer-events: none;
}
#article-imlangtk-panel .masthead-rule {
    height: 3px;
    background: linear-gradient(90deg, #5c7cfa 0%, #c9b99a 50%, transparent 100%);
}
#article-imlangtk-panel .masthead-inner {
    max-width: 860px;
    margin: 0 auto;
    padding: 4rem 2rem 0;
    position: relative;
}
#article-imlangtk-panel .eyebrow {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #5c7cfa;
    margin-bottom: 1.6rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
#article-imlangtk-panel .eyebrow::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(92,124,250,0.35);
    max-width: 120px;
}
#article-imlangtk-panel h1 {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: clamp(2.6rem, 6vw, 4.2rem);
    font-weight: 500;
    line-height: 1.15;
    color: #fff;
    margin-bottom: 1.5rem;
    letter-spacing: -0.01em;
}
#article-imlangtk-panel h1 em { font-style: italic; color: #c9b99a; }
#article-imlangtk-panel .masthead-lead {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1.22rem;
    line-height: 1.65;
    color: rgba(245,240,232,0.80);
    max-width: 640px;
    margin-bottom: 3rem;
}
#article-imlangtk-panel .meta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    color: rgba(245,240,232,0.50);
}
#article-imlangtk-panel .meta-row span { text-transform: uppercase; }
#article-imlangtk-panel .meta-row strong { color: rgba(245,240,232,0.75); font-weight: 500; }
#article-imlangtk-panel .wave-divider { display: block; width: 100%; overflow: hidden; line-height: 0; margin-top: -1px; }
#article-imlangtk-panel .wave-divider svg { display: block; width: 100%; }
#article-imlangtk-panel .page-body {
    max-width: 860px;
    margin: 0 auto;
    padding: 0 2rem 6rem;
    background: #fffdf7;
}
#article-imlangtk-panel .section { margin-top: 5rem; }
#article-imlangtk-panel .section-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: #5c7cfa;
    margin-bottom: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}
#article-imlangtk-panel .section-label::before {
    content: '';
    width: 28px;
    height: 2px;
    background: #5c7cfa;
    flex-shrink: 0;
}
#article-imlangtk-panel h2 {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: clamp(1.7rem, 3.5vw, 2.4rem);
    font-weight: 500;
    line-height: 1.2;
    color: #1a1a2e;
    margin-bottom: 1.6rem;
    letter-spacing: -0.01em;
}
#article-imlangtk-panel h3 {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1.25rem;
    font-weight: 500;
    color: #1a1a2e;
    margin: 2.2rem 0 0.8rem;
    line-height: 1.35;
}
#article-imlangtk-panel p {
    margin-bottom: 1.2rem;
    color: #2c2c3e;
}
#article-imlangtk-panel .hr { border: none; border-top: 1px solid rgba(26,26,46,0.12); margin: 3.5rem 0; }
#article-imlangtk-panel .hr-warm { border-top-color: rgba(201,185,154,0.45); }
#article-imlangtk-panel .pullquote {
    border-left: 3px solid #5c7cfa;
    margin: 2.5rem 0;
    padding: 1.4rem 1.8rem;
    background: rgba(92,124,250,0.08);
    border-radius: 0 8px 8px 0;
}
#article-imlangtk-panel .pullquote p {
    font-family: 'EB Garamond', Georgia, serif;
    font-style: italic;
    font-size: 1.22rem;
    line-height: 1.55;
    color: #2d3561;
    margin: 0;
}
#article-imlangtk-panel .pullquote cite {
    display: block;
    margin-top: 0.75rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #5c7cfa;
    font-style: normal;
}
#article-imlangtk-panel .cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1.25rem;
    margin: 2rem 0;
}
#article-imlangtk-panel .card {
    background: #f5f0e8;
    border: 1px solid rgba(201,185,154,0.45);
    border-radius: 10px;
    padding: 1.5rem;
}
#article-imlangtk-panel .card-icon { font-size: 1.8rem; margin-bottom: 0.8rem; display: block; }
#article-imlangtk-panel .card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #5c7cfa;
    margin-bottom: 0.6rem;
}
#article-imlangtk-panel .card p { font-size: 0.9rem; color: #2c2c3e; margin: 0; }
#article-imlangtk-panel ul, #article-imlangtk-panel ol {
    padding-left: 1.5rem;
    margin-bottom: 1.2rem;
    color: #2c2c3e;
}
#article-imlangtk-panel li { margin-bottom: 0.5rem; }
#article-imlangtk-panel strong { color: #1a1a2e; font-weight: 600; }
#article-imlangtk-panel em { color: #2d3561; }
#article-imlangtk-panel .note-box {
    background: rgba(92,124,250,0.06);
    border: 1px solid rgba(92,124,250,0.2);
    border-left: 3px solid #5c7cfa;
    border-radius: 0 8px 8px 0;
    padding: 1.2rem 1.5rem;
    margin: 2rem 0;
}
#article-imlangtk-panel .note-box p { color: #2c2c3e; margin: 0; }
#article-imlangtk-panel .data-table { width: 100%; border-collapse: collapse; margin: 2rem 0; font-size: 0.92rem; }
#article-imlangtk-panel .data-table th {
    background: #1a1a2e;
    color: #f5f0e8;
    padding: 10px 12px;
    text-align: left;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
#article-imlangtk-panel .data-table td { padding: 10px 12px; border-bottom: 1px solid rgba(26,26,46,0.10); color: #2c2c3e; }
#article-imlangtk-panel .data-table tr:last-child td { border-bottom: none; }
#article-imlangtk-panel footer {
    background: #1a1a2e;
    color: rgba(245,240,232,0.65);
    padding: 3rem 2rem;
    text-align: center;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.8rem;
}
"""

    panel_html = f"""
<div id="article-imlangtk-panel" class="sukien-article-panel imlangtk-body">
    <style>
{fix_css}
    </style>
    <div style="padding: 14px 20px; background: #1a1a2e;">
        <button onclick="openThuVienArticle('')" style="background: transparent; border: 1px solid rgba(92,124,250,0.5); color: #5c7cfa; padding: 7px 16px; cursor: pointer; font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; letter-spacing: 0.05em; border-radius: 4px;">
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
    return panel_html

def main():
    panel_html = process_html()

    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()

    # Remove old panel and replace with new one
    # Find start of old panel
    start_marker = '\n<div id="article-imlangtk-panel" class="sukien-article-panel imlangtk-body">'
    end_marker = '\n\n<div id="article-phathoc-panel"'
    
    start_idx = index_html.find(start_marker)
    end_idx = index_html.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        index_html = index_html[:start_idx] + '\n' + panel_html + '\n' + index_html[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(index_html)
        print("Successfully rebuilt panel with correct CSS")
    else:
        print(f"Could not find markers. start_idx={start_idx}, end_idx={end_idx}")

if __name__ == '__main__':
    main()
