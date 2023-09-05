import sys


def solution(h, m):
    if m - 45 < 0:
        h -= 1
        if h < 0:
            h = 23
        m = m + 15
    else:
        m -= 45
    return [h, m]


if __name__ == "__main__":
    read = sys.stdin.readline
    H, M = map(int, read().split())
    ans = solution(H, M)
    print(ans[0], ans[1])
