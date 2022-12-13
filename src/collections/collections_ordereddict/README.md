| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the key that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

__Example Code__

```python
>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
```

---

__Task__

You are the manager of a supermarket.

You have a list of ___n___ items together with their prices that consumers bought on a particular day.

Your task is to print each ```item_name``` and ```net_price``` in order of its first occurrence.

- ```item_name``` = Name of the item.

- ```net_price``` = Quantity of the item sold multiplied by the price of each item.

__Input Format__

The first line contains the number of items, ___n___.

The next ___n___ lines contains the item's name and price, separated by a space.

__Constraints__

$0 < n \le 100$

__Output Format__

Print the ```item_name``` and ```net_price``` in order of its first occurrence.

__Sample Input__

```
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
```

__Sample Output__

```
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
```

__Explanation__

BANANA FRIES: Quantity bought: __1__, Price: __12__

Net Price: __12__

POTATO CHIPS: Quantity bought: __2__, Price: __30__

Net Price: __60__

APPLE JUICE: Quantity bought __2__, Price: __10__

Net Price: __20__

CANDY: Quantity bought: __4__, Price: __5__

Net Price: __20__

---

<details><summary>Solution</summary>
    
```python

```
</details>