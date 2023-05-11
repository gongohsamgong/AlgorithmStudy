import sys


def solution(n, m, arr, index):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(index, n+1):
        arr.append(i)
        solution(n, m, arr, i + 1)
        arr.pop()


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    array = []
    solution(N, M, array, 1)
