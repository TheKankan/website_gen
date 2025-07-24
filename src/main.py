from textnode import *
import os
import shutil
from copystatic import copy_content
from generatepage import generate_pages_recursive

dest = os.path.join(os.getcwd(), "public")
src = os.path.join(os.getcwd(), "static")

content = os.path.join(os.getcwd(), "content/")
template = os.path.join(os.getcwd(), "template.html")
output_dir = os.path.join(os.getcwd(), "public/")

def main():
    print("Deleting public directory...")
    if os.path.exists(dest):
        shutil.rmtree(dest)

    print("Copying static files to public directory...")
    copy_content(src, dest)

    generate_pages_recursive(content, template, output_dir)


main()