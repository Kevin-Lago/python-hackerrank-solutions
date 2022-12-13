import itertools

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    [print(t, end=" ") for t in list(itertools.product(a, b))]
