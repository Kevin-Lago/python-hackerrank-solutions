| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/python_functionals/reduce_function)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/re_split)</img> |
|:---|:---:|---:|

# Detect Floating Point Number

You are given a string $n$.

Your task is to verify that $n$ is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

1. Number can start with ```+```, ```-``` or ```.``` symbol.

    For example:
    
    :heavy_check_mark: +4.50
    
    :heavy_check_mark: -1.0
    
    :heavy_check_mark: .5
    
    :heavy_check_mark: -.7
    
    :heavy_check_mark: +.4
    
    :x: -+4.5

2. Number must contains at least $1$ decimal value.

    For example:
    
    :x: 12.
    
    :heavy_check_mark: 12.0

3. Number must have exactly one ```.``` symbol

4. Number must not give any exceptions when converted using $float(n)$

__Input Format__

The first line contains an integer $t$, the number of test cases.

The next $t$ line(s) contains a string $n$.

__Constraints__

- $0 < t < 10$

__Output Format__

Output True or False for each test case.

__Sample Input__

```
4
4.0O0
-1.00
+4.54
SomeRandomStuff
```

__Sample Output__

```
False
True
True
False
```

__Explanation__

$4.0O0$: 'O' is not a digit.

$-1.00$: is valid.

$+4.54$: is valid.

$SomeRandomStuff$: is not a number

---

<details><summary>Solution</summary>
    
```python
import re

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = input()
        test = re.search("^[-+]?\\d*\\.\\d*$", n)

        try:
            another = float(test.group())
            print(True)
        except AttributeError as e:
            print(False)
```
</details>
