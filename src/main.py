from textnode import TextNode, TextType


def main (): 
    node = TextNode('hello', TextType["NORMAL"], 'https://google.com')
    print(node)



main()
