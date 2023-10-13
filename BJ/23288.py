import sys
from collections import deque

read = sys.stdin.readline
N, M, K = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
dice = [1, 2, 3, 4, 5, 6]
x, y, direction, score = 0, 0, 0, 0

# 동-북-서-남: 반시계 방향, 동쪽부터 시작
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(x, y, value):
    visited = set()
    visited.add((x, y))
    q = deque()
    q.append((x, y))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) not in visited and graph[nx][ny] == value:
                    cnt += 1
                    q.append((nx, ny))
                    visited.add((nx, ny))
    return cnt


for i in range(K):
    if not (0 <= x + dx[direction] < N and 0 <= y + dy[direction] < M):
        direction = (direction + 2) % 4
    x, y = x + dx[direction], y + dy[direction]

    # 연속해서 이동할 수 있는 칸 수 * 칸의 점수
    score += (bfs(x, y, graph[x][y]) + 1) * graph[x][y]
    if direction == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif direction == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif direction == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if dice[5] > graph[x][y]:
        direction = (direction + 3) % 4
    elif dice[5] < graph[x][y]:
        direction = (direction + 1) % 4
    else:
        continue


print(score)
