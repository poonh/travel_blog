from bs4 import BeautifulSoup

def modify_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <span> tags with specific style and remove them
    for span in soup.find_all('span', {'style': 'font-size: small;'}):
        span.unwrap()  # Removes the <span> tag but keeps its content
    
    # Find all <div> tags with specific class and style, and replace them with <p>
    for div in soup.find_all('div', {'class': 'DUwDvf fontHeadlineLarge', 'style': 'text-align: left;'}):
        div.name = 'p'  # Change the tag from <div> to <p>
        # Remove class and style attributes (if not needed in <p>)
        del div['class']
        del div['style']
    
    return str(soup)

# Example usage: reading from an HTML file
with open('github_html/2022_nagahama.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Modify the HTML content
modified_html = modify_html_content(html_content)

# Write the modified HTML back to a file
with open('modified_file.html', 'w', encoding='utf-8') as file:
    file.write(modified_html)

print("HTML has been modified.")

