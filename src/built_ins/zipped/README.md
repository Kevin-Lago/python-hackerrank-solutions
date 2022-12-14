| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Zipped!

[zip(iterable, ...)]()

This function returns a list of tuples. The $i^th$ tuple contains the $i^th$ element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

__Sample Code__

```python
>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
```

---

__Task__

The National University conducts and examination of $n$ students in $x$ subjects.

Your task is to compute the average scores of each student.

$Average Score = Sum of the score obtained in all subjects by a student / Total number of subjects$

The format for the general mark sheet is:

```
Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 
```

__Input Format__

The first line contains $n$ and $x$ separated by a space.

The next $x$ lines contains the space separated marks obtained by students in a particular subject.

__Constraints__

$0 < n \le 100$

$0 < x \le 100$

__Output Format__

Print the averages of all students on separate lines.

The averages must be correct up to $1$ decimal place.

__Sample Input__

```
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
```

__Sample Output__

```
90.0 
91.0 
82.0 
90.0 
85.5  
```

__Explanation__

Marks obtained by $student 1: 89, 90, 91$

Average marks of $student 1: 270 / 3 = 90$

Marks obtained by $student 2: 90, 91, 92$

Average marks of $student 2: 273 / 3 = 91$

Marks obtained by $student 3: 78, 85, 83$

Average marks of $student 3: 246 / 3 = 82$

Marks obtained by $student 4: 93, 88, 89$

Average marks of $student 4: 270 / 3 = 90$

Marks obtained by $student 5: 80, 86, 90.5$

Average marks of $student 5: 256.5 / 3 = 85.5$

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n, x = map(int, input().split())
    grades = [list(map(float, input().split())) for i in range(x)]
    students = zip(*grades)

    [print(sum(s) / x) for s in students]
```
</details>
