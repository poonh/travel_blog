import glob
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin
import re
from datetime import datetime
import requests
import time

# Function to clean the title by removing unwanted symbols and extra spaces
def clean_title(title):
    # Replace various quotation marks with a space
    cleaned_title = re.sub(r'[“”"\'《》()（）:：]+', ' ', title)
    # Remove leading and trailing spaces
    cleaned_title = cleaned_title.replace(" ","")
    return cleaned_title

def update_index_file(year,cate,title,author,content,newhtmlname,index_file):
     first_line = f'<a href="https://yhcqw.github.io/yhcq/{newhtmlname}"target="_blank"><i>{title}({author})</i></a>({year})</br>\n '
     pattern = r'[\(（](http[^\s\)）]+)[\)）]'
     def replace_link(match):
        url = match.group(1)
        return f'<a href="{url}" target="_blank">'
     content = re.sub(pattern, replace_link, content)
     all_content = first_line+'\n'+content+"\n"+'<hr class="linebreak">\n'
     cate_item = ["wenge-begins","mao-begins","society-begins","people-begins","foreign-begins"," mis-begins","discussion-begins"]
     cate_line = []
     today = datetime.today()
     formatted_date = today.strftime("%Y年%-m月%-d日")
     with open(index_file,"r") as indexfile:
         lines = indexfile.readlines()
         for i,line in enumerate(lines):
             if "最后更新" in line:
                 lines[i] = f"最后更新：{formatted_date}</br>\n"
         for cat in cate_item:
            for i,line in enumerate(lines):
                if cat in line:
                    cate_line.append(i+7)
            continue
     if cate == "wenge":
        lines.insert(cate_line[0], all_content + '\n')
     elif cate == "mao":
        lines.insert(cate_line[1], all_content + '\n')
     elif cate == "society":
        lines.insert(cate_line[2], all_content + '\n')
     elif cate == "people":
        lines.insert(cate_line[3], all_content + '\n')
     elif cate == "foreign":
        lines.insert(cate_line[4], all_content + '\n')
     elif cate == "mis":
        lines.insert(cate_line[5], all_content + '\n')
     elif cate == "discussion":
        lines.insert(cate_line[6], all_content + '\n')
     with open(index_file, "w", encoding='utf-8') as newfile:
        newfile.writelines(lines)  # Use writelines() on the file object, not on the list
   
def check_for_repetition(year,title,author,indexhtml):
    with open(indexhtml,"r") as index_html:
         lines = index_html.readlines()
         for line in lines:
             if (line.find('<a href="https://yhcqw.github.io/yhcq') != -1 and line.find(year) != -1 and line.find(title) != -1) or (line.find('<a href="https://yhcqw.github.io/yhcq') != -1 and line.find(year) != -1 and line.find(author) != -1):
                 return False
    return True
          
          
def extract_OEBPS_content(html_file_path):
    html_file_path = f'book/OEBPS/{html_file_path}'
    with open(html_file_path, 'r', encoding='utf-8') as file:
        # Read and parse the HTML file
        html_file_path = f'book/OEBPS/{html_file_path}'
        soup = BeautifulSoup(file, 'html.parser')
        
        # Find the <h2> tag
        h2_tag = soup.find('h2')
        if not h2_tag:
            return "No <h2> tag found in the HTML file."

        # Get all content after <h2> tag
        content = h2_tag.find_all_next()
        
        # Convert the content to string, excluding the last 4 lines
        extracted_lines = []
        for item in content:
            if item.name:
                extracted_lines.append(str(item))
        
        if len(extracted_lines) < 4:
            return "Not enough content to exclude the last 4 lines."

        # Join lines and exclude the last 4 lines
        extracted_text = '\n'.join(extracted_lines)
        return extracted_text

def retrieve_OEBPS(year,title,author,indexfile):
    yr = year[:4]        # First 4 characters for the year
    issue_number = year[4:]  # Last 2 characters for the issue number
    # Remove leading zero from issue number if present and format the output
    title = clean_title(title)
    formatted_issue = f"{yr}年第{int(issue_number)}期"
    print(f"Retrieving {yr}年第{int(issue_number)}期 {title}")
    with open("index1999-2010.txt", "r", encoding="utf-8") as indexfile:
       lines = indexfile.readlines()  # Read all lines at once
       location = None
#       linenumber = None
    # Loop through lines to find the required information
       for i, line in enumerate(lines):
        # Extract parts from each line
           title_from_index_1999 = clean_title(line.split()[2])
           magnum = line.split()[1]
           if "作者:" in line:
               author_from_index_1999 = line.split("作者:")[1]
           else:
               author_from_index_1999 = "No author"
        # Perform the comparison to find the location
           if (formatted_issue == magnum and title == title_from_index_1999) or (formatted_issue == magnum and author.split()[0] in author_from_index_1999.split()[0]):
              location = line.split()[0]
#              linenumber = i - 1
              break  # Stop loop once location is found
       if location:
          extract_OEBPS_content(str(location))
          return location
       else:
          return f"X:{formatted_issue} {title}"
    
def author_pinyin(author):
    authorpy=pinyin.get(author.split()[0],format="strip")
    return authorpy
    
