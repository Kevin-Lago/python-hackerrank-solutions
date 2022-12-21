import string


def print_rangoli(size):
    letters = list(string.ascii_lowercase)
    width = size * 2

    for i in range(size - 1):
        print("-" * size)
    print(letters)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
