#2017_fujinsan.html
#2017_amakusa
#2017_nagano

import os
import re

def process_html(input_file, template_file, output_file):
    # Step 1: Read the input HTML file
    with open(input_file, 'r', encoding='utf-8') as infile:
        input_lines = infile.readlines()

    # Step 2: Extract content between "<p>上一章</p>" and "<p>下一章</p>"
    start_marker = "<p>上一章</p>"
    end_marker = "<p>下一章</p>"
    extracting = False
    extracted_content = []
    img_counter = 1

    for line in input_lines:
        # Remove <a href> tags with "http://hotels.ctrip.com"
        line = re.sub(r'<a href="http://hotels\.ctrip\.com[^>]*>.*?</a>', '', line)
        
        # Remove <a href> tags with "http://you.ctrip.com/sight/"
        line = re.sub(r'<a href="http://you\.ctrip\.com/sight/[^>]*>.*?</a>', '', line)

        # Check for <img class="replace-file-img"> and replace it with desired <div> and <img> tag
        if '<img class="replace-file-img"' in line:
            # Create the new <div> and <img> tag
            new_div = f"""
                <div class="picture-container">
                <img border="0" class="picture" data-original-height="1536" data-original-width="2048"
                src="https://poonh.github.io/travel_blog/html_pics/2017_nagano/{img_counter}.JPG"/>
                <div style="text-align: center;">
                </div></div>
            """
            extracted_content.append(new_div.strip())  # Append the new image structure
            img_counter += 1  # Increment image counter
            continue  # Skip the original <img> line

        # Preserve lines of content between images
        if start_marker in line:
            extracting = True  # Start extracting after this line
            continue
        if end_marker in line:
            break  # Stop extracting before this line
        if extracting:
            extracted_content.append(line.strip())

    extracted_content = "\n".join(extracted_content)

    # Step 3: Read the template HTML file
    with open(template_file, 'r', encoding='utf-8') as template:
        template_lines = template.readlines()

    # Step 4: Insert extracted content into the template
    main_start_marker = "<!--main content begins-->"
    main_end_marker = "<!--main content ends-->"
    output_lines = []
    content_inserted = False

    for line in template_lines:
        output_lines.append(line)
        if main_start_marker in line and not content_inserted:
            output_lines.append(extracted_content + "\n")
            content_inserted = True

    # Step 5: Write to the output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(output_lines)

    print(f"Processed content saved to {output_file}")


# Example usage
input_html = "blogger_new_html/2018_shiretoko.html"
template_html = "template.html"
output_html = "github_html/2018_shiretoko.html"

process_html(input_html, template_html, output_html)

