| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/say_hello_world_with_python)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/arithmetic_operators)</img> |
|:---|:---:|---:|

# Python If-Else

__Task__

Given an integer, $n$, perform the following conditional actions:

- If $n$ is odd, print ```Weird```

- If $n$ is even and in the inclusive range of $2$ to $5$, print ```Not Weird```

- If $n$ is even and in the inclusive range of $6$ to $20$, print ```Weird```

- If $n$ is even and greater than $20$, print ```Not Weird```

__Input Format__

A single line containing a positive integer, $n$.

__Constraints__

- $1 \le n \le 100$

__Output Format__

Print ```Weird``` if the number is weird. Otherwise, print ```Not Weird.```

__Sample Input 0__

```
3
```

__Sample Output 0__

```
Weird
```

__Explanation 0__

$n = 3$

$n$ is odd and odd numbers are weird, so print ```Weird```

__Sample Input 1__

```
24
```

__Sample Output 1__

```
Not Weird
```

__Explanation 1__

$n = 24$

$n > 20$ and $n$ is even, so it is not weird.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
```
</details>
