def mini_max_sum(arr):
    minimum = list(arr)
    maximum = list(arr)

    minimum.remove(max(arr))
    maximum.remove(min(arr))

    print(sum(minimum), sum(maximum))


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    mini_max_sum(arr)
