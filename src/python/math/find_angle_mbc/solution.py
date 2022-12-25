import math

if __name__ == '__main__':
    c, a = int(input()), int(input())
    b = math.hypot(a, c)

    print(f"{round(math.degrees(math.atan(c / a)))}\N{DEGREE SIGN}")
