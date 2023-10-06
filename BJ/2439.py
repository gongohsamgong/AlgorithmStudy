import sys


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    for i in range(N):
        print(' ' * (N-1-i), end='')
        print('*' * (i+1))
