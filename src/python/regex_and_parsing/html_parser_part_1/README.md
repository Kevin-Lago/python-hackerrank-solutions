| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/hex_color_code)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/html_parser_part_2)</img> |
|:---|:---:|---:|

# HTML Parser - Part 1

[HTML]()

Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

[Parsing]()

Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

[HTMLParser]()

An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments and other markup elements are encountered.

__Example__ (based on the original Python documentation):

```python
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Found a start tag  :", tag
    def handle_endtag(self, tag):
        print "Found an end tag   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Found an empty tag :", tag

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")
```

__Output__

```
Found a start tag  : html
Found a start tag  : head
Found a start tag  : title
Found an end tag   : title
Found an end tag   : head
Found a start tag  : body
Found a start tag  : h1
Found an end tag   : h1
Found an empty tag : br
Found an end tag   : body
Found an end tag   : html
```

[.handle_starttag(tag, attrs)]()

This method is called to handle the start tag of an element. (For example: <div class='marks'>)

The tag argument is the name of the tag converted to lower case.

The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag's <> brackets.

[.handle_endtag(tag)]()

This method is called to handle the end tag of an element. (For example: </div>)

The tag argument is the name of the tag converted to lowercase.

[.handle_startendtag(tag, attrs)]()

This method is called to handle the empty tag of an element. (For example: <br />)

The tag argument is the name of the tag converted to lowercase.

The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag's <> brackets.

---

__Task__

You are given an HTML code snippet of $n$ lines.

Your task is to print start tags, end tags and empty tags separately.

Format your result in the following way:

```
Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2
```

Here, the ```->``` symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.

The ```>``` symbol acts as a separator of the attribute and the attribute value.

If an HTML tag has no attribute then simply print the name of the tag.

If an attribute has no attribute value then simply print the name of the attribute value as ```None```.

__Note:__ Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (```<-- Comments -->```). Comments can be multi-line as well.

__Input Format__

The first line contains integer $n$, the number of lines in a HTML code snippet.

The next $n$ lines contain HTML code.

__Constraints__

- $0 < n < 100$

__Output Format__

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.

User proper formatting as explained in the problem statement.

__Sample Input__

```
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
```

__Sample Output__

```
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
```

---

<details><summary>Solution</summary>
    
```python
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
```
</details>
