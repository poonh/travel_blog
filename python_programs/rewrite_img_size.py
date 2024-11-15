import os
import re

# Folder containing the HTML files
folder_path = 'github_html'

# Regular expression to match <img> tags with border="0" and class="picture"
# and remove both height and width attributes within those tags
pattern = re.compile(r'(<img[^>]*\bborder="0"[^>]*\bclass="picture"[^>]*)(\s(height|width)="[^"]*")*', re.IGNORECASE)

# Function to remove height and width attributes in matching tags
def remove_height_width(match):
    # Return the tag without any height or width attributes
    return re.sub(r'\s(height|width)="[^"]*"', '', match.group(0))

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove height and width attributes only if the <img> tag has border="0" and class="picture"
        modified_content = re.sub(pattern, remove_height_width, content)

        # Overwrite the original file with the modified content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

print("Height and width attributes removed from matching <img> tags in all HTML files.")

