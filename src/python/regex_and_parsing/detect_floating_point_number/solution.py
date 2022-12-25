import re

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = input()
        test = re.search("^[-+]?\\d*\\.\\d*$", n)

        try:
            another = float(test.group())
            print(True)
        except AttributeError as e:
            print(False)
