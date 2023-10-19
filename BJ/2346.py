import sys
from collections import deque

read = sys.stdin.readline
N = int(read())

order = list(map(int, read().split()))
q = deque(i+1 for i in range(N))

for i in range(N):
    popped = q.popleft()
    print(popped, end=' ')
    direction = order[popped-1]
    if direction > 0:
        q.rotate(-direction + 1)
    else:
        q.rotate(-direction)
