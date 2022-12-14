| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Linear Algebra

The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.

__linalg.det__

The linalg.det tool computes the determinant of an array.

```python
print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0
```

__linalg.eig__

The linalg.eig computes the eigenvalues and right eigenvectors of a square array.

```python
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]
```

__linalg.inv__

The linalg.inv tool computes the (multiplicative) inverse of a matrix.

```python
print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]
```

Other routines can be found [here]()

---

__Task__

You are given a square matrix $a$ with dimensions $n x n$. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

__Input Format__

The first line contains the integer $n$.

The next $n$ lines contains the $n$ space separated elements of array $a$.

__Output Format__

Print the determinant of $a$.

__Sample Input__

```
2
1.1 1.1
1.1 1.1
```

__Sample Output__

```
0.0
```

---

<details><summary>Solution</summary>
    
```python
import numpy

if __name__ == '__main__':
    n = int(input())
    a = [list(map(float, input().split())) for i in range(n)]

    print(round(numpy.linalg.det(a), 2))
```
</details>
