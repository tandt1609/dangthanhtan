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
    # Colors from Đại bàng tái sinh:
    # bg: #0e0b08
    # text: #f5ede0
    
    bg_color = "#0e0b08"
    text_color = "#f5ede0"
    
    # index.html replacements
    index_replacements = [
        # Gann
        ('--void:       #0A0C1A;', f'--void:       {bg_color};'),
        ('--parchment:  #EDE8DC;', f'--parchment:  {text_color};'),
        
        # Darvas
        ('--ink:        #0D0F14;', f'--ink:        {bg_color};'),
        ('--paper:      #F2EDDF;', f'--paper:      {text_color};')
    ]
    
    # style.css replacements
    style_replacements = [
        # Chicxulub
        ('--achx-void: #05050A;', f'--achx-void: {bg_color};'),
        ('--achx-bone: #F2EAD8;', f'--achx-bone: {text_color};'),
        
        # Tiến sĩ Đồng
        ('--bg:#181511;', f'--bg:{bg_color};'),
        ('--ink:#F1E8D9;', f'--ink:{text_color};'),
        
        # Lược sử Đồng
        ('--bg:          #0D1610;', f'--bg:          {bg_color};'),
        ('--ink:         #EEF2EE;', f'--ink:         {text_color};'),
        
        # Lý thuyết
        ('--lt-bg:          #05091A;', f'--lt-bg:          {bg_color};'),
        ('--lt-bg-card:     #090E20;', f'--lt-bg-card:     #1a1410;'), # db-ink
        ('--lt-text:        #D8E4F5;', f'--lt-text:        {text_color};')
    ]
    
    update_file('index.html', index_replacements)
    update_file('style.css', style_replacements)
    
    # Bust cache
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'style\.css(\?v=\d+)+', 'style.css?v=23', html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Busted CSS cache to v23")

if __name__ == '__main__':
    main()
