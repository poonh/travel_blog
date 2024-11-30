import os

def update_image_paths(directory):
    # The specific image paths to replace
    replacements = {
        'pictures/saijo.JPG': 'https://poonh.github.io/travel_blog/pictures/saijo.JPG',
        'pictures/saijo_big5.JPG': 'https://poonh.github.io/travel_blog/pictures/saijo_big5.JPG',
    }

    # Iterate through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)

                # Read the content of the HTML file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace the image paths
                for old, new in replacements.items():
                    content = content.replace(f'<img src="{old}"', f'<img src="{new}"')

                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated: {file_path}")

# Replace 'github_html' with the actual path to your directory
update_image_paths('github_html')

