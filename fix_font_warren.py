import sys

def main():
    # Fix Libre Baskerville -> EB Garamond in style.css
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    old_count = content.count('Libre Baskerville')
    content = content.replace("'Libre Baskerville', Georgia, serif", "'EB Garamond', Georgia, serif")
    content = content.replace("'Libre Baskerville', serif", "'EB Garamond', Georgia, serif")
    new_count = content.count('Libre Baskerville')

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"style.css: replaced {old_count - new_count} occurrences. Remaining: {new_count}")

    # Also check index.html for any inline Libre Baskerville
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    old_count2 = html.count('Libre Baskerville')
    if old_count2 > 0:
        html = html.replace("'Libre Baskerville', Georgia, serif", "'EB Garamond', Georgia, serif")
        html = html.replace("'Libre Baskerville', serif", "'EB Garamond', Georgia, serif")
        new_count2 = html.count('Libre Baskerville')
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"index.html: replaced {old_count2 - new_count2} occurrences. Remaining: {new_count2}")
    else:
        print("index.html: no Libre Baskerville found")

    # Also check - is Raleway OK for Vietnamese? 
    # Raleway is a sans-serif and may also have issues with Vietnamese.
    # Let's check what Raleway is used for in .article-warren-buffett
    raleway_count = content.count('Raleway')
    print(f"\nRaleway occurrences in style.css: {raleway_count}")
    # Raleway is used for eyebrow/heading labels (Raleway font) - these are mostly ASCII/short labels
    # but the main body text uses Libre Baskerville -> now EB Garamond
    # The .wb-lead first-letter dropcap also uses Raleway which is fine (it's just one letter)

    print("\nDone! Libre Baskerville replaced with EB Garamond.")

if __name__ == '__main__':
    main()
