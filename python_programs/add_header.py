import re

def modify_html_file(html_file, header_file='replace_header.txt'):
    # Read the replacement content for <header> from the text file
    with open(header_file, 'r', encoding='utf-8') as f:
        header_content = f.read()

    # Read the original HTML file content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Replace content within <header> tags
    header_pattern = re.compile(r'(<header>)(.*?)(</header>)', re.DOTALL)
    modified_content = re.sub(header_pattern, rf'\1{header_content}\3', html_content)

    # Check if <article> is followed immediately by <br><br><br><br> on the next line and add if missing
    article_pattern = re.compile(r'(<article>\s*\n)(?!<br><br><br><br>\s*\n)')
    modified_content = re.sub(article_pattern, r'\1<br><br><br><br>\n', modified_content)

    # Write the modified content back to the original file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    print(f"Modified {html_file} successfully.")

filename="2022_yuki"

html_file = f'github_html/{filename}_ad.html'  # replace with your file
modify_html_file(html_file)

html_file = f'github_html/{filename}_info.html'  # replace with your file
modify_html_file(html_file)

html_file = f'github_html/{filename}.html'  # replace with your file
print(html_file)
modify_html_file(html_file)

print(f"open github_html/{filename}_ad.html github_html/{filename}_info.html github_html/{filename}.html")
