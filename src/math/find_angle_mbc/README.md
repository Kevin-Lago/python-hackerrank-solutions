| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/)</img> |
|:---|:---:|---:|

# Find Angle MBC

![HackerrankFindAngleMBCDiagram](1.png)

$abc$ is a right triangle, $90^{\circ}$ at $b$.

Therefore, $\measuredangle mbc = 90^{\circ}$.

Point $m$ is the midpoint of hypotenuse $ac$.

You are given the lengths $ab$ and $bc$.

Your task is to find $\measuredangle mbc$ (angle $\theta^{\circ}$, as shown in the figure) in degrees.

__Input Format__

The first line contains the length of side $ab$.

The second line contains the length of side $bc$.

__Constraints__

- $0 < ab \le 100$

- $0 < bc \le 100$

- Lengths $ab$ and $bc$ are natural numbers.

__Output Format__

Output $\measuredangle mbc$ in degrees.

__Note:__ Round the angle to the nearest integer.

__Examples__

if angle is 56.5000001°, then output $57^{\circ}$

If angle is 56.5000000°, then output $57^{\circ}$.

If angle is 56.4999999°, then output $57^{\circ}$.

$0^{\circ} < \theta^{\circ} < 90^{\circ}$

__Sample Input__

```
10
10
```

__Sample Output__

```
45°
```

---

<details><summary>Solution</summary>
    
```python
import math

if __name__ == '__main__':
    c, a = int(input()), int(input())
    b = math.hypot(a, c)

    print(f"{round(math.degrees(math.atan(c / a)))}\N{DEGREE SIGN}")
```
</details>
