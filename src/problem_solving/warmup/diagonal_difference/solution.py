def diagonal_difference(arr):
    length = len(arr)

    return abs(
        sum([arr[i][i] for i in range(length)]) -
        sum([arr[i][length - i - 1] for i in range(length)])
    )


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    print(diagonal_difference(arr))
