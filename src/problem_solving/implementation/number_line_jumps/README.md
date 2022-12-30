| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Number Line Jumps

You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready ot jump in the positive direction (i.e., toward positive infinity).

- The first kangaroo starts at location $x1$ and moves at a rate of $v1$ meters per jump.

- The second kangaroo starts at location $x2$ and moves at a rate of $v2$ meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return ```YES```, otherwise return ```NO```.

__Example__

$x1 = 2$

$v1 = 1$

$x2 = 1$

$v2 = 2$

After one jump, they are both at $x = 3$, $(x1 + v1 = 2 + 1, x2 + v2 = 1 + 2)$, so the answer is ```YES```.

__Function Description__

Complete the function kangaroo in the editor below.

kangaroo has the following parameter(s):

- int x1, int v1: starting position and jump distance for kangaroo 1

- int x2, int v2: starting position and jump distance for kangaroo 2

__Returns__

- string: either ```YES``` or ```NO```

__Input Format__

A single line of four space-separated integers denoting the respective values of $x1, v1, x2,$ and $v2$.

__Constraints__

- $0 \le x1 < x2 \le 10000$

- $1 \le v1 \le 10000$

- $1 \le v2 \le 10000$

__Sample Input 0__

```
0 3 4 2
```

__Sample Output 0__

```
YES
```

__Explanation 0__

The two kangaroos jump through the following sequence of locations:

![HackerrankKangarooDiagram](1.png)

From the image, it is clear that the kangaroos meet at the same location (number $12$ on the number line) after same number of jumps ($4$ jumps), and we print ```YES```.

__Sample Input 1__

```
0 2 5 3
```

__Sample Output 1__

```
NO
```

__Explanation 1__

The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e., $x_{2} > x_{1}$). Because the second kangaroo moves at a faster rate (meaning $v_{2} > v_{1}$) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up. This, we print ```NO```.

---

<details><summary>Solution</summary>
    
```python
def kangaroo(x1, v1, x2, v2):
    return "YES" if v1 > v2 and (x2 - x1) % (v1 - v2) == 0 else "NO"


if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())
    print(kangaroo(x1, v1, x2, v2))
```
</details>
