| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/the_captains_room)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/check_strict_superset)</img> |
|:---|:---:|---:|

# Check Subset

You are given two sets, ___a___ and ___b___.

Your job is to find whether set ___a___ is a subset of set ___b___.

If set ___a___ is a subset of set ___b___, print ```True```.

If set ___a___ is not a subset of set ___b___, print ```False```.

__Input Format__

The first line will contain the number of test cases, ___t___.

The first line of each test case contains the number of elements in set ___a___.

The second line of each test case contains the space separated elements of set ___a___.

The third line of each test case contains the number of elements in set ___b___.

The fourth line of each test case contains the space separated elements of set ___b___.

__Constraints__

- $0 < t < 21$

- $0 < Number of elements in each set < 1001$

__Output Format__

Output ```True``` or ```False``` for each test case on separate lines.

__Sample Input__

```
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
```

__Sample Output__

```
True 
False
False
```

__Explanation__

__Test Case 01 Explanation__

Set ___a___ = {1 2 3 5 6}

Set ___b___ = {9 8 5 6 3 2 4 7}

All the elements of set ___a___ are elements of set ___b___.

Hence, set ___a___ is a subset of set ___b___.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        a = set(map(int, input().split()))

        m = int(input())
        b = set(map(int, input().split()))

        print(a.issubset(b))
```
</details>