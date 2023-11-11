# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 0:북 1:동 2:남 3:서
trolley = ['^', '>', 'v', '<']
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    game_map = []
    for _ in range(H):
        game_map.append(list(input().rstrip()))
    N = int(input())
    order = list(input().rstrip())
    x, y, direction = 0, 0, 0
    for i in range(H):
        for j in range(W):
            if game_map[i][j] == '^':
                x, y = i, j
                direction = 0
                break
            elif game_map[i][j] == '>':
                x, y = i, j
                direction = 1
                break
            elif game_map[i][j] == 'v':
                x, y = i, j
                direction = 2
                break
            elif game_map[i][j] == '<':
                x, y = i, j
                direction = 3
                break
    for i in range(N):
        if order[i] == 'U':
            direction = 0
            if 0 <= x-1 < H and game_map[x-1][y] == '.':
                game_map[x][y] = '.'
                x -= 1
        elif order[i] == 'D':
            direction = 2
            if 0 <= x+1 < H and game_map[x+1][y] == '.':
                game_map[x][y] = '.'
                x += 1
        elif order[i] == 'L':
            direction = 3
            if 0 <= y-1 < W and game_map[x][y-1] == '.':
                game_map[x][y] = '.'
                y -= 1
        elif order[i] == 'R':
            direction = 1
            if 0 <= y+1 < W and game_map[x][y+1] == '.':
                game_map[x][y] = '.'
                y += 1
        else:
            ball_x, ball_y = x, y
            while 0 <= ball_x + dx[direction] < H and 0 <= ball_y + dy[direction] < W:
                ball_x += dx[direction]
                ball_y += dy[direction]
                if game_map[ball_x][ball_y] == '*':
                    game_map[ball_x][ball_y] = '.'
                    break
                elif game_map[ball_x][ball_y] == '#':
                    break
        game_map[x][y] = trolley[direction]

    print("#%d" % test_case, end=' ')
    for i in range(H):
        for j in range(W):
            print(game_map[i][j], end='')
        print()
