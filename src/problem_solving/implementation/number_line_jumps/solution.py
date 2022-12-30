def kangaroo(x1, v1, x2, v2):
    return "YES" if v1 > v2 and (x2 - x1) % (v1 - v2) == 0 else "NO"


if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())
    print(kangaroo(x1, v1, x2, v2))
