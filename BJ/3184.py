import sys
from collections import deque

read = sys.stdin.readline
R, C = map(int, read().split())
yard = []
for _ in range(R):
    yard.append(list(read().rstrip()))

final_sheep, final_wolf = 0, 0


def bfs(r, c, array, x, y):
    sheep, wolf = 0, 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x, y])
    if array[x][y] == 'o':
        sheep += 1
    elif array[x][y] == 'v':
        wolf += 1
    array[x][y] = '#'
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and array[nx][ny] != '#':
                if array[nx][ny] == 'o':
                    sheep += 1
                elif array[nx][ny] == 'v':
                    wolf += 1
                q.append((nx, ny))
                array[nx][ny] = '#'
    return sheep, wolf


visited = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if yard[i][j] in 'ov':
            sheep, wolf = bfs(R, C, yard, i, j)
            if sheep > wolf:
                final_sheep += sheep
            else:
                final_wolf += wolf

print(final_sheep, final_wolf)
