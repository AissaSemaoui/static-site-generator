import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_has_text(self): 
        node = TextNode("We testing this text exist", TextType.NORMAL)
        self.assertEqual(node.text, "We testing this text exist")

    def test_has_url (self) : 
        node = TextNode("Testing if the url exist", TextType.LINK, "https://google.com")
        self.assertEqual(node.url, "https://google.com")
        
if __name__ == "__main__":
    unittest.main()
