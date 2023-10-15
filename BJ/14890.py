import sys


def rotate(graph):
    n = len(graph)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[i][j] = graph[n-1-j][i]
    return rotated


def check(graph):
    bridge = [False] * N
    for i in range(N-1):
        if graph[i] == graph[i+1]:
            continue

        if abs(graph[i] - graph[i+1]) > 1:
            return False

        if graph[i] > graph[i+1]:   # 왼쪽이 더 클 경우
            criterion = graph[i+1]   # 낮은 오른쪽을 기준으로 l개만큼 이어지나 봐야함
            for j in range(i+1, i+1+L):
                if 0 <= j < N:
                    if graph[j] != criterion:
                        return False
                    if bridge[j]:
                        return False
                    bridge[j] = True
                else:
                    return False

        else:   # 오른쪽이 더 클 경우
            criterion = graph[i]
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    if graph[j] != criterion:
                        return False
                    if bridge[j]:
                        return False
                    bridge[j] = True
                else:
                    return False
    return True


read = sys.stdin.readline
N, L = map(int, read().split())
field = [list(map(int, read().split())) for _ in range(N)]

cnt = 0
for column in field:
    if check(column):
        cnt += 1

field = rotate(field)

for row in field:
    if check(row):
        cnt += 1

print(cnt)
