import itertools

if __name__ == '__main__':
    k, m = map(int, input().split())
    lol = [list(map(int, input().split())) for i in range(k)]
    cartesian_product = list(itertools.product(*lol))
    remainders = [sum([e * e for e in cartesian_product[i]]) % m for i in range(len(cartesian_product))]
    largest_remainder = max(remainders)

    for i in range(len(remainders)):
        if (remainders[i] > 760):
            print(remainders[i])

    # for i in range(len(cartesian_product)):
    #     remainder = sum([e * e for e in cartesian_product[i]]) % m
    #     if remainder > largest_remainder:
    #         largest_remainder = remainder

    print(largest_remainder)
