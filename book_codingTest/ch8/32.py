import sys


def solution(n, array):
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                up_left = 0
            else:
                up_left = array[i-1][j-1]
            if j == 1:
                up = 0
            else:
                up = array[i-1][j]
            dp[i][j] = dp[i][j] + max(up_left, up)
    return max(dp[n-1])


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    dp = []
    for _ in range(n):
        dp.append(list(map(int, read().split())))
    ans = solution(n, dp)
    print(ans)
