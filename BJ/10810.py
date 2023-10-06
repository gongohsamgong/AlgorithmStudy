import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    answer = [0] * (N+1)
    for _ in range(M):
        start, end, ball = map(int, read().split())
        for i in range(start, end+1):
            answer[i] = ball
    for i in range(1, N+1):
        print(answer[i], end=' ')
