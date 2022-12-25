| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/nested_lists)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/lists)</img> |
|:---|:---:|---:|

# Finding the percentage

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.

Print the average of the marks array for the student name provided, showing 2 places after the decimal.

__Example__

$marks key: value pairs are$

$'alpha': [20, 30, 40]$

$'beta': [30, 50, 70]$

$query_name = 'beta'$

The __query_name__ is 'beta'. beta's average score is $(30 + 50 + 70) / 3 = 50.0$.

__Input Format__

The first line contains the integer $n$, the number of students' record. The next $n$ lines contains the names and marks obtained by a student, each value separated by a space. The final line contains $query_name$, the name of a student to query.

__Constraints__

- $2 \le n \le 10$

- $0 \le marks[i] \le 100$

- $length of marks array = 3$

__Output Format__

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

__Sample Input 0__

```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

__Sample Output 0__

```
56.00
```

__Explanation 0__

Marks for Malika are ${52, 56, 60}$ whose average is $52 + 56 + 60 / 3 = 56$

__Sample Input 1__

```
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
```

__Sample Output 1__

```
26.50
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    print("{:.2f}".format(sum(student_marks[query_name]) / len(student_marks[query_name])))
```
</details>
