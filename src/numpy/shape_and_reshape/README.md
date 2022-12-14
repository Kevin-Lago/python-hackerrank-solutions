| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Shape and Reshape

__shape__

The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

__(a). Using shape to get array dimensions__

```python
import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 1 row and 5 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 
```

__(b). Using shape to change array dimensions__

```python
import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
[[1 2]
[3 4]
[5 6]]
```

__Reshape__

The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.

```python
import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]
```

---

__Task__

You are given a space separated list of nine integers. Your task is to convert this list into a $3x3$ NumPy array.

__Input Format__

A single line of input containing __9__ space separated integers.

__Output Format__

Print the $3x3$ NumPy array.

__Sample Input__

```
1 2 3 4 5 6 7 8 9
```

__Sample Output__

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

---

<details><summary>Solution</summary>
    
```python
import numpy

if __name__ == '__main__':
    a = numpy.array(input().split(), int)
    print(a.reshape((3,3)))
```
</details>