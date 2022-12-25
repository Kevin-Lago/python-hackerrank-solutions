import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        cc = input()

        if re.match("^[456]", cc) \
                and (re.match("^\\d{4}-\\d{4}-\\d{4}-\\d{4}$", cc) or re.match("^\\d{16}$", cc)) \
                and not re.search("(\\d)\\1{3,}", cc.replace("-", "")):
            print("Valid")
            continue

        print("Invalid")
