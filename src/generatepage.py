import os
from blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(content)
    content = markdown_to_html_node(content).to_html()
    final_output = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True) #create dest_path if it doesn't exist and all necessary directories

    with open(dest_path, "w") as f:
        f.write(final_output)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    if content == []:
        return
    for element in content:
        full_path = os.path.join(dir_path_content, element)
        if os.path.isfile(full_path): #if it's a file we generate a page
            new_path = os.path.join(dest_dir_path, element.replace(".md", ".html")) # new path with .html extension
            generate_page(full_path, template_path, new_path)

        if os.path.isdir(full_path): #if it's a folder we call the function again
            generate_pages_recursive(full_path, template_path, os.path.join(dest_dir_path, element))



def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("no title found")

