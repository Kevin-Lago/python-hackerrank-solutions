| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Between Two Sets

There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered

2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

__Example__

$a = [2, 6]$

$b = [24, 26]$

There are two numbers between the arrays: $6$ and $12$.

$6 % 2 = 0$, $6 % 6 = 0$, $24 % 6 = 0$ and $36 % 6 = 0$ for the first value.

$12 % 2 = 0$, $12 % 6 = 0$ and $24 % 12 = 0$, $36 % 12 = 0$ for the second value. Return $2$.

__Function Description__

Complete the get_total_x function in the editor below. It should return the number of integers that are between the sets.

get_total_x has the following parameter(s):

- int[n] a: an array of integers

- int[m] b: an array of integers

__Returns__

- int: the number of integers that are between the sets

__Input Format__

The first line contains two space-separated integers, $n$ and $m$, the number of elements in arrays $a$ and $b$.

The second line contains $n$ distinct space-separated integers $a[i]$ where $0 \le i < n$.

The third line contains $m$ distinct space-separated integers $b[j]$ where $0 \le j < m$

__Constraints__

- $1 \le n, m \le 10$

- $1 \le a[i] \le 100$

- $1 \le b[j] \le 100$

__Sample Input__

```
2 3
2 4
16 32 96
```

__Sample Output__

```
3
```

__Explanation__

2 and 4 divide evenly into 4, 8, 12 and 16

4, 8 and 16 divide evenly into 16, 32 and 96.

4, 8 and 16 are the only three numbers for which each element of $a$ is a factor of all elements of $b$.

---

<details><summary>Solution</summary>
    
```python

```
</details>
