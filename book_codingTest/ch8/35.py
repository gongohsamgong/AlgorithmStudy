import sys


def solution(n):
    dp = [0] * n
    dp[0] = 1
    i2, i3, i5 = 0, 0, 0
    next2, next3, next5 = 2, 3, 5
    for l in range(1, n):
        dp[l] = min(next2, next3, next5)
        # 여서 if elif 차이 줜나 중요하다 그거땜에 틀림 니기럴~~
        if dp[l] == next2:
            i2 += 1
            next2 = dp[i2] * 2
        if dp[l] == next3:
            i3 += 1
            next3 = dp[i3] * 3
        if dp[l] == next5:
            i5 += 1
            next5 = dp[i5] * 5
    print(dp)
    return dp[n-1]


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    ans = solution(N)
    print(ans)
