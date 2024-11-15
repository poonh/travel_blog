import re
import requests

def extract_img_links(html_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Regex to extract the src attribute from any <img> tag containing "https://dimg02.c-ctrip.com"
    img_links = re.findall(r'<img\s[^>]*src=["\'](https://dimg02\.c-ctrip\.com[^"\']+)["\'][^>]*>', html_content)

    # Display the list of extracted links
    for idx, link in enumerate(img_links, start=1):
        print(f"{idx}. {link}")

    return img_links

def save_img_from_list(img_links, index, save_name):
    if 0 < index <= len(img_links):
        img_url = img_links[index - 1]
        try:
            # Send a request to the image URL
            response = requests.get(img_url, stream=True)
            if response.status_code == 200:
                # Save the image with the provided name
                with open(save_name, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Image saved as {save_name}")
            else:
                print(f"Failed to download image, status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"Index {index} is out of range. Please enter a number between 1 and {len(img_links)}.")

# Example usage
html_file = 'blogger_new_html/2020_kenminnohama_cycling.html'  # Replace with the path to your HTML file
links = extract_img_links(html_file)

# Enter the position and desired file name
#position = int(input("Enter the position of the image you want to download: "))
#save_name = input("Enter the name to save the image as (include .jpg): ")
position = ["1","23","35","57","70"]
for i,name in enumerate(position):
   save_img_from_list(links, int(name), f"/Users/china_108/Desktop/tmp/{name}.JPG")

