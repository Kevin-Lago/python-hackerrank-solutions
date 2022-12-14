| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Input()

```This challenge is only for Python 2```

[input()]()

In __Python 2__, the expression input() is equivalent to eval(raw_input(prompt)).

__Code__

```python
>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
```

---

__Task__

You are given a [polynomial]() $p$ of a single indeterminate (or variable), $x$.

You are also given the values of $x$ and $k$. Your task is to verify if $p(x) = k$

__Constraints__

All coeffiecients of polynomials $p$ are integers.

$x$ and $y$ are also integers.

__Input Format__

The first line contains the space separated values of $x$ and $k$.

The second line contains the polynomial $p$.

__Output Format__

Print ```True``` if $p(x) = k$. Otherwise, print ```False```.

__Sample Input__


```
1 4
x**3 + x**2 + x + 1
```

__Sample Output__

```
True
```

__Explanation__

$p(1) = 1^3 + 1^2 + 1 + 1 = 4 = k$

Hence, the output is ```True```.

---

<details><summary>Solution</summary>
    
```python

```
</details>
