# Mutations

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand with an example.

You are given an immutable string, and you want to make changes to it.

__Example__

```python
string = "abracadabra"
```

You can access an index by:

```python
print(string[5])
```

What if you would like to assign a value?

```python
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```
