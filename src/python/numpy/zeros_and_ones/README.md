| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/concatenate)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/eye_and_identity)</img> |
|:---|:---:|---:|

# Zeros and Ones

[zeros]()

The zeros tool returns a new array with a given shape and type filled with $0$'s

```python
import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]
```

[ones]()

The ones tool returns a new array with a given shape and type filled with $1$'s.

---

__Task__

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools ```numpy.zero``` and ```numpy.ones```.

__Input Format__

A single ling containing the space-separated integer.

__Constraints__

$1 \le each integer \le 3$

__Output Format__

First, print the array using the ```numpy.zeros``` tool and then print the array with the ```numpy.ones``` tool.

__Sample Input 0__

```
3 3 3
```

__Sample Output 0__

```
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
```

__Explanation 0__

Print the array built using ```numpy.zeros``` and ```numpy.ones``` tools and you get the result as shown.

---

<details><summary>Solution</summary>
    
```python

```
</details>
