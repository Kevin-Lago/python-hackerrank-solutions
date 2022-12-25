| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/mutations)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/string_validators)</img> |
|:---|:---:|---:|

# Find a string

In this challenge, the user enters a string and substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

__Note:__ String letters are case-sensitive.

__Input Format__

The first line of input contains the original string. The next line contains the substring.

__Constraints__

- $1 \le len(string) \le 200$

- Each character in the string is an ascii character.

__Output Format__

Output the integer number indicating the total number of occurrences of the substring in the original string.

__Sample Input__

```
ABCDCDC
CDC
```

__Sample Output__

```
2
```

__Concept__

Some string processing examples, [such as these](https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation), might be useful.

There are a couple of new concepts:

In Python, the length of a string is found by the function ```len(s)```, where $s$ is the string.

To traverse through the length of a string, use a for loop:

```python
for i in range(0, len(s)):
    print(s[i])
```

A range function is used to loop over some length:

```python
range(0, 5)
```

Here, the range loops over $0$ to $4$. $5$ is excluded.

---

<details><summary>Solution</summary>
    
```python
def count_substring(string, sub_string):
    substring_count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            substring_count += 1

    return substring_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
```
</details>
 