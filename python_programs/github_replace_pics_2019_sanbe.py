import re

def replace_img_tags_and_stylesheet(html_file, output_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Regex to find all <img> tags with src containing "https://dimg02.c-ctrip.com"
    img_tags = re.findall(r'(<img\s[^>]*src=["\']https://dimg02\.c-ctrip\.com[^>]*>)', html_content)

    # Replacement template for the <img> tag with new src
    replacement_template = '<img src="https://poonh.github.io/travel_blog/html_pics/2019_sanbe/{i}.JPG" class="picture">'

    # Initialize the replacement counter
    replacement_count = 0

    # Replace all matching <img> tags
    for idx, img_tag in enumerate(img_tags, start=1):
        replacement = replacement_template.format(i=idx)
        html_content = html_content.replace(img_tag, replacement, 1)  # Replace only the first occurrence
        replacement_count += 1  # Increment the counter for each replacement

    # Change the stylesheet path from "style.css" to "../style.css"
    html_content = html_content.replace('<link rel="stylesheet" href="style.css">', '<link rel="stylesheet" href="../style.css">')

    # Write the modified HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as new_file:
        new_file.write(html_content)

    print(f"HTML file successfully written to {output_file}")
    print(f"Number of replacements made: {replacement_count}")

# Example usage
html_file = 'blogger_new_html/2019_sanbe.html'  # Replace with the path to your HTML file
output_file = html_file.replace("blogger_new_html","github_html")  # Replace with your

replace_img_tags_and_stylesheet(html_file, output_file)

