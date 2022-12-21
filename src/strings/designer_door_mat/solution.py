if __name__ == '__main__':
    n, m = map(int, input().split())
    ch = int((m - 3) / 2)
    rh = int((n - 1) / 2)

    [print("-" * (ch - (3 * r)) + ".|." * (2 * (r + 1) - 1) + "-" * (ch - (3 * r))) for r in range(rh)]
    print("-" * int((m - 7) / 2) + "WELCOME" + "-" * int((m - 7) / 2))
    [print(
        "-" * (ch - (3 * (rh - r - 1))) + ".|." * (2 * (rh - r) - 1) + "-" * (ch - (3 * (rh - r - 1)))
    ) for r in range(rh)]
