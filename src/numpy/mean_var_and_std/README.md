| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Mean, Var, and Std

__mean__

The mean tool computes the arithmetic mean along the specified axis.

```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5
```

By default, the axis is ```None```. Therefore, it compute the mean of the flattened array.

__var__

The var tool computes the arithmetic variance along the specified axis.

```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25
```

By default, the axis is ```None```. Therefore, it computes the variance of the flattened array.

__std__

The std tool computes the arithmetic standard deviation along the specified axis.

```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
```

By default, the axis is ```None```. Therefore, it computes the standard deviation of the flattened array.

---

__Task__

You are given a 2-D array of size $n x m$

Your task is to find:

1. The mean along axis $1$

2. The var along axis $0$

3. The std along axis $None$

__Input Format__

The first line contains the space separated values of $n$ and $m$.

The next $n$ lines contains $m$ space separated integers.

__Output Format__

First, print the mean.

Second, print the var.

Third, print the std.

__Sample Input__

```
2 2
1 2
3 4
```

__Sample Output__

```
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
```

---

<details><summary>Solution</summary>
    
```python

```
</details>
