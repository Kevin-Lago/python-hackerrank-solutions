import re

if __name__ == '__main__':
    s = input()

    lowercase = sorted("".join(c for c in re.findall(r"[a-z]", s)))
    uppercase = sorted("".join(c for c in re.findall(r"[A-Z]", s)))
    digits = sorted([c for c in re.findall(r"[0-9]", s)])
    digits = sorted([c for c in digits], key=lambda i: int(i) % 2 == 0)

    print("".join(lowercase + uppercase + digits))
