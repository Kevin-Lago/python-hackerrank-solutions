from math import sqrt, atan2
import re

if __name__ == '__main__':
    z = input()
    x = int(re.match(r"^-?\d+", z).group())
    y = int(re.split(r"^-?\d+", z)[1][:-1])

    print(sqrt(x**2 + y**2))
    print(atan2(y, x))
