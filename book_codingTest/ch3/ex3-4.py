import sys


def solution(n, k):
    cnt = 0
    while n != 1:
        if n % k == 0:
            n = n // k
        else:
            n -= 1
        cnt += 1
    return cnt
    


if __name__ == '__main__':
    read = sys.stdin.readline
    N, K = map(int, read().split())
    ans = solution(N, K)
    print(ans)