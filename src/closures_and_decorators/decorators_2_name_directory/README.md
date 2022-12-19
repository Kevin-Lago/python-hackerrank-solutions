| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Decorators 2 - Name Directory

Let's use decorators to build a name directory! You are given some information about $n$ people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry David, the output should be:

```
Mr. Henry Davids
```

For Mary George, the output should be:

```
Ms. Mary George
```

__Input Format__

The first line contains the integer $n$, the number of people.

$n$ lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

__Constraints__

$1 \le n \le 10$

__Output Format__

Output $n$ names on separate lines in the format described above in ascending order of age.

__Sample Input__

```
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
```

__Sample Output__

```
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
```

__Concept__

For sorting a nested list based on some parameter, you can use the itemgetter library. You can read more about it [here]().

---

<details><summary>Solution</summary>
    
```python
def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda s: int(s[2]))]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
```
</details>
