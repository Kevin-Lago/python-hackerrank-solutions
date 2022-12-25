from email.utils import parseaddr, formataddr
import re

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        name, email = parseaddr(input())

        if re.search(r"^[a-zA-Z]([\w.-]+)?@([a-zA-Z]+)\.[a-zA-Z]{1,3}$", email):
            print(formataddr((name, email)))
