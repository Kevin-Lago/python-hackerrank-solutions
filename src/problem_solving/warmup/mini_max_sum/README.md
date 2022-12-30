| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Mini-Max Sum

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

__Example__

$arr = [1, 3, 5, 7, 9]$

The minimum sum is $1 + 3 + 5 + 7 = 16$ and the maximum sum is $3 + 5 + 7 + 9 = 24$. The function prints

```
16 24
```

__Function Description__

Complete the mini_max_sum function in the editor below.

mini_max_sum has the following parameter(s):

- int[5] arr: an array of $5$ integers

__Print__

Print two space-separated integers on one line: the minimum sum and the maximum sum of $4$ of $5$ elements.

__Input Format__

A single line of five space-separated integers.

__Constraints__

- $1 \le arr[i] \le 10^{9}$

__Output Format__

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer)

__Sample Input__

```
1 2 3 4 5
```

__Sample Output__

```
10 14
```

__Explanation__

The numbers are $1, 2, 3, 4$ and $5$. Calculate the following sums using four of the five integers:

1. Sum everything except $1$, the sum is $2 + 3 + 4 + 5 = 14$

2. Sum everything except $2$, the sum is $1 + 3 + 4 + 5 = 13$

3. Sum everything except $3$, the sum is $1 + 2 + 4 + 5 = 12$

4. Sum everything except $4$, the sum is $1 + 2 + 3 + 5 = 11$

5. Sum everything except $5$, the sum is $1 + 2 + 3 + 4 = 10$

__Hint:__ Beware of integer overflow! Use 64-bit integer.

---

<details><summary>Solution</summary>
    
```python
def mini_max_sum(arr):
    minimum = list(arr)
    maximum = list(arr)

    minimum.remove(max(arr))
    maximum.remove(min(arr))

    print(sum(minimum), sum(maximum))


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    mini_max_sum(arr)
```
</details>
