| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/string_split_and_join)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/mutations)</img> |
|:---|:---:|---:|

# What's Your Name?

You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

> Hello ```firstname``` ```lastname```! You just delved into python.

__Function Description__

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

- string first: the first name

- string last: the last name

__Prints__

- string: 'Hello $firstname lastname$! You just delved into python' where $firstname$ and $lastname$ are replace with $first$ and $last$.

__Input Format__

The first line contains the first name, and the second line contains the last name.

__Constraints__

The length of the first and last names are each $\le 10$.

__Sample Input__

```
Ross
Taylor
```

__Sample Output__

```
Hello Ross Taylor! You just delved into python.
```

__Explanation__

The input read by the program is stored as a string data type. A string is a collection of characters.

---

<details><summary>Solution</summary>
    
```python
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```
</details>
