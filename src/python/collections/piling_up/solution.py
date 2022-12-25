from collections import deque

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        d = deque(map(int, input().split()))
        can_stack = True
        top = 0

        if d[0] > d[-1]:
            top = d[0]
            d.popleft()
        else:
            top = d[-1]
            d.pop()

        while d:
            if d[0] >= d[-1] <= top:
                top = d[0]
                d.popleft()
            elif d[0] < d[-1] <= top:
                top = d[-1]
                d.pop()
            else:
                can_stack = False
                break

        print("Yes" if can_stack else "No")
