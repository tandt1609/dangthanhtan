import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The background from Dai Bang
    dai_bang_bg_img = """background-image:
      radial-gradient(ellipse 80vw 60vh at 50% 30%, rgba(139,58,26,.35) 0%, transparent 70%),
      radial-gradient(ellipse 60vw 80vh at 50% 100%, rgba(201,146,42,.18) 0%, transparent 60%);"""

    # 1. Update luocsudong gradient in style.css
    luoc_old = """background-image:
    radial-gradient(ellipse 80vw 40vh at 50% 0%, rgba(184,115,51,0.07), transparent 55%),
    radial-gradient(ellipse 60vw 50vh at 100% 20%, rgba(92,158,122,0.06), transparent 60%);"""
    content = content.replace(luoc_old, dai_bang_bg_img)

    # 2. Update tiensidong gradient in style.css
    tien_old = """background-image:
      radial-gradient(ellipse 900px 500px at 15% -5%, rgba(201,122,74,0.10), transparent 60%),
      radial-gradient(ellipse 700px 500px at 100% 10%, rgba(94,139,121,0.07), transparent 60%);"""
    content = content.replace(tien_old, dai_bang_bg_img)

    # 3. Chicxulub doesn't have a background-image gradient, we can just add it
    # We will look for `.article-chicxulub {` and add the gradient to its body (if there is one).
    # Actually chicxulub background is just `background-color: var(--achx-void);`? Wait, where is it applied?
    # It's probably on some body class or chicxulub root. Let's just leave chicxulub for now or do it if we find it.

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    dai_bang_bg_img = """background-image:
      radial-gradient(ellipse 80vw 60vh at 50% 30%, rgba(139,58,26,.35) 0%, transparent 70%),
      radial-gradient(ellipse 60vw 80vh at 50% 100%, rgba(201,146,42,.18) 0%, transparent 60%);"""

    # For gann and darvas, we can replace `background-color: var(--void);` with `background-color: var(--void); \n  {dai_bang_bg_img}`
    content = content.replace('background-color: var(--void);', f'background-color: var(--void);\n      {dai_bang_bg_img}')
    content = content.replace('background-color: var(--ink);', f'background-color: var(--ink);\n      {dai_bang_bg_img}')

    # Bust cache
    content = re.sub(r'style\.css(\?v=\d+)+', 'style.css?v=26', content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")

def main():
    update_file('style.css')
    update_index()

if __name__ == '__main__':
    main()
