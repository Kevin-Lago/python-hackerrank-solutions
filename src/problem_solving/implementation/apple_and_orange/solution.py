def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples = sum([1 if s <= point + a <= t else 0 for point in apples])
    oranges = sum([1 if s <= point + b <= t else 0 for point in oranges])
    print(apples, oranges, sep='\n')


if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())

    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    count_apples_and_oranges(s, t, a, b, apples, oranges)
