| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/introduction/print_function)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/find_the_runner_up_score)</img> |
|:---|:---:|---:|

# List Comprehensions 

Let's learn about list comprehensions! You are given three integers $x$, $y$ and $z$ representing the dimensions of a cuboid along with an integer $n$. Print a list of all possible coordinates given by $(i, j, k)$ on a 3D grid where the sum of $i + j + k$ is not equal to $n$. Here, $0 \le i \le x; 0 \le j \le y; 0 \le k \le z$. Please use list comprehensions rather than multiple loops, as a learning exercise.

__Example__

$x = 1$

$y = 1$

$z = 2$

$n = 3$

All permutations of $[i, j, k]$ are:

$[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]$

Print an array of elements that do not sum to $n = 3$.

$[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]$

__Input Format__

Four integers $x$, $y$, $z$ and $n$, each on a separate line.

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

Each variable $x$, $y$, $z$ will have values of $0$ or $1$. All permutations of lists in the form 

$[i, j, k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]$

Remove all arrays that sum to $n = 2$ to leave only the valid permutations.

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
