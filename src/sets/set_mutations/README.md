| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/sets/set_symmetric_difference_operation)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/sets/the_captains_room)</img> |
|:---|:---:|---:|

# Set Mutations

We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

__We can use the following operations to create mutations to a set:__

__.update()__ or ```|=```

Update the set by adding elements from an iterable/another set

```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
```

__.intersection_update()__ or ```&=```

Update the set by keeping only the elements found in it and na iterable/another set.

```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
```

__.difference_update()__ or ```-=```

Update the set by removing elements found in an iterable/another set.

```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
```

__.symmetric_difference_update()__ or ```^=```

Update the set by only keeping the elements found in either set, but not in both.

```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
```

---

__Task__

You are given a set ___a___ and ___n___ number of other sets. These ___n___ number of sets have to perform some specific mutation operations on set ___a___.

__Input Format__

The first line contains the number of elements in set ___a___.

The second line contains the space separated list of elements in set ___a___.

The third line contains integer ___n___, the number of other sets.

the next __2 * _n___ lines are divided into ___n___ parts containing two lines each.

The first line of each part contains the space separated entries of the operation name and the length of the other set.

the second line of each part contains space separated list of elements in the other set.

$0 < len(set(a)) < 1000$

$0 < len(otherSets) < 100$

$0 < n < 100$

__Output Format__

Output the sum of element in set ___a___.

__Sample Input__

```
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
```

__Sample Output__

```
38
```

__Explanation__

After the first operation, (intersection_update operation), we get:

set ___a___ = ___set_([1,2,3,4,5,6,7,8,9,11])__

After the second operation, (update operation), we get:

set ___a___ = ___set_([1,2,3,4,5,6,7,8,9,11,55,66])__

After the third operation, (symmetric_difference_update operation), we get:

set ___a___ = ___set_([1,2,3,4,5,6,8,9,11,22,35,55,58,62,66])__

After the fourth operation, (difference_update operation), we get:

set ___a___ = ___set_([1,2,3,4,5,6,8,9])__

The sum of elements in set ___a___ after the operations is __38__.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))

    m = int(input())

    for i in range(m):
        q, x = input().split()
        s = set(map(int, input().split()))

        if q == "intersection_update":
            a.intersection_update(s)
            continue

        if q == "update":
            a.update(s)
            continue

        if q == "symmetric_difference_update":
            a.symmetric_difference_update(s)
            continue

        if q == "difference_update":
            a.difference_update(s)
            continue

    print(sum(a))
```
</details>