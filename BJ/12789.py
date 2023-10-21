import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
people = list(map(int, read().split()))

tmp = deque()
target = 1

for i in people:
    tmp.append(i)
    while tmp and tmp[-1] == target:
        tmp.pop()
        target += 1
    if len(tmp) > 1 and tmp[-1] > tmp[-2]:
        print("Sad")
        break

if len(tmp) == 0:
    print("Nice")
