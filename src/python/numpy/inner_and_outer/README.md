| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/dot_and_cross)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/polynomials)</img> |
|:---|:---:|---:|

# Inner and Outer

__inner__

The inner tool returns the [inner product]() of two arrays.

```python
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4
```

__outer__

The outer tool returns the [outer product]() of two arrays.

```python
import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
```

---

__Task__

You are given two arrays: $a$ and $b$.

Your task is to compute their inner and outer product.

__Input Format__

The first line contains the space separated elements of array $a$.

The second line contains the space separated elements of array $b$.

__Output Format__

First, print the inner product.

Second, print the outer product.

__Sample Input__

```
0 1
2 3
```

__Sample Output__

```
3
[[0 0]
 [2 3]]
```

---

<details><summary>Solution</summary>
    
```python
import numpy

if __name__ == '__main__':
    a = numpy.array(list(map(int, input().split())))
    b = numpy.array(list(map(int, input().split())))
    
    print(numpy.inner(a, b))
    print(numpy.outer(a, b))
```
</details>
