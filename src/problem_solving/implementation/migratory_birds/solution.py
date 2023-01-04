import collections


def migratory_birds(arr):
    counter = collections.Counter(arr)
    highest_value = max(counter.values())

    for i in range(1, 6):
        if counter[i] == highest_value:
            return i


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(migratory_birds(arr))
