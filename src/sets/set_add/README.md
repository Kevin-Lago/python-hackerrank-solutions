| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/sets/symmetric_difference)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/sets/set_discard_remove_and_pop)</img> |
|:---|:---:|---:|

# Set .add()

If we want to add a single element to an existing set, we can use the .add() operation.

It adds the element to the set and returns '```None```'.

__Example__

```python
>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
```

__Task__

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from the stack of ___n___ country stamps.

Find the total number of distinct country stamps.

__Input Format__

The first line contains an integer ___n___, the total number of country stamps.

The next ___n___ line contains the name of the country where the stamp is form.

__Constraints__

$0 \le n \le 1000$

__Output Format__

Output the total number of distinct country stamps on a single line.

__Sample Input__

```
7
UK
China
USA
France
New Zealand
UK
France 
```

__Sample Output__

```
5
```

__Explanation__

UK and France repeat twice. Hence, the total number of distinct country stamps is __5__ (five).

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    a = set()

    for i in range(n):
        a.add(input())

    print(len(a))
```
</details>