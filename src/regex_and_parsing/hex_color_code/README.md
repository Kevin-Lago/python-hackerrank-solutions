| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Hex Color Code

CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green and Blue color values (RGB).

Specifications of HEX Color Code

- It must start with a '#' symbol.

- It can have $3$ or $6$ digits.

- Each digit is in the range of $0$ to $f$. ($1,2,3,4,5,6,7,8,9,0,A,B,C,D,E$ and $F$).

- $A-F$ letters can be lower case. ($a,b,c,d,e$ and $f$ are also valid digits).

__Examples__

```
Valid Hex Color Codes
#FFF 
#025 
#F0A1FB 

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
```

You are given $n$ lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

```
Selector
{
	Property: Value;
}
```

__Input Format__

The first line contains $n$, the number of code lines.

The next $n$ lines contains CSS Codes.

__Constraints__

$0 < n < 50$

__Output Format__

Output the color codes with '#' symbols on separate lines.

__Sample Input__

```
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
```

__Sample Output__

```
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
```

__Explanation__

\#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.

Hence, the valid color codes are:

\#FfFdF8

\#aef

\#f9f9f9

\#fff

\#ABC

\#fff

__Note:__ There are no comments (// or /* */) in CSS Code.

---

<details><summary>Solution</summary>
    
```python
import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        line = input()
        matches = re.findall(r"(?<!^)#{1}[0-9a-fA-F]{3,6}", line)

        for match in matches:
            print(match)
```
</details>
