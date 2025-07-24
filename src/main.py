from textnode import *
import os
import shutil
from copystatic import copy_content

dest = os.path.join(os.getcwd(), "public")
src = os.path.join(os.getcwd(), "static")

def main():
    print("Deleting public directory...")
    if os.path.exists(dest):
        shutil.rmtree(dest)

    print("Copying static files to public directory...")
    copy_content(src, dest)


main()