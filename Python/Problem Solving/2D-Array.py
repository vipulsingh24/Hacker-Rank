'''
Hourglass problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    smax = -63  # -9*7
    
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            tl = arr[i][j]      # top left
            tc = arr[i][j+1]    # top center
            tr = arr[i][j+2]    # top right
            mc = arr[i+1][j+1]  # mid 
            bl = arr[i+2][j]    # bottom left
            bc = arr[i+2][j+1]  # bottom center
            br = arr[i+2][j+2]  # bottom right
            total_sum = tl + tc + tr + mc + bl + bc + br
            smax = max(smax, total_sum)
    return smax

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

