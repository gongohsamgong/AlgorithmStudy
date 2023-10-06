import sys


def solution(n, a, b):
    total = 0
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        total += a[i] * b[i]
    return total


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    A = list(map(int, read().split()))
    B = list(map(int, read().split()))
    answer = solution(N, A, B)
    print(answer)
