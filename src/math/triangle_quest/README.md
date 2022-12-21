| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Triangle Quest

You are given a positive integer $n$. Print a numerical triangle of height $n - 1$ like the one below:

```
1
22
333
4444
55555
......
```

Can you do it using only __arithmetic operations, a single for loop and print statement?__

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

__Note:__ Using anything related to strings will give a score of $0$.

__Input Format__

A single line containing integer, $n$.

__Constraints__

$1 \le n \le 9$

__Output Format__

Print $n - 1$ lines as explained above.

__Sample Input__

```
5
```

__Sample Output__

```
1
22
333
4444
```

---

<details><summary>Solution</summary>
    
```python
[print(int((10 ** i - 1) / 9 * i)) for i in range(1, int(input()))]
```
</details>
