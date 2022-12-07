# Capitalize!

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, ```alison heck``` should be capitalized correctly as ```Alison Heck```.

__alison heck -> Alison Heck__

Given a full name, your task is to capitalize the name appropriately.

__Input Format__

A single line of input containing the full name, ___s___.

__Constraints__

- __0 < _len(s)_ < 1000__

- The string consists of alphanumeric characters and spaces.

__Note:__ in a word only the first character is capitalized. Example ```12abc``` when capitalized remains ```12abc```.

__Output Format__

Print the capitalized string, ___s___.

__Sample Input__

```
chris alan
```

__Sample Output__

```
Chris Alan
```

__Solution__

```python
import os


def solve(s):
    return " ".join(s[:1].upper() + s[1:] for s in s.split(" "))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
```
