import sys
from collections import deque

read = sys.stdin.readline
N = int(read())

q = deque(i for i in range(1, N+1))

i = 0
while len(q) > 1:
    q.popleft()
    q.rotate(-1)
print(q[0])


