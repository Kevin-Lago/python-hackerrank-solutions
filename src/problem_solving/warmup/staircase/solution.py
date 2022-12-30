def staircase(n):
    [print(" " * (n - i) + "#" * i) for i in range(1, n + 1)]
    # for i in range(1, n + 1):
    #     print(" " * (n - i) + "#" * i)


if __name__ == '__main__':
    n = int(input())
    staircase(n)
