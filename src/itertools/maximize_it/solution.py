from itertools import product

if __name__ == '__main__':
    k, m = map(int, input().split())
    n = [list(map(int, input().split()))[1:] for i in range(k)]

    cartesian_product = list(product(*n))
    print(max([sum([e**2 for e in cartesian_product[i]]) % m for i in range(len(cartesian_product))]))
