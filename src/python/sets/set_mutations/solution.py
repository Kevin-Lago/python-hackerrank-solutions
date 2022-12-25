if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))

    m = int(input())

    for i in range(m):
        q, x = input().split()
        s = set(map(int, input().split()))

        if q == "intersection_update":
            a.intersection_update(s)
            continue

        if q == "update":
            a.update(s)
            continue

        if q == "symmetric_difference_update":
            a.symmetric_difference_update(s)
            continue

        if q == "difference_update":
            a.difference_update(s)
            continue

    print(sum(a))
