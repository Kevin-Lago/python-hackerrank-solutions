from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = defaultdict(list)

    for i in range(n):
        w = input()
        a[w].append(i)

    for i in range(m):
        w = input()
        if a[w]:
            print(" ".join([str(i + 1) for i in a[w]]))
        else:
            print("-1")
