| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/basic_data_types/lists)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/strings/swap_case)</img> |
|:---|:---:|---:|

# Tuples

__Task__

Given an integer, ___n___, and ___n___ space-separated integers as input, create a tuple, ___t___, of those ___n___ integers. Then compute and print the result of ___hash(t)___.

__Note:__ [hash()](https://docs.python.org/3/library/functions.html#hash) is on of the function in the ```__builtins__``` module, so it need not be imported.

__Input Format__

The first line contains an integer, ___n___, denoting the number of elements in the tuple.

The second line contains ___n___ space-separated integers describing the elements in tuple ___t___.

__Output Format__

Print the result of ___hash(t)___

__Sample Input 0__

```
2
1 2
```

__Sample Output 0__

```
3713081631934410656
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    t = tuple(input().split())

    print(hash(t))
```
</details>
