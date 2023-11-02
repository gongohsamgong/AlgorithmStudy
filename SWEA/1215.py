def rotate(arr):
    ret = [[0] * 8 for _ in range(8)]
    for x in range(8):
        for y in range(8):
            ret[7-y][x] = arr[x][y]
    return ret


def check(arr):
    for n in range(N//2):
        s, e = 0, N-1
        s += n
        e -= n
        if arr[s] != arr[e]:
            return False
    return True


for test_case in range(1, 11):
    N = int(input())
    board = [list(input().rstrip()) for _ in range(8)]
    answer = 0

    for i in range(8):
        for j in range(9 - N):
            temp = board[i][j:j + N]
            if check(temp):
                answer += 1

    board = rotate(board)

    for i in range(8):
        for j in range(9 - N):
            temp = board[i][j:j + N]
            if check(temp):
                answer += 1
    print("#%d %d" % (test_case, answer))
