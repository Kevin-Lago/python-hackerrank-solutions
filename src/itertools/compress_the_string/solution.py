import itertools

if __name__ == '__main__':
    s = input()
    a = [(len(list(l)), int(c)) for c, l in itertools.groupby(s)]

    [print(t, end=" ") for t in a]
