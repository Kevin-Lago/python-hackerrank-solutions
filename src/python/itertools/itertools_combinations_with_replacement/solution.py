import itertools

if __name__ == '__main__':
    s, k = input().split()
    a = sorted(list("".join(sorted(cwr)) for cwr in itertools.combinations_with_replacement(s, int(k))))

    [print(i) for i in a]
