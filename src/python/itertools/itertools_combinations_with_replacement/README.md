| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/itertools/itertools_combinations)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/itertools/compress_the_string)</img> |
|:---|:---:|---:|

# itertools.combinations_with_replacement()

[itertools.combinations_with_replacement(iterable, r)]()

This tool returns ___r___ length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

__Sample Code__

```python
>>> from itertools import combinations_with_replacement
>>> 
>>> print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,2))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
```

---

__Task__

You are given a string ___s___.

Your task is to print all possible size ___k___ replacement combinations of the string in lexicographic sorted order.

__Input Format__

A single line containing the string ___s___ and value ___k___ separated by a space.

__Constraints__

$0 < k \le len(s)$

The string contains only UPPERCASE characters.

__Output Format__

Print the combinations with their replacements of string ___s___ of separate lines.

__Sample Input__

```
HACK 2
```

__Sample Output__

```
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
```

---

<details><summary>Solution</summary>
    
```python

```
</details>