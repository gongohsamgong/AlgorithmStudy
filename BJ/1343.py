import sys


def solution(array):
    array = array.replace('XXXX', 'AAAA')
    array = array.replace('XX', 'BB')
    return array


if __name__ == "__main__":
    read = sys.stdin.readline
    board = read()
    answer = solution(board)
    if 'X' in answer:
        print(-1)
    else:
        for i in range(len(answer)):
            print(answer[i], end='')
