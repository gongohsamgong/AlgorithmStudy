import sys
from collections import deque

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    result = []
    graph = []
    for _ in range(n):
        graph.append(list(map(int, read().strip())))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                cnt = bfs(graph, i, j)
                result.append(cnt)
    result.sort()
    a = len(result)
    print(a)
    for i in range(a):
        print(result[i])
