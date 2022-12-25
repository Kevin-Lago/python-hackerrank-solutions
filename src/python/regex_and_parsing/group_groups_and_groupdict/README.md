| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/re_split)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/re_findall_and_re_finditer)</img> |
|:---|:---:|---:|

# Group(), Groups() & Groupdict()

[group()]()

A group() expression returns one or more subgroups of the match

```python
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
```

[groups()]()

A groups() expression returns a tuple containing all the subgroups of the match.

```python
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')
```

[groupdict()]()

A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.

```python
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
```

---

__Task__

You are given a string $s$.

Your task is to find the first occurrence of an alphanumeric character in $s$. (read from left to right) that has consecutive repetitions.

__Input Format__

A single line of input containing the string $s$.

__Constraints__

$0 < len(s) < 100$

__Output Format__

Print the first occurrence of the repeating character. If there are no repeating characters, print ```-1```.

__Sample Input__

```
..12345678910111213141516171820212223
```

__Sample Output__

```
1
```

__Explanation__

```..``` is the first repeating character, but it is not alphanumeric.

```1``` is the first (from left to right) alphanumeric repeating character of the string in the substring ```111```.

---

<details><summary>Solution</summary>
    
```python
import re

if __name__ == '__main__':
    m = re.search("([a-zA-Z0-9]+)\\1+", input())

    try:
        print(m.groups()[0])
    except AttributeError as e:
        print("-1")
```
</details>
