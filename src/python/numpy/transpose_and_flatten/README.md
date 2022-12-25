| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/shape_and_reshape)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/concatenate)</img> |
|:---|:---:|---:|

# Transpose and Flatten

__Transpose__

We can generate the transposition of an array using the tool ```numpy.transpose```.

It will not affect the original array, but it will create a new array.

```python
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]
```

__Flatten__

The tool flatten creates a copy of the input array flattened to one dimension.

```python
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]
```

---

__Task__

You are given a $n x m$ integer array matric with space separated elements ($n$ = rows and $m$ = columns).

__Input Format__

The first line contains the space separated values of $n$ and $m$.

The next $n$ lines contains the space separated elements of $m$ columns.

__Output Format__

First, print the transpose array and then print the flatten.

__Sample Input__

```
2 2
1 2
3 4
```

__Sample Output__

```
[[1 3]
 [2 4]]
[1 2 3 4]
```

---

<details><summary>Solution</summary>
    
```python
import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    r = numpy.array([input().split() for i in range(n)], int)
    print(r.transpose())
    print(r.flatten())
```
</details>