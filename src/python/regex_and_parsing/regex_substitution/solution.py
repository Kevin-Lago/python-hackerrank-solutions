import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        s = input()

        s = re.sub("(?<=\\s)(&&)(?=\\s)", "and", s)
        s = re.sub("(?<=\\s)(\\|\\|)(?=\\s)", "or", s)

        print(s)
