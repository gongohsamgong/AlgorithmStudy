import sys
INF = int(1e9)


# n: 노드 개수
def solution(graph, n):
    for i in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][b] > graph[a][i] + graph[i][b]:
                    graph[a][b] = graph[a][i] + graph[i][b]

    ans = INF

    for i in range(1, n+1):
        ans = min(ans, graph[i][i])

    return ans


if __name__ == '__main__':
    read = sys.stdin.readline
    V, E = map(int, read().split())
    graph = [[INF] * (V+1) for _ in range(V+1)]

    for i in range(E):
        a, b, c = map(int, read().split())
        graph[a][b] = c

    answer = solution(graph, V)
    if answer == INF:
        print(-1)
    else:
        print(answer)