| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# HTML Parser - Part 2

[.handle_comment(data)]()

This method is called when a commend is encountered (e.g. <!-- comment -->).

The data argument is the content inside the comment tag.

```python
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          print "Comment  :", data
```

[.handle_data(data)]()

This method is called to process arbitrary data (e.g. text nodes and the content of <script>...</script> and <style>...</style>).

The data argument is the text content of HTML.

```python
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print "Data     :", data
```

---

__Task__

You are given an HTML code snippet of $n$ lines.

Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:

```
>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:  
```

__Note:__ Do not print data if data == ```'\n'```

__Input Format__

The first line contains integer $n$, the number of lines in the HTML code snippet.

The next $n$ lines contains HTML code.

__Constraints__

$0 < n < 100$

__Output Format__

Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.

__Sample Input__

```
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
```

__Sample Output__

```
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
```

---

<details><summary>Solution</summary>
    
```python
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
```
</details>
