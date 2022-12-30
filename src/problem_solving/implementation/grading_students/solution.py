def grading_student(grades):
    rounded_grades = list()

    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
            continue
        if grade + 5 - grade % 5 - grade < 3:
            rounded_grades.append(grade + 5 - grade % 5)
            continue
        rounded_grades.append(grade)

    return rounded_grades


if __name__ == '__main__':
    n: int = int(input())
    grades = list()

    for _ in range(n):
        grades.append(int(input()))

    [print(grade) for grade in grading_student(grades)]
