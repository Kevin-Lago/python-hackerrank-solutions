| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/strings/the_minion_game)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/sets/introduction_to_sets)</img> |
|:---|:---:|---:|

# Merge The Tools!

Consider the following:

- A string, $s$, of length $n$ where $s = c_{0}c_{1}...c_{n-1}$.

- An integer, $k$, where $k$ is a factor of $n$.

We can split $s$ into $n / k$ substrings where each substring, $t_{i}$, consists of a contiguous block of $k$ characters in $s$.

Then, use each $t_{i}$ to create string $u_{i}$ such that:

- The characters in $u_{i}$ are a subsequence of the characters in $t_{i}$.

- Any repeat occurrence of a character is removed from the string such that each character in $u_{i}$ occurs exactly once. In other words, if the character at some index $j$ in $t_{i}$ occurs at a previous index $< j$ in $t_{i}$, then do not include the character in string $u_{i}$.

Given $s$ and $k$, print $n \ k$ lines where each line $i$ denotes string $u_{i}$.

__Example__

$s = 'AAABCADDE'$

$k = 3$

There are three substrings of length $3$ to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so $u_{i} = 'A'. The second substring has all distinct characters, so $u_{2} = 'BCA'$. The third substring has $2$ different characters, so $u_{3} = 'DE'$. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

__Function Description__

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

- string s: the string to analyze

- int k: the size of substrings to analyze

__Prints__

Print each subsequence on a new line. There will be $n / k$ of them. No return value is expected.

__Input Format__

The first line contains a single string, $s$.

The second line contains an integer, $k$, the length of each substring.

__Constraints__

- $1 \le n \le 10^4$

- $1 \le k \le n$

- It is guaranteed that $n$ is a multiple of $k$.

__Sample Input__

```
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
```

__Sample Output__

```
AB
CA
AD
```

__Explanation__

Split $s$ into $n / k = 9 / 3 = 3$ equal parts of length $k = 3$. Convert each $t_{i}$ to $u_{i}$ by removing any subsequent occurrences of non-distinct characters in $t_{i}$:

1. $t_{0} = "AAB" -> u_{0} = "AB"$

2. $t_{1} = "CAA" -> u_{1} = "CA"$

3. $t_{2} = "ADA" -> u_{2} = "AD"$

Print each $u_{i}$ on a new line. 

---

<details><summary>Solution</summary>
    
```python
def merge_the_tools(string, k):
    t = [string[k * i:k * i + k] for i in range(int(len(string) / k))]
    u = ["".join(dict.fromkeys(s).keys()) for s in t]

    [print(s) for s in u]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
```
</details>
