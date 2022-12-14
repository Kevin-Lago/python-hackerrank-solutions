| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Concatenate

Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:

```python
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]
```

If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

```python
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]
```

---

__Task__

You are given two integer arrays of size $n x p$ and $m x p$ ($n$ and $m$ are rows, and $p$ is the column). Your task is to concatenate the arrays along axis $0$.

__Input Format__

The first line contains space separated integers $n$, $m$ and $p$.

The next $n$ lines contains the space separated elements of the $p$ columns.

After that, the next $m$ lines contains the space separated elements of the $p$ columns.

__Output Format__

Print the concatenated array of size $(n + m) x p$

__Sample Input__

```
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
```

__Sample Output__

```
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
```

---

<details><summary>Solution</summary>
    
```python

```
</details>
