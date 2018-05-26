#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_ = -sys.maxsize
    min_ = sys.maxsize
    
    for i in range(len(arr)):
        sum = 0
        b = arr[:]
        b.remove(arr[i])
        for num in b:
            sum += num
        
        if (sum > max_):
            max_ = sum
        if (sum < min_):
            min_ = sum
            
    print(min_, max_)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

