import sys


def solution(n, time_array, pay_array):
    dp = [0] * (n+1)
    total = 0
    for i in range(n-1, -1, -1):
        due = time_array[i] + i
        if due <= n:
            dp[i] = max(pay_array[i] + dp[due], total)
            total = dp[i]
        else:
            dp[i] = total
    return total


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    time, pay = [], []
    for _ in range(N):
        array = list(map(int, read().split()))
        time.append(array[0])
        pay.append(array[1])
    ans = solution(N, time, pay)
    print(ans)
