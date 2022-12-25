if __name__ == '__main__':
    a, b, m = int(input()), int(input()), int(input())

    print(a ** b)
    print(a ** b % m)

    print(pow(a, b))
    print(pow(a, b, m))
