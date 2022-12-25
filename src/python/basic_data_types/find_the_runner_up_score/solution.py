if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())

    max_value = max(arr)
    arr = list(filter(lambda e: e != max_value, arr))

    print(max(arr))
