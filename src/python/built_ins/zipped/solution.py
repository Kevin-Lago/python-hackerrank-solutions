if __name__ == '__main__':
    n, x = map(int, input().split())
    grades = [list(map(float, input().split())) for i in range(x)]
    students = zip(*grades)

    [print(sum(s) / x) for s in students]
