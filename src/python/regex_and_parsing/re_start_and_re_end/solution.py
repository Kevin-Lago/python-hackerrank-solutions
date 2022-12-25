import re

if __name__ == '__main__':
    s, k = input(), input()

    p = re.compile(k)
    m = p.search(s)

    if m:
        while m:
            print((m.start(), m.end() - 1))
            m = p.search(s, m.start() + 1)
    else:
        print((-1, -1))
