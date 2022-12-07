# sWAP cASE

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice verse.

__For Example:__

```
Www.HackerRank.com -> wWW.hACKERrANK.COM
Pythonist 2 -> pYTHONIST 2
```

__Function Description__

Complete the swap_case function in the editor below.

swap_case has the following parameters:

- string s: the string to modify

__Returns__

- string: the modified string.

__Input Format__

A single line containing a string ___s___

__Constraints__

__0 < _len(s) <= 100__

__Sample Input 0__

```
HackerRank.com presents "Pythonist 2".
```

__Sample Output 0__

```
hACKERrANK.COM PRESENTS "pYTHONIST 2".
```

__Solution__

```python
def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```
