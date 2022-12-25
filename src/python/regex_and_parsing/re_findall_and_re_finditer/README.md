| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/group_groups_and_groupdict)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/re_start_and_re_end)</img> |
|:---|:---:|---:|

# Re.findall() & Re.finditer()

[re.findall()]()

the expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.

```python
>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```

[re.finditer()]()

The expression re.finditer() returns an iterator yielding ```MatchObject``` instances over all non-overlapping matches for the re pattern in the string.

```python
>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```

---

__Task__

You are given a string $s$. It consists of alphanumeric characters, spaces and symbols (```+```, ```-```).

Your task is to find all the substrings of $s$ that contains $2$ or more vowels.

Also, these substrings must lie in between $2$ consonants and should contains vowels only.

__Note:__

Vowels are defined as ```AEIOU``` and ```aeiou```.

Consonants are defined as: ```QWRTYPSDFGHJKLZXCVBNM``` and ```qwrtypsdfghjklzxcvbnm```.

__Input Format__

A single line of input containing string $s$.

__Constraints__

$0 < len(s) < 100$

__Output Format__

Print the matched substrings in their order of occurrence on separate lines.

If no match is found, print ```-1```.

__Sample Input__

```
rabcdeefgyYhFjkIoomnpOeorteeeeet
```

__Sample Output__

```
ee
Ioo
Oeo
eeeee
```

__Explanation__

$ee$ is located between consonant $d$ and $f$.

$loo$ is located between consonant $k$ and $m$.

$Oeo$ is located between consonant $p$ and $r$.

$eeeee$ is located between consonant $t$ and $t$.

---

<details><summary>Solution</summary>
    
```python

```
</details>
