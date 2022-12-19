def wrapper(f):
    def fun(l):
        return f([
            f"+91 {n[3:8]} {n[8:]}" if len(n) == 13 else
            f"+91 {n[2:7]} {n[7:]}" if len(n) == 12 else
            f"+91 {n[1:6]} {n[6:]}" if len(n) == 11 else
            f"+91 {n[0:5]} {n[5:10]}" for n in l])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
