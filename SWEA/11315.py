import sys
sys.stdin = open("sample_input.txt", "r")


def solution():
    for x in range(N):
        for y in range(N):
            if board[x][y] == 'o':
                for d in range(4):
                    cnt = 1
                    nx = x + dx[d]
                    ny = y + dy[d]
                    while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[d]
                        ny += dy[d]
                        if cnt >= 5:
                            return 'YES'
    return 'NO'


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input().rstrip()) for _ in range(N)]
    cnt = 0
    answer = 'NO'
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]
    answer = solution()
    print("#%d %s" % (test_case, answer))
