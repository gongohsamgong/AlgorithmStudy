import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
q = deque()

for i in range(N):
    order = list(map(int, read().split()))
    if order[0] == 1:
        q.appendleft(order[1])
    elif order[0] == 2:
        q.append(order[1])
    elif order[0] == 3:
        print(q.popleft() if q else -1)
    elif order[0] == 4:
        print(q.pop() if q else -1)
    elif order[0] == 5:
        print(len(q))
    elif order[0] == 6:
        print(0 if q else 1)
    elif order[0] == 7:
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
