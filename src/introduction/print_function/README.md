| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/introduction/write_a_function)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/basic_data_types/list_comprehensions)</img> |
|:---|:---:|---:|

# Print Function

The included code stub will read an integer, ___n___, from STDIN.

Without using any string methods, try to print the following:

__123 ... _n___

Note that "..." represents the consecutive values in between.

__Example__

___n_ = 5__

Print the string __12345__.

__Input Format__

The first line contains an integer _n_.

__Constraints__

__1 <= _n_ <= 150__

__Output Format__

Print the list of integers from __1__ through ___n___ as a string, without spaces.

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
