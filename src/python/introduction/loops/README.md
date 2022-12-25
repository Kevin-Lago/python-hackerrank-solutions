| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/python_division)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/write_a_function)</img> |
|:---|:---:|---:|

# Loops

__Task__

The provided code stud reads an integer, $n$, from STDIN. For all non-negative integers $i < n$, print $i^{2}$.

__Example__

$n = 3$

The list of non-negative integers that are less than $n = 3$ is $[0, 1, 2]$. Print the square of each number on a separate line.

```
0
1
4
```

__Input Format__

The first and only line contains the integer, $n$.

__Constraints__

- $1 \le n \le 20$

__Output Format__

Print $n$ lines, one corresponding to each ___i___.

__Sample Input 0__

```
5
```

__Sample Output 0__

```
0
1
4
9
16
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i * i)
```
</details>
