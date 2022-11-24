import sys
INF = int(1e9)


def solution(graph, n):
    for i in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])
    return graph


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    m = int(read())
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(m):
        a, b, c = map(int, read().split())
        if graph[a][b] > c: # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다라는 조건 충족을 위해.
            graph[a][b] = c

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    res = solution(graph, n)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
