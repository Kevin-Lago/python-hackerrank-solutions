| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/itertools/itertools_permutations)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/itertools/itertools_combinations_with_replacement)</img> |
|:---|:---:|---:|

# itertools.combinations()

[itertools.combinations(iterable, r)]()

This tool returns the ___r___ length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

__Sample Code__

```python
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
```

---

__Task__

You are given a string ___s___

Your task is to print all possible combinations, up to size ___k___, of the string in lexicographic sorted order.

__Constraints__

$0 < k < len(s)$

The string contains only UPPERCASE characters.

__Output Format__

Print the different combinations of string ___s___ on separate lines.

__Sample Input__

```
HACK 2
```

__Sample Output__

```
A
C
H
K
AC
AH
AK
CH
CK
HK
```

---

<details><summary>Solution</summary>
    
```python
import itertools

if __name__ == '__main__':
    s, k = input().split(" ")

    for i in range(1, int(k) + 1):
        [print(t) for t in sorted(list(["".join(sorted(c)) for c in itertools.combinations(s, i)]))]
```
</details>