import numpy
numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(numpy.eye(n, m))
