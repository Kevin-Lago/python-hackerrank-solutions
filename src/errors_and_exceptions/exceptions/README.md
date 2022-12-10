| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/date_and_time/time_delta)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/errors_and_exceptions/incorrect_regex)</img> |
|:---|:---:|---:|

# Exceptions

### [Exceptions](https://docs.python.org/2/tutorial/errors.html#exceptions)

Errors detected during executing are called exceptions.

__Examples:__

__ZeroDivisionError__

This error is raised when the second argument of a division or modulo operation is zero.

```python
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
```

__ValueError__

This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

```python
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
```

To learn more about difference built-in exceptions [click here](https://docs.python.org/2/library/exceptions.html#module-exceptions).

### [Handling Exceptions](https://docs.python.org/2/tutorial/errors.html#handling-exceptions)

The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.

```python
#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
```

__Output__

Error Code: integer division or module by zero

---

__Task__

You are given two values ___a___ and ___b___.

Perform integer division and print ___a___/___b___.

__Input Format__

The first line contains ___t___, the number of test cases.

The next ___t___ lines each contains the space separated values of ___a___ and ___b___.

__Constraints__

- $0 < t < 10$

__Output Format__

Print the values of ___a___/___b___.

In the case of a ZeroDivisionError or ValueError, print the error code.

__Sample Input__

```
3
1 0
2 $
3 1
```

__Sample Output__

```
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
```

__Note:__

For integer division in __Python3__ user ```//```.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        except ValueError as e:
            print(f"Error Code: {e}")
```
</details>