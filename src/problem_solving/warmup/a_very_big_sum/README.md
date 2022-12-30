| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# A Very Big Sum

In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

__Function Description__

Complete the a_very_big_sum function in the editor below. It must return the sum of all array elements.

a_very_big_sum has the following parameters(s):

- int[n] ar: an array of integers.

__Return__

- long: the sum of all array elements

__Input Format__

The first line of the input consists of an integer $n$.

The next line contains $n$ space-separated integers contained in the array.

__Output Format__

Return the integer sum of the elements in the array.

__Constraints__

- $1 \le n \le 10$

- $0 \le ar[i] \le 10^{10}$

__Sample Input__

```
5
1000000001 1000000002 1000000003 1000000004 1000000005
```

__Sample Output__

```
5000000015
```

__Note:__

The range of the 32-bit integer is $(-2^{31})$ to $(2^{31} - 1)$ or $[-2147483648, 2147483647]$.

When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.

---

<details><summary>Solution</summary>
    
```python
import os


def a_very_big_sum(ar):
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = a_very_big_sum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
```
</details>
