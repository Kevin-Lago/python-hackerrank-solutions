# String Split and Join

In python, a string can be split on a delimiter.

__Example__

```python
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings.
>>> print(a)
['this', 'is', 'a', 'string']
```

Joining a string is simple:

```python
>>> a = "-".join(a)
>>> print(a)
this-is-a-string
```

__Task__

You are given a string. Split the string on a "``` ```" (space) delimitr and join using a ```-``` hyphen.

__Function Description__

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

- string line: a string of space separated words.

__Returns__

- string: the resulting string

__Input Format__

The one line contains a string consisting of space separated words.

__Sample Input__

```
this is a string
```

__Sample Output__

```
this-is-a-string
```

__Solution__

```python
def split_and_join(line):
    split_line = line.split(" ")
    return "-".join(split_line)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
```

