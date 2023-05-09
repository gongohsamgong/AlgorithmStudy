import sys


def solution(n, array):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                array[i][j] = 1 # set queen

    return cnt


def place_queen(x, y, n, array):
    if array[y][x] == 0:
        array[y] = [-1] * n
        array[x] = [-1] * n
        while True:
            new_x = x - 1
            new_y -= 1
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                break


        array[y][x] = 1 # set queen



def count_queen(array):



if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    board = [[0]*N for _ in range(N)]
    solution(N, board)
