import sys


"""
def change_color(start, array):
    count = 0
    for i in range(8):
        for j in range(8):
            if j % 2 == 0:
                if i % 2 == 0 and array[i][j] != start:
                    count += 1
                if i % 2 != 0 and array[i][j] == start:
                    count += 1
            else:
                if i % 2 == 0 and array[i][j] == start:
                    count += 1
                if i % 2 != 0 and array[i][j] != start:
                    count += 1
    return count


def solution(n, m, board):
    candidate = []
    for j in range(0, n - 7):
        for i in range(0, m - 7):
            start_x = i
            start_y = j
            new_array = []
            for k in range(start_y, start_y + 8):
                count = 0
                new_array.append(board[k][start_x:start_x+8])
            # WBWB
            start_white = change_color('W', new_array)
            # BWBW
            start_black = change_color('B', new_array)
            candidate.append(min(start_white, start_black))
    return min(candidate)
"""


def change_color(array, a, b, color):
    count = 0
    for i in range(a, a + 8):
        for j in range(b, b + 8):
            if (i+j) % 2 == 0:
                if array[i][j] != color:
                    count += 1
            else:
                if array[i][j] == color:
                     count += 1


def solution(n, m, board):
    candidate = []
    for j in range(0, n - 7):
        for i in range(0, m - 7):
            start_x = i
            start_y = j
            change_color(array, i, j, color):


            candidate.append(min(start_white, start_black))
    return min(candidate)


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [list(read().rstrip()) for _ in range(N)]
    ans = solution(N, M, board)
    print(ans)
