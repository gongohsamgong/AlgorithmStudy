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
#  1. INTEGER_ARRAY cost
#  2. INTEGER x
#

def solution(cost, x):
    # Write your code here
    _sum = 0
    total = x
    for i in range(len(cost) - 1, -1, -1):
        if cost[i] <= total:
            total -= cost[i]
            _sum += 2 ** i
    return _sum % 1000000007


if name == 'main':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    x = int(input().strip())

    result = solution(cost, x)

    fptr.write(str(result) + '\n')

    fptr.close()