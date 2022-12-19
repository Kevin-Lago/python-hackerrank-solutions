if __name__ == '__main__':
    n = int(input())
    a = list(input().split())
    print(all([int(i) > 0 for i in a]) and any([i == i[::-1] for i in a]))
