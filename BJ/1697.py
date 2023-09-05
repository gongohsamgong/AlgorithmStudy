from collections import deque
import sys

MAX = 100001


def bfs(dist, n, k):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return dist[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)


if __name__ == '__main__':
    read = sys.stdin.readline
    n, k = map(int, read().split())
    dist = [0] * MAX
    ans = bfs(dist, n, k)
    print(ans)
