| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Reduce Function

Given a list of rational numbers, find their product.

__Concept__

The ```reduce()``` function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say ```[1,2,3]``` and you have to find its sum.

```python
>>> reduce(lambda x, y : x + y,[1,2,3])
6
```

You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding thee initial value at the beginning of the list. For example:

```python
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1
```

__Input Format__

First line contains $n$, the number of rational numbers.

The $i^th$ of next $n$ lines contain two integers each, the numerator ($n_{i}$) and denominator ($d_{i}$) of the $i^th$ rational number in the list.

__Constraints__

- $1 \le n \le 100$

- $1 \le n_{i}, d_{i} \le 10^9$

__Output Format__

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than $1$.

__Sample Input__

```
3
1 2
3 4
10 6
```

__Sample Output__

```
5 8
```

__Explanation__

Required product is $1\2 3\4 10\6 = 5\8$

---

<details><summary>Solution</summary>
    
```python
from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda n, d: n * d, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
```
</details>
