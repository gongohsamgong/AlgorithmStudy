import sys

read = sys.stdin.readline
N = int(read())
desert = [list(map(int, read().split())) for _ in range(N)]
answer = 0

# 순서 유의, 항상 (0, -1, 0)이 꼭 뒤에 있어야 if r == 0: 일때 날아간 모래를 합친 spread 값을 뺄 수 있음
left = [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-2, 0, 0.02), (-1, 0, 0.07),
        (1, 0, 0.07), (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, -x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]

rates = {'left': left, 'right': right, 'up': up, 'down': down}

now = [N//2, N//2]


def move(cnt, dx, dy, direction):
    global answer
    for _ in range(cnt + 1):
        now[0], now[1] = now[0] + dx, now[1] + dy
        if now[0] < 0 or now[1] < 0:
            break

        spread = 0
        for d_x, d_y, r in rates[direction]:
            nx, ny = now[0] + d_x, now[1] + d_y
            if r == 0:
                sand = desert[now[0]][now[1]] - spread
            else:
                sand = int(desert[now[0]][now[1]] * r)
            if 0 <= nx < N and 0 <= ny < N:
                desert[nx][ny] += sand
            else:
                answer += sand
            spread += sand


for i in range(N):
    if i % 2 == 0:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    if i % 2 == 1:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')

print(answer)
