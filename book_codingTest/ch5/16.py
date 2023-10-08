import sys

read = sys.stdin.readline
N, M = map(int, read().split())
lab = []
for _ in range(N):
    lab.append(list(map(int, read().split())))
# 벽 설치한 뒤의 지도
temp = [[0] * M for _ in range(N)]
result = 0


def virus(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = lab[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1


dfs(0)
print(result)
