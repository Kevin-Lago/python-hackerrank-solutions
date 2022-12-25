| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/built_ins/input)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/built_ins/athlete_sort)</img> |
|:---|:---:|---:|

# Python Evaluation

The ```eval()``` expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.

For example:

```
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
```

Here, ```eval()``` can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.

For example:

```python
>>> type(eval("len"))
<type 'builtin_function_or_method'>
```

Without eval()

```python
>>> type("len")
<type 'str'>
```

---

__Task__

You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).

__Note:__ Python 2 users, please import from ```__future__ import print_function```

__Constraint__

Input string is less than 1000 characters.

__Sample Input__

```python
print(2 + 3)
```

__Sample Output__

```
5
```

---

<details><summary>Solution</summary>
    
```python

```
</details>
