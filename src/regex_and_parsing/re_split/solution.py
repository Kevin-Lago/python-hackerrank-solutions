import re
regex_pattern = r"[,.]"

if __name__ == '__main__':
    print("\n".join(re.split(regex_pattern, input())))
