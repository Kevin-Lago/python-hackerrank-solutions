import re

if __name__ == '__main__':
    m = re.search("([a-zA-Z0-9]+)\\1+", input())

    try:
        print(m.groups()[0])
    except AttributeError as e:
        print("-1")
