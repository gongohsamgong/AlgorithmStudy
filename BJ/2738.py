import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    A, B = [], []
    for _ in range(N):
        A.append(list(map(int, read().split())))
    for _ in range(N):
        B.append(list(map(int, read().split())))
    for i in range(N):
        for j in range(M):
            print(A[i][j] + B[i][j], end=' ')
        print()
