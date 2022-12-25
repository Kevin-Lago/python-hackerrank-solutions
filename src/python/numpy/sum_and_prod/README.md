| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/floor_ceil_and_rint)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/numpy/min_and_max)</img> |
|:---|:---:|---:|

# Sum and Prod

__Sum__

The sum tool returns the sum of array elements over a given axis

```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis = 0))            #Output : [4 6]
print(numpy.sum(my_array, axis = 1))            #Output : [3 7]
print(numpy.sum(my_array, axis = None))         #Output : 10
print(numpy.sum(my_array))                      #Output : 10
```

By default, the axis value is ```None```. Therefore, it performs a sum over all the dimensions of the input array.

__Prod__

The prod tool returns the product of array elements over a give axis.

```python
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.prod(my_array, axis = 0))           #Output : [3 8]
print(numpy.prod(my_array, axis = 1))           #Output : [2 12]
print(numpy.prod(my_array, axis = None))        #Output : 24
print(numpy.prod(my_array))                     #Output : 24
```

By default, the axis value is ```None```. Therefore, it performs the product over all the dimensions of the input array.

___

__Task__

You are given a 2-D array with dimensions __N__ x __M__

Your task is to perform the _sum_ tool over axies __0__ and the nfind the _product_ of that result.

__Input Format__

The first line of input contains space separated values of _N_ and _M_.

The next _N_ lines contains _M_ space separated integers.

__Output Format__

Compute the sum along axis __0__. then, print the product of that sum

__Sample Input__

```
2 2
1 2
3 4
```

__Sample Output__

```
24
```

__Explanation__

The usm along axis __0__ = __[4, 6]__

The product of this sum = __24__

---

<details><summary>Solution</summary>
    
```python
import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [numpy.array(list(map(int, input().split()))) for i in range(n)]

    print(numpy.product(numpy.sum(a, 0)))
```
</details>
