if __name__ == '__main__':
    m = input()
    a = set(input().split(" "))

    n = input()
    b = set(input().split(" "))

    arr = list(map(int, a.difference(b))) + list(map(int, b.difference(a)))
    arr.sort()

    for i in range(len(arr)):
        print(arr[i])
