| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Validating Credit Card Numbers

You and Fredrick are good friends. Yesterday, Fredrick received $n$ credit cards from $ABCD Bank$. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from $ABCD Bank$ has the following characteristics:

- It must start with a $4, 5$ or $6$.

- It must contain exactly $16$ digits.

- It must only consist of digits ($0-9$)

- It may have digits in groups of $4$, separated by one hyphen $"-"$.

- It must __NOT__ use any other separator like ``` ```, ```_```, ect.

- It must __NOT__ have $4$ or more consecutive repeated digits.

__Examples:__

__Valid Credit Card Numbers__

```
4253625879615786
4424424424442444
5122-2368-7954-3214
```

__Invalid Credit Card Numbers__

```
42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
```

__Input Format__

The first line of input contains an integer $n$.

The next $n$ lines contain credit card numbers.

__Constraints__

$0 < n < 100$

__Output Format__

Print ```Valid``` if the credit card number is valid. Otherwise, print ```Invalid```. Do not print the quotes.

__Sample Input__

```
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
```

__Sample Output__

```
Valid
Valid
Invalid
Valid
Invalid
Invalid
```

__Explanation__

4123456789123456 : $Valid$

5123-4567-8912-3456 : $Valid$

61234-567-8912-3456 : $Invalid$, because the card number is not divided into equal groups of $4$.

4123356789123456 : $Valid$

5133-3367-8912-3456 : $Invalid$, consecutive digits $3333$ is repeating $4$ times.

5123 - 3567 - 8912 - 3456 : $Invalid$, because space ``` ``` and ```-``` are used as separators

---

<details><summary>Solution</summary>
    
```python

```
</details>
