#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sumr,suml= 0,0
    l = len(arr)
    for i in range(l):
        sumr += arr[i][i]
    brr= [arr[l-1-r][r] for r in range(l-1,-1,-1)]
    suml = sum(brr,0)
    last = sumr - suml
    return abs(sumr-suml)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
