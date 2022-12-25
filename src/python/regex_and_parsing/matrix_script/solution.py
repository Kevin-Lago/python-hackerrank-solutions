#!/bin/python3

import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

message = "".join([s[i:i+1] for i in range(m) for s in matrix])
print(re.sub(r"(?<=\w)([!@#$%& ]{1,})(?=\w)", " ", message))
