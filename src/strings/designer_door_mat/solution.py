def generate_mat(n, m):
    for y in range(n):
        for x in range(m):
            print()
            print("-"*m/2-7+"WELCOME"+"-"*m/2-7)


if __name__ == '__main__':
    n, m = int(input().split(" "))
    s = '-'

    print((s*int(m)).center(m))

    for y in range(int(n)):
        if (y == int(int(n) / 2) - 1):
            print("".join("-" for i in range(int((int(m) - 7) / 2)))+"WELCOME"+"".join("-" for i in range(int((int(m) - 7) / 2))))
        else:
            print()
    print(n, m)

