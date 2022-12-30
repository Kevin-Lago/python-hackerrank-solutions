def a_very_big_sum(ar):
    return sum(ar)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))

    result = a_very_big_sum(ar)
    print(result)
