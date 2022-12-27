import sys
from collections import deque


def bfs(graph, x, y, color):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == color and not visited[nx][ny]:  # each color check
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1

    return cnt * cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    n, m = map(int, read().split())
    arr = []
    for i in range(m):
        arr.append(list(map(str, read().rstrip())))

    visited = [[False] * n for i in range(m)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    white, blue = 0, 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 'W' and not visited[i][j]:
                white += bfs(arr, i, j, 'W')
            elif arr[i][j] == 'B' and not visited[i][j]:
                blue += bfs(arr, i, j, 'B')
    print(white, blue)