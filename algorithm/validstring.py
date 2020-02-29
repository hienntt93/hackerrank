#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    val = dict()
    key = dict()
    max_v = 0
    key = Counter(s)
    val = Counter(key.values())
    min_v = min(key.values())
    for k,v in key.items():
        if max_v < v : max_v = v


    l = len(val)
    if l==1: return 'YES'
    elif l <= 2:
        if max_v - min_v ==1 and val[max_v]==1 or val[min_v]==1: return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = str(isValid(s)).upper()

    fptr.write(result + '\n')

    fptr.close()
