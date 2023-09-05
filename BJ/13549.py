import sys
from collections import deque


def bfs(n, k):
  visited = [0] * 100001
  q = deque()
  q.append(n)
  visited[n] = 1
  while q:
    s = q.popleft()
    if s == k:
      return visited[s] - 1
    if 0 <= s - 1 < 100001 and visited[s - 1] == 0:
      visited[s - 1] = visited[s] + 1
      q.append(s - 1)
    if 0 < s * 2 < 100001 and visited[s * 2] == 0:
      visited[s * 2] = visited[s]
      q.appendleft(s * 2)
    if 0 <= s + 1 < 100001 and visited[s + 1] == 0:
      visited[s + 1] = visited[s] + 1
      q.append(s + 1)


if __name__ == '__main__':
  read = sys.stdin.readline
  n, k = map(int, read().split())
  ans = bfs(n, k)
  print(ans)