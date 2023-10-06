import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    arr = [i for i in range(N+1)]
    for _ in range(M):
        i, j = map(int, read().split())
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    for i in range(1, N+1):
        print(arr[i], end=' ')
