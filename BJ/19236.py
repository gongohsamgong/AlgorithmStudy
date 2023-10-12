import copy

board = [[] for _ in range(4)]

# 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 번호, 방향
        fish.append([data[2 * j], data[2 * j + 1] - 1])
    board[i] = fish

max_score = 0


# sx: shark x, sy: shark y
def dfs(sx, sy, score, board):
    global max_score
    # 번호, 시작할때 (sx, sy) = (0, 0)
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    # 먹으니 해당 물고기 번호는 사라짐. 번호 = 0으로 바뀜
    board[sx][sy][0] = 0

    # 물고기(no.1 ~ no.16) 움직임, 작은 물고기부터 순서대로 이동
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        # 먹혀서 없는 물고기 번호의 좌표, 넘어감
        if f_x == -1 and f_y == -1:
            continue
        # 아직 존재하는 물고기 번호의 방향
        f_d = board[f_x][f_y][1]

        for i in range(8):
            # 반시계 방향으로 45도씩 회전
            nd = (f_d + i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            # 물고기가 이동할 수 없는 칸의 조건: 공간을 벗어나거나 상어가 있는 경우
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            # 방향
            board[f_x][f_y][1] = nd
            # trade: 물고기 번호, 방향 모두 trade
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음, 먹었으니 방향도 먹은 물고기의 방향으로 바뀜
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        # 해당 방향으로 이동
        nx = sx + dx[s_d] * i
        ny = sy + dy[s_d] * i
        if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))


dfs(0, 0, 0, board)
print(max_score)
