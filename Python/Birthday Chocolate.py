#!/bin/python3

import math
import os
import random
import sys

# Complete the solve function below.
def solve(s, d, m):
    count = 0
    for i in range(len(s)):
        sum_ = 0
        sum_ = sum(s[i: i+m])
        if sum_ == d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

