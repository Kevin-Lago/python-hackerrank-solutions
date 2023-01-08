def find_point(px, py, qx, qy):
    rx = 2 * qx - px
    ry = 2 * qy - py

    return [rx, ry]


if __name__ == '__main__':
    n = int(input().strip())

    for _ in range(n):
        px, py, qx, qy = map(int, input().split())

        [print(p, end=" ") for p in find_point(px, py, qx, qy)]
