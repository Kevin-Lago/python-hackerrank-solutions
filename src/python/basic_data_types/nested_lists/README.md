| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/find_the_runner_up_score)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/finding_the_percentage)</img> |
|:---|:---:|---:|

# Nested Lists

Given the names and grades for each student in a class of $n$ students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

__Note:__ If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

__Example__

$records = [["chi", 20.0],["beta",50.0],["alpha",50.0]]$

The ordered list of scores is $[20.0,50.0]$, so the second lowest score is $50.0$. There are two students with that score: $["beta","alpha"]$. Ordered alphabetically, the names are printed as:

```
alpha
beta
```

__Input Format__

The first line contains an integer, $n$, the number of students.

The $2n$ subsequent lines describe each student over $2$ lines.

- The first line contains a student's name.

- The second line contains their grade.

__Constraints__

- $2 \le n \le 5$

- There will always be one or more students having the second lowest grade.

__Output Format__

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

__Sample Input__

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

__Sample Output__

```
Berry
Harry
```

__Explanation__

There are $5$ students in this class whose names and grades are assembled to build the following list:

```python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]```

The lowest grade of $37.2$ belongs to Tina. The second lowest grade of $37.21$ belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    students = []

    for i in range(n):
        name = input()
        score = float(input())

        students.insert(i, [name, score])

    students.sort(key=lambda s: s[0])
    lowest_grade = min(students, key=lambda s: s[1])[1]

    for i in range(n):
        if students[n - i - 1][1] == lowest_grade:
            students.remove(students[n - i - 1])

    second_lowest_grade = min(students, key=lambda s: s[1])[1]

    for i in range(n - 1):
        if students[i][1] == second_lowest_grade:
            print(students[i][0])
```
</details>