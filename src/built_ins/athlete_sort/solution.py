if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    k = int(input())
    a.sort(key=lambda e: e[k])

    for i in range(len(a)):
        [print(j, end=" ") for j in a[i]]
        print()
