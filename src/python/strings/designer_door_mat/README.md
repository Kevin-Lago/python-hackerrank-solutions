| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/text_wrap)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/string_formatting)</img> |
|:---|:---:|---:|

# Designer Door Mat

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

- Mat size must be ___n * m___. (___n___ is an odd natural number, and ___m___ is __3__ times ___n___)

- The design should have 'WELCOME' written in the center.

- The design pattern should only user ```|```, ```.``` and ```-``` characters.

__Sample Designs__

```
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
```

__Input Format__

A single line containing the space separated values of ___n___ and ___m___.

__Constraints__

- __5 < _n_ < 101__

- __15 < _m_ < 303__

__Output Format__

Output the design pattern.

__Sample Input__

```
9 27
```

__Sample Output__

```
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n, m = map(int, input().split())
    ch = int((m - 3) / 2)
    rh = int((n - 1) / 2)

    [print("-" * (ch - (3 * r)) + ".|." * (2 * (r + 1) - 1) + "-" * (ch - (3 * r))) for r in range(rh)]
    print("-" * int((m - 7) / 2) + "WELCOME" + "-" * int((m - 7) / 2))
    [print(
        "-" * (ch - (3 * (rh - r - 1))) + ".|." * (2 * (rh - r) - 1) + "-" * (ch - (3 * (rh - r - 1)))
    ) for r in range(rh)]
```
</details>
