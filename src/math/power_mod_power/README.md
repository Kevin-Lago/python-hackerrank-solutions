| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Power - Mod Power

So far, we have only heard of Python's powers. Now, we will witness them!

Powers or exponents in Python can be calculated using the built-in power function. Call he power function $a^b$ as shown below.

```python
pow(a, b)
```

or

```python
a ** b
```

It's also possible to calculate $a^b % m$

```python
pow(a, b, m)
```

This is very helpful in combinations where you have to print the resultant % mod.

__Note:__ Here, $a$ and $b$ can be floats or negatives, but, if a third argument is present, $b$ cannot be negative.

__Note:__ Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().

__Task__

You are given three integers: $a$, $b$ and $m$. Print two lines

On the first line, print the result of pow(a, b). On the second line, print the result of pow(a,b,m).

__Input Format__

The first line contains $a$, the second line contains $b$, and the third line contains $m$.

__Constraints__

$1 \le a \le 10$

$1 \le b \le 10$

$2 \le m \le 1000$

__Sample Input__

```
3
4
5
```

__Sample Output__

```
81
1
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    a, b, m = int(input()), int(input()), int(input())

    print(a ** b)
    print(a ** b % m)
```
</details>
