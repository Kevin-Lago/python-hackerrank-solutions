| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# collections.Counter()

### [collections.Counter()](https://docs.python.org/2/library/collections.html#collections.Counter)

A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

__Sample Code__

```python
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
```

---

__Task__

___Raghu___ is a shoe owner. His ship has ___x___ number of shoes.

He has a list containing the size of each shoe he has in his shop.

There are ___n___ number of customer who are willing to pay ___x<sub>i</sub>___ amount of money only if they get the shoe of their desired size.

Your task is to compute how much money __Raghu___ earned.

__Input Format__

The first line contains ___x___, the number of shoes.

The second line contains the space separated list of all the shoe sizes in the shop.

The third line contains ___n___, the number of customers.

The next ___n___ lines contain the space separated values of the ___shoe size___ desired by the customer and ___x<sub>i</sub>___, the price of the shoe.

__Constraints__

$0 < x < 10^3$

$0 < n \le 10^3$

$20 < x_{i} < 100$

$2 < shoe size < 20$

__Output Format))

Print the amount of money earned by ___Raghu___.

__Sample Input__

```
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
```

__Sample Output__

```
200
```

__Explanation__

__Customer 1__: Purchased size 6 shoe for __$55__.

__Customer 2__: Purchased size 6 shoe for __$45__.

__Customer 3__: Size 6 no longer available, so no purchase.

__Customer 4__: Purchased size 4 shoe for __$40__.

__Customer 5__: Purchased size 18 shoe for __$60__.

__Customer 6__: Size 10 not available, so no purchased.

Total money earned = __55 + 45 + 40 + 60 = $200__

---

<details><summary>Solution</summary>
    
```python
import collections

if __name__ == '__main__':
    x = int(input())
    a = list(map(int, input().split()))

    n = int(input())
    c = collections.Counter(a)
    total = 0

    for i in range(n):
        shoe_size, price = map(int, input().split())

        if (c[shoe_size] > 0):
            c[shoe_size] -= 1
            total += price

    print(total)
```
</details>