| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Classes: Dealing with Complex Numbers

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

__Input Format__

One line of input: The real and imaginary part of a number separated by a space.

__Output Format__

For two complex numbers ___c___ and ___d___, the output should be in the following sequence on separated lines:

- ___c + d___

- ___c - d___

- ___c * d___

- ___c / d___

- ___mod(c)___

- ___mod(d)___

For complex numbers with non-zero real(___a___) and complex part(___b___), the output should be in the following format:

___a + b<sub>i</sub>___

Replace the plus symbol (+) with a minus symbol (-) when ___b < 0___

For complex number with a zero complex part i.e. real numbers, the output should be:

___a + 0.00i___

For complex numbers where the real part is zero and the complex part(___b___) is non-zero, the output should be:

___0.00 + bi___

__Sample Input__

```
2 1
5 6
```

__Sample Output__

```
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
```

__Concept__

Python is a fully object-oriented language like C++, Java, ect. For reading about classes, refer [here](https://diveintopython3.net/iterators.html#defining-classes).

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

```
__add__-> Can be overloaded for + operation
```

```
__sub__ -> Can be overloaded for - operation
```

```
__mul__ -> Can be overloaded for * operation
```

For more information on operator overloading in Python, refer [here](https://docs.python.org/3.2/reference/datamodel.html).

---

<details><summary>Solution</summary>
    
```python
import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return __class__(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return __class__(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        prod = complex(self.real, self.imaginary) * complex(no.real, no.imaginary)
        return __class__(prod.real, prod.imag)

    def __truediv__(self, no):
        prod = complex(self.real, self.imaginary) / complex(no.real, no.imaginary)
        return __class__(prod.real, prod.imag)

    def mod(self):
        m = math.sqrt(self.real**2 + self.imaginary**2)
        return __class__(m, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
```
</details>
