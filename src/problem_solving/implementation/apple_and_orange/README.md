| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Apple and Orange

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:

- The red region denotes the house, where $s$ is the start point, and $t$ is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.

- Assume the trees are located on a single point, where the apple tree is a point $a$, and the orange tree is at point $b$.

- When a fruit falls from its tree, it lands $d$ units of distance from its tree of origin along the $x$-axis. *A negative value of $d$ means the fruit fell $d$ units to the tree's left, and a positive value of $d$ means it falls $d$ units to the tree's right.*

![HackerrankAppleandOrangeDiagram](1.png)

Given the value of $d$ for $m$ apples and $n$ oranges, determine how many apples and oranges will fall on Sam's house (i.e, in the inclusive range $[s, t]$)?

For example, Sam's house is between $s = 7$ and $t = 10$. The apple tree is located at $a = 4$ and the orange at $b = 12$. There are $m = 3$ apples and $n = 3$ oranges. Apples are thrown $apples = [2, 3, -4]$ units distance from $a$, and $oranges = [3, -2, -4]$ units distance. Adding each apple distance to the position of the tree, they land as $[4 + 2, 4 + 3, 4 + -4] = [6, 7, 0]$. Oranges land at $[12 + 3, 12 + -2, 12 + -4] = [15, 10, 8]$. One apple and two oranges land in the inclusive range $7$ to $10$ so we print

```
1
2
```

__Function Description__

Complete the count_apples_and_oranges function in the editor below. It should print then number of apples and oranges that land on Sam's house, each on a separate line.

count_apples_and_oranges has the following parameter(s):

- s: integer, starting point of Sam's house location.

- t: integer, ending location of Sam's house location.

- a: integer, location of the Apple tree.

- b: integer, location of the Orange tree.

- apples: integer array, distances at which each apple falls from the tree.

- oranges: integer array, distances at which each orange falls from the tree.

__Input Format__

The first line contains two space-separated integers denoting the respective values of $s$ and $t$.

The second line contains two space-separated integer denoting the respective values of $a$ and $b$.

The third line contains two space-separated integers denoting the respective values of $m$ and $n$.

The fourth line contains, $m$, space-separated denoting the respective distances that each apple falls from point $a$.

The fifth line contains $n$ space-separated itneger denoting the respective distances that each orange falls from point $b$.

__Constraints__

- $1 \le s, t, a, b, m, n \le 10^{5}$

- $-10^{5} \le d \le  10^{5}$

- $a < s < t < b$

__Output Format__

Print two integers on two different lines:

1. The first integer: the number of apples that fall on Sam's house.

2. The second integer: the number of oranges that fall on Sam's house.

__Sample Input__

```
7 11
5 15
3 2
-2 2 1
5 -6
```

__Sample Output__

```
1
1
```

__Explanation__

The first apple falls at position $5 - 2 = 3$.

The second apple falls at position $5 + 2 = 7$.

The third apple falls at position $5 + 1 = 6$.

The first orange falls at position $15 + 5 = 20$.

The second orange falls at position $15 - 6 = 9$.

Only one fruit (the second apple) falls within the region between $7$ and $11$, so we print $1$ as our first line of output.

Only the second orange falls within the region between $7$ and $11$, so we print $1$ as our second line of output.

---

<details><summary>Solution</summary>
    
```python
def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples = sum([1 if s <= point + a <= t else 0 for point in apples])
    oranges = sum([1 if s <= point + b <= t else 0 for point in oranges])
    print(apples, oranges, sep='\n')


if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())

    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    count_apples_and_oranges(s, t, a, b, apples, oranges)
```
</details>
