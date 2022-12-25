| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/list_comprehensions)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/nested_lists)</img> |
|:---|:---:|---:|

# Find the Runner-Up Score!

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given $n$ scores. Store them in a list and find the score of the runner-up.

__Input Format__

The first line contains $n$. The second line contains an array $a[]$ of $n$ integers each separated by a space.

__Constraints__

- $2 \le n \le 10$

- $-100 \le a[i] \le 100$

__Output Format__

Print the runner-up score.

__Sample Input__

```
5
2 3 6 6 5
```

__Sample Output__

```
5
```

__Explanation__

Given list is $[2,3,6,6,5]$. The maximum score is $6$, second maximum is $5$. Hence, we print $5$ as runner-up score.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_value = max(arr)
    arr = list(filter(lambda e: e != max_value, arr))

    print(max(arr))
```
</details>
