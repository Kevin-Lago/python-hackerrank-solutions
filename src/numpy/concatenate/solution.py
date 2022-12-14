import numpy

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    a = numpy.concatenate([map(int, input().split()) for i in range(n + m)], axis=0)
    print(a)
