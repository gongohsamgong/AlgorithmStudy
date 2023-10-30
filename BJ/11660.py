import sys

read = sys.stdin.readline
N, M = map(int, read().split())
chart = [[0] * (N+1)]
sum_chart = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    temp = [0] + list(map(int, read().split()))
    chart.append(temp)

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_chart[i][j] = sum_chart[i-1][j] + sum_chart[i][j-1] - sum_chart[i-1][j-1] + chart[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    total = sum_chart[x2][y2] - sum_chart[x2][y1-1] - sum_chart[x1-1][y2] + sum_chart[x1-1][y1-1]
    print(total)
