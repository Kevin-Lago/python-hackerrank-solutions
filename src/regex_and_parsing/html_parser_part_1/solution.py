from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        [print(f"-> {attr[0]} > {attr[1]}") for attr in attrs]

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        [print(f"-> {attr[0]} > {attr[1]}") for attr in attrs]


if __name__ == '__main__':
    n = int(input())
    parser = MyHTMLParser()
    s = "".join([input() for i in range(n)])
    parser.feed(s)
