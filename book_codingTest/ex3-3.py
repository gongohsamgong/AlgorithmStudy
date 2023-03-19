import sys


def solution(n, arr):
    _min = []
    for i in range(n):
        _min.append(min(arr[i]))
    return max(_min)


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    array = []
    for _ in range(N):
        array.append(list(map(int, read().split())))
    answer = solution(N, array)
    print(answer)
    