from bs4 import BeautifulSoup

def check_missing_jpgs(html_content, total_jpgs=167):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all JPG image references
    image_tags = soup.find_all('img')
    found_jpgs = set()

    # Extract image names (assuming they end with .JPG and follow the pattern 'number.JPG')
    for img in image_tags:
        if 'src' in img.attrs and img['src'].lower().endswith('.jpg'):
            # Get the filename without the path
            filename = img['src'].split('/')[-1]  # Get the last part after '/'
            if filename.isdigit() or filename.split('.')[0].isdigit():  # If the filename is a number
                found_jpgs.add(int(filename.split('.')[0]))  # Add the number to the set
    
    # Check for missing JPGs
    all_jpgs = set(range(1, total_jpgs + 1))
    missing_jpgs = all_jpgs - found_jpgs

    if missing_jpgs:
        print(f"Missing JPGs: {sorted(missing_jpgs)}")
    else:
        print("All JPGs are present.")

# Example usage: reading from an HTML file
with open('github_html/2022_shimane_momiji.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Check for missing JPGs
check_missing_jpgs(html_content)

