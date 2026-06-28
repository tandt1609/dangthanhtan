import unicodedata

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if there are NFD characters
nfd_count = sum(1 for c in content if unicodedata.combining(c) > 0)
print(f"Found {nfd_count} combining (NFD-style) characters before normalization")

# Normalize to NFC
content_nfc = unicodedata.normalize('NFC', content)

nfd_count_after = sum(1 for c in content_nfc if unicodedata.combining(c) > 0)
print(f"Found {nfd_count_after} combining characters after NFC normalization")

if nfd_count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content_nfc)
    print(f"SUCCESS: Normalized {nfd_count} characters in index.html")
else:
    print("No NFD characters found - issue may be elsewhere")
    
# Also fix all source files in 'file for wed'
import os
source_dir = r'd:\Documents\Google Antygravity\file for wed'
for filename in os.listdir(source_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(source_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            src = f.read()
        nfd = sum(1 for c in src if unicodedata.combining(c) > 0)
        if nfd > 0:
            src_nfc = unicodedata.normalize('NFC', src)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(src_nfc)
            print(f"Fixed source file: {filename} ({nfd} NFD chars)")
