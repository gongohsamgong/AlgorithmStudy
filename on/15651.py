import sys


def solution(n, m, array, index):
    if len(array) == m:
        print(' '.join(map(str, array)))
        return
    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            solution(n, m, array, i)
            array.pop()


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    answer = []
    solution(N, M, answer, 1)
