import unittest

from htmlnode import HTMLNode 


class TestHTMLNode (unittest.TestCase): 
    def test_has_tag (self) : 
        node = HTMLNode("p")
        self.assertEqual(node.tag, "p")

    def test_has_value (self) : 
        node = HTMLNode("p", 'hello world')
        self.assertEqual(node.value, "hello world")

    def test_has_children (self) : 
        node = HTMLNode("p", None, [HTMLNode("p", "I'm a child")])
        self.assertEqual(len(node.children), 1)
