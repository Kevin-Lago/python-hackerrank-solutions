| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/introduction/say_hello_world_with_python)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/introduction/arithmetic_operators)</img> |
|:---|:---:|---:|

# Python If-Else

__Task__

Given an integer, _n_, perform the following conditional actions:

- If _n_ is odd, print ```Weird```

- If _n_ is even and in the inclusive range of __2__ to __5__, print ```Weird```

- If _n_ is even and in the inclusive range of __6__ to __20__, print ```Weird```

- If _n_ is even and greater than __20__, print ```Not Weird```

__Input Format__

A single line containing a positive integer, _n_.

__Constraints__

- 1 <= _n_ <= 100

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

___n_ = 3__

___n___ is odd and odd numbers are weird, so print ```Weird```

__Sample Input 1__

```
24
```

__Sample Output 1__

```
Not Weird
```

__Explanation 1__

___n_ = 24__

___n_ > 20__ and ___n___ is even, so it is not weird.

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
