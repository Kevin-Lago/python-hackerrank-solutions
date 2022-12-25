| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/classes/classes_dealing_with_complex_numbers)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/built_ins/zipped)</img> |
|:---|:---:|---:|

# Class 2 - Find the Torsional Angle

You are given four points ___a, b, c___ and ___d___ in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points ___a, b, c___ and ___b, c, d___ in degrees(__not radian__). Let the angle be ___phi___.

___Cos(PHI) =___

__Input Format__

One line of input containing the space separated floating number values of the __x, y__ and __z__ coordinates of a point.

__Output Format__

Output the angle correct up to two decimal places.

__Sample Input__

```
0 4 5
1 7 6
0 5 9
1 7 2
```

__Sample Output__

```
8.19
```

---

<details><summary>Solution</summary>
    
```python
import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return __class__(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return __class__(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
```
</details>
