import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
q = deque()

for i in range(N):
    order = list(read().split())
    if order[0] == 'push':
        q.append(int(order[1]))
    elif order[0] == 'pop':
        print(q.popleft() if q else -1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(0 if q else 1)
    elif order[0] == 'front':
        print(q[0] if q else -1)
    elif order[0] == 'back':
        print(q[-1] if q else -1)
