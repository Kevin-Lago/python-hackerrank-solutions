import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        line = input()
        matches = re.findall(r"(?<!^)#{1}[0-9a-fA-F]{3,6}", line)

        for match in matches:
            print(match)
