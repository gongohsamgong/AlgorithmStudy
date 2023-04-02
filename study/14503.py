import sys


read = sys.stdin.readline
N, M = map(int, read().split())
r, c, d = map(int, read().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, read().split())))

visited = [[0] * M for _ in range(N)]

# 방향 d 북:0 서:3 남:2 동:1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1
                break
    if flag == 0:
        if graph[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r = r - dr[d]
            c = c - dc[d]
        