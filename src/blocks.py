from enum import Enum
from htmlnode import *
from textnode import *
from convertnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    for obj in blocks:
        if obj == "":
            continue
        obj = obj.strip()
        filtered_blocks.append(obj)
    return filtered_blocks

def block_to_block_type(block):
    #heading
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
            

    #code
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    #quote
    blocklist = block.split("\n")
    quoteflag = False
    for line in blocklist:
        line = line.strip()
        if not line.startswith(">"):
            quoteflag = False
            break
        quoteflag = True
    if quoteflag == True:
        return BlockType.QUOTE
        
    #unordered list
    unorderedflag = False
    for line in blocklist:
        line = line.strip()
        if not line.startswith("- "):
            unorderedflag = False
            break
        unorderedflag = True
    if unorderedflag == True:
        return BlockType.UNORDERED_LIST
    
    #ordered list
    number = 0
    orderedflag = False
    for line in blocklist:
        number += 1
        line = line.strip()
        if not line.startswith(f"{number}. "):
            orderedflag = False
            break
        orderedflag = True
    if orderedflag == True:
        return BlockType.ORDERED_LIST

    #paragraph
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    blocktype = block_to_block_type(block)

    if blocktype == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if blocktype == BlockType.HEADING:
        return heading_to_html_node(block)
    if blocktype == BlockType.CODE:
        return code_to_html_node(block)
    if blocktype == BlockType.QUOTE:
        return quote_to_html_node(block)
    if blocktype == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if blocktype == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):

    return ParentNode("", children, None)

def code_to_html_node(block):
    

def quote_to_html_node(block):
    return ParentNode("blockquote", children, None)

def unordered_list_to_html_node(block):
    return ParentNode("ul", children, None)

def ordered_list_to_html_node(block):
    return ParentNode("ol", children, None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

