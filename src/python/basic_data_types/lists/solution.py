if __name__ == '__main__':
    n = int(input())
    l = []

    commands = {
        "insert": lambda *args: l.insert(int(args[0][0]), int(args[0][1])),
        "print": lambda *args: print(l),
        "remove": lambda *args: l.remove(int(args[0][0])),
        "append": lambda *args: l.append(int(args[0][0])),
        "sort": lambda *args: l.sort(),
        "pop": lambda *args: l.pop(),
        "reverse": lambda *args: l.reverse()
    }

    for i in range(n):
        string = input().split(" ")

        try:
            commands[string[0]](string[1:])
        except():
            print("command does not exist")
