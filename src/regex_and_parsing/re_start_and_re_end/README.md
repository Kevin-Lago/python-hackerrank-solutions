| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Re.start() & Re.end()

[start() & end()]()

These expressions return the indices of the start and end of the substring matched by the group.

```python
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
```

---

__Task__

You are given a string $s$.

Your task is to find the indices of the start and end of string $k$ and $s$.

__Input Format__

The first line contains the string $s$.

The second line contains the string $k$.

__Constraints__

$0 < len(s) < 100$

$0 < len(k) < len(s)$

__Output Format__

Print the tuple in this format: (start _index, end _index).

If no match is found, print ```(-1, -1)```.

__Sample Input__

```
aaadaa
aa
```

__Sample Output__

```
(0, 1)
(1, 2)
(4, 5)
```

---

<details><summary>Solution</summary>
    
```python

```
</details>
