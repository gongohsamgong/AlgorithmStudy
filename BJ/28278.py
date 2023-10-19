import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
q = deque()

for _ in range(N):
    order = list(map(int, read().split()))
    if order[0] == 1:
        q.append(order[1])
    elif order[0] == 2:
        print(q.pop() if q else -1)
    elif order[0] == 3:
        print(len(q))
    elif order[0] == 4:
        print(0 if q else 1)
    elif order[0] == 5:
        print(q[-1] if q else -1)

