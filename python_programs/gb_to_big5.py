import os
from opencc import OpenCC

def convert_simplified_to_traditional(file_path):
    """
    Convert Simplified Chinese to Traditional Chinese in an HTML file while preserving the formatting.
    - Rename the output file to include '_big5' in the name.
    - Replace '繁體版' with '简体版'.
    - Replace 'index_big5.html' with 'index.html'.
    - Add '_big5' to links under <li> tags, except for 'index_big5.html', which is replaced with 'index.html'.
    - Replace 'saijo.JPG' with 'saijo_big5.JPG'.
    - For <a href> tags not within <li>, update links containing 'github_html' ending with '.html' to end with '_big5.html'.
    """
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} does not exist or is not a valid file.")
        return
    
    print(f"Processing: {file_path}")
    
    # Initialize the OpenCC converter for Simplified to Traditional conversion
    cc = OpenCC('s2t')
    
    try:
        # Read the original HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace specific terms
        content = content.replace("saijo.JPG", "saijo_big5.JPG")
        
        # Function to handle links under <li> tags
        def add_big5_to_links(line):
            if "<li>" in line and "href=" in line:
                parts = line.split("href=")
                for i in range(1, len(parts)):
                    quote_start = parts[i][0]  # Get the quote type (' or ")
                    link = parts[i].split(quote_start)[1]  # Extract the href value
                    if link != "index.html" and not link.endswith("_big5.html"):
                        base, ext = os.path.splitext(link)
                        new_link = f"{base}_big5{ext}"
                        parts[i] = parts[i].replace(link, new_link)
                return "href=".join(parts)
            return line
        
        # Function to handle <a href> links outside <li>
        def update_github_links(line):
            if "<a " in line and "href=" in line and "github_html" in line:
                parts = line.split("href=")
                for i in range(1, len(parts)):
                    quote_start = parts[i][0]  # Get the quote type (' or ")
                    link = parts[i].split(quote_start)[1]  # Extract the href value
                    if link.endswith(".html") and not link.endswith("_big5.html"):
                        base, ext = os.path.splitext(link)
                        new_link = f"{base}_big5{ext}"
                        parts[i] = parts[i].replace(link, new_link)
                return "href=".join(parts)
            return line
        
        content_lines = content.splitlines()
        updated_lines = []

        for line in content_lines:
            line = add_big5_to_links(line)  # Process <li> links
            line = update_github_links(line)  # Process <a> links outside <li>
            updated_lines.append(line)

        # Convert only the Chinese characters to Traditional while keeping formatting
        converted_content = "\n".join(updated_lines)
        converted_content = cc.convert(converted_content)
        
        # Additional replacements
        converted_content = converted_content.replace('index_big5.html">繁體版', 'index.html">简体版')
        converted_content = converted_content.replace('index_big5.html" onclick="hideMobileMenu()">繁體版', 'index.html" onclick="hideMobileMenu()">简体版')
        
        converted_content = converted_content.replace('search_script','search_script_big5')

        # Generate the new file name
        dir_name, original_name = os.path.split(file_path)
        base_name, ext = os.path.splitext(original_name)
        new_file_name = f"{base_name}_big5{ext}"
        new_file_path = os.path.join(dir_name, new_file_name)
        
        # Write the modified content to the new file
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(converted_content)
        
        print(f"Converted file saved as: {new_file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory):
    """
    Process all HTML files in the given directory.
    """
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    print(f"Processing directory: {directory}")
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    if not html_files:
        print("No HTML files found in the directory.")
        return
    
    for file_name in html_files:
        file_path = os.path.join(directory, file_name)
        convert_simplified_to_traditional(file_path)

def main():
    # Specify the directory containing the HTML files
    directory = "big5_convert"  # Update to the target directory
    
    # Process all HTML files in the directory
    if os.path.isdir(directory):
        process_directory(directory)
    else:
        print(f"Error: Directory '{directory}' does not exist.")
        

if __name__ == "__main__":
    main()





"""
import os
from opencc import OpenCC

def convert_simplified_to_traditional(file_path):
    
#    Convert Simplified Chinese to Traditional Chinese in an HTML file while preserving the formatting.
#    - Rename the output file to include '_big5' in the name.
#    - Replace '繁體版' with '简体版'.
#    - Replace 'index_big5.html' with 'index.html'.
#    - Add '_big5' to links under <li> tags, except for 'index_big5.html', which is replaced with 'index.html'.
#    - Replace 'saijo.JPG' with 'saijo_big5.JPG'.
    
    if not os.path.isfile(file_path):
        print("Invalid file path. Please check and try again.")
        return
    
    # Initialize the OpenCC converter for Simplified to Traditional conversion
    cc = OpenCC('s2t')
    
    # Read the original HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace specific terms
#    content = content.replace("繁體版", "简体版")
#    content = content.replace("index_big5.html", "index.html")
    content = content.replace("saijo.JPG", "saijo_big5.JPG")
    
    # Handle links under <li> tags
    def add_big5_to_links(line):
        if "<li>" in line and "href=" in line:
            parts = line.split("href=")
            for i in range(1, len(parts)):
                quote_start = parts[i][0]  # Get the quote type (' or ")
                link = parts[i].split(quote_start)[1]  # Extract the href value
                if link != "index.html" and not link.endswith("_big5.html"):
                    base, ext = os.path.splitext(link)
                    new_link = f"{base}_big5{ext}"
                    parts[i] = parts[i].replace(link, new_link)
            return "href=".join(parts)
        return line

    content_lines = content.splitlines()
    updated_lines = []

    for line in content_lines:
        updated_lines.append(add_big5_to_links(line))

    # Convert only the Chinese characters to Traditional while keeping formatting
    converted_content = "\n".join(updated_lines)
    converted_content = cc.convert(converted_content)
    
    # Generate the new file name
    dir_name, original_name = os.path.split(file_path)
    base_name, ext = os.path.splitext(original_name)
    new_file_name = f"{base_name}_big5{ext}"
    new_file_path = os.path.join(dir_name, new_file_name)
    
    converted_content = converted_content.replace('index_big5.html">繁體版','index.html">简体版')
    converted_content = converted_content.replace('index_big5.html" onclick="hideMobileMenu()">繁體版','index.html" onclick="hideMobileMenu()">简体版')
    
    # Write the modified content to the new file
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(converted_content)
    
    print(f"Converted file saved as: {new_file_path}")




def main():
    # Input the HTML file to process
    file_path = "author.html"
    convert_simplified_to_traditional(file_path)

    file_path = "journal_list.html"
    convert_simplified_to_traditional(file_path)
    
    file_path = "index.html"
    convert_simplified_to_traditional(file_path)
    
    file_path = "europe.html"
    convert_simplified_to_traditional(file_path)
    
    file_path = "web_and_program.html"
    convert_simplified_to_traditional(file_path)
    
    file_path = "other_japan.html"
    convert_simplified_to_traditional(file_path)
if __name__ == "__main__":
    main()
    
"""

