def print_rangoli(size):
    [print(2 * n * '-' + '-'.join([chr(ord('a') + abs(i) + n) for i in range(-(size - n - 1), (size - n))]) + 2 * n * '-') for n in [abs(r) for r in range(-(size - 1), size)]]
    for n in [abs(r) for r in range(-(size - 1), size)]:
        center = '-'.join([chr(ord('a') + abs(i) + n) for i in range(-(size - n - 1), (size - n))])
        print(2 * n * '-' + center + 2 * n * '-')


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
