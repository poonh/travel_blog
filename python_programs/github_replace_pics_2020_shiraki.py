import re

def replace_img_tags_and_stylesheet(html_file, output_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Regex to find all <img> tags with src from ctrip and <img> tags with border attribute
    img_tags_ctrip = re.findall(r'(<img\s[^>]*src=["\'][^"\']*mafengwo[^>]*>)', html_content)
    img_tags_border = re.findall(r'(<a\s[^>]*><img\s[^>]*border=["\'][^"\']*["\'][^>]*>)', html_content)

    # Total replacements counter
    total_replacements = 0

    # Process the ctrip image tags and replace them in the HTML content
    for idx, img_tag in enumerate(img_tags_ctrip, start=1):
        replacement = f'<div class="picture-container">\n    <img src="https://poonh.github.io/travel_blog/html_pics/2020_shiraki/{idx}.JPG" class="picture">\n</div>\n<div style="text-align: center;"></div>'
        html_content = html_content.replace(img_tag, replacement, 1)  # Replace first occurrence
        total_replacements += 1  # Increment the counter

    # Process the border image tags and replace them in the HTML content
    for idx, img_tag in enumerate(img_tags_border, start=len(img_tags_ctrip) + 1):
        full_tag = re.search(r'<a\s[^>]*><img\s[^>]*border=["\'][^"\']*["\'][^>]*>', img_tag)
        if full_tag:
            # Replace the entire <a> tag including <img> with the new structure
            replacement = f'<div class="picture-container">\n    <img src="https://poonh.github.io/travel_blog/html_pics/2020_shiraki/{idx}.JPG" class="picture">\n</div>\n<div style="text-align: center;"></div>'
            html_content = html_content.replace(full_tag.group(0), replacement, 1)  # Replace first occurrence
            total_replacements += 1  # Increment the counter

    # Change the stylesheet link
    html_content = re.sub(r'(<link\s+rel=["\']stylesheet["\s]+href=["\'])[^"\']*(["\'])', r'\1../style.css\2', html_content)

    # Write the modified HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Print the total number of replacements made
    print(f"Total replacements made: {total_replacements}")




# Example usage
html_file = 'blogger_new_html/2020_shiraki.html'  # Replace with the path to your HTML file
output_file = html_file.replace("blogger_new_html","github_html")  # Replace with your

replace_img_tags_and_stylesheet(html_file, output_file)

