def modify_html(input_html):
    # Read the new header content from "new_header_all.txt"
    with open("new_header_all.txt", "r", encoding="utf-8") as new_header_file:
        new_header_content = new_header_file.read()
    
    # Read the content to be added from "add_image_icon.txt"
    with open("image_icon.txt", "r", encoding="utf-8") as image_icon_file:
        image_icon_content = image_icon_file.read()
    
    # Read the HTML file content
    with open(input_html, "r", encoding="utf-8") as html_file:
        html_content = html_file.readlines()
    
    # Step 1: Remove all content before </header> and replace with new_header_all.txt
    modified_content = []
    header_found = False
    for line in html_content:
        if "</header>" in line:
            header_found = True
            # Insert new header content and keep the </header> line
            modified_content.append(new_header_content + "\n")
            modified_content.append(line)
            continue
        # Skip lines before </header>
        if header_found:
            modified_content.append(line)
    
    # Step 2: Look for <article> followed by <br><br><br><br> and add image icon content
    final_content = []
    i = 0
    while i < len(modified_content):
        line = modified_content[i]
        final_content.append(line)
        
        # Check for <article> and <br><br><br><br> sequence
        if "<article>" in line and i + 1 < len(modified_content) and "<br><br><br><br>" in modified_content[i + 1]:
            final_content.append(modified_content[i + 1])  # Append the <br><br><br><br> line
            final_content.append(image_icon_content + "\n")  # Insert image icon content after <br><br><br><br>
            i += 1  # Skip the <br><br><br><br> line already processed
            
        i += 1
    
    # Write the modified content back to the original HTML file
    with open(input_html, "w", encoding="utf-8") as html_file:
        html_file.writelines(final_content)
    
    print(f"Modified '{input_html}' successfully.")

# Get the input HTML file from the user

input_html = "2023_setouchi"
modify_html(f"github_html/{input_html}_ad.html")
modify_html(f"github_html/{input_html}_info.html")
modify_html(f"github_html/{input_html}.html")

