import collections


def migratory_birds(arr):
    counter = collections.Counter(arr)

    for i in range(1, 6):
        if counter[i] == max(counter.values()):
            return i


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(migratory_birds(arr))
