from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    a = list(input().split())
    k = int(input())

    test = [''.join(c) for c in list(combinations(a, k))]
    print(round(sum(['a' in c for c in test]) / len(test), 3))
