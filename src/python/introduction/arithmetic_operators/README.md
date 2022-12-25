| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/python_if_else)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/python_division)</img> |
|:---|:---:|---:|

# Arithmetic Operators

__Task__

The provided code stub reads two integers from STDIN, $a$ and $b$. Add code to print three lines where:

1. The first line contains the sum of the two numbers.

2. The second line contains the difference of the two numbers (first - second)

3. The third line contains the product of the two numbers.

__Example__

$a = 3$

$b = 5$

Print the following:

```
8
-2
15
```

__Input Format__

The first line contains the first integer, $a$.

The second line contains the second integer, $b$.

__Constraints__

- $1 \le a \le 10^{10}$

- $1 \le b \le 10^{10}$

__Output Format__

Print the three lines as explained above.

__Sample Input 0__

```
3
2
```

__Sample Output 0__

```
5
1
6
```

__Explanation__

$3 + 2 = 5$

$3 - 2 = 1$

$3 * 2 = 6$

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)
```
</details>
