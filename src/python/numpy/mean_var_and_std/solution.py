import numpy
numpy.printoptions(legacy='1.13')

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [numpy.array(list(map(int, input().split()))) for i in range(n)]

    print(numpy.mean(a, 1))
    print(numpy.var(a, 0))
    print(round(numpy.std(a), 11))
