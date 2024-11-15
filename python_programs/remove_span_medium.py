import re

# Input the HTML file name
file_name = input("Enter the HTML file name (including .html extension): ")

# Regular expressions to match specific <span> and </span> tags
open_span_pattern = re.compile(r'<span\s+style="font-size:\s*medium;">', re.IGNORECASE)
close_span_pattern = re.compile(r'</span>', re.IGNORECASE)

# Read the HTML file
with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

# Remove the specific <span> tags and replace </span> with <br>
modified_content = re.sub(open_span_pattern, '', content)
modified_content = re.sub(close_span_pattern, '<br>', modified_content)

# Overwrite the original file with the modified content
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(modified_content)

print(f"Processed file '{file_name}': removed specific <span> tags and replaced </span> with <br>.")

