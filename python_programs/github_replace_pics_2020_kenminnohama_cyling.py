import re

def replace_img_tags_and_stylesheet(html_file, output_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Regex to find all relevant <img> tags, either with src from ctrip or with border attribute
    img_tags = re.findall(r'(<img\s[^>]*src=["\']https://dimg02\.c-ctrip\.com[^>]*>)|(<img\s[^>]*border=["\'][^"\']*["\'][^>]*>)', html_content)

    # Total replacements counter
    total_replacements = 0

    # Process the image tags and replace them in the HTML content
    for idx, match in enumerate(img_tags, start=1):
        if match[0]:  # This means it matched the first regex for ctrip images
            # Replace the entire <img> tag with the new structure
            replacement = f'<div class="picture-container">\n    <img src="https://poonh.github.io/travel_blog/html_pics/2020_kenminnohama_cycling/{idx}.JPG" class="picture">\n</div>\n<div style="text-align: center;"></div>'
            html_content = html_content.replace(match[0], replacement, 1)  # Replace first occurrence
            total_replacements += 1  # Increment the counter
        elif match[1]:  # This means it matched the second regex for border images
            # Replace the entire <img> tag with the new structure
            replacement = f'<div class="picture-container">\n    <img src="https://poonh.github.io/travel_blog/html_pics/2020_kenminnohama_cycling/{idx}.JPG" class="picture">\n</div>\n<div style="text-align: center;"></div>'
            full_tag = re.search(r'<[^>]*border=["\'][^"\']*["\'][^>]*>', match[1])
            if full_tag:
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
html_file = 'blogger_new_html/2020_kenminnohama_cycling.html'  # Replace with the path to your HTML file
output_file = html_file.replace("blogger_new_html","github_html")  # Replace with your

replace_img_tags_and_stylesheet(html_file, output_file)

