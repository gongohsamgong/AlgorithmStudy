import sys
from collections import deque


def bfs(start_x, start_y, graph, n, m):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, read().rstrip())))
    answer = bfs(0, 0, graph, N, M)
    print(answer)
