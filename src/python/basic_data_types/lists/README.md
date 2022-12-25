| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/finding_the_percentage)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/basic_data_types/tuples)</img> |
|:---|:---:|---:|

# Lists

Consider a list (```list = []```). You can perform the following commands:

1. ```insert i e```: insert integer $e$ at position $i$.

2. ```print```: Print the list

3. ```remove e```: Delete the first occurrence of integer $e$.

4. ```append e```: Insert integer $e$ at the end of the list.

5. ```sort```: Sort the list.

6. ```pop```: Pop the last element from the list.

7. ```reverse```: Reverse the list.

Initialize your list and read in the value of $n$ followed by $n$ lines of commands where each command will be of $7$ types listed above. Iterate through each command in order and perform the corresponding operation on your list.

__Example__

$n = 4$

$append 1$

$append 2$

$insert 3 1$

$print$

- $append 1$: Append $1$ to the list, $arr = [1]$.

- $append 2$: Append $2$ to the list, $arr = [1, 2]$.

- $insert 3 1$: Insert $3$ at index $1$, $arr = [1, 3, 2]$

- $print$: Print the array.

    Output:
    
```
[1, 3, 2]
```

__Input Format__

The first line contains an integer, $n$, denoting the number of commands.

Each line $i$ of the $n$ subsequent lines contains one of the commands described above.

__Constraints__

- The elements added to the list must be integers.

__Output Format__

For each command of type ```print```, print the list on a new line.

__Sample Input__

```
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

__Sample Output__

```
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    l = []

    commands = {
        "insert": lambda *args: l.insert(int(args[0][0]), int(args[0][1])),
        "print": lambda *args: print(l),
        "remove": lambda *args: l.remove(int(args[0][0])),
        "append": lambda *args: l.append(int(args[0][0])),
        "sort": lambda *args: l.sort(),
        "pop": lambda *args: l.pop(),
        "reverse": lambda *args: l.reverse()
    }

    for i in range(n):
        string = input().split(" ")

        try:
            commands[string[0]](string[1:])
        except():
            print("command does not exist")
```
</details>
