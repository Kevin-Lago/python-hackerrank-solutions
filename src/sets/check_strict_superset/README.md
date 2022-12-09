| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/sets/check_subset)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/polar_coordinates)</img> |
|:---|:---:|---:|

# Check Strict Superset

You are given a set ___a___ and ___n___ other sets.

Your job is to find whether set ___a___ is a strict superset of each of the ___n___ sets/

Print ```True```, if ___a___ is a strict superset of each of the ___n___ sets. Otherwise, print ```False```.

A strict superset has at least one element that does not exist in its subset.

__Example__

Set__([1,3,4])__ is a strict superset of set__([1,3])__.

Set__([1,3,4])__ is not a strict superset of set__([1,3,4])__.

Set__([1,3,4])__ is not a strict superset of set__([1,3,5])__.

__Input Format__

The first line contains the space separated elements of set ___a___.

The second line contains integer ___n___, the number of other sets.

The next ___n___ lines contains the space separated elements of the other sets.

__Constraints__

- $0 < len(set(a)) < 501$

- $0 < n < 21$

- $0 < len(otherSets) < 101$

__Output Format__

Print ```True``` is set ___a___ is a strict superset of all other ___n___ sets. Otherwise, print ```False```.

__Sample Input__

```
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```

__Sample Output__

```
False
```

__Explanation__

Set ___a___ is the strict superset of the set__([1,2,3,4,5])__ but not of the set__([100,11,12])__ because __100__ is not in set ___a___.

Hence, the output is ```False```

---

<details><summary>Solution</summary>
    
```python

```
</details>