| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/tuples)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/string_split_and_join)</img> |
|:---|:---:|---:|

# sWAP cASE

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice verse.

__For Example:__

```
Www.HackerRank.com -> wWW.hACKERrANK.COM
Pythonist 2 -> pYTHONIST 2
```

__Function Description__

Complete the swap_case function in the editor below.

swap_case has the following parameters:

- string s: the string to modify

__Returns__

- string: the modified string.

__Input Format__

A single line containing a string $s$

__Constraints__

- 0 < len(s) \le 1000$

__Sample Input__

```
HackerRank.com presents "Pythonist 2".
```

__Sample Output__

```
hACKERrANK.COM PRESENTS "pYTHONIST 2".
```

---

<details><summary>Solution</summary>
    
```python
def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```
</details>
