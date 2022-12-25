| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/math/find_angle_mbc)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/math/mod_divmod)</img> |
|:---|:---:|---:|

# Triangle Quest 2

You are given a positive integer $n$.

Your task is to print a palindromic triangle of size $n$.

For example, a palindromic triangle of size $5$ is:

```
1
121
12321
1234321
123454321
```

You can't take more than two lines. The first line (a for-statement) is already written for you.

You have to complete the code using exactly one print statement.

__Note:__

Using anything related to strings will give a score of $0$.

Using more than one for-statement will give a score of $0$.

__Input Format__

A single line of input containing the integer $n$.

__Constraints__

$0 < n < 10$

__Output Format__

Print the palindromic triangle og size $n$ as explained above.

__Sample Input__

```
5
```

__Sample Output__

```
1
121
12321
1234321
123454321
```

---

<details><summary>Solution</summary>
   
```python
for i in range(1, int(input()) + 1):
    print((10 ** i // 9) ** 2)
```

or
 
```python
[print((10 ** i // 9) ** 2) for i in range(1, int(input()) + 1)]
```
</details>
