# Find a String

In this challenge, the user enters a string and substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

__NOTE:__ String letters are case-sensitive.

__Input Format__

The first line of input contains the original string. The next line contains the substring.

__Constraints__

__1 <= _len(string)_ <= 200__

Each character in the string is an ascii character.

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

Some string processing examples, [such as these](), might be useful.

There are a couple of new concepts:

In Python, the length of a string is found by the function ```len(s)```, where ___s___ is the string.

To traverse through the length of a string, use a for loop:

```python
for i in range(0, len(s)):
    print(s[i])
```

A range function is used to loop over some length:

```python
range(0, 5)
```

Here, the range loops over __0__ to __4__. __5__ is excluded.

__Solution__

```python
def count_substring(string, sub_string):
    substring_count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if (string[i:i + len(sub_string)] == sub_string):
            substring_count += 1

    return substring_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
```
 