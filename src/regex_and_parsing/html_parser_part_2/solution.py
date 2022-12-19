from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(f">>> Data \n{data}")


if __name__ == '__main__':
    html = "\n".join([input() for i in range(int(input()))])
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
