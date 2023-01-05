| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Day of the Programmer

Marie invented a [Time Machine]() and wants to test it by time-traveling to visit Russia on the [Day of the Programmer]() (The 256th day of the year) during a year in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the [Julian Calendar](); Since 1919 they used the [Gregorian Calendar]() System. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

- Divisible by 400

- Divisible by 4 and not divisible by 100

Given a year, $y$, find the date of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format ```dd.mm.yyyy```, where ```dd``` is the two-digit day, ```mm``` is the two-digit month and ```yyyy``` is $y$.

For example, the given $year$ = 1984. 1984 divisible by 4, so it is a leap year. The 256th day of a leap year after 1918 is September 12, so the answer is $12.09.1984$.

__Function Description__

Complete the day_of_programmer function in the editor below. It should return a string representing the dat of the 256th day of the given year.

day_of_programmer has the following parameter(s):

- year: an integer

__Input Format__

A single integer denoting year $y$.

__Constraints__

- $1700 \le y \le 2700$

__Output Format__

Print the full date of Day of the Programmer during year $y$ in the format ```dd.mm.yyyy```, where ```dd``` is the two-digit day, ```mm``` is the two-digit month and ```yyyy``` is $y$.

__Sample Input 0__

```
2017
```

__Sample Output 0__

```
13.09.2017
```

__Explanation 0__

In the year $y = 2017$, January has 31 days, February has 28 days, March has 31 days, April has 30 days, May has 31 days, June has 30 days, July has 31 days, and August has 31 days. When we sum the total number of days in the first eight months, we get 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 = 243. Day of the Programmer is the 256th day, so then calculate 256 - 243 = 13 to determine that it falls on day 13 of the 9th month (September). We then print the full date in the specified format, which is ```13.09.2017```.

__Sample Input 1__

```
2016
```

__Sample Output 1__

```
12.09.2016
```

__Explanation 1__

Year $y = 2016$ is a leap year, so February has 29 days but all the other months have the same number of days as in 2017. When we sum the total number of days in the first eight months, we get 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 = 244. Day of the Programmer is the 256th day, so then calculate 256 - 244 = 12 to determine that it falls on day 12 of the 9th month (September). We then print the full date in the specified format, which is ```12.09.2016```.

__Sample Input 2__

```
1800
```

__Sample Output 2__

```
12.09.1800
```

__Explanation 2__

Since 1800 is leap year as per Julian calendar. Day lies on 12 September.

---

<details><summary>Solution</summary>
    
```python

```
</details>
