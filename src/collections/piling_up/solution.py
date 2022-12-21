if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        for i in range(len(b)):
            for j in range(i, len(b)):
                if b[j] < b[i]:
                    print("No")
                    break

        print("Yes")
