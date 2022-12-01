<p style="width: 100%; text-align: center">
    <a href="https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/introduction/python_division">
        Previous
    </a>
    <a style="width: 100%; text-align: center" href="https://github.com/Kevin-Lago/python-hackerrank-solutions">
        Home
    </a>
    <a href="https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/introduction/write_a_function">
        Next
    </a>
</p>

# Loops

__Task__

The provided code stud reads an integer, _n_, from STDIN. For all non-negative integers ___i_ < _n___, print ___i_<sup>2</sup>__.

__Example__

___n_ = 3__

The list of non-negative integers that are less than ___n_ = 3__ is __[0, 1, 2]__. Print the square of each number on a separate line.

```
0
1
4
```

__Input Format__

The first and only line contains the integer, _n_.

__Constraints__

__1 <= _n_ <= 20__

__Output Format__

Print ___n___ lines, one corresponding to each ___i___.

__Sample Input 0__

```
5
```

__Sample Output 0__

```
0
1
4
9
16
```

__Solution__

```python
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i * i)
```
