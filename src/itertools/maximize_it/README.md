| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Maximize It!

You are given a function $f(x) = x^2$. You are also give ___k___ lists. The $i^th$ list consists of $n_{i}$ elements.

You have to pick one element from each list so that the value from the equation below ismaximized:

$s = (f(x_{1}) + f(x_{2}) + ... + f(x_{k})) % m$

$x_{i}$ denotes the element picked from the $i^th$ list. Find the maximized value $s_{max}$ obtained.

$%$ denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

__Input Format__

The first line contains __2__ space separated integers ___k___ and ___m___.

The next ___k___ lines each contains an integer $n_{i}$, denoting the number of elements in the $i^th$ list, followed by $n_{i}$ space separated integers denoting the elements in the list.

__Constraints__

$1 \le k \le 7$

$1 \le m \le 1000$

$1 \le n_{i} \le 7$

$1 \le Magnitude of elements in list$

__Output Format__

Output a single integer denoting the value $s_{max}$.

__Sample Input__

```
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
```

__Sample Output__

```
206
```

__Explanation__

Picking $5$ from the $1^st$ list, $9$ from the $2^nd$ list and $10$ from the $3^rd$ list give the maximum $s$ value equal to $(5^2 + 9^2 + 10^2) % 1000 = 206$

---

<details><summary>Solution</summary>
    
```python

```
</details>