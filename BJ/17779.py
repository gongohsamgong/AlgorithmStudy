import sys

read = sys.stdin.readline

N = int(read())
city = [list(map(int, read().split())) for _ in range(N)]

minimum_difference = int(1e9)


def cal(x, y, d1, d2):
    elec = [0 for i in range(5)]
    temp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(d1+1):
        temp[x+i][y-i] = 5
        temp[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        temp[x+i][y+i] = 5
        temp[x+d1+i][y-d1+i] = 5
    for i in range(x+1, x+d1+d2):
        flag = False
        for j in range(1, N+1):
            if temp[i][j] == 5:
                flag = not flag
            if flag:
                temp[i][j] = 5

    for r in range(1, N+1):
        for c in range(1, N+1):
            if 1 <= r < x+d1 and 1 <= c <= y and temp[r][c] == 0:
                elec[0] += city[r-1][c-1]
            elif 1 <= r <= x+d2 and y < c <= N and temp[r][c] == 0:
                elec[1] += city[r-1][c-1]
            elif x+d1 <= r <= N and 1 <= c < y-d1+d2 and temp[r][c] == 0:
                elec[2] += city[r-1][c-1]
            elif x+d2 < r <= N and y-d1+d2 <= c <= N and temp[r][c] == 0:
                elec[3] += city[r-1][c-1]
            elif temp[r][c] == 5:
                elec[4] += city[r-1][c-1]

    return max(elec) - min(elec)


for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    minimum_difference = min(minimum_difference, cal(x, y, d1, d2))

print(minimum_difference)
