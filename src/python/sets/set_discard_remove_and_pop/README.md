| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/set_add)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/set_union_operation)</img> |
|:---|:---:|---:|

# Set .discard(), .remove() & .pop()

__.remove(x)__

This operation removes the element ___x___ from the set.

If element ___x___ does not exist, it raises a ```KeyError```.

The .remove(x) operation returns ```None```.

__Example__

```python
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0
```

---

__.discard(x)__

This operation also removes elements ___x___ from the set.

If element ___x___ does not exist, it __does not__ raise a ```KeyError```.

The .discard(x) operation return ```None```.

__Example__

```python
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
```

---

__.pop()__

This operation removes and return an arbitrary element from the set.

If there are elements to remove, it raise a ```KeyError```.

__Example__

```python
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
```

---

__Task__

You have a non-empty set ___s___, and you have to execute ___n___ commands given in ___n___ lines.

The commands will be pop, remove and discard.

__Input Format__

The first line contains integer ___n___, the number of elements in the set ___s___.

The second line contains ___n___ space separated element os set ___s___. All of the elements are non-negative integers, less than or equal to 9.

The third line contains integer ___n___, the number of commands.

The next ___n___ lines contains either pop, remove and/or discard commands followed by their associated value.

__Constraints__

$0 < n < 20$

__Output Format__

Print the sum of the elements of set ___s___ on a single line.

__Sample Input__

```
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
```

__Sample Output__

```
4
```

__Explanation__

After completing these __10__ operations on the set, we get set__([4])__. Hence, the sum is __4__.

__Note:__ Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    q = int(input())

    for i in range(q):
        query = input()

        if (query.__contains__("pop")):
            s.pop()
            continue

        if (query.__contains__("remove")):
            s.remove(int(query.split(" ")[1]))
            continue

        if (query.__contains__("discard")):
            s.discard(int(query.split(" ")[1]))
            continue

    print(sum(s))
```
</details>