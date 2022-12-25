import collections

if __name__ == '__main__':
    x = int(input())
    a = list(map(int, input().split()))

    n = int(input())
    c = collections.Counter(a)
    total = 0

    for i in range(n):
        shoe_size, price = map(int, input().split())

        if (c[shoe_size] > 0):
            c[shoe_size] -= 1
            total += price

    print(total)
