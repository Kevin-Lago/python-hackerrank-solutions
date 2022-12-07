# Arithmetic Operators

__Task__

The provided code stub reads two integers from STDIN, ___a___ and ___b___. Add code to print three lines where:

1. The first line contains the sum of the two numbers.

2. The second line contains the difference of the two numbers (first - second)

3. The third line contains the product of the two numbers.

__Example__

___a_ = 3__

___b_ = 5__

Print the following:

```
8
-2
15
```

__Input Format__

The first line contains the first integer, ___a___.

The second line contains the second integer, ___b___.

__Constraints__

__1 <= _a_ <= 10<sup>10</sup>__

__1 <= _b_ <= 10<sup>10</sup>__

__Output Format__

Print the three lines as explained above.

__Sample Input 0__

```
3
2
```

__Sample Output 0__

```
5
1
6
```

__Explanation__

__3 + 2 = 5__

__3 - 1 = 1__

__3 * 2 = 6__

---

<details><summary>Solution</summary>
    
```python
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
    
        print(a + b)
        print(a - b)
        print(a * b)
```
</details>
