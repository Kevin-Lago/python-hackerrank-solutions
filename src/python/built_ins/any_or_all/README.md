| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/built_ins/athlete_sort)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/built_ins/ginorts)</img> |
|:---|:---:|---:|

# Any or All

[any()]()

This expression returns ```True``` if __any__ element of the iterable is true.

If the iterable is empty, it will return ```False```.

__Code__

```python
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False
```

[all()]()

This expression returns ```True``` if __all__ of the elements of the iterable are true. If the iterable is empty, it will return ```True```.

__Code__

```python
>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
```

---

__Task__

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a [palindromic integer]().

__Input Format__

The first line contains an integer $n$. $n$ is the total number of integers in the list.

The second line contains the space separated list of $n$ integers.

__Constraints__

$0 < n < 100$

__Output Format__

Print ```True``` if all the conditions of the problem statement are satisfied. Otherwise, print ```False```.

__Sample Input__

```
5
12 9 61 5 14 
```

__Sample Output__

```
True
```

__Explanation__

__Condition 1:__ All the integers in the list are positive.

__Condition 2:__ 5 is a palindromic integer.

Hence, the output is ```True```.

Can you solve this challenge in ```3 lines of code or less```?

There is ```no penalty``` for solutions that are correct but have more than 3 lines.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n = int(input())
    a = list(input().split())
    print(all([int(i) > 0 for i in a]) and any([i == i[::-1] for i in a]))
```
</details>
