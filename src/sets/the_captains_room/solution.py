import collections

if __name__ == '__main__':
    k = int(input())
    l = list(map(int, input().split()))

    captains_room = [item for item, count in collections.Counter(l).items() if count == 1]
    print(captains_room[0])
