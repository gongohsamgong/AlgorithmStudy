import sys


def solution(n, m, array):
    dp = []
    for i in range(n*m):
        if i % m == 0:
            dp.append(array[i:i+m])
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + dp[i][j]
            elif i == n-1:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + dp[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + dp[i][j]
    result = 0
    for k in range(n):
        result = max(result, dp[k][m-1])
    return result


if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        n, m = map(int, read().split())
        array = list(map(int, read().split()))
        ans = solution(n, m, array)
        print(ans)
