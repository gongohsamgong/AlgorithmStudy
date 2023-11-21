def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    # board = list(zip(*board))
    board = [list(col) for col in zip(*board)]
    print(board)
    for move in moves:
        move -= 1
        for i in range(n):
            if board[move][i] != 0:
                stack.append(board[move][i])
                board[move][i] = 0
                break
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
