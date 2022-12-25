import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        s = input()

        p = re.compile("^[789]\\d{9}$")
        m = p.search(s)

        if m:
            print("YES")
        else:
            print("NO")