def extract_notes_from_pages(pagesfile):

    def extract_content(lines):
        year = lines[0].strip()
        pattern = r'\[(.*?)\](.*)\s*[（(](.*?)[）)]$'
        match = re.match(pattern, lines[1])
        if match:
           category = match.group(1).strip()  # Extract category
           title = match.group(2).strip()     # Extract title
           author = match.group(3).strip()    # Extract author
           content = []
           for i in range(2,len(lines)):
              if lines[i].find("SQL") == -1:
#                 content = content + f'{lines[i]}'+"\n"
                 if len(lines[i]) != 1:
                    lines[i] = lines[i].replace("\n","")
                    content.append(f'{lines[i]}</br>')
              else:
                 break
           content_str = "\n".join(content)
        else:
            print(f'{line[0].replace("\n","")} {line[1]} not extracted')
       
        return year,category,title,author,content_str
  
    linebegin= []
    lineend = []
    years = []
    categories = []
    titles = []
    authors = []
    contents = []

    with open(pagesfile, 'r', encoding='utf-8') as file:
         lines = file.readlines()
         
    for index, line in enumerate(lines, start=0):
        if line.strip().isdigit() and len(line.strip()) == 6:
            linebegin.append(index) #continue here line end
    
    for i in range(1,len(linebegin)):
        lineend.append(linebegin[i]-1)
        
    lineend.append(len(lines)-1)
# Iterate over the lines and check for the year-month pattern
    for i in range(0,len(linebegin)):
        if (lines[linebegin[i]+1].find("[") != -1 and lines[linebegin[i]+1].find("]") != -1):
            year,category,title,author,content = extract_content(lines[linebegin[i]:lineend[i]])
            years.append(year)
            categories.append(category)
            titles.append(title)
            authors.append(author)
            contents.append(content)
    return years,categories,titles,authors,contents

    
    


 


def combinefile(templatefile,articlehtml,newfilename):
    main_before,main_after = extract_template(templatefile)
    main_content = extract_main_content(articlehtml)
    new_content = main_before+main_content+main_after
    with open(newfilename, 'w', encoding='utf-8') as file:
        file.write(new_content)
        
        
def list_html_files(directory):
    # Create the search pattern
    pattern = os.path.join(directory, '*.html')
    
    # Use glob to find all files matching the pattern
    html_files = glob.glob(pattern)
    
    # Extract filenames from the full paths
    html_files = [os.path.basename(file) for file in html_files]
    
    return html_files


def extract_text_from_html(file_path,template,newfile):#extract text from blogger html
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extract the title text
    title_element = soup.find('title')
    title_text = title_element.text if title_element else None
    
    
    # Find the first occurrence of the <time class='published'>
    time_element = soup.find(lambda tag: tag.name == "time" and "published" in tag.get("class", []))

    
    if time_element:
        # Get the parent element to start extracting text from the first following tag
        start_element = time_element.find_next()
        # Extract text starting from the found tag
        extracted_text = []
        if start_element:
            for element in start_element.children:
                extracted_text.append(str(element))
        extracted_text_combined = '\n'.join(extracted_text)
        main_before,main_after = extract_template(template)
        main_before = main_before.replace("<title></title>",f"<title>{title_text}</title>")
        main_before = main_before.replace('<h3 style="text-align: center";></h3>',f'<h3 style="text-align: center";>{title_text}</h3>')
        new_content = main_before+extracted_text_combined+main_after
        with open(newfile, 'w', encoding='utf-8') as file:
            file.write(new_content)
        return title_text, extracted_text_combined
    
    return None, None  # Return None if <time class='published'> is not foundp


def rewrite_new_html_to_upload(input_file, output_file, folder):
    # Read the input HTML file
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use the lxml parser for better handling of HTML
    soup = BeautifulSoup(html_content, 'lxml')  # Use 'lxml' parser for better HTML handling

    # Find the <main> tag
    main_tag = soup.find('main')
    if main_tag is not None:
        # Extract the inner content of <main> (without the <main> tag itself)
        main_content = main_tag.decode_contents()

        # Parse the inner content as a new BeautifulSoup object
        main_soup = BeautifulSoup(main_content, 'lxml')

        # Remove all <div> tags but keep their content
        for div in main_soup.find_all('div'):
            div.unwrap()

        # Remove all <span> tags while keeping the content
        for span in main_soup.find_all('span'):
            span.unwrap()

        # Replace <a> with <img> tags for images
        image_count = 1  # Counter for images
        for anchor in main_soup.find_all('a'):
            img_tag = anchor.find('img')
            if img_tag and img_tag['src']:
                # Create the new image tag
                new_img_tag = f'<div class="picture-container">\n' \
                              f'<img class="picture" src="https://yhcqw.github.io/yhcq/longdiary_html_pics/{folder}/{image_count}.JPG"/>\n' \
                              '</div>\n'
                # Replace the anchor with the new image tag
                anchor.replace_with(BeautifulSoup(new_img_tag, 'lxml'))
                image_count += 1  # Increment the image count

        # Convert back to string and add <br/><br/> after each closing </p> tag
        result_main_html = str(main_soup).replace('</p>', '</p><br/><br/>')

        # Clear the existing content in <main> and add modified content back
        main_tag.clear()
        main_tag.append(BeautifulSoup(result_main_html, 'lxml'))

    # Write the modified HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Cleaned and modified HTML content has been saved to {output_file}")



