import sys


def solution(t, array):
    answer = []
    for i in range(t):
        h, w, n = array[i][0], array[i][1], array[i][2]
        y = n % h
        if n % h == 0:
            x = n // h
            y += h
        else:
            x = 1 + n // h
        room = 100 * y + x
        answer.append(room)
    return answer


if __name__ == '__main__':
    read = sys.stdin.readline
    T = int(read())
    array = [list(map(int, read().split())) for _ in range(T)]
    answer_array = solution(T, array)
    for i in range(T):
        print(answer_array[i])
