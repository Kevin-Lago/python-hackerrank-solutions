| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/regex_substitution)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/validating_phone_numbers)</img> |
|:---|:---:|---:|

# Validating Roman Numerals

You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print ```True```.

Otherwise, print ```False```. Try o create a regular expression for a valid Roman numeral.

__Input Format__

A single line of input containing a string of Roman characters.

__Output Format__

Output a single line containing ```True``` or ```False``` according to the instructions above.

__Constraints__

The number will be between $1$ and $3999$ (both included).

__Sample Input__

```
CDXXI
```

__Sample Output__

```
True
```

__References__

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is [available here](). You could also go through the link below to read more about regular expression in Python.

[https://developers.google.com/edu/python/regular-expressions](https://developers.google.com/edu/python/regular-expressions)

---

<details><summary>Solution</summary>
    
```python
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
```
</details>
