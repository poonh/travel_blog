from bs4 import BeautifulSoup

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Remove <p> tags with no text
    for p in soup.find_all('p'):
        if not p.get_text(strip=True):  # If the <p> tag contains no text (even whitespace)
            p.decompose()  # Remove the <p> tag entirely

    # 2. Remove <div style="text-align: center;"></div> followed by <br>, <br/>, or </br>
    for div in soup.find_all('div', {'style': 'text-align: center;'}):
        if not div.get_text(strip=True):  # If the <div> contains no text
            next_sibling = div.find_next_sibling()
            if next_sibling and next_sibling.name in ['br', 'br/'] or (next_sibling and next_sibling.name == 'br' and not next_sibling.get_text(strip=True)):
                div.decompose()  # Remove the empty <div>
                next_sibling.decompose()  # Remove the <br> (or similar) tag

    return str(soup)

# Example usage: reading from an HTML file
with open('github_html/2022_shimane_momiji.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Clean the HTML content
cleaned_html = clean_html(html_content)

# Write the cleaned HTML back to a file
with open('cleaned_file.html', 'w', encoding='utf-8') as file:
    file.write(cleaned_html)

print("HTML has been cleaned.")

