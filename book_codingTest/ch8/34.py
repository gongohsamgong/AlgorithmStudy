import sys


"""
def solution(n, array):
    cnt = 0
    for i in range(n-1):
        if array[i] < array[i+1]:
            cnt += 1
        else:
            continue
    return cnt
"""


def solution(n, array):
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return n - max(dp)


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    power = list(map(int, read().split()))
    power.reverse()
    ans = solution(N, power)
    print(ans)
