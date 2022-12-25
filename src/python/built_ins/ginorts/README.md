| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/built_ins/any_or_all)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/python_functional/map_and_lambda_function)</img> |
|:---|:---:|---:|

# ginortS

You are given a string $s$.

$s$ contains alphanumeric characters only.

![SortingGif](1.gif)

Your task is to sort the $s$ in the following manner:

- All sorted lowercase letters are ahead of uppercase letters.

- All sorted uppercase letters are ahead of digits.

- All sorted odd digits are ahead of sorted even digits.

__Input format__

A single line of input contains the string $s$.

__Constraints__

- $0 < len(s) < 1000$

__Output Format__

Output the sorted string $s$.

__Sample Input__

```
Sorting1234
```

__Sample Output__

```
ginortS1324
```

---

<details><summary>Solution</summary>
    
```python
import re

if __name__ == '__main__':
    s = input()

    lowercase = sorted("".join(c for c in re.findall(r"[a-z]", s)))
    uppercase = sorted("".join(c for c in re.findall(r"[A-Z]", s)))
    digits = sorted([c for c in re.findall(r"[0-9]", s)])
    digits = sorted([c for c in digits], key=lambda i: int(i) % 2 == 0)

    print("".join(lowercase + uppercase + digits))
```
</details>
