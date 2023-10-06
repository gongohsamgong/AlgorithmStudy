import sys


def solution(dp, array, n):
    for i in range(n):
        for j in range(i + array[i][0], n+1):
            if dp[j] < dp[i] + array[i][1]:
                dp[j] = dp[i] + array[i][1]
    return dp[-1]


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    array = []
    dp = [0] * (n + 1)
    for i in range(n):
        array.append(list(map(int, read().split())))
    ans = solution(dp, array, n)
    print(ans)
