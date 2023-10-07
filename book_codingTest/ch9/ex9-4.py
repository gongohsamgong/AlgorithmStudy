import sys
INF = int(1e9)


def solution(n, m, array, x, k):
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                array[b][c] = min(array[b][c], array[b][a] + array[a][c])
    if array[1][k] == INF or array[k][x] == INF:
        return -1
    return array[1][k] + array[k][x]


if __name__ == "__main__":
    read = sys.stdin.readline
    # N: 회사 개수, M: 경로 개수
    N, M = map(int, read().split())
    edge_graph, graph = [], [[INF] * (N+1) for _ in range(N+1)]
    # edge_graph = [[1, 2], [1, 3]]: 1번이 2, 3번과 연결되어있음을 의미
    for _ in range(M):
        i, j = map(int, read().split())
        graph[i][j] = graph[j][i] = 1
    for i in range(1, N):
        for j in range(1, N):
            if i == j:
                graph[i][j] = 0
    # X: 목표 회사 K: 소개팅 회사
    X, K = map(int, read().split())
    answer = solution(N, M, graph, X, K)
    print(answer)
