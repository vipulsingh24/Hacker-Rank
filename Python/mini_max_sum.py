'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

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

