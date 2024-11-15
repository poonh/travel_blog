from bs4 import BeautifulSoup

def remove_small_font_span(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <span> tags with specific style and remove them
    for span in soup.find_all('span', {'style': 'font-size: small;'}):
        span.unwrap()  # Removes the <span> tag but keeps its content
    
    return str(soup)

# Example usage: reading from an HTML file
with open('github_html/2022_nagahama.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Remove the specific <span> tags
modified_html = remove_small_font_span(html_content)

# Write the modified HTML back to the file
with open('github_html/2022_nagahama.html', 'w', encoding='utf-8') as file:
    file.write(modified_html)

print("Specified <span> tags have been removed.")

