import sys


def solution(n, L, J):
    dp = [[0] * 101 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, 101):
            if L[i] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][99]


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    L = [0] + list(map(int, read().split()))
    J = [0] + list(map(int, read().split()))
    print(solution(n, L, J))
