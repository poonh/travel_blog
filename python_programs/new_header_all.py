import os

def process_html_file(file_path, replace_header_file):
    try:
        # Read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Extract the title
        title_name = ""
        for line in lines:
            if "<title>" in line and "</title>" in line:
                title_name = line.strip().split("<title>")[1].split("</title>")[0]
                #print(title_name)
                break
                
        
        if not title_name:
            print(f"No title found in {file_path}. Skipping file.")
            return
        
        # Locate the specific image line and check the next line
        img_tag = '<img border="0" width=100% src="https://poonh.github.io/travel_blog/pictures/saijo.JPG"/>'
        condition_met = False  # Flag to track if the condition is met
        
        for i, line in enumerate(lines):
            if img_tag in line.strip():
                #print(lines[i + 1].strip())
                if i + 1 < len(lines) and lines[i + 1].strip() == "<br><br>":
                    # Remove lines up to the next line after the image tag
                    lines = lines[i + 2:]  # Skip the current and next line
                    condition_met = True
                break
                
        if condition_met == False:
            print(f"Condition not met in file: {file_path}")
            return
        
                    
        
        # Read the replacement header file
        with open(replace_header_file, 'r', encoding='utf-8') as replace_file:
            replace_header = replace_file.read()
        
        # Replace the <title> tag in the replacement content
        replace_header = replace_header.replace("<title></title>", f"<title>{title_name}</title>")
        
        # Combine the replacement header with the remaining lines
        new_content = replace_header + "\n" + "".join(lines)
        
        # Overwrite the original HTML file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        #print(f"Processed and updated: {file_path}")
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

        


def main():
    # Folder containing the HTML files
    folder_path = "github_html"
    
    # Specify the replacement header file
    replace_header_file = "replace_header.txt"
    
    if not os.path.isfile(replace_header_file):
        print(f"Replacement header file '{replace_header_file}' not found. Please ensure it exists.")
        return
    
    # List all HTML files in the folder, excluding those with 'ehime' in the filename
    for file_name in os.listdir(folder_path):
        # Check if the file is an HTML file and does not contain 'ehime'
        if file_name.endswith(".html"):
            file_path = os.path.join(folder_path, file_name)
            
            if not os.path.isfile(file_path):
                print(f"Skipping invalid file: {file_path}")
                continue
            
            # Process the file
            process_html_file(file_path, replace_header_file)

if __name__ == "__main__":
    main()


