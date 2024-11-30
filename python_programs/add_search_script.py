import os

def modify_html_files(folder_path):
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is an HTML file
        if file_name.endswith(".html"):
            file_path = os.path.join(folder_path, file_name)
            
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Determine the script to add based on the file name
            if "big5" in file_name.lower():
                additional_script = '<script src="../search_script2_big5.js"></script>\n'
            else:
                additional_script = '<script src="../search_script2.js"></script>\n'
            
            # Check and add the additional script after the specified line
            modified_lines = []
            script_added = False
            for line in lines:
                modified_lines.append(line)
                if '<script src="../script.js"></script>' in line and not script_added:
                    modified_lines.append(additional_script)
                    script_added = True
            
            # Write back the modified content to the same file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)
            
            print(f"Modified: {file_name}")

# Specify the folder containing the HTML files
folder_path = "github_html"  # Adjust this path as needed

# Call the function to modify HTML files
modify_html_files(folder_path)

