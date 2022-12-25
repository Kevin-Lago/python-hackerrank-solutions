| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/itertools/itertools_combinations_with_replacement)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/itertools/iterables_and_iterators)</img> |
|:---|:---:|---:|

# Compress the String!

In this task, we would like for you to appreacate the usefulness of groupby() function of itertools. To read more about this function, [check this out]().

You are given a string ___s___. Suppose a character '___c___' occurs consecutively ___x___ times in the string. Replace these consecutive occurrences of the character '___c___' with (___x___, ___c___) in the string.

For a better understanding of the problem, check the explanation.

__Input Format__

A single line of input consisting of the string ___s___.

__Output Format__

A single line of output consisting of the modified string.

__Constraints__

All the characters of ___s___ denote integers between __0__ and __9__.

$1 \le |s| \le 10^4$

__Sample Input__

```
1222311
```

__Sample Output__

```
(1, 1) (3, 2) (1, 3) (2, 1)
```

__Explanation__

First, the character __1__ occurs only once. It is replaced by __(1, 1)__. Then the character __2__ occurs three times, and it is replaced by __(3, 2)__ and so on.

Also, note the single space within each compression and between the compressions.

---

<details><summary>Solution</summary>
    
```python
import itertools

if __name__ == '__main__':
    s = input()
    a = [(len(list(l)), int(c)) for c, l in itertools.groupby(s)]

    [print(t, end=" ") for t in a]
```
</details>