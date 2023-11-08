import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    answer = 0
    test_case = int(input())
    board = [list(input().rstrip()) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            for r in range(1, 101):
                row = board[i][j:j+r]
                if row == row[::-1]:
                    if len(row) > answer:
                        answer = len(row)

    board = list(zip(*board))

    for i in range(100):
        for j in range(100):
            for r in range(1, 101):
                row = board[i][j:j + r]
                if row == row[::-1]:
                    if len(row) > answer:
                        answer = len(row)

    print("#%d %d" % (test_case, answer))
