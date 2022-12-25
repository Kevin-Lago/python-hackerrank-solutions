| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/introduction_to_sets)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/symmetric_difference)</img> |
|:---|:---:|---:|

# No Idea!

There is an array of ___n___ integers. There are also __2 disjoin sets__, ___a___ and ___b___, each containing ___m___ integers. You like all the integers in set ___a___ and dislike all the integers in set ___b___. You initial happiness is __0__. For each ___i___ integer in the array, if $i \in a$, you add __-1__ to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

__Note:__ Since ___a___ and ___b___ are sets, they have no repeated elements. However, the array might contain duplicate elements.

__Constraints__

$1 \le n \le 10^{5}$

$1 \le m \le 10^{5}$

$1 \le Any integer in the input \le 10^{9}$

__Input Format__

The first line contains integers ___n___ and ___m___ separated by a space.

The second line contains ___n___ integers, the elements of the array.

The third and fourth lines contain ___m___ integers, ___a___ and ___b___, respectively.

__Output Format__

Output a single integer, your total happiness.

__Sample Input__

```
3 2
1 5 3
3 1
5 7
```

__Sample Output__

```
1
```

__Explanation__

You gain __1__ unit of happiness for elements __3__ and __1__ in set ___a___. You lose __1__ unit for __5__ in set ___b___. The element __7__ in set ___b___ does not exist in the array so it is not included in the calculation.

Hence, the total happiness is __2 - 1 = 1__.

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    n, m = input().split(" ")
    arr = input().split(" ")

    a = set(input().split(" "))
    b = set(input().split(" "))

    happiness = 0

    for i in range(len(arr)):
        if (a.__contains__(arr[i])):
            happiness += 1

        if (b.__contains__(arr[i])):
            happiness -= 1

    print(happiness)
```
</details>