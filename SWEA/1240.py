# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    encode_board = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    N, M = map(int, input().split())
    array = [list(input().rstrip()) for _ in range(N)]
    line, last_index = 0, 0
    code_array = [0] * 8
    encode = ''
    for i in range(N):
        if '1' in array[i]:
            line = i
            last_index = len(array[i]) - 1 - array[i][::-1].index('1')
            break
    for i in range(7, -1, -1):
        code_array[i] = array[line][last_index - 6:last_index + 1]
        last_index -= 7
    for i in range(8):
        temp = "".join(code_array[i])
        if temp in encode_board:
            encode += str(encode_board.index(temp))
    total = 0
    for i in range(8):
        if i % 2 == 0:
            total += 3 * int(encode[i])
        else:
            total += int(encode[i])
    answer = 0
    if total % 10 == 0:
        for i in range(8):
            answer += int(encode[i])
    print("#%d %d" % (test_case, answer))
