def compare_triplets(a, b):
    return [
        sum([1 if a[i] > b[i] else 0 for i in range(3)]),
        sum([1 if a[i] < b[i] else 0 for i in range(3)])
    ]


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(compare_triplets(a, b))
