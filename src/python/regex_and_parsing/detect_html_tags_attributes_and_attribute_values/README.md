| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/html_parser_part_2)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/validating_uid)</img> |
|:---|:---:|---:|

# Detect HTML Tags, Attributes and Attribute Values

You are given an HTML code snippet of $n$ lines.

Your task is to detect and print all the HTML tag, attributes and attribute values.

Print the detected items in the following format:

```
Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]
```

The ```->``` symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.

The ```>``` symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

__Note:__ Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (```<!-- Comments -->```). Comments can be multiline.

All attributes have an attribute value.

__Input Format__

The first line contains an integer $n$, the number of lines in the HTML code snippet.

The next $n$ lines contain HTML code.

__Constraints__

$0 < n < 100$

__Output Format__

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.

Format your answer as explained in the problem statement.

__Sample Input__

```
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
```

__Sample Output__

```
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
```

__Explanation__

- __head__ tag: Print the head tag only because it has no attribute.

- __title__ tag: Print the title tag only because it has no attribute.

- __object__ tag: Print the object tag. In the next $4$ lines, print the attributes type, data, width and height along with their respective values.

- __<!-- Comment -->__ tag: Don't detect anything inside it.

- __param__ tag: Print the param tag. In the next $2$ lines, print the attributes name along with their respective values.

---

<details><summary>Solution</summary>
    
```python
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
```
</details>
