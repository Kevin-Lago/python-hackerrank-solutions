| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/string_formatting)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/capitalize)</img> |
|:---|:---:|---:|

# Alphabet Rangoli

You are given an integer, $n$. Your task is to print an alphabet rangoli of size $n$. (Rangoli is a form of indian folk art based on creating of patterns.)

Different sizes of alphabet rangoli are shown below:

```
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
```

The center of the rangoli has the first alphabet letter a, and the boundary has the $n^{th}$ alphabet letter (in alphabetical order).

__Function description__

Complete the rangoli function in the editor below.

rangoli has the following parameters:

- int size: the size of the rangoli

__Returns__

- string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

__Input Format__

Only one line of input containing $n$, the size of the rangoli.

__Constraints__

- $0 < n < 27$

__Sample Input__

```
5
```

__Sample Output__

```
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

---

<details><summary>Solution</summary>
    
```python
def print_rangoli(size):
    for n in [abs(r) for r in range(-(size - 1), size)]:
        center = '-'.join([chr(ord('a') + abs(i) + n) for i in range(-(size - n - 1), (size - n))])
        print(2 * n * '-' + center + 2 * n * '-')
```

or

```python
def print_rangoli(size):
    [print(2 * n * '-' + '-'.join([chr(ord('a') + abs(i) + n) for i in range(-(size - n - 1), (size - n))]) + 2 * n * '-') for n in [abs(r) for r in range(-(size - 1), size)]]
```

or

```python
def print_rangoli(size):
    [[
        print(2 * n * '-', end=""), 
        print('-'.join([chr(ord('a') + abs(i) + n) for i in range(-(size - n - 1), (size - n))]), end=""),
        print(2 * n * '-')
    ] for n in [abs(r) for r in range(-(size - 1), size)]]
```
</details>
