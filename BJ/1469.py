import sys


def solution(n, numbers):



if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    elements = list(map(int, read().split()))
    answer = solution(N, elements)
    for i in range(len(answer)):
        print(answer[i], end=' ')