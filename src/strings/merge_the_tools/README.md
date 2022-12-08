| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/strings/the_minion_game)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/sets/introduction_to_sets)</img> |
|:---|:---:|---:|

# Merge The Tools!

Consider the following:

- A string, ___s___, of length ___n___ where ___s = c<sub>0</sub>c<sub>1</sub>...c<sub>n-1</sub>.

- An integer, ___k___, where ___k___ is a factor of ___n___.

We can split ___s___ into ___n___ / ___k___ substrings where each substring, ___t<sub>i</sub___, consists of a contiguous block of ___k___ characters in ___s___.

Then, use each ___t<sub>i</sub>___ to create string ___u<sub>i</sub>___ such that:

- The carachters in ___u<sub>i</sub>___ are a subsequence of the characters in ___t<sub>i</sub>

- Any repeat occurrences of a character is removed from the string such that each character in ___u<sub>i</sub>___ occurs exactly once. In other words, if the character at some index ___j___ abd ___t<sub>i</sub>___ occurs at a previous index < ___j___ in ___t<sub>i</sub>___, then do not include the character in string ___u<sub>i</sub>___

Given ___s___ and ___k___, print ___n___ / ___k___ lines where each line ___i___ denotes string ___u<sub>i</sub>___.

__Example__

___s___ = __'AAABCADDE'__

___k___ = __3__

There are three substrings of length __3__ to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so ___u<sub>1</sub>___ = 'A'. The second substring has all distinct characters, so ___u<sub>2</sub>___ = 'BCA'

---

<details><summary>Solution</summary>
    
```python

```
</details>
