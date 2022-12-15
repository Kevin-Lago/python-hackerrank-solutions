| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/numpy/eye_and_identity)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/numpy/floor_ceil_and_rint)</img> |
|:---|:---:|---:|

# Array Mathematics

Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.

```python
import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
```

---

__Task__

You are given two integer arrays, $a$ and $b$ of dimensions $n x m$.

Your task is to perform the following operations:

1. Add ($a + b$)

2. Subtract ($a - b$)

3. Multiply ($a * b$)

4. Integer Division ($a / b$)

5. Mod ($a % b$)

6. Power ($a ** b$)

__Note__

The method ```numpy.floor_divide()``` works like ```numpy.divide()``` except it performs a floor division.

__Input Format__

The first line contains two space separated integers, $n$ and $m$.

The next $n$ lines contains $m$ space separated integers of array $a$.

The following $n$ lines contains $m$ space separated integers of array $b$.

__Output Format__

Print the result of each operation in the given order under __Task__.

__Sample Input__

```
1 4
1 2 3 4
5 6 7 8
```

__Sample Output__

```
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
```

Use ```//``` for division in Python 3.

---

<details><summary>Solution</summary>
    
```python
import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = numpy.array([numpy.array(input().split(), int) for i in range(n)])
    b = numpy.array([numpy.array(input().split(), int) for i in range(n)])

    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.floor_divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))
```
</details>
