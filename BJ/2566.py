import sys


def solution(array):
    max_number, row, column = 0, 0, 0
    for i in range(9):
        for j in range(9):
            if array[i][j] >= max_number:
                max_number = array[i][j]
                row, column = i+1, j+1
    return max_number, row, column


if __name__ == "__main__":
    read = sys.stdin.readline
    arr = [list(map(int, read().split())) for _ in range(9)]
    max_number, row, column = solution(arr)
    print("%d\n%d %d" % (max_number, row, column))
