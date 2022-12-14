| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Polynomials

__poly__

The poly tool returns the coefficients of a polynomial with the given sequence of roots.

```python
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]
```

__roots__

The roots tool returns the roots of a polynomial with the given coefficients.

```python
print numpy.roots([1, 0, -1])           #Output : [-1.  1.]
```

__polyint__

The polyint tool returns an antiderivative (infinite integral) of a polynomial.

```python
print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]
```

__polyder__

The polyder tool returns the derivative of the specified order of a polynomial.

```python
print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]
```

__polyval__

The polyval tool evaluates the polynomial at specific value.

```python
print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34
```

__polyfit__

The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.

```python
print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
```

The function [polyadd](), [polysub](), [polymul]() and [polydiv]() also handle proper addition, subtraction, multiplications and division of polynomial coefficients, respectively.

---

__Task__

You are given the coefficients of a polynomial $p$.

Your task is to find the value of $p$ at point $x$.

__Input Format__

The first line contains the space separated value of the coefficients in $p$.

The second line contains the value of $x$.

__Output Format__

Print the desired value.

__Sample Input__

```
1.1 2 3
0
```

__Sample Output__

```
3.0
```

---

<details><summary>Solution</summary>
    
```python

```
</details>
