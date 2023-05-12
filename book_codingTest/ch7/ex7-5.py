import sys


def solution(n, m, part, need):
    for i in range(m):
        if need[i] in part:
            print('yes', end=' ')
        else:
            print('no', end=' ')


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    parts = list(map(int, read().split()))
    parts.sort()
    M = int(read())
    needs = list(map(int, read().split()))
    solution(N, M, parts, needs)
