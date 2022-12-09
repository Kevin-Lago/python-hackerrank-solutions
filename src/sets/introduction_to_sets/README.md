| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Introduction to Sets

A set is an unordered collection of elements without duplicate entries.

When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

__Example__

```python
>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
```

Basically, sets are used for membership testing and eliminating duplicate entries.

__Task__

Now, lets use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, he asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

___Average___ = ___Sum of Distinct Heights___ / ___Total Number of Distinct Heights___

__Function Description__

Complete the average function in the editor below.

average has the following parameters:

- int arr: an array of integers

__Returns__

- float: the resulting float value rounded to 3 places after the decimal.

__Input Format__

The first line contains the integer, ___n___, the size of ___arr___

The second line contains the ___n___ space-separated integers, ___arr[i]___

__Constraints__

__0 < _n_ <= 100__

__Sample Input__

```
STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
```

__Sample Output__

```
169.375
```

__Explanation__

Here, set(__[154,161,167,170,171,174,176,182]__) is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.

___Average_ = 1355 / 8 = 169.375__

---

<details><summary>Solution</summary>
    
```python
def average(array):
    return sum(set(array)) / len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
```
</details>
