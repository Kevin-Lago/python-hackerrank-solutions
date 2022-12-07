# Text Wrap

You are given a string ___string___ and width ___max_width___.

Your task is to wrap the string into a paragraph of width ___w___.

__Function Description__

Complete the wrap function in the editor below.

wrap has the following parameters:

- string string: a long string

- int max_width: the width to wrap to

__Returns__

- string: a single string with newline characters ('\n') where the breaks should be

__Input Format__

The first line contains a string, ___string___.

The second line contains the width, ___max_width___.

__Constraints__

- __0 < _len(string)_ < 1000__

- __0 < _max_width_ < len(string)__

__Sample input 0__

```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```

__Sample Output 0__

```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
```

__Solution__

```python
import textwrap


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
```
