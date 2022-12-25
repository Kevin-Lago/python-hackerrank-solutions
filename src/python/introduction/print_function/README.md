| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/write_a_function)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/list_comprehensions)</img> |
|:---|:---:|---:|

# Print Function

The included code stub will read an integer, $n$, from STDIN.

Without using any string methods, try to print the following:

$123...n$

Note that "..." represents the consecutive values in between.

__Example__

$n = 5$

Print the string $12345$.

__Input Format__

The first line contains an integer $n$.

__Constraints__

- $1 \le n \le 150$

__Output Format__

Print the list of integers from $1$ through $n$ as a string, without spaces.

__Sample Input 0__

```
3
```

__Sample Output 0__

```
123
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i + 1, end="")
```
</details>
