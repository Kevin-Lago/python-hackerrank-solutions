import numpy

if __name__ == '__main__':
    n = int(input())
    a = [list(map(float, input().split())) for i in range(n)]

    print(round(numpy.linalg.det(a), 2))
