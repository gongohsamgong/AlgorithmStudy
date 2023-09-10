import sys


def solution(array):
    array.sort(key=lambda x: (x[1], x[0]))
    return array


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    dots = []
    for _ in range(N):
        dots.append(list(map(int, read().split())))
    result = solution(dots)
    for i in range(N):
        print("%d %d" % (result[i][0], result[i][1]))
