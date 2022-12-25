| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/text_alignment)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/designer_door_mat)</img> |
|:---|:---:|---:|

# Text Wrap

You are given a string $s$ and width $w$.

Your task is to wrap the string into a paragraph of width $w$.

__Function Description__

Complete the wrap function in the editor below.

wrap has the following parameters:

- string string: a long string

- int max_width: the width to wrap to

__Returns__

- string: a single string with newline characters ('\n') where the breaks should be

__Input Format__

The first line contains a string, $s$.

The second line contains the width, $w$.

__Constraints__

- $0 < len(s) < 1000$

- $0 < w < len(s)$

__Sample input__

```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```

__Sample Output__

```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```

---

<details><summary>Solution</summary>
    
```python
import textwrap


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
```
</details>
