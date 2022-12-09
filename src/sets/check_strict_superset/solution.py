if __name__ == '__main__':
    a = set(map(int, input().split()))
    n = int(input())
    issupersetofall = True

    for i in range(n):
        s = set(map(int, input().split()))

        if not a.issuperset(s):
            issupersetofall = False
            break

    print(issupersetofall)
