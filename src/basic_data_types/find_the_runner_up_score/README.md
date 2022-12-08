| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/basic_data_types/list_comprehensions)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/basic_data_types/nested_lists)</img> |
|:---|:---:|---:|

# Find the Runner-Up Score!

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given ___n___ scores. Store them in a list and find the score of the runner-up.

__Input Format__

The first line contains ___n___. The second line contains an array ___a[]___ of ___n___ integers each separated by a space.

__Constraints__

- __2 <= _n_ <= 10__

- __-100 <= _a[i]_ <= 100__

__Output Format__

Print the runner-up score.

__Sample Input__

```
5
2 3 6 6 5
```

__Sample Output 0__

```
5
```

__Explanation 0__

Given list is __[2,3,6,6,5]__. The maximum score is __6__, second maximum is __5__. Hence, we print __5__ as runner-up score.

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
