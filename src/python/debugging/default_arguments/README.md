| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/debugging/words_score)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> |
|:---|:---:|

# Default Arguments

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

---

Python supports a useful concept of default argument values. For each keywords argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it.

For example, consider the following increment function:

```python
def increment_by(n, increment=1):
    return n + increment
```

The function works like this:

```python
>>> increment_by(5, 2)
7
>>> increment_by(4)
5
```

Debug the given function ```print_from_stream``` using the default value of one of its arguments.

The function has teh following signature:

```python
def print_from_stream(n, stream):
```

This function should print the first ___n___ values returns by ```get_next()``` method of ```stream``` object provided as an argument. Each of these values should be printed in a separate line.

Whenever the function is called without the ```stream``` argument, it should use an instance of ```EvenStream``` class defined in the code stubs below as the value of ```stream```.

Your function will be tested on several cases by the locked template code.

__Input Format__

The input is read by the provided locked code template. in the first line, there is a single integer ___q___ denoting the number of queries. Each of the following ___q___ lines contains a ```stream_name``` following by integer ___n___, and it corresponds to a single test for your function.

__Constraints__

- $1 \le q \le 100$

- $1 \le n \le 10$

__Output Format__

The output is produced by the provided and locked code template. For each of the queries (```stream_name```, ```n```), if the ```stream_name``` is even then ```print_from_stream(n)``` is called. Otherwise, if the ```stream_name``` is odd, then ```print_from_stream(n, OddStream())``` is called.

__Sample Input__

```
3
odd 2
even 3
odd 5
```

__Sample Output__

```
1
3
0
2
4
1
3
5
7
9
```

__Explanation__

There are __3__ queries in the sample.

In the first query, the function ```print_from_stream(2, OddStream())``` is executed, which leads to printing values __1__ and __3__ in separated lines as the first two non-negative odd numbers.

In the second query, the function ```print_from_stream(3)``` is executed, which leads to printing values __2, 4__ and __6__ in separated lines as the first three non-negative even numbers.

In the third query, the function ```print_from__stream(5, OddStream())``` is executed, which leads to printing values __1,3,5,7__ and __9__ in separated lines as the first five non-negative odd numbers.

---

<details><summary>Solution</summary>
    
```python
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=None):
    if stream == None:
        stream = EvenStream()

    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
```
</details>