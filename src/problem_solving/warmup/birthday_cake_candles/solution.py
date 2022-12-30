def birthday_cake_candles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    n = int(input())
    candles = list(map(int, input().split()))
    print(birthday_cake_candles(candles))
