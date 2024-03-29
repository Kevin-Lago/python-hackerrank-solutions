| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/capitalize)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/strings/merge_the_tools)</img> |
|:---|:---:|---:|

# The Minion Game

Kevin and Stuart want to play the '__The Minion Game__'.

__Game Rules__

Both players are given the same string, $s$.

Both players have to make substrings using the letters of the string $s$.

Stuart has to make words starting with consonants.

Kevin has to make words starting with vowels.

The game ends when both players have made all possible substrings.

__Scoring__

A player gets +1 point for each occurrence of the substring in the string $s$.

__For Example:__

String $s$ = BANANA

Kevin's vowel beginning word = ANA

Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 points.

For better understanding, see the image below:

![HackerrankTheMinionGameDiagram](1.png)

Your task is to determine the winner of the game and their score.

__Function Description__

Complete the minion_game in the editor below.

minion_game has the following parameters:

- string string: the string to analyze

__Prints__

- string: the winner's name and score, separated by a space on one line, or ```Draw``` if there is no winner.

__Input Format__

A single line of input containing the string $s$.

__Note:__ The string $s$ will contain only uppercase letters: $[A-Z]$.

__Constraints__

- $0 < len(s \le 10^{6})$

__Sample Input__

```
BANANA
```

__Sample Output__

```
Stuart 12
```

__Note:__

Vowels are only defined as ```AEIOU```. In this problem, ```Y``` is not considered a vowel.

---

<details><summary>Solution</summary>
    
```python
def minion_game(string):
    s = sum([len(string) - i for i, c in enumerate(string) if c not in 'AEIOU'])
    k = sum([len(string) - i for i, c in enumerate(string) if c in 'AEIOU'])

    if k > s:
        print(f"Kevin {k}")
    elif s > k:
        print(f"Stuart {s}")
    else:
        print(f"Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
```
</details>
