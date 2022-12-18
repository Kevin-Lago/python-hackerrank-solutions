import email.utils as e
import email.parser as p

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        name, email = input().split()
        p.
        t = e.parseaddr(f"{name} {email}")
        l = e.formataddr(t)

        print()
