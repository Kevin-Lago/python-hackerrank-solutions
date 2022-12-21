| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Iterables and Iterators

The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their [documentation here]().

You are given a list of ___n___ lowercase English letters. For a given integer ___k___, you can select any ___k___ indices (assume __1__ - based indexing) with a uniform probability from the list.

Find the probability that at least one of the ___k___ indices selected will contain the letter: '___a___'.

__Input Format__

The input consists of three lines. The first line contains the integer ___n___, denoting the length of the list. 

The next line consists of ___n___ space-separated lowercase English letters, denoting the elements of the list.

The first and the last line of input contains the integer ___k___, denoting the number of indices to be selected.

__Output Format__

Output a single line consisting of the probability that at least one of the ___k___ indices selected contains the letter: '___a___'.

__Note:__ The answer must be correct up to 3 decimal places.

__Constraints__

$1 \le n \le 10$

$1 \le k \le n$

All the letters in the list are lowercase English letters.

__Sample Input__

```
4
a a c d
2
```

__Sample Output__

```
0.8333
``` 

__Explanation__

All possible unordered tuples of length __2__ comprising of indices from __1__ to __4__ are:

__(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)__

Out of these __6__ combinations, __5__ of them contains either index __1__ or index __2__ which are the indices the contain the letter '___a___'.

Hence, the answer is $5 / 6$.

---

<details><summary>Solution</summary>
    
```python
from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    a = list(input().split())
    k = int(input())

    test = [''.join(c) for c in list(combinations(a, k))]
    print(round(sum(['a' in c for c in test]) / len(test), 3))
```
</details>