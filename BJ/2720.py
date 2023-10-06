import sys


def solution(c):
    for coin in [25, 10, 5, 1]:
        print(c // coin, end=' ')
        c %= coin


if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    for i in range(T):
        C = int(read())
        solution(C)
