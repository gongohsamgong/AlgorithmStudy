import sys


def solution(n, array):
    dp = [0] * 1001
    dp[0] = array[0]
    for i in range(1, n):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + array[i])
            else:
                dp[i] = max(dp[i], array[i])
    return max(dp)


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    array = list(map(int, read().split()))
    print(solution(n, array))
