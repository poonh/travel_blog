from bs4 import BeautifulSoup

def process_youtube_links(link_file):
    # Read the YouTube links from the text file
    with open(link_file, 'r', encoding='utf-8') as file:
        links = file.readlines()

    # Process the links to replace "shorts" and "youtu.be"
    processed_links = []
    for link in links:
        link = link.strip()  # Remove any leading/trailing whitespace
        if "shorts" in link:
            processed_link = link.replace("shorts", "embed")
        elif "youtu.be" in link:
            processed_link = link.replace("youtu.be", "youtube.com/embed/")
        else:
            processed_link = link  # Keep the link unchanged if it doesn't match

        processed_links.append(processed_link)

    return processed_links

def replace_img_tags_and_iframe(html_file, output_file, youtube_links):
    # Read the HTML file
    filename = html_file.split("/")[1].replace(".html", "")
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize counters
    total_img_replacements = 0
    total_iframe_replacements = 0

    # Find all <img> tags with a "border" attribute
    img_tags = soup.find_all('img', border=True)

    # Process each <img> tag
    for idx, img_tag in enumerate(img_tags, start=1):
        # Check if the <img> tag is inside an <a> tag (i.e., if there's a surrounding <a> href)
        parent_a_tag = img_tag.find_parent('a', href=True)
        
        if parent_a_tag:
            # Remove the <a> tag but keep the <img> tag inside it
            parent_a_tag.unwrap()

        # Replace the <img> tag's src with the new structure
        img_tag['src'] = f"https://poonh.github.io/travel_blog/html_pics/{filename}/{idx}.JPG"
        img_tag['class'] = 'picture'  # Add the class 'picture' to the <img> tag

        # Wrap the <img> tag in a <div class="picture-container"> and a center div for alignment
        picture_container = soup.new_tag('div', **{'class': 'picture-container'})
        img_tag.wrap(picture_container)
        center_div = soup.new_tag('div', style='text-align: center;')
        picture_container.insert_after(center_div)

        total_img_replacements += 1

    # Ensure the number of iframe replacements matches the number of processed links
    iframe_tags = soup.find_all('iframe', allowfullscreen="allowfullscreen")
    for idx, iframe_tag in enumerate(iframe_tags):
        if idx < len(youtube_links):  # Ensure we don't exceed the number of links
            # Replace the iframe tag with the desired structure
            new_div = soup.new_tag('div', style='text-align: center;')
            new_iframe = soup.new_tag('iframe', width='60%', height='315', src=youtube_links[idx],
                                      frameborder='0',
                                      allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture',
                                      allowfullscreen='allowfullscreen')

            # Remove the old iframe and insert the new one
            iframe_tag.replace_with(new_iframe)
            new_iframe.insert_before(new_div)

            # Increment the iframe replacements counter
            total_iframe_replacements += 1

    # Update the stylesheet link
    stylesheet_tag = soup.find('link', rel="stylesheet")
    if stylesheet_tag:
        stylesheet_tag['href'] = "../style.css"

    # Write the modified HTML to the output file with each tag on a new line
    with open(output_file, 'w', encoding='utf-8') as file:
        # Convert the soup to string, ensuring each tag is on a new line
        formatted_html = str(soup).replace('><', '>\n<')  # Add new lines between tags
        file.write(formatted_html)

    # Print the total number of replacements made
    print(f"Total image replacements made: {total_img_replacements}")
    print(f"Total iframe replacements made: {total_iframe_replacements}")

# Example usage
html_file = 'blogger_new_html/2020_autumn_kenminnohama.html'  # Replace with the path to your HTML file
output_file = html_file.replace("blogger_new_html", "github_html")  # Replace with your output path

# Process the YouTube links from the text file
link_file = '2020_autumn_kenminnohama_links.txt'  # Replace with the path to your link file
youtube_links = process_youtube_links(link_file)

# Call the function to replace img and iframe tags
replace_img_tags_and_iframe(html_file, output_file, youtube_links)


