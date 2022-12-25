| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/xml/xml2_find_the_maximum_depth)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/closures_and_decorators/decorators_2_name_directory)</img> |
|:---|:---:|---:|

# Standardize Mobile Number Using Decorators

Let's dive into decorators! You are given ___n___ mobile numbers. Sort them in ascending order then print them in the standard format shown below:

```
+91 xxxxx xxxxx
```

The given mobile numbers may have __+91__, __91__ or __0__ written before the actual __10__ digit number. Alternatively, there may not be any prefix at all.

__Input Format__

The first line of input contains an integer ___n___, the number of mobile phone numbers.

___n___ lines follow each containing a mobile number.

__Output Format__

Print ___n___ mobile numbers on separate lines in the required format.

__Sample Input__

```
3
07895462130
919875641230
9195969878
```

__Sample Output__

```
+91 78954 62130
+91 91959 69878
+91 98756 41230
```

__Concept__

Like most other programming languages, Python has the concept of closures. Extending these closures give us decorators, which are an invaluable asset. You can learn about decorator in 12 easy steps [here](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/).

To solve the above question, make a list of mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.

---

<details><summary>Solution</summary>
    
```python
def wrapper(f):
    def fun(l):
        return f([
            f"+91 {n[3:8]} {n[8:]}" if len(n) == 13 else
            f"+91 {n[2:7]} {n[7:]}" if len(n) == 12 else
            f"+91 {n[1:6]} {n[6:]}" if len(n) == 11 else
            f"+91 {n[0:5]} {n[5:10]}" for n in l])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
```
</details>