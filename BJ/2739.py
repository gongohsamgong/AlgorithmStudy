import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    for i in range(1, 10):
        print(N, '*', i, '=', N*i)
