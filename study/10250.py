import sys


def solution(t, array):
    answer = []
    xx = ''
    for i in range(t):
        # height, width, consumer
        h, w, n = array[i][0], array[i][1], array[i][2]
        x = 1 + n // h
        if x // 10 == 0:
            xx = '0' + str(x)
        if n % h == 0:
            y = h
        else:
            y = n % h
        room = str(y) + xx
        answer.append(room)
    return answer


if __name__ == '__main__':
    read = sys.stdin.readline
    T = int(read())
    array = [list(map(int, read().split())) for _ in range(T)]
    answer_array = solution(T, array)
    for i in range(T):
        print(answer_array[i])
