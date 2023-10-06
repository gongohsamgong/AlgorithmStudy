from collections import deque
import sys

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
            else:
                continue
    print(graph[n-1][m-1])


if __name__ == '__main__':
    read = sys.stdin.readline
    n, m = map(int, read().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, read().strip())))
    visited = [[0]*m for _ in range(n)]
    bfs(graph, 0, 0)