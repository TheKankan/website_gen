from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:

        if node.text_type != TextType.NORMAL:
            result.append(node)
        else:
            temp_node = node.text.split(delimiter)
            if len(temp_node) % 2 == 0:
                raise Exception("Invalid Markdown Synthax")

            i = 0
            for word in temp_node:
                if word != "":
                    if i % 2 == 0:
                        result.append(TextNode(word, TextType.NORMAL))
                    else:
                        result.append(TextNode(word, text_type))
                i += 1
    return result
    

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue

        original_text = node.text
        matches = extract_markdown_images(original_text)
        if len(matches) == 0:
            result.append(node)
            continue

        for match in matches:
            sections = original_text.split(f"![{match[0]}]({match[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.NORMAL))
            result.append(TextNode(match[0], TextType.IMAGE, match[1]))
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, TextType.NORMAL))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue

        original_text = node.text
        matches = extract_markdown_links(original_text)
        if len(matches) == 0:
            result.append(node)
            continue

        for match in matches:
            sections = original_text.split(f"[{match[0]}]({match[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.NORMAL))
            result.append(TextNode(match[0], TextType.LINK, match[1]))
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, TextType.NORMAL))

    return result