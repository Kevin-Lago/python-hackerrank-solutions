| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/find_a_string)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/text_alignment)</img> |
|:---|:---:|---:|

# String Validators

Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, ect.

[str.isanum()](https://docs.python.org/2/library/stdtypes.html#str.isalnum)

This method checks if all the caracters of a string are alphanumeric (a-z, A-Z, and 0-9).

```python
print('ab123'.isalnum())
print('ab123#'.isalnum())
```

prints

```
True
False
```

---

[str.isalpha()]()

This method checks if all the characters of a string are alphabetical (a-z and A-Z).

```python
print('abcD'.isalpha())
print('abcd1'.isalpha())
```

prints

```
True
False
```

---

[str.isdigit()]()

This method checks if all the characters of a string are digits (0-9).

```python
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
```

---

[str.islower()]()

This method checks if all the characters of a string are lowercase characters (a-z).

```python
print('abcd123#'.islower())
print('Abcd123#'.islower())
```

prints

```
True
False
```

---

[str.isupper()]()

This method checks if all the characters of a string are uppercase characters (A-Z).

```python
print('ABCD123#'.isupper())
print('Abcd123#'.isupper())
```

prints

```
True
False
```

---

__Task__

You are given a string $s$.

Your task is to find out if the string $s$ contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

__Input Format__

A single line containing a string $s$.

__Constraints__

- $0 < len(s) < 1000$

__Output Format__

In the first line, print ```True``` if $s$ has any alphanumeric characters. Otherwise, print ```False```.

In the second line, print ```True``` if $s$ has any alphabetical characters. Otherwise, print ```False```.

In the third line, print ```True``` if $s$ has any digits. Otherwise, print ```False```.

In the fourth line, print ```True``` if $s$ has any lowercase characters. Otherwise, print ```False```.

In the fifth line, print ```True``` if $s$ has any uppercase characters. Otherwise, print ```False```.

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

---

<details><summary>Solution</summary>
    
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
</details>

<details><summary>Better Solution</summary>
    
```python
if __name__ == '__main__':
    s = input()
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))
```
</details>

<details><summary>Interesting Solution</summary>
    
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
</details>
