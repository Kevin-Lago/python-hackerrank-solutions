| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/whats_your_name)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/find_a_string)</img> |
|:---|:---:|---:|

# Mutations

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand with an example.

You are given an immutable string, and you want to make changes to it.

__Example__

```python
>>> string = "abracadabra"
```

You can access an index by:

```python
>>> print string[5]
a
```

What if you would like to assign a value?

```python
>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

How would you approach this?

- One solution is to convert the string to a list and then change the value.

__Example__

```python
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
```

- Another approach is to slice the string and join it back.

Example

```python
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
```

__Task__

Read a given string, change the character at a given index and then print the modified string.

__Function Description__

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

- string string: the string to change

- int position: the index to insert the character at

- string character: the character to insert

__Returns__

- string: the altered string

__Input Format__

The first line contains a string, ___string___.

The next line contains an integer ___position___, the index location and a string ___character___, separated by a space.

__Sample Input__

```
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
```

__Sample Output__

```
abrackdabra
```

---

<details><summary>Solution</summary>
    
```python
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```
</details>
