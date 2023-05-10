import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    array = [list(read().split()) for _ in range(N)]
    array.sort(key=lambda x: int(x[1]))
    for i in range(N):
        print(array[i][0], end=' ')
