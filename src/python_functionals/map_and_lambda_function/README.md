| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Map and Lambda Function

Let's learn some new Python concepts! You have to generate a list of the first $n$ fibonacci numbers, $0$ being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

__Concept__

The ```map()``` function applies a function to every member of an iterable and returns the result. It take two parameters: first, the function that is to be applied and secondly, the iterabels.

Let's say you are given a list of names, and you have to print a list that contains the length of each name.

```python
>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  
```

Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

```python
>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
```

__Note:__

Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.

__Input Format__

One line of input: an integer $n$.

__Constraints__

$0 \le n \le 15$

__Output Format__

A list on a single line containing the cubes of the first $n$ fibonacci numbers.

__Sample Input__

```
5
```

__Sample Output__

```
[0, 1, 1, 8, 27]
```

__Explanation__

The first $5$ fibonacci numbers are $[0,1,1,2,3]$, and their cubes are $[0,1,1,8,27]$.

---

<details><summary>Solution</summary>
    
```python

```
</details>
