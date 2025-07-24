from textnode import *
import os

def main():
    dest = os.path.join(os.getcwd(), "public")
    src = os.path.join(os.getcwd(), "static")
    copy_content(src, dest)

def copy_content(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(src):
        raise Exception("path to source doesn't exist")

    #Deleting existing elements
    to_delete = os.listdir(dest):
    if to_delete != []: 
        for element in to_delete:
            full_path = os.path.join(dest, element)
            if os.path.isfile(full_path): #delete file
                os.remove(full_path)
            elif os.path.isdir(full_path): #delete folder
                shutil.rmtree(full_path)
        
    #copying elements from src to dest
    to_copy = os.listdir(src)
    if to_copy != []:
        for element in to_copy:
            full_path = os.path.join(src, element)
            if os.path.isfile(full_path): #copy file
                shutil.copy(full_path, dest)
            elif os.path.isdir(full_path): #copy folder
                dest_path = os.path.join(dest, element)
                copy_content(full_path, dest_path)








main()