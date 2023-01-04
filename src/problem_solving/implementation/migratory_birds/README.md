| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Migratory Birds

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

__Example__

$arr = [1,1,2,2,3]$

There are two each of types $1$ and $2$, and one sighting of type $3$. Pick the lower of the two types seen twice: type $1$.

__Function Description__

Complete the migratory_birds function in the editor below.

migratory_birds has the following parameter(s):

- int[n] arr: the types of birds sighted

__Returns__

- int: the lowest type id of the most frequently sighted birds.

__Input Format__

The first line contains an integer, $n$, the size of $arr$.

The second line describes $arr$ as $n$ space-separated integers, each a type number of the bird sighted.

__Constraints__

- $5 \le n \le 2 x 10^{5}$

- It is guaranteed that each type is $1$, $2$, $3$, $4$, or $5$.

__Sample Input 0__

```
6
1 4 4 4 5 3
```

__Sample Output 0__

```
4
```

__Explanation 0__

The different types of birds occur in the following frequencies:

- Type $1$: $1$ bird

- Type $2$: $0$ birds

- Type $3$: $1$ bird

- Type $4$: $3$ birds

- Type $5$: $1$ bird

The type number that occurs at the highest frequency is type $4$, so we print $4$ as our answer.

__Sample Input 1__

```
11
1 2 3 4 5 4 3 2 1 3 4
```

__Sample Output 1__

```
3
```

__Explanation 1__

The different types of birds occur in the following frequencies:

- Type $1$: $2$ birds

- Type $2$: $2$ birds

- Type $3$: $3$ birds

- Type $4$: $3$ birds

- Type $5$: $1$ bird

Two types have a frequency of $3$, and the lower of those is type $3$.

---

<details><summary>Solution</summary>
    
```python
import collections


def migratory_birds(arr):
    counter = collections.Counter(arr)
    highest_value = max(counter.values())

    for i in range(1, 6):
        if counter[i] == highest_value:
            return i


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(migratory_birds(arr))
```
</details>
