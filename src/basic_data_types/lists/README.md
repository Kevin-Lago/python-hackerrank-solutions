# Lists

Consider a list (```list = []```). You can perform the following commands:

1. ```insert i e```: insert integer ___e___ at position ___i___.

2. ```print```: Print the list

3. ```remove e```: Delete the first occurrence of integer ___e___.

4. ```append e```: Insert integer ___e___ at the end of the list.

5. ```sort```: Sort the list.

6. ```pop```: Pop the last element from the list.

7. ```reverse```: Reverse the list.

Initialize your list and read in the value of ___n___ followed by ___n___ lines of commands where each command will be of __7__ types listed above. Iterate thrrough each command in order and perform the corresponding operation on your list.

__Example__

___n_ = 4__

___append_ 1__

___append_ 2__

___insert 3 1___

___print___

- ___append_ 1__: Append __1__ to the list, ___arr_ = [1]__.

- ___append_ 2__: Append 2 to the list, ___arr_ = [1,2]__.

- ___insert_ 3 1__: Insert 3 at index __1__, ___arr_ = [1,3,2]__

- ___print_: Print the array.

    Output:
    
```
[1, 3, 2]
```

__Input Format__

The first line contains an integer, ___n___, denoting the number of commands.

Each line ___i___ of the ___n___ subsequent lines contains one of the commands described above.

__Constraints__

- The elements added to the list must be integers.

__Output Format__

For each command of type ```print```, print the list on a new line.

__Sample Input 0__

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

__Sample Output 0__

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
