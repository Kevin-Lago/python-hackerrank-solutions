| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/arithmetic_operators)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/loops)</img> |
|:---|:---:|---:|

# Python: Division

__Task__

The provided code stub reads two integers, $a$ and $b$, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division ___a // b___. The second line should contain the result of float division, ___a / b___.

No rounding or formatting is necessary.

__Example__

$a = 3$

$b = 5$

- The result of integer division $3 / 5 = 0$.

- The result of float division is $3 / 5 = 0.6$.

Print:

```
0
0.6
```

__Input Format__

The first line contains the first integer, $a$.

The second line contains the second integer, $b$.

__Output Format__

Print the two lines as described above.

__Sample Input 0__

```
4
3
```

__Sample Output 0__

```
1
1.33333333333
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)
```
</details>
