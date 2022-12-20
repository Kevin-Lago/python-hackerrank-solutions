| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Collections.deque()

A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either and pops from either side of the deque with approximately the same $O(1)$ performance in either direction.

Click on the link to learn more about $deque()$ methods.

Click on the link to learn more about various approaches to working with deques: $Deque Recipes$

__Example__

```
>>> from collections import deque
>>> d = deque()
>>> d.append(1)
>>> print d
deque([1])
>>> d.appendleft(2)
>>> print d
deque([2, 1])
>>> d.clear()
>>> print d
deque([])
>>> d.extend('1')
>>> print d
deque(['1'])
>>> d.extendleft('234')
>>> print d
deque(['4', '3', '2', '1'])
>>> d.count('1')
1
>>> d.pop()
'1'
>>> print d
deque(['4', '3', '2'])
>>> d.popleft()
'4'
>>> print d
deque(['3', '2'])
>>> d.extend('7896')
>>> print d
deque(['3', '2', '7', '8', '9', '6'])
>>> d.remove('2')
>>> print d
deque(['3', '7', '8', '9', '6'])
>>> d.reverse()
>>> print d
deque(['6', '9', '8', '7', '3'])
>>> d.rotate(3)
>>> print d
deque(['8', '7', '3', '6', '9'])
```

---

__Task__

Perform append, pop, popleft and appendleft methods on an empty deque $d$.

__Input Format__

The first line contains an integer $n$, the number of operations.

The next $n$ lines contains the space separated names of methods and their values.

__Constraints__

$0 < n \le 100$

__Output Format__

Print the space separated elements of deque $d$.

__Sample Input__

```
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```

__Sample Output__

```
1 2
```

---

<details><summary>Solution</summary>
    
```python
from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    q = [input().split() for i in range(n)]

    for c in q:
        if 'appendleft' in c:
            d.appendleft(c[1])
            continue

        if 'append' in c:
            d.append(c[1])
            continue

        if 'popleft' in c:
            d.popleft()
            continue

        if 'pop' in c:
            d.pop()
            continue

    [print(e, end=" ") for e in d]
```
</details>
