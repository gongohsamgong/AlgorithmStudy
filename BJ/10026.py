import sys
from collections import deque


def bfs(n, array, visited_array, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and array[nx][ny] == array[x][y]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    picture = []
    for _ in range(N):
        picture.append(list(read().rstrip()))
    visited = [[0] * N for _ in range(N)]
    normal, blind = 0, 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(N, picture, visited, i, j)
                normal += 1

    for i in range(N):
        for j in range(N):
            visited[i][j] = 0
            if picture[i][j] == 'R':
                picture[i][j] = 'G'

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(N, picture, visited, i, j)
                blind += 1

    print(normal, blind)
