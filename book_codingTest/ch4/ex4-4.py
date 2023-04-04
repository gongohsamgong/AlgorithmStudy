import sys


def solution(n, m, a, b, direction, map_array):
    cnt = 0
    
    return cnt


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    A, B, d = map(int, read().split())
    _map = [list(map(int, read().split())) for _ in range(N)]
    ans = solution(N, M, A, B, d, _map)
    print(_map)
    