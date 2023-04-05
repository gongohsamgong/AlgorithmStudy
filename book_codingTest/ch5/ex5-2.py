import sys
from collections import deque


def bfs(n, m, graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[x][y] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n-1][m-1]


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    graph = [list(map(int, read().rstrip())) for _ in range(N)]
    ans = bfs(N, M, graph, 0, 0)
    print(ans)
