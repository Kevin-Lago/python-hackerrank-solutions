def birthday(s, d, m):
    for i in range(len(s) - m):

    print()


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    d, m = map(int, input().split())
    print(birthday(s, d, m))
