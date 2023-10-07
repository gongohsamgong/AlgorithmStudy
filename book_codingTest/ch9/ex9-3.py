import sys
INF = int(1e9)


def floydWarshall(n, m, graph):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for _ in range(m):
        a, b, c = map(int, read().split())
        graph[a][b] = c

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return graph


if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    m = int(read())
    graph = [[INF] * (n+1) for _ in range(n+1)]
    answer = floydWarshall(n, m, graph)
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(answer[i][j], end=' ')
        print()
