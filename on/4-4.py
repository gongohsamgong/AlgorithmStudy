n, m = map(int, input().split())
x, y, dir = map(int, input().split())
cnt = 0

visit = [[0] * m for _ in range(n)]
visit[x][y] = 1 # if visited, 1 표시

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

if dir == 0:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
elif dir == 1:
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
elif dir == 2:
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
else:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

while array[x][y] == 0: # 육지일때
    for i in range(4):
        if visit[x+dx[i]][y+dy[i]] == 0 and array[x+dx[i]][y+dy[i]] == 0:
            x += dx[i]
            y += dy[i]
            cnt += 1
            break