if __name__ == '__main__':
    n, m = input().split(" ")
    arr = input().split(" ")

    a = set(input().split(" "))
    b = set(input().split(" "))

    happiness = 0

    for i in range(len(arr)):
        if (a.__contains__(arr[i])):
            happiness += 1

        if (b.__contains__(arr[i])):
            happiness -= 1

    print(happiness)

