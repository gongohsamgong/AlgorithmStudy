import sys


def solution(n, m, a, b):
    max_b = max(b)
    cnt = 0
    for i in range(n):
        if a[i] > max_b:
            cnt += m
        else:


if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        N, M = map(int, read().split())
        A = list(map(int, read().split()))
        B = list(map(int, read().split()))
        B.sort()
        solution(N, M, A, B)
