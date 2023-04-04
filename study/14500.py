import sys

if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    array = [list(map(int, read().split())) for _ in range(N)]
    print(array)
