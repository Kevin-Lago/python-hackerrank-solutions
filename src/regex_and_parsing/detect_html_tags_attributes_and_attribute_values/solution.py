from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print(f"-> {attr[0]} > {attr[1]}") for attr in attrs]


if __name__ == '__main__':
    n = int(input())
    html = '\n'.join([input() for i in range(n)])
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
