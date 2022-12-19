| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# XML 1 - Find the Score

You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.

__Input Format__

The first line contains $n$, the number of lines in the XML document.

The next $n$ lines follow containing the XML document.

__Output Format__

Output a single line, the integer score of the given XML document.

__Sample Input__

```
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
```

__Sample Output__

```
5
```

__Explanation__

The feed and subtitle tag have one attribute each - lang.

The title and updated tags have no attributes.

The link tag has three attributes - rel, type and href.

So, the total score is $1 + 1 + 3 = 5$

There may be any level of nesting in the XML document. To learn about XML parsing, refer [here]()

__Note:__ in order to parse and generate an XML element tree, use the following code:

```python
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))
```

Here, XML is the variable containing the string.

Also, to find the number of keys in a dictionary, use the len function:

```python
>> dicti = {'0': 'This is zero', '1': 'This is one'}
>> print (len(dicti))

2
```

---

<details><summary>Solution</summary>
    
```python
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    attr_number = 0
    
    for child in node.iter():
        attr_number += len(child.attrib)

    return attr_number

    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
```
</details>
