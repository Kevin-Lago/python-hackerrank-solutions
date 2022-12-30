| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Staircase

Staircase detail

This is a staircase of size $n = 4$:

```
   #
  ##
 ###
####
```

Its base and height are both equal to $n$. It is drawn using ```#``` symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size $n$.

__Function Description__

Complete the staircase function in the editor below.

staircase has the following parameter(s):

- int n: an integer

__Print__

Print a staircase as described above.

__Input Format__

A single integer, $n$, denoting the size of the staircase.

__Constraints__

- $0 < n \le 100$

__Output Format__

Print a staircase of size $n$ using ```#``` symbols and spaces.

__Note:__ The last line must have $0$ spaces in it.

__Sample Input__

```
6
```

__Sample Output__

```
     #
    ##
   ###
  ####
 #####
######
```

__Explanation__

The staircase is right-aligned, composed of ```#``` symbols and spaces, and has a height and width of $n = 6$.

---

<details><summary>Solution</summary>
    
```python
def staircase(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)


if __name__ == '__main__':
    n = int(input())
    staircase(n)
```

or

```python
def staircase(n):
    [print(" " * (n - i) + "#" * i) for i in range(1, n + 1)]


if __name__ == '__main__':
    n = int(input())
    staircase(n)
```
</details>