def download_images_from_html(html_file, save_folder):
    # Create the folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Read the HTML content from the file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    valid_extensions = ('.jpg','.jpeg','.JPG','.JPEG','.PNG''.png')

    for index, img in enumerate(images, start=1):
        img_url = img.get('src')
        downloaded_num = len(images)
        parts = img_url.split("/")
        if parts[2] == "s5000":
           img_url = img_url
        else:
           parts[-2] = "s4032"
           img_url = "/".join(parts)

#        print(index,img_url)
#        if img_url and img_url.endswith(valid_extensions):
        if img_url:  # Ensure it's a JPG image
            try:
                # Send a GET request to the image URL
                response = requests.get(img_url)
                response.raise_for_status()  # Check for request errors

                # Define the file path
                file_path = os.path.join(save_folder, f"{index}.JPG")

                # Save the image to the specified path
                with open(file_path, 'wb') as f:
                    f.write(response.content)

                print(f"Downloaded: {file_path}")
            except Exception as e:
                print(f"Failed to download {img_url}: {e}")
                
    jpg_files = glob.glob(os.path.join(save_folder, "*.JPG"))
    if len(jpg_files) == downloaded_num:
        print(f'{save_folder} all files successfully downloaded')
    else:
        print(jpg_files,downloaded_num)
        print(f'{save_folder} is missing some images')

def save_html(url, folder):
    # Extract the year and month from the URL (last part of the URL)
    parts = url.rstrip('/').split('/')
    year_month = parts[-2] + parts[-1]  # Concatenate year and month, e.g., '202403'
    file_name = f"{year_month}.html"
    
    # Define the file path
    file_path = os.path.join(folder, file_name)
    
    # Send an HTTP request to get the HTML content
    response = requests.get(url)
    
    # Save the HTML content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    print(f"Saved: {file_path}")

def save_html_from_file(input_file, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Read the input file line by line
    with open(input_file, 'r') as infile:
        for line in infile:
            url = line.strip()
            if url:
                save_html(url, output_folder)

def extract_links(soup):
    """Extract all unique links from the soup that match the criteria."""
    links = set()  # Use a set to store links to avoid duplicates
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('https://soybeantravel.blogspot.com/') and href.endswith('.html'):
            links.add(href)
    return links

def find_more_posts_link(soup):
    """Find the link to '更多博文' (More Posts) if it exists."""
    more_posts_link = soup.find('a', {'class': 'blog-pager-older-link'}, href=True)
    if more_posts_link:
        return more_posts_link['href']
    return None

def get_html_content(url):
    """Send a request to the URL and return the parsed BeautifulSoup object."""
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return BeautifulSoup(response.text, 'html.parser')

def save_links_to_file(links, file_name):
    """Save the unique links to a file."""
    with open(file_name, 'w') as file:
        for link in sorted(links):
            file.write(f"{link}\n")
    print(f"All links saved to {file_name}")

def extract_all_links(initial_file, output_file):
    base_url = 'https://soybeantravel.blogspot.com/'
    all_links = set()  # To store all unique links

    # Read the initial HTML file
    with open(initial_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the initial HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract the initial set of links
    all_links.update(extract_links(soup))
    
    # Find and follow the "更多博文" (More Posts) link
    more_posts_link = find_more_posts_link(soup)
    
    while more_posts_link:
        print(f"Following link: {more_posts_link}")
        
        # Get the HTML content of the next page
        soup = get_html_content(more_posts_link)
        
        # Extract links from the new page and update the set
        all_links.update(extract_links(soup))
        
        # Find the next "更多博文" link, if any
        more_posts_link = find_more_posts_link(soup)
        
        # Pause briefly between requests to avoid overwhelming the server
        time.sleep(1)
    
    # Save the collected links to the output file
    save_links_to_file(all_links, output_file)


# Function to download content and create files/folders
def process_blogger_links(file_path):
    html_folder = 'blogger_html'
    html_pics_folder = 'html_pics'
    with open(file_path, 'r') as file:
        for line in file:
            # Split line into link and name
            link, name = line.strip().split(' ')
            # Define paths
            html_file_path = os.path.join(html_folder, f'{name}.html')
            pics_folder_path = os.path.join(html_pics_folder, name)
            
            # Create directory for pictures
            os.makedirs(pics_folder_path, exist_ok=True)
            print(f'Created folder: {pics_folder_path}')
            
            # Fetch the content from the link
            try:
                response = requests.get(link)
                response.raise_for_status()  # Raise an exception for HTTP errors
                
                # Save the content to the HTML file
                with open(html_file_path, 'w', encoding='utf-8') as html_file:
                    html_file.write(response.text)
                print(f'Saved HTML file: {html_file_path}')
            
            except requests.exceptions.RequestException as e:
                print(f"Failed to retrieve {link}: {e}")

# Run the function with the text file containing the links and names

