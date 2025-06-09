import unittest

from textnode import *
from convertnode import *


class TestConvertNode(unittest.TestCase):
    def test_result(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes, 
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ]
        )

    def test_empty(self):
        node = TextNode("", TextType.NORMAL)

        with self.assertRaises(Exception):
            split_nodes_delimiter(node, "`", TextType.CODE)

    def test_result_multiple(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        node2 = TextNode("also `code block`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)

        self.assertEqual(
            new_nodes, 
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
                TextNode("also ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
            ]
        )

    def test_result_no_start(self):
        node = TextNode("`code block` coding", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes, 
            [
                TextNode("code block", TextType.CODE),
                TextNode(" coding", TextType.NORMAL),
            ]
        )

    def test_result_single(self):
        node = TextNode("`code block`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes, 
            [
                TextNode("code block", TextType.CODE),
            ]
        )
    
    def test_result_invalid_type(self):
        node = TextNode("this should not work `code block`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        with self.assertRaises(Exception):
            split_nodes_delimiter(node, "`", TextType.CODE)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.NORMAL),
            ],
            new_nodes,
        )
    
if __name__ == "__main__":
    unittest.main()