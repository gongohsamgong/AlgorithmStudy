import sys


def solution(n, k, stuff, bag):
    for i in range(1, n+1):
        for j in range(1, k+1):
            weight = stuff[i][0]
            value = stuff[i][1]
            if j < weight:
                bag[i][j] = bag[i - 1][j]
            else:
                bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])
    return bag[n][k]


if __name__ == "__main__":
    read = sys.stdin.readline
    N, K = map(int, read().split())
    stuff = [[0, 0]]
    for _ in range(N):
        stuff.append(list(map(int, read().split())))
    bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    ans = solution(N, K, stuff, bag)
    print(ans)
