import sys


def solution(n, m, array, array_yn):
    for i in range(m):
        if array_yn[i] in array:
            print(1, end=' ')
        else:
            print(0, end=' ')


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    cards = set(list(map(int, read().split())))
    M = int(read())
    cards_YN = list(map(int, read().split()))
    solution(N, M, cards, cards_YN)
