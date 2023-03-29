# https://www.acmicpc.net/problem/14889
import sys


def solution(n, arr):
    difference = [] # abs 사용 예정
    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            difference.append(abs(arr[i][j] - arr[j][i]))
    print(difference)
    return min(difference)


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    graph = [list(map(int, read().split())) for _ in range(N)]
    ans = solution(N, graph)
    print(ans)
    