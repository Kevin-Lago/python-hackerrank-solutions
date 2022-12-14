import numpy

if __name__ == '__main__':
    n = int(input())
    a = [numpy.array(list(map(int, input().split()))) for i in range(n)]
    b = [numpy.array(list(map(int, input().split()))) for i in range(n)]

    print(numpy.matmul(a, b))
