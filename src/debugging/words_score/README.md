| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/numpy/linear_algebra)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/debugging/default_arguments)</img> |
|:---|:---:|---:|

# Words Score

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

---

Consider that vowels in the alphabet are ```a, e, i, o, u``` and ```y```.

Function ```score_words``` takes a list of lowercase words as an argument and returns a score as follows:

The score of a single word is __2__ if the word contains an even number of vowels. Otherwise, the score of this word is __1__. The score for the whole list of words is the sum of scores of all words in the list.

Debug the given function ```score_words``` such that it returns a correct score.

Your function will be tested on several cases by the locked template code.

__Input Format__

The input is read by the provided locked code template. In the first line, there is a single integer ___n___ denoting the number of words. In the second line, there are ___n___ space-separated lowercase words.

__Constraints__

- $1 \le n \le 20$

- Each word has at most __20__ letters and all letters are English lowercase letters.

__Output Format__

The output is produced by the provided and locked code template. It calls function ```score_words``` with the list of words read from the input as teh argument and prints the returned score to the output.

__Sample Input 0__

```
2
hacker book
```

__Sample Output 0__

```
4
```

__Explanation 0__

There are two words in the input: ```hacker``` and ```book```. The score of the word ```hacker``` is __2__ because it contains an even number of vowels, i.e. __2__ vowels, and the score of ```book``` is __2__ for the same reason. Thus the total score is __2 + 2 = 4__.

__Sample Input 1__

```
3
programming is awesome
```

__Sample Output 1__

```
4
```

__Explanation 1__

There are __3__ words in the input: ```programming```, ```is``` and ```awesome```. The score of ```programming``` is __1__ since it contains __3__ vowels, an odd number of vowels. The score of ```is``` is also __1__ because it has an odd number of vowels. The score of ```awesome``` is __2__ since it contains __4__ vowels, an even number of vowels. Thus, the total score is __1 + 1 + 2 = 4__.

---

<details><summary>Solution</summary>
    
```python
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


if __name__ == '__main__':
    n = int(input())
    words = input().split()
    print(score_words(words))
```
</details>