import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    array = [i for i in range(N+1)]
    for _ in range(M):
        i, j = map(int, read().split())
        array[i], array[j] = array[j], array[i]
    for i in range(1, N+1):
        print(array[i], end=' ')
