def solution(board, skill):
    answer = 0

    for type, r1, c1, r2, c2, degree in skill:
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if type == 1:
                    board[x][y] -= degree
                else:
                    board[x][y] += degree

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer
