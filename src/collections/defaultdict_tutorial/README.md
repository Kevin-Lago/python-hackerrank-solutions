| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# DefaultDict Tutorial

The defaultdict tool is a container in the collection class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a default dict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

__For Example:__

```python
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
```

This prints:

```
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
```

In this challenge, you will be given __2__ integer, ___n___ and ___m___. There are ___n___ words, which might repeat, in word group ___a___.

There are ___m___ words belonging to word group ___b___. For each ___m___ words, check whether the word has appeared in group ___a___ or not. Print the indices of each occurrence of ___m___ in group ___a___. If it does not appear, print __-1__.

__Example__

Group ___a___ contains 'a', 'b', 'a' Group ___b___ ocntains 'a', 'c'

For the first word in group ___b___, 'a', it appears at positions __1__ and __3__ in group ___a___. The second word, 'c', does not appear in group ___a___, so print __-1__

Expected output:

```
1 3
-1
```

__Input Format__

- $1 \le n \le 10000$

- $1 \le m \le 100$

- $1 \le length of each word in the input \le 100$

__Output Format__

Output ___m___ lines.

The ___i<sup>th</sup>___ line should contain the __1__-indexed positions of the occurrences of the ___i<sup>th</sup>___ word separated by spaces.

__Sample Input__

```
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
```

__Sample Output__

```
1 2 4
3 5
```

__Explanation__

__'a'__ appeared __3__ times in positions __1, 2__ and __4__.

__'b'__ appeared __2__ times in positions __3__ and __5__.

In the sample problem, if __'c'__ also appeared in word group ___b___, you would print __-1__.

---

<details><summary>Solution</summary>
    
```python
from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = defaultdict(list)

    for i in range(n):
        w = input()
        a[w].append(i)

    for i in range(m):
        w = input()
        if a[w]:
            print(" ".join([str(i + 1) for i in a[w]]))
        else:
            print("-1")
```
</details>