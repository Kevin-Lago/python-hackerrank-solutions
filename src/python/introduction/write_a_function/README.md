| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/loops)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/print_function)</img> |
|:---|:---:|---:|

# Write a Function

An extra day is added to the calendar almost every four years as Feburary 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

- The year can be evenly divided by 4, is a leap year, unless:

    - The year can be evenly divided by 100, it is NOT a leap year, unless:
    
        - The year is also evenly divisible by 400. Then it is a leap year.
        
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. [Source](https://www.timeanddate.com/date/leapyear.html)

__Task__

Given a year, determine whether it is a leap year. If it is a leap year. If it is a leap year, return the boolean ```True```, otherwise return ```False```.

Note that the code stub provided reads from STDIN and passes the arguments to the ```is_leap``` function. it is only necessary to complete the ```is_leap``` function.

__Input Format__

Read $year$, the year to test.

__Constraints__

- $1900 \le year \le 10^{5}$

__Output Format__

The function must return a Boolean value (True/False). Output is handled by the provided code stub.

__Sample Input__

```
1990
```

__Sample Output__

```
False
```

__Explanation__

1990 is not a multiple of 4 hence it's not a leap year

---

<details><summary>Solution</summary>
    
```python
def is_leap(year):
    leap = False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap
```
</details>
