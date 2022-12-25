| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/alphabet_rangoli)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/the_minion_game)</img> |
|:---|:---:|---:|

# Capitalize!

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, ```alison heck``` should be capitalized correctly as ```Alison Heck```.

$alison heck -> Alison Heck$

Given a full name, your task is to capitalize the name appropriately.

__Input Format__

A single line of input containing the full name, $s$.

__Constraints__

- $0 < len(s) < 1000$

- The string consists of alphanumeric characters and spaces.

__Note:__ in a word only the first character is capitalized. Example ```12abc``` when capitalized remains ```12abc```.

__Output Format__

Print the capitalized string, $s$.

__Sample Input__

```
chris alan
```

__Sample Output__

```
Chris Alan
```

---

<details><summary>Solution</summary>
    
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
</details>
