import sys

read = sys.stdin.readline
N, M, x, y, K = map(int, read().split())
map_array = [list(map(int, read().split())) for _ in range(N)]
# 동: 1, 서: 2, 북: 3, 남: 4
order = list(map(int, read().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 6

for i in range(K):
    d = order[i] - 1
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if map_array[nx][ny] == 0:
        map_array[nx][ny] = dice[5]
    else:
        dice[5] = map_array[nx][ny]
        map_array[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])
