import os
import requests
from bs4 import BeautifulSoup

def download_images(url, save_folder):
    # Step 1: Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page, status code: {response.status_code}")
        return

    # Step 2: Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find all <img> tags with the class "replace-file-img"
    img_tags = soup.find_all('img', class_='replace-file-img')

    # Step 4: Create the save folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    # Step 5: Download each image and save it as 1.JPG, 2.JPG, ...
    for idx, img_tag in enumerate(img_tags, start=1):
        img_url = img_tag.get('src')
        if img_url:
            try:
                # Download the image
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    # Create the file path
                    file_name = os.path.join(save_folder, f"{idx}.JPG")
                    # Write the image to the file
                    with open(file_name, 'wb') as file:
                        file.write(img_response.content)
                    print(f"Downloaded image {idx} to {file_name}")
                else:
                    print(f"Failed to download image {idx} from {img_url}")
            except Exception as e:
                print(f"Error downloading image {idx}: {e}")

if __name__ == "__main__":
    # Input the URL of the page and the folder where you want to save the images
    url = "https://soybeantravel.blogspot.com/2019/12/2018.html"
    save_folder = "../html_pics/2018_shiretoko"

    # Call the download function
    download_images(url, save_folder)

