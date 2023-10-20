import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
A = list(map(int, read().split()))  # 0:큐, 1:스택
B = list(map(int, read().split()))
M = int(read())
C = list(map(int, read().split()))

q = deque()

for i in range(N):
    if A[i] == 0:
        q.appendleft(B[i])
    # 스택은 그냥 똑같은 값 넣었다 똑같은 값 빼는것 밖에 안되므로 큐에 해당하는 부분만 하나의 큐에 넣기

for i in range(M):
    q.append(C[i])
    print(q.popleft(), end=' ')
