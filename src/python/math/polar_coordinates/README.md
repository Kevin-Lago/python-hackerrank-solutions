| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/check_strict_superset)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/math/find_angle_mbc)</img> |
|:---|:---:|---:|

# Polar Coordinates

__Polar coordinates__ are an alternative way of representing Cartesian coordinates or [Complex Numbers](https://en.wikipedia.org/wiki/Complex_number).

A complex number $z$

$z = x + yj$

Is completely determined by its real part $x$ and imaginary part $y$.

Here, $j$ is the [imaginary unit]().

A polar coordinate ($r, \varphi$)

![HackerrankPolarAxis](1.png)

is completely determined by modulus $r$ and phase angle $\varphi$.

If we convert complex number $z$ to its polar coordinate, we find:

$r$: Distance from $z$ to origin, i.e. $\sqrt{x^2 + y^2}$

$\varphi$: Counter clockwise angle measured from the positive $x$-axis to the line segment that joins $z$ to the origin.

Python's [cmath]() module provides access to the mathematical functions for complex numbers.

__cmath.phase__

This tool returns the phase of complex number $z$ (also known as the argument of $z$).

```python
>>> phase(complex(-1.0, 0.0))
3.1415926535897931
```

__abs__

This tool returns the modulus (absolute value) of complex number $z$.

```python
>>> abs(complex(-1.0, 0.0))
1.0
```

__Task__

You are given a complex $z$. Your task is to convert it to polar coordinates.

__Input Format__

A single line containing the complex number $z$. Note: complex() function can be used in python to convert the input as a complex number.

__Constraints__

Given number is a valid complex number

__Output Format__

Output two lines:

The first line should contain the value of $r$.

The second line should contain the value of $\varphi$.

__Sample Input__

```
1+2j
```

__Sample Output__

```
2.23606797749979 
1.1071487177940904
```

__Note:__ The output should be correct up to 3 decimal places.

---

<details><summary>Solution</summary>
    
```python
from math import sqrt, atan2
import re

if __name__ == '__main__':
    z = input()
    x = int(re.match(r"^-?\d+", z).group())
    y = int(re.split(r"^-?\d+", z)[1][:-1])

    print(sqrt(x**2 + y**2))
    print(atan2(y, x))
```
</details>