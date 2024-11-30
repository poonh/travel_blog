import os
import requests
from bs4 import BeautifulSoup

def download_images(html_file, save_folder):
    # Create the folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML file using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags containing "点击查看原图"
    links = soup.find_all('a', title="点击查看原图")
    print(len(links))

    # Download and save the images sequentially
    for i, link in enumerate(links, start=1):
        # Extract the href attribute
        image_url = link.get('href')
        if not image_url:
            continue

        # Download the image
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()

            # Save the image as 1.JPG, 2.JPG, etc.
            filename = os.path.join(save_folder, f"{i}.JPG")
            with open(filename, 'wb') as image_file:
                for chunk in response.iter_content(1024):
                    image_file.write(chunk)

            print(f"Downloaded: {filename}")

        except requests.RequestException as e:
            print(f"Failed to download {image_url}: {e}")

    print(f"Downloaded {i} images to {save_folder}")

# Example usage
html_file = "blogger_new_html/2014_neusiedl.html"
save_folder = "html_pics/2014_neusiedl"
download_images(html_file, save_folder)

