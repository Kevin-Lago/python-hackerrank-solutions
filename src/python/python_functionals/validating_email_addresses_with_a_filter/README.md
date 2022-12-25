| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/python_functionals/map_and_lambda_function)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/python_functionals/reduce_function)</img> |
|:---|:---:|---:|

# Validating Email Addresses With a Filter

You are given an integer $n$ followed by $n$ email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must following these rules:

- It must have the username@websitename.extension format type.

- The username can only contain letters, digits, dashes and underscores $[a-z], [A-Z], [0-9],[_-]$.

- The website name can only have letters and digits $[a-z], [A-Z], [0-9]$.

- The extension can only contain letters $[a-z], [A-Z]$.

- The maximum length of the extension is 3.

__Concept__

A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters.

Let's say you have to make a list of the squares of integers from $0$ to $9$ (both included).

```python
>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
```

Now, you only require those elements that are greater than $10$ but less than $80$.

```python
>> l = list(filter(lambda x: x > 10 and x < 80, l))
```

Easy, isn't it?

__Example__

Complete the function fun in the editor below.

fun has the following parameters:

- string s: the string to test

__Returns__

- boolean: whether the string is a valid email or not

__Input Format__

The first line of input is the integer $n$, the number of email addresses.

$n$ lines follow, each containing a string.

__Constraints__

Each line is a non-empty string.

__Sample Input__

```
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
```

__Sample Output__

```
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
```

---

<details><summary>Solution</summary>
    
```python
import re


def fun(s):
    if re.search("^[a-zA-Z0-9_\\-]+@[a-zA-Z0-9]+\\.[a-zA-Z]{0,3}$", s):
        return True
    return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
```
</details>
