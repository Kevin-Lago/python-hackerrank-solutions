if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    q = int(input())

    for i in range(q):
        query = input()

        if (query.__contains__("pop")):
            s.pop()
            continue

        if (query.__contains__("remove")):
            s.remove(int(query.split(" ")[1]))
            continue

        if (query.__contains__("discard")):
            s.discard(int(query.split(" ")[1]))
            continue

    print(sum(s))
