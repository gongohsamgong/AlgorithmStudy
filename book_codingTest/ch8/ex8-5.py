import sys


def solution(n):
    d = [0] * 300001
    for i in range(2, n+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5] + 1)
    return d[n]


if __name__ == "__main__":
    read = sys.stdin.readline
    X = int(read())
    ans = solution(X)
    print(ans)