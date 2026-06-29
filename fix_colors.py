import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

def main():
    text_color = "#f5ede0"
    
    # style.css replacements
    style_replacements = [
        # Lược sử Đồng
        ('--ink-soft:    #BCC8BC;', f'--ink-soft:    {text_color};'),
        
        # Tiến sĩ Đồng
        ('--ink-soft:#CCC1AD;', f'--ink-soft:{text_color};'),
    ]
    
    update_file('style.css', style_replacements)
    
    # Bust cache
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'style\.css(\?v=\d+)+', 'style.css?v=24', html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Busted CSS cache to v24")

if __name__ == '__main__':
    main()
