| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# collections.namedtuple()

### [collections.namedtuple()](https://docs.python.org/2/library/collections.html#collections.namedtuple)

Basically, namedtuples are easy to create, lightweight object types.

They turn tuple into convenient containers for simple tasks.

With namedtuples, you don't have to use integer indices for accessing members of a tuple

__Example__

__Code 01__

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```

__Code 02__

```python
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
```

---

__Task__

Dr. John Wesley has a spreadsheet containing a list of student's ___IDs___, ___marks___, ___class___ and ___name___.

Your task is to help Dr. Wesley calculate the average marks of the students/

$Average = \frac{Sum of all marks}{Total Students}$

__Note:__

1. Columns can be in any order. ___IDs___, ___marks___, ___class___ and ___name___ can be written in any order in the spreadsheet.

2. Columns names are ```ID```, ```MARKS```, ```CLASS``` and ```NAME```. (The spelling and case type of these names won't change.)

__Input Format__

The first line contains an integer ___n___, the total number of students.

The second line contains the names of the columns in any order.

The next ___n___ lines contains the ___marks___, ___IDs___, ___name___ and ___class___, under their respective column names.

__Constraints__

$0 < n \le 100$

__Output Format__

Print the average marks of the list corrected to 2 decimal places.

__Sample Input__

__TestCase 01__

```
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
```

__TestCase 02__

```
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
```

__Sample Output__

__TestCase 01__

```
78.00
```

__TestCase 02__

```
81.00
```

__Explanation__

__TestCase 01__

$Average = (97 + 50 + 91 + 72 + 80)/5$

Can you solve this challenge in ```4 lines of code of less```?

__Note:__ There is no penalty for solutions that are correct but have more than 4 lines

---

<details><summary>Solution</summary>
    
```python
from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    Student = namedtuple("Student", list(input().split()))

    average = sum([int(Student(*input().split()).MARKS) for i in range(n)])
    print("%.2f" % (average / n))
```
</details>