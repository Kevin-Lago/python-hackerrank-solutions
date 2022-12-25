| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/regex_and_parsing/validating_postal_codes)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/xml/xml_1_find_the_score)</img> |
|:---|:---:|---:|

# Matrix Script

Neo has a complex matrix script. The matrix script is a $n x m$ grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

![HackerrankMatrixScript](1.png)

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space ``` ``` for better readability.

Neo feels that there is no need to user '```if```' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z and 0-9]

__Input Format__

The first line contains space-separated integers $n$ (rows) and $m$ (columns) respectively.

The next $n$ lines contain the row elements of the matrix script.

__Constraints__

$0 < n, m < 100$

__Note:__ A $0$ score will be awarded for using '```if```' conditions in your code.

__Output Format__

Print the decoded matrix script.

__Sample Input__

```
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
```

__Sample Output__

```
This is Matrix#  %!
```

__Explanation__

The decoded script is:

```
This$#is% Matrix#  %!
```

Neo replaces the symbols or spaces between two alphanumeric characters with a single space ``` ``` for better readability.

So, the final decoded script is:

```
This is Matrix#  %!
```

---

<details><summary>Solution</summary>
    
```python
import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

message = "".join([s[i:i+1] for i in range(m) for s in matrix])
print(re.sub(r"(?<=\w)([!@#$%& ]{1,})(?=\w)", " ", message))
```
</details>
