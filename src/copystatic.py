import os
import shutil

def copy_content(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    if not os.path.exists(src):
        raise Exception("path to source doesn't exist")
        
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