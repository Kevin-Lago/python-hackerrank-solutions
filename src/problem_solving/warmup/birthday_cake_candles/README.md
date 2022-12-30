| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Birthday Cake Candles

You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

__Example__

$candles = [4, 4, 1, 3]$

The maximum height candles are $4$ units high. There are $2$ of them, so return $2$.

__Function Description__

Complete the function birthday_cake_candles in the editor below.

birthday_cake_candles has the following parameter(s):

- int[n] candles: the candle heights

__Returns__

- int: the number of candles that are tallest

__Input Format__

The first lien contains a single integer, $n$, the size of $candles[]$.

The second line contains $n$ space-separated integers, where each integer $i$ describes the height of $candles[i]$.

__Constraints__

- $1 \le n \le 10^{5}$

- $1 \le candles[i] \le 10^{7}$

__Sample Input__

```
4
3 2 1 3
```

__Sample Output__

```
2
```

__Explanation__

Candle heights are $[3, 2, 1, 3]$. The tallest candles are $3$ units, and there are $2$ of them.

---

<details><summary>Solution</summary>
    
```python
def birthday_cake_candles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    n = int(input())
    candles = list(map(int, input().split()))
    print(birthday_cake_candles(candles))
```
</details>
