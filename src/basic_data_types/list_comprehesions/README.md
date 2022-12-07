| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/introduction/print_function)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/basic_data_types/find_the_runner_up_score)</img> |
|:---|:---:|---:|

# List Comprehensions 

Let's learn about list comprehensions! You are given three integers _x_, _y_ and _z_ representing the dimensions of a cuboid along with an integer _n_. Print a list of all possible coordinates given by (_i_, _j_, _k_) on a 3D grid where the sum of _i_ + _j_ + _k_ is not equal to _n_. Here, 0 <= _i_ <= _x_; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.

__Example__

_x_ = 1

_y_ = 1

_z_ = 2

_n_ = 3

All permutations of [_i_, _j_, _k_] are:

__[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]__

Print an array of elements that do not sum to _n_ = 3.

__Input Format__

Four integers _x_, _y_, _z_ and _n_, each on a separate line.

__Constraints__

Print the list in lexicographic increasing order.

__Sample Input 0__

```
1
1
1
2
```

__Sample Output 0__

```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

__Explanation 0__

Each variable _x_, _y_, _z_ will have values of 0 or 1. All permutations of lists in the form 

__[_i_, _j_, _k_] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]__

Remove all arrays that sum to _n_ = 2 to leave only the valid permutations.

__Sample Input 1__

```
2
2
2
2
```

__Sample Output 1__

```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    array = [[i, j, k]
             for i in range(x + 1)
             for j in range(y + 1)
             for k in range(z + 1) if i + j + k != n]

    print(array)
```
</details>
