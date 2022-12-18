| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Regex Substitution

The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).

The method is called for all matches and can be used to modify strings in different wats.

The re.sub() method returns the modified string as an output.

Learn more about [re.sub()]().

__Transformation of Strings__

```python
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
```

__Output__

```
1 4 9 16 25 36 49 64 81
```

__Replacement in Strings__

```python
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment
```

__Output__

```
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
```

---

__Task__

You are given a text of $n$ lines. the text contains ```&&``` and ```||``` symbols.

Your task is to modify those symbols to the following:

```
&& -> and
|| -> or
```

Both ```&&``` and ```||``` should have a space " " on both sides.

__Input Format__

The first line contains the integer, $n$.

The next $n$ lines each contains a line of the text.

__Constraints__

$0 < n < 100$

Neither ```&&``` nor ```||``` occur in the start or end of each line.

__Output Format__

output the modified text

__Sample Input__

```
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
```

__Sample Output__

```
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.    
```

---

<details><summary>Solution</summary>
    
```python
import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        s = input()

        s = re.sub("(?<=\\s)(&&)(?=\\s)", "and", s)
        s = re.sub("(?<=\\s)(\\|\\|)(?=\\s)", "or", s)

        print(s)
```
</details>
