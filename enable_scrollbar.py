import sys

def main():
    try:
        with open('style.css', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: style.css not found")
        sys.exit(1)

    old_scrollbar = """::-webkit-scrollbar {
    display: none; /* Hide scrollbar for Chrome, Safari, Opera */
}"""

    # We will style a nice, slim, elegant scrollbar
    new_scrollbar = """/* ===== CUSTOM SCROLLBAR ===== */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: var(--bg-dark); 
}
::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.15); 
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.3); 
}
"""

    if old_scrollbar in content:
        content = content.replace(old_scrollbar, new_scrollbar)
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated scrollbar styles in style.css.")
    else:
        print("Could not find the hidden scrollbar block in style.css.")
        # Try a more flexible replacement
        import re
        content = re.sub(r'::-webkit-scrollbar\s*\{\s*display:\s*none;[^}]*\}', new_scrollbar, content)
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Used regex to replace scrollbar styles.")

if __name__ == '__main__':
    main()
