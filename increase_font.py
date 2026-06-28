import sys

def main():
    try:
        with open('style.css', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: style.css not found")
        sys.exit(1)

    # Replace font-size in .article-warren-buffett
    old_size = "font-size: 17px;"
    new_size = "font-size: 20px;"
    
    if old_size in content:
        content = content.replace(old_size, new_size)
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated font size from 17px to 20px.")
    else:
        print("Could not find 'font-size: 17px;' in style.css")

if __name__ == '__main__':
    main()
