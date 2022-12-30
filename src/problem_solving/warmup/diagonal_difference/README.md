| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix $arr$ is shown below:

```
1 2 3
4 5 6
9 8 9  
```

The left-to-right diagonal is $1 + 5 + 9 = 15$. The right to left diagonal is $3 + 5 + 9 = 17$. Their absolute difference is $|15 - 17| = 2$.

__Function Description__

Complete the diagonal_difference function in the editor below.

diagonal_difference takes the following parameter:

- int[n][m] arr: an array of integers

__Return__

- int: the absolute diagonal difference

__Input Format__

The first line contains a single integer, $n$, the number of rows and columns in the square matrix $arr$.

Each of the next $n$ lines describe a row, $arr[i]$, and consists of $n$ space-separated integers $arr[i][j]$.

__Constraints__

- $-100 \le arr[i][j] \le 100$

__Output Format__

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

__Sample Input__

```
3
11 2 4
4 5 6
10 8 -12
```

__Sample Output__

```
15
```

__Explanation__

The primary diagonal is:

```
11
   5
     -12
```

Sum across the primary diagonal: $11 + 5 - 12 = 4$

The secondary diagonal is:

```
     4
   5
10
```

Sum across the secondary diagonal: $4 + 5 + 10 = 19$

Difference: $|4- 19| = 15$

__Note:__ $|x|$ is the [absolute value](https://www.mathsisfun.com/numbers/absolute-value.html) of x

---

<details><summary>Solution</summary>
    
```python
import os


def diagonal_difference(arr):
    length = len(arr)

    return abs(
        sum([arr[i][i] for i in range(length)]) -
        sum([arr[i][length - i - 1] for i in range(length)])
    )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = [list(map(int, input().split())) for i in range(n)]

    result = diagonal_difference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
```
</details>
