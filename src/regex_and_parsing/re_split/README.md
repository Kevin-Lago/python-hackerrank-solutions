| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Re.split()

You are given a string $s$ consisting only of digits ```0-9```, commas ```,```, and dots ```.```.

Your task is to complete the ```regex_pattern``` defined below, which will be used to re.split() all of the ```,``` and ```.``` symbols in $s$.

It's guaranteed that every comma and every dot in $s$ is proceeded and followed by a digit..

__Sample Input__

```
100,000,000.000
```

__Sample Output__

```
100
000
000
000
```

---

<details><summary>Solution</summary>
    
```python
regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, input())))
```
</details>
