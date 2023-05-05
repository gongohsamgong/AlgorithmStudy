import sys


def dfs(n, m, cnt, index, arr):
    if cnt - 1 == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(index, n+1):
        arr.append(i)
        dfs(n, m, cnt+1, i, arr)
        arr.pop()


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    array = []
    dfs(N, M, 1, 1, array)
