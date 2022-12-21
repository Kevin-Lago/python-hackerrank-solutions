from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    c = Counter(s).most_common()

    [print(c[i][0], c[i][1]) for i in range(3)]
