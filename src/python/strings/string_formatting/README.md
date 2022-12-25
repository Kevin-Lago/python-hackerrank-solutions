| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/designer_door_mat)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/alphabet_rangoli)</img> |
|:---|:---:|---:|

# String Formatting

Given an integer, ___n___, print the following values for each integer ___i___ from __1__ to ____n____:

1. Decimal

2. Octal

3. Hexadecimal (capitalized)

4. Binary

__Function Description__

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

- int number: the maximum value to print

__Prints__

The four values must be printed on a single line in the order specified above for each ___i___ from __1__ to ___number___. Each value should be space-padded to match the width of the binary value of ___number___ and the values should be separated by a single space.

__Input Format__

A single integer denoting ___n___.

__Constraints__

- __1 <= _n_ <= 99__

__Sample Input__

```
17
```

__Sample Output__

```
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
```

---

<details><summary>Solution</summary>
    
```python
def print_formatted(number):
    w = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
```
</details>
