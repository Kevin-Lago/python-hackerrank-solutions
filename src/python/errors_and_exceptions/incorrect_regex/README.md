| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/errors_and_exceptions/exceptions)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/classes/classes_dealing_with_complex_numbers)</img> |
|:---|:---:|---:|

# Incorrect Regex

You are given a string ___s___.

Your task is to find out whether ___s___ is a valid [regex](https://en.wikipedia.org/wiki/Regular_expression) or not.

__Input Format__

The first line contains integer ___t___, the number of test cases.

The next ___t___ lines contains the string ___s___.

__Constraints__

- $0 < t < 100$

__Output Format__

Print ```True``` or ```False``` for each test case.

__Sample Input__

```
2
.*\+
.*+
```

__Sample Output__

```
True
False
```

__Explanation__

__.*/+__: Valid regex.

__.*+__: Has the error ```multiple repeat```. Hence it is invalid.

---

<details><summary>Solution</summary>
    
```python
import re

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        s = input()

        try:
            re.compile(s)
            print("True")
        except Exception:
            print("False")
```
</details>