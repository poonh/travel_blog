import create_art_commands
import ebooklib
from ebooklib import epub
import shutil
import os
import subprocess
import glob
#create_art_commands.retrieve_OEBPS()

#folders = [item for item in os.listdir("longdiary_html_pics") if os.path.isdir(os.path.join("longdiary_html_pics", item))]
#print(folders)
folder = '2024_chaozhou'
with open("github_command.txt","w") as gitfile:
     B = f'mkdir html_pics/{folder}\n'
     Bb = f'touch html_pics/{folder}/test\n'
     C = f'git add html_pics/{folder}\n'
     D = f'git commit -m "Add html_pics/{folder} with initial files"\n'
     E = f'git push origin main\n'
     A = f'cp /Users/china_108/Desktop/travel_journal/html_pics/{folder}/* html_pics/{folder}/.\n'
     gitfile.write(B+Bb+C+D+E+A)
     jpg_files = [f for f in os.listdir(f'html_pics/{folder}') if f.endswith('.JPG')]
     count = len(jpg_files)
     for jpg in jpg_files:
           a = f'git add --force html_pics/{folder}/{jpg}\n'
           b = f'git commit -m "Upload html_pics/{folder}/{jpg}"\n'
           c = 'git push origin main\n'
           gitfile.write(a+b+c)




exit()
with open("github_command.txt","w") as gitfile:
     folder_path = f'longdiary_html'
     html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]
     count = len(html_files)
     for html in html_files:
           A = f'cp /Users/china_108/Desktop/yhcq2/longdiary_html/{html} longdiary_html/.\n'
           a = f'git add --force longdiary_html/{html}\n'
           b = f'git commit -m "Upload longdiary_html/{html}"\n'
           c = 'git push origin main\n'
           gitfile.write(A+a+b+c)

  

with open("github_command.txt","w") as gitfile:
   for folder in folders:
     folder_path = f'longdiary_html_pics/{folder}'
     if os.path.exists(folder_path) and os.path.isdir(folder_path):  # Check if the folder exists
        jpg_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.jpg')]
        jpg_count = len(jpg_files)
        print(f"{folder}: {jpg_count} JPG files")  # Print count with folder name
        for i in range(1,jpg_count+1):
           A = f'cp /Users/china_108/Desktop/yhcq2/longdiary_html_pics/{folder}/{i}.JPG longdiary_html_pics/{folder}/.\n'
           a = f'git add --force longdiary_html_pics/{folder}/{i}.JPG\n'
           b = 'git commit -m "Upload multiple images"\n'
           c = 'git push origin main\n'
           gitfile.write(A+a+b+c)

     else:
        print(f"{folder} does not exist or is not a directory.")


  
    

