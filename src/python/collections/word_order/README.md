| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/collections/collections_ordereddict)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/collections/collections_deque)</img> |
|:---|:---:|---:|

# Word Order

You are given $n$ words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the words. See the sample input/output for clarification.

__Note:__ Each input line ends with a "\n" characters.

__Constraints__

$1 \le n \le 10^5$

The sum of the lengths of all the words do not exceed $10^6$

All the words are composed of lowercase English letters only.

__Input Format__

The first line contains the integer, $n$.

The next $n$ lines each contain a word.

__Output Format__

Output $2$ lines.

On the first line, output the number of distinct words from the input.

On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

__Sample Input__

```
4
bcdef
abcdefg
bcde
bcdef
```

__Sample Output__

```
3
2 1 1
```

__Explanation__

There are $3$ distinct words. Here, $"bcdef"$ appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are $"bcdef", "abcdefg"$ and $"bcde"$ which corresponds to the output.

---

<details><summary>Solution</summary>
    
```python
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    c = Counter([input() for i in range(n)])

    print(len(c))
    [print(c[k], end=" ") for k in c]
```
</details>
