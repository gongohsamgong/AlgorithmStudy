import sys


def solution(n, m, k, x, array):
    distance = 0
    # for i in range(n):




if __name__ == "__main__":
    read = sys.stdin.readline
    N, M, K, X = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(M)]
    ans = solution(N, M, K, X, graph)
    print(ans)
