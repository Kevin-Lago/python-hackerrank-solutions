| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Time Conversion

Given a time in $12$-[hour AM/PM format], convert it to military (24-hour) time.

__Note:__ 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.

12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

__Example__

- $s = '12:01:00PM'$

    Return '12:01:00'.
    
- $s = '12:01:00AM'$

    Return '00:01:00'
    
__Function Description__

Complete the time_conversion function in the editor below. It should return a new string representing the input time in 24-hour format.

time_conversion has the following parameter(s):

- string s: a time in 12-hour format

__Returns__

- string: the time in 24-hour format

__Input Format__

A single string $s$ that represents a time in 12-hour clock format (i.e: $hh:mm:ssAM$ or $hh:mm:ssPM$).

__Constraints__

- All input times are valid

__Sample Input__

```
07:05:45PM
```

__Sample Output__

```
19:05:45
```

---

<details><summary>Solution</summary>
    
```python
from datetime import datetime


def time_conversion(s):
    return datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")


if __name__ == '__main__':
    s = input()
    print(time_conversion(s))
```
</details>
