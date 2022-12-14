| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Min and Max

__min__

The tool min returns the minimum value along a given axis.

```python
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0
```

By default, the axis value is ```None```. Therefor, it finds the minimum over all the dimensions of the input array.

__max__

The tool max returns the maximum value along a given axis.

```python
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
```

By default, the axis value is ```None```. Therefor, it finds the maximum over all the dimensions of the input array.

---

__Task__

You are given a 2-D array with dimensions $n x m$.

Your task is to perform the min function over axis __1__ and then find the max of that.

__Input Format__

The first line of input contains the space separated values of $n$ and $m$.

The next $n$ lines contains $m$ space separated integers.

__Output Format__

Compute the min along axis $1$ and then print the max of that result.

__Sample Input__

```
4 2
2 5
3 7
1 3
4 0
```

__Sample Output__

```
3
```

__Explanation__

The min along axis $1 = [2,3,1,0]$

The max of $[2,3,1,0] = 3$

---

<details><summary>Solution</summary>
    
```python

```
</details>
