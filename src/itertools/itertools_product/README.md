| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# itertools.product()

[itertools.product()]()

This tool computes the [cartesian product]() of input iterables.

It is equivalent to nested for-loops.

For example, ```product(a, b)``` returns the same as ```((a, b) for x in a for y in b)```

__Sample Code__

```python
>>> from itertools import product
>>>
>>> print list(product([1,2,3],repeat = 2))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>>
>>> print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
>>>
>>> A = [[1,2,3],[3,4,5]]
>>> print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
>>>
>>> B = [[1,2,3],[3,4,5],[7,8]]
>>> print list(product(*B))
[(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
```

---

__Task__

You are given two lists ___a___ and ___b___. Your task is to compute their cartesian product $a x b$

__Eample__

```python
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
```

__Note:__ ___a___ and ___b___ are sorted lists, and the cartesian product's tuples should be output in sorted order.

__Input Format__

The first line contains the space separated elements of list ___a___.

The second line contains the space separated elements of list ___b___.

Both lists have no duplicate integer elements.

__Constraints__

$0 < a < 30$

$0 < b < 30$

__Sample Input__

```
1 2
3 4
```

__Sample Output__

```
(1, 3) (1, 4) (2, 3) (2, 4)
```

---

<details><summary>Solution</summary>
    
```python
import itertools

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    [print(t, end=" ") for t in list(itertools.product(a, b))]
```
</details>