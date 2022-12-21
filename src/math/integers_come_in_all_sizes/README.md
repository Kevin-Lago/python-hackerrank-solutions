| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Integers Come In All Sizes

Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: $2^31 - 1$ (c++ int) or $2^63 - 1$ (c++ long long int).

As we know, the result of $a^b$ grows really fast with increasing $b$.

Let's do some calculations on very large integers.

__Task__

Read four numbers, $a, b, c$ and $d$, and print the result of $a^b + c^d$

__Input Format__

Integers $a, b, c$ and $d$ are given on four separate lines, respectively.

__Constraints__

$1 \le a \le 1000$

$1 \le b \le 1000$

$1 \le c \le 1000$

$1 \le d \le 1000$

__Output Format__

Print the result of $a^b + c^d$ on one line.

__Sample Input__

```
9
29
7
27
```

__Sample Output__

```
4710194409608608369201743232
```

__Note:__ This result is bigger than $2^63 - 1$. Hence, it won't fit in the long long int of C++ or a 64-bit integer.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    a, b, c, d = [int(input()) for i in range(4)]
    print(a**b + c**d)
```
</details>
