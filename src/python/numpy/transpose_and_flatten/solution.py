import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    r = numpy.array([input().split() for i in range(n)], int)
    print(r.transpose())
    print(r.flatten())
