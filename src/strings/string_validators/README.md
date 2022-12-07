# String Validators

Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, ect.

[str.isanum()](https://docs.python.org/2/library/stdtypes.html#str.isalnum)

This method checks if all the caracters of a string are alphanumeric (a-z, A-Z, and 0-9).

```python

```
---

[str.isalpha()]()

This method checks if all the characters of a string are alphabetical (a-z and A-Z).

```python

```
---

[str.isdigit()]()

This method checks if all the characters of a string are digits (0-9).

```python

```
---

[str.islower()]()

This method checks if all the characters of a string are lowercase characters (a-z).

```python

```
---

[str.isupper()]()

This method checks if all the characters of a string are uppercase characters (A-Z).

```python

```
---

__Task__

You are given a string ___s___.

Your task is to find out if the string ___s___ contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

__Input Format__

A single line containing a string ___s___.

__Constraints__

__0 <= _len(s)_ <= 1000__

__Output Format__

In the first line, print ```True``` if ___s___ has any alphanumeric characters. Otherwise, print ```False```.

In the second line, print ```True``` if ___s___ has any alphabetical characters. Otherwise, print ```False```.

In the third line, print ```True``` if ___s___ has any digits. Otherwise, print ```False```.

In the fourth line, print ```True``` if ___s___ has any lowercase characters. Otherwise, print ```False```.

In the fifth line, print ```True``` if ___s___ has any uppercase characters. Otherwise, print ```False```.

__Sample Input__

```
qA2
```

__Sample Output__

```
True
True
True
True
True
```

__Solution__

```python
if __name__ == '__main__':
    s = input()
    hasalnum = False
    hasalpha = False
    hasdigit = False
    haslower = False
    hasupper = False

    for i in range(len(s)):
        if (hasalnum and hasalpha and hasdigit and haslower and hasupper):
            break
        if (s[i:i + 1].isalnum()):
            hasalnum = True
        if (s[i:i + 1].isalpha()):
            hasalpha = True
        if (s[i:i + 1].isdigit()):
            hasdigit = True
        if (s[i:i + 1].islower()):
            haslower = True
        if (s[i:i + 1].isupper()):
            hasupper = True

    print(hasalnum)
    print(hasalpha)
    print(hasdigit)
    print(haslower)
    print(hasupper)
```

__Better Solution__

```python
if __name__ == '__main__':
    s = input()
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))
```

__Interesting Solution__

```python
def check(s, func_list):
        res = []
        for f in func_list:
                res.append(any([getattr(str(l),f)() for l in s]))
        return res


if __name__ == '__main__':
    s = input()
    res = check(s, ["isalnum", "isalpha", "isdigit", "islower", "isupper"])
    for r in res:
            print(r)
```
