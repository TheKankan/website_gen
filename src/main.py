from textnode import *
import os
import shutil
from copystatic import copy_content
from generatepage import generate_pages_recursive
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_content(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()