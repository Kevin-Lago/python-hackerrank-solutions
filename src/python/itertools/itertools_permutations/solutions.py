import itertools

if __name__ == '__main__':
    s, k = input().split(" ")

    a = sorted(["".join(p) for p in itertools.permutations(s, int(k))])
    [print(a) for a in a]
