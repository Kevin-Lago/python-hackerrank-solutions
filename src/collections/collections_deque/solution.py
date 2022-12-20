from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()
    q = [input().split() for i in range(n)]

    # commands = {
    #     'appendleft': lambda e: d.appendleft(e),
    #     'append': lambda e: d.append(e),
    #     'popleft': lambda e: d.popleft(),
    #     'pop': lambda i: d.pop()
    # }
    #
    # for i in q:
    #     commands[i[0]](i[1])

    for c in q:
        if 'appendleft' in c:
            d.appendleft(c[1])
            continue

        if 'append' in c:
            d.append(c[1])
            continue

        if 'popleft' in c:
            d.popleft()
            continue

        if 'pop' in c:
            d.pop()
            continue

    [print(e, end=" ") for e in d]
