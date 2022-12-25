import calendar

if __name__ == '__main__':
    m, d, y = map(int, input().split())
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    print(days[calendar.weekday(y, m, d)])
