#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER z
#

def solution(x, y, z):
    # Write your code here
    ans = 0
    target = y - x
    if abs(target) > z:
        ans = -1
        return ans
    if target > 0:
        ans = x + target
        ans += (z-target) // 2
    elif target == 0:
        ans = x + (z // 2)
    else:
        ans = x + ((z + target) // 2)

    return ans
if name == 'main':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    result = solution(x, y, z)

    fptr.write(str(result) + '\n')

    fptr.close()