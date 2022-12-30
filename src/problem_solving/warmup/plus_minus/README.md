| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Plus Minus

Given an array of integers, calculate the ratios of its elements that are positive, negative and zero. Print the decimal value of each fraction on a new line with $6$ places after the decimal.

__Note:__ This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to $10^{-4}$ are acceptable.

__Example__

$arr = [1, 1, 0, -1, -1]$

There are $n = 5$ elements, two positive, two negative and one zero. Their ratios are $2 / 5 = 0.400000$, $2 / 5 = 0.400000$ and $1 / 5 = 0.200000$. Results are printed as:

```
0.400000
0.400000
0.200000
```

__Function Description__

Complete the plus_minus function in the editor below.

plus_minus has the following parameter(s):

- int[n] arr: an array of integers

__Print__

Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with $6$ digits after the decimal. The function should not return a value.

__Input Format__

The first line contains an integer, $n$, the size of the array.

The second line contains $n$ space-separated integers that describe $arr[n]$.

__Constraints__

- $0 < n \le 100$

- $-100 \le arr[i] \le 100$

__Output Format__

Print hte following $3$ lines, each to $6$ decimals:

1. proportion of positive values

2. proportion of negative values

3. proportion of zeros

__Sample Input__

```
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
``` 

__Sample Output__

```
0.500000
0.333333
0.166667
```

__Explanation__

There are $3$ positive numbers, $2$ negative numbers, and $1$ zero in the array.

The proportions of occurrence are positive: $3 / 6 = 0.500000$, negative: $2 / 6 = 0.333333$ and zeros: $1 / 6 = 0.166667$

---

<details><summary>Solution</summary>
    
```python
def plus_minus(arr):
    positives, negatives, zeros, length = 0, 0, 0, len(arr)

    for e in arr:
        if e > 0:
            positives += 1
        elif e < 0:
            negatives += 1
        else:
            zeros += 1

    print("{:f}".format(positives / length))
    print("{:f}".format(negatives / length))
    print("{:f}".format(zeros / length))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plus_minus(arr)
```
</details>
