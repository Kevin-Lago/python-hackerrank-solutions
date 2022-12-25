from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    Student = namedtuple("Student", list(input().split()))

    average = sum([int(Student(*input().split()).MARKS) for i in range(n)])
    print("%.2f" % (average / n))
