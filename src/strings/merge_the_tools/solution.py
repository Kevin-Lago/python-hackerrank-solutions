def merge_the_tools(string, k):
    t = [string[k * i:k * i + k] for i in range(int(len(string) / k))]
    u = ["".join(dict.fromkeys(s).keys()) for s in t]

    [print(s) for s in u]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
