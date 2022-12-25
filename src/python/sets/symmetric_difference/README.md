| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/no_idea)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/set_add)</img> |
|:---|:---:|---:|

# Symmetric Difference

__Objective__

Today, we're learning about a new data type: sets.

__Concept__

If the input are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter.

Usage:

```
>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']
```

If the list values are all integer types, use the map() method to convert all the strings to integers.

```
>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]
```

Sets are an unordered collection of unique values. A single set contains values of any immutable data type.

__Creating Sets__

```python
>> myset = {1, 2} # Directly assigning values to a set
>> myset = set()  # Initializing a set
>> myset = set(['a', 'b']) # Creating a set from a list
>> myset
{'a', 'b'}
```

__Modifying Sets__

Using the add() function:

```python
>> myset.add('c')
>> myset
{'a', 'c', 'b'}
>> myset.add('a') # As 'a' already exists in the set, nothing happens
>> myset.add((5, 4))
>> myset
{'a', 'c', 'b', (5, 4)}
```

Using the update() function:

```python
>> myset.update([1, 2, 3, 4]) # update() only works for iterable objects
>> myset
{'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
>> myset.update({1, 7, 8})
>> myset
{'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
>> myset.update({1, 6}, [5, 13])
>> myset
{'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}
```

__Removing Items__

Both the discard() and remove() functions take a single value as an argument and removes that value from the set. If taht value is not present, discard() does nothing, but remove() will raise a KeyError exception.

```python
>> myset.discard(10)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
>> myset.remove(13)
>> myset
{'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}
```

__Common Set Operations__

Using union(), intersection() and difference() functions.

```python
>> a = {2, 4, 5, 9}
>> b = {2, 4, 11, 12}
>> a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
>> a.intersection(b) # Values which exist in a and b
{2, 4}
>> a.difference(b) # Values which exist in a but not in b
{9, 5}
```

The union() and intersection() functions are symmetric methods:

```python
>> a.union(b) == b.union(a)
True
>> a.intersection(b) == b.intersection(a)
True
>> a.difference(b) == b.difference(a)
False
```

These [other built-in data structures in Python](https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-4--built-in-data-structures-strings-lists-tuples-dictionaries-mutability) are also useful.

__Task__

Given __2__ sets of integers, ___m___ and ___n___, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either ___m___ or ___n___ but do not exist in both.

__Input Format__

The first line of input contains an integer, ___m___.

The second line contains ___m___ space-separated integers.

The third line contains an integer, ___n___.

The fourth line contains ___n___ space-separated integers.

__Output Format__

Output the symmetric difference integer in ascending order, one per line.

__Sample Input__

```
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
```

__Sample Output__

```
5
9
11
12
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    m = input()
    a = set(input().split(" "))

    n = input()
    b = set(input().split(" "))

    arr = list(map(int, a.difference(b))) + list(map(int, b.difference(a)))
    arr.sort()

    for i in range(len(arr)):
        print(arr[i])
```
</details>