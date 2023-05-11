import sys


def solution(n):
    d = [0] * 1001
    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = (d[i-1] + 2 * d[i-2]) % 796796
    return d[n]


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    ans = solution(N)
    print(ans)
