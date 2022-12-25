import itertools

if __name__ == '__main__':
    s, k = input().split(" ")

    for i in range(1, int(k) + 1):
        [print(t) for t in sorted(list(["".join(sorted(c)) for c in itertools.combinations(s, i)]))]
