regex_integer_in_range = r"^[1-9][0-9][0-9][0-9][0-9][0-9]$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re

if __name__ == '__main__':
    P = input()
    print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
