def plus_minus(arr):
    positives, negatives, zeros, length = 0, 0, 0, len(arr)

    for e in arr:
        if e > 0:
            positives += 1
        elif e < 0:
            negatives += 1
        else:
            zeros += 1

    print("{:f}".format(positives / length))
    print("{:f}".format(negatives / length))
    print("{:f}".format(zeros / length))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plus_minus(arr)
