| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Company Logo

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string $s$, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

- Print the three most common characters along with their occurrence count.

- Sort in descending order of occurrence count.

- If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,

__GOOGLE__ would have it's logo with the letters G, O, E.

__Input Format__

A single line of input containing the string $s$.

__Constraints__

- $3 < len(s) \le 10^4$

- $s$ has at least $3$ distinct characters.

__Output Format__

Print the three most common characters along with their occurrence count each on a separate line.

Sort output in descending order of occurrence count.

If the occurrence count is the same, sort the characters in alphabetical order.

__Sample Input__

```
aabbbccde
```

__Sample Output__

```
b 3
a 2
c 2
```

__Explanation__

__aaBBBccde__

Here, b occurs $3$ times. It is printed first.

Both a and c occur $2$ times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

__Note:__ The string $s$ has at least $3$ distinct characters.

---

<details><summary>Solution</summary>
    
```python
from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    c = Counter(s).most_common()

    [print(c[i][0], c[i][1]) for i in range(3)]
```
</details>
