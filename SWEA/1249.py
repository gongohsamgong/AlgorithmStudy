# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    time[x][y] = map_array[x][y]
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0: continue
                if visited[nx][ny] == 0:
                    time[nx][ny] = time[x][y] + map_array[nx][ny]
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + map_array[nx][ny]:
                        time[nx][ny] = time[x][y] + map_array[nx][ny]
                        q.append((nx, ny))
    return time[N - 1][N - 1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    map_array = [list(map(int, input().rstrip())) for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    answer = bfs(0, 0)
    print("#%d %d" % (test_case, answer))
