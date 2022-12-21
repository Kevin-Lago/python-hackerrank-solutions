from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    ordered_dictionary = OrderedDict()

    for i in range(n):
        s = input().split()
        item, price = " ".join(s[:len(s) - 1]), int(s[len(s) - 1:][0])
        ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)

    [print(f"{k} {ordered_dictionary[k]}") for k in ordered_dictionary]
