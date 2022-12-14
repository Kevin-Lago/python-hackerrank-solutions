import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = numpy.array([numpy.array(input().split(), int) for i in range(n)])
    b = numpy.array([numpy.array(input().split(), int) for i in range(n)])

    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.floor_divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))
