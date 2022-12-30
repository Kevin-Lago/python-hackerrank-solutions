| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Compare the Triplets

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding point on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triple b = (b[0], b[1], b[2]).

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1] and a[2] with b[2].

- If a[i] > b[i], then Alice is awarded 1 point.

- If a[i] < b[i], then Bob is awarded 1 point.

- If a[i] = b[i], then neither person receives a point.

Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

__Example__

a = [1, 2, 3]

b = [3, 2, 1]

- For elements a[0] and b[0], Bob is awarded a point because a[0] < b[0].

- For the equal elements a[1] and b[1], no points are earned.

- Finally, for elements a[2] and b[2], a[2] > b[2] so Alice receives a point.

The return array is [1, 1] with Alice's score first and Bob's second.

__Function Description__

Complete the function compare_triplets in the editor below.

compare_triplets has the following parameter(s):

- int[3] a: Alice's challenge rating

- int[3] b: Bob's challenge rating

__Return__

- int[2]: Alice's score is in the first position, and Bob's score is in the second.

__Input Format__

The first line contains 3 space-separated integers, a[0], a[1] and a[2], the respective values in triplet a.

The second line contains 3 space-separated integers, b[0], b[1] and b[2], the respective values in triplet b.

__Constraints__

- $1 \le a[i] \le 100$

- $1 \le b[i] \le 100$

__Sample Input 0__

```
5 6 7
3 6 10
```

__Sample Output 0__

```
1 1
```

__Explanation 0__

In this example:

- $a = (a[0], a[1], a[2]) = (5, 6, 7)$

- $b = (b[0], b[1], b[2]) = (3, 6, 10)$

Now, let's compare each individual score:

- $a[0] > b[0]$, so Alice receives $1$ point.

- $a[1] = b[1]$, so nobody receives a point.

- $a[2] < b[2]$, so Bob receives $1$ point.

Alice's comparison score is $1$, and Bob's comparison score is $1$. Thus, we return the array $[1, 1]$.

__Sample Input 1__

```
17 28 30
99 16 8
```

__Sample Output 1__

```
2 1
```

__Explanation 1__

Comparing the $0^{th}$ elements, $17 < 99$ so Bob receives a point.

Comparing the $1^{st}$ and $2^{nd}$ elements, $28 > 16$ and $30 > 8$ so Alice receives two points.

The return array is $[1, 2]$.

---

<details><summary>Solution</summary>
    
```python
import os


def compare_triplets(a, b):
    return [
        sum([1 if a[i] > b[i] else 0 for i in range(3)]), 
        sum([1 if a[i] < b[i] else 0 for i in range(3)])
    ]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
```
</details>
