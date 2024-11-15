import re

def replace_img_tags_keep_order(html_file, output_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Regex to find both <img src> and <img class> tags
    img_tags = re.findall(r'(<img\s[^>]*src=[\'"][^\'"]+[\'"][^>]*>)|(<img\sclass=[\'"][^\'"]+[\'"][^>]*>)', html_content)

    # Replacement template for each <img> tag
    replacement_template = '''
<div class="picture-container">
    <img src="https://poonh.github.io/travel_blog/html_pics/2019_hiruzen/{i}.JPG" class="picture">
</div>
<div style="text-align: center;"></div>
'''

    # Flatten the tuples from findall, removing None values (findall returns tuples of matches)
    img_tags = [tag for tag_pair in img_tags for tag in tag_pair if tag]

    # Replace all <img> tags with the formatted divs
    for idx, img_tag in enumerate(img_tags, start=1):
        replacement = replacement_template.format(i=idx)
        html_content = html_content.replace(img_tag, replacement, 1)  # Replace only the first occurrence of the tag

    html_content = html_content.replace('<link rel="stylesheet" href="style.css">', '<link rel="stylesheet" href="../style.css">')

    # Write the modified HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as new_file:
        new_file.write(html_content)

    print(f"HTML file successfully written to {output_file}")

# Example usage
html_file = 'blogger_new_html/2019_hiruzen.html'  # Replace with the path to your HTML file
output_file = html_file.replace("blogger_new_html","github_html")  # Replace with your

replace_img_tags_keep_order(html_file, output_file)

