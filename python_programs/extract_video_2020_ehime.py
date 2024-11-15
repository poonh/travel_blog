import requests
from bs4 import BeautifulSoup
import re
import webbrowser

def extract_iframe_links(html_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <iframe> tags (maintains the order of appearance)
    iframes = soup.find_all('iframe')

    # Extract and return the 'src' links for <iframe> with "allowfullscreen" attribute
    links = [iframe['src'] for iframe in iframes if 'allowfullscreen' in iframe.attrs and 'src' in iframe.attrs]

    return links

def get_first_play_url(iframe_link):
    # Fetch the HTML content from the iframe link
    print(f"Fetching iframe link: {iframe_link}")
    response = requests.get(iframe_link)
    
    if response.status_code == 200:
        html_content = response.text

        # Find the first occurrence of "play_url" and extract the URL
        match = re.search(r'"play_url"\s*:\s*"([^"]+)"', html_content)
        
        if match:
            play_url = match.group(1)
            print(f"Found play URL: {play_url}")
            return play_url  # Return the first matched play_url link
        else:
            print(f"No play URL found in the iframe content.")
    else:
        print(f"Failed to fetch iframe content (status code: {response.status_code}).")
    
    return None

# Example usage
html_file = 'blogger_new_html/2024_chaozhou.html'
iframe_links = extract_iframe_links(html_file)

# Extract the first play_url from the first iframe link
num = 1
with open("2024_chaozhou_links.txt", "w") as new_file:
    for i,iframe_link in enumerate(iframe_links):
#        play_url = get_first_play_url(iframe_link)
        
            # Save iframe link and play_url to file
            new_file.write(f"{num}:{iframe_link}\n")
            new_file.flush()  # Ensure the contents are written to the file

            # Open the iframe link in Safari
            webbrowser.get("safari").open(iframe_link)
            
            num += 1
