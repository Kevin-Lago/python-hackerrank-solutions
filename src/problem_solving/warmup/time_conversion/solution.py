from datetime import datetime


def time_conversion(s):
    return datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")


if __name__ == '__main__':
    s = input()
    print(time_conversion(s))
