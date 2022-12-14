| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Arrays

The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.

To use the NumPy module, we need to import it using:

```python
import numpy
```

__Arrays__

A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.

```python
import numpy

a = numpy.array([1,2,3,4,5])
print a[1]          #2

b = numpy.array([1,2,3,4,5],float)
print b[1]          #2.0
```

In the above example, ```numpy.array()``` is used to convert a list into a NumPy array. The second argument (float) can be used to set the type of array elements.

---

__Task__

You are given a space separated list of numbers.

Your task it to print a reversed NumPy array with the element type ```float```.

__Input Format__

A single line of input containing space separated numbers.

__Output Format__

Print the reverse NumPy array with type float.

__Sample Input__

```
1 2 3 4 -8 -10
```

__Sample Output__

```
[-10.  -8.   4.   3.   2.   1.]
```

---

<details><summary>Solution</summary>
    
```python

```
</details>