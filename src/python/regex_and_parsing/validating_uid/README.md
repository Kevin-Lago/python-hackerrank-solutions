| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/detect_html_tags_attributes_and_attribute_values)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/validating_credit_card_numbers)</img> |
|:---|:---:|---:|

# Validating UID

ABCXYZ company has up to $100$ employees.

The company decides to create a unique identification number (UID) for each of its employees.

The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

- It must contain at least $2$ uppercase English alphabetic characters.

- It must contain at least $3$ digits ($0-9$)

- It should only contain alphanumeric characters ($a-z, A-Z$ & $0-9$)

- No character should repeat.

- There must be exactly $10$ characters in a valid UID.

__Input Format__

The first line contains an integer $t$, the number of test cases.

The next $t$ lines contains an employee's UID.

__Output Format__

For each test case, print ```Valid``` if the UID is valid. Otherwise, print ```Invalid```, on separate lines.

__Sample Input__

```
2
B1CD102354
B1CDEF2354
```

__Sample Output__

```
Invalid
Valid
```

__Explanation__

__B1CD102354__: $1$ is repeating -> Invalid

__B1CFEF2354__: Valid

---

<details><summary>Solution</summary>
    
```python
import re

if __name__ == '__main__':
    t = int(input())
    uids = [input() for i in range(t)]

    for uid in uids:
        if re.match(r"[a-zA-Z0-9]{10}", uid) \
                and len(set(uid)) == 10 \
                and len(re.findall("[A-Z]", uid)) >= 2 \
                and len(re.findall("[0-9]", uid)) >= 3:
            print("Valid")
            continue

        print("Invalid")
```
</details>
