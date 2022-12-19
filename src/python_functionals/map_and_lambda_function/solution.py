cube = lambda x: x**3


def fibonacci(n):
    if n == 0:
        return []

    series = [0]

    for i in range(n-1):
        if i == 0:
            series.append(1)
        else:
            series.append(series[i] + series[i-1])

    return series


if __name__ == '__main__':
    n = int(input())
    test = fibonacci(5)
    print(list(map(cube, fibonacci(n))))
