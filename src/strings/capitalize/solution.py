import os


# Complete the solve function below.
def solve(s):
    s = " ".join(s[:1].upper() + s[1:] for s in s.split(" "))

    print(s)
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
