| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/strings/string_validators)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/strings/text_wrap)</img> |
|:---|:---:|---:|

# Text Alignment

In Python, a string of text can be aligned left, right and center.

__.ljust(width)__

This method returns a left aligned string of length width.

```python
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
```
---

__.center(width)__

This method returns a centered string of length width.

```python
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
```

__.rjust(width)__

This method returns a right aligned string of length width.

```python
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
```
---

__Task__

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.

Your task is to replace the blank (```______```) with rjust, ljust or center.

__Input Format__

A single line containing the thickness value for the logo.

__Constraints__

The thickness must be an odd number.

__0 < _thickness_ < 50

__Sample Input__

```
5
```

__Sample Output__

```
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
```

---

<details><summary>Solution</summary>
    
```python
if __name__ == '__main__':
    thickness = int(input()) #This must be an odd number
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
```
</details>
