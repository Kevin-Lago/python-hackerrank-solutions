import datetime


def time_delta(t1, t2):
    t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    td = t1 - t2 if t1 > t2 else t2 - t1

    return int(td.total_seconds())


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
