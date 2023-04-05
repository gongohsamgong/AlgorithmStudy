import sys


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split()) # N:세로, M, 가로
    graph = [list(map(int, read().split())) for _ in range(N)]
