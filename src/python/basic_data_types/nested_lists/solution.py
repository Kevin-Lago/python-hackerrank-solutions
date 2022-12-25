if __name__ == '__main__':
    n = int(input())
    students = []

    for i in range(n):
        name = input()
        score = float(input())

        students.insert(i, [name, score])

    students.sort(key=lambda s: s[0])
    lowest_grade = min(students, key=lambda s: s[1])[1]

    for i in range(n):
        if students[n - i - 1][1] == lowest_grade:
            students.remove(students[n - i - 1])

    second_lowest_grade = min(students, key=lambda s: s[1])[1]

    for i in range(n - 1):
        if students[i][1] == second_lowest_grade:
            print(students[i][0])
