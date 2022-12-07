| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/basic_data_types/find_the_runner_up_score)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/basic_data_types/finding_the_percentage)</img> |
|:---|:---:|---:|

# Nested Lists

Given the names and grades for each student in a class of ___n___ students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

__Note:__ If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

__Example__

___records_ = [["chi", 20.0],["beta",50.0],["alpha",50.0]]__

The ordered list of scores is __[20.0,50.0]__, so the second lowest score is __50.0__. There are two students with that score: __["beta","alpha"]__. Ordered alphabetically, the names are printed as:

```
alpha
beta
```

__Input Format__

The first line contains an integer, ___n___, the number of students.

The __2n__ subsequent lines describe each student over __2__ lines.

- The first line contains a student's name.

- The second line contains their grade.

__Constraints__

- __2 <= _n_ <= 5__

- There will always be one or more students having the second lowest grade.

__Output Format__

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

__Sample Input 0__

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

__Sample Output 0__

```
Berry
Harry
```

__Explanation 0__

There are __5__ students in this class whose names and grades are assembled to build the following list:

```python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]```

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

---

<details><summary>Solution</summary>
    
```python

```
</details>