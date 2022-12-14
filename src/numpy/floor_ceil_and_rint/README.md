| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Floor, Ceil and Rint

__floor__

The tool floor returns the floor of the input element-wise.

The floor of $x$ is the largest integer $i$ where $i \le x$

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
```

__ceil__

The tool ceil returns the ceiling of the input element-wise.

The ceiling of $x$ is the smallest integer $i$ where $i \le x$

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
```

__rint__

The rint tool rounds to the nearest integer of input element-wise.

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```

---

__Task__

You are given a 1-D array, $a$. Your task is to print the $floor$, $ciel$, and $rint$ of all the elements of $a$.

__Note__

In order to get the correct output format, add the line ```numpy.set_printoptions(legacy='1.13')``` below the numpy import.

__Input Format__

A single line of input containing the space separated elements of array $a$.

__Output Format__

On the first line, print the $floor$ of $a$.

On the second line, print the $ceil$ of $a$.

On the third line, print the $rint$ of $a$.

__Sample Input__

```
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
```

__Sample Output__

```
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```

---

<details><summary>Solution</summary>
    
```python

```
</details>
