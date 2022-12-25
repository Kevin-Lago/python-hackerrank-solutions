| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/zeros_and_ones)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/array_mathematics)</img> |
|:---|:---:|---:|

# Eye and Identity

__identity__

The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as $1$ and the rest as $0$. The default type of elements is float.

```python
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```

__eye__

The eye tool returns a 2-D array with $1$'s as the diagonal and $0$'s elsewhere. The diagonal can be main, upper or lower depending on the optional parameter $k$. A positive $k$ is for the upper diagonal, a negative $k$ is for the lower, and a $0$ $k$ (default) is for the main diagonal.

```python
import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
```

---

__Task__

Your task is to print an array of size $n x m$ with its main diagonal elements as $1$'s and $0$'s everywhere else.

__Note__

In order to get alignment correct, please insert the line ```nump.set_printoptions(legacy='1.13')``` below the numpy import.

__Input Format__

A single line containing the space separated values of $n$ and $m$.

$n$ denotes the rows.

$m$ denots the columns.

__Output Format__

Print the desired $n x m$ array.

__Sample Input__

```
3 3
```

__Sample Output__

```
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```

---

<details><summary>Solution</summary>
    
```python

```
</details>
