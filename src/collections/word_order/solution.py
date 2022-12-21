from collections import Counter

if __name__ == '__main__':
    n = int(input())
    c = Counter([input() for i in range(n)])

    print(len(c))
    [print(c[k], end=" ") for k in c]
