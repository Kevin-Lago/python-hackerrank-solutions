| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/validating_credit_card_numbers)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/matrix_script)</img> |
|:---|:---:|---:|

# Validating Postal Codes

A valid postal code $p$ have to fulfill both below requirements:

1. $p$ must be a number in the range from $100000$ to $999999$ inclusive.

2. $p$ must not contain more tha one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

```
121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
```

Your task is to provide two regular expressions ```regex_integer_in_range``` and ```regex_alternating_repetitive_digit_pair```. Where:

```regex_integer_in_range``` should match only integers range from $100000$ to $999999$ inclusive

```regex_alertnating_repetitive_digit_pair``` should find alternating repetitive digits pairs in a given string.

Both these regular expressions will be used by the provided code template to check if the input string $p$ is a valid postal code using the following expression:

```python
(bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
```

__Input Format__

Locked stub code in the editor reads a single string denoting $p$ from stdin and uses provided expression and your regular expressions to validate if $p$ is a valid postal code.

__Output Format__

You are not responsible for printing anything to stdout. Locked stub code in the editor does that.

__Sample Input__

```
110000
```

__Sample Output__

```
False
```

__Explanation__

110$0$0$0$ : (0, 0) and (0, 0) are two alternating digit pairs. Hence, it is an invalid postal code.

__Note:__

A score of $0$ will be awarded for using '```if```' conditions in your code.

You have to pass all the test cases to get a positive score.

---

<details><summary>Solution</summary>
    
```python
regex_integer_in_range = r"^[1-9][0-9][0-9][0-9][0-9][0-9]$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re

if __name__ == '__main__':
    P = input()
    print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
```
</details>
