def simple_array_sum(ar):
    return sum(ar)


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(simple_array_sum(ar))
