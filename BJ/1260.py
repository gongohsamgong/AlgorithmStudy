"""
from collections import deque


def dfs(n, graph, v, visited1):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if visited1[i] == 0 and graph[v][i] == 1:
            dfs(n, graph, i, visited1)


def bfs(n, graph, v, visited2):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited2[i] = 1


if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1  # 인접 행렬
    print(graph)
    visited1 = [False] * (n + 1)
    visited2 = [False] * (n + 1)
    dfs(n, graph, v, visited1)
    print('')
    bfs(n, graph, v, visited2)

"""

# 4 5 1 n, m, v
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4


import sys
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)


def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        out = q.popleft()
        print(out, end=' ')
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M, V = map(int, read().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[a].sort()
    print(graph)
    visited1 = [False] * (N+1)
    visited2 = [False] * (N+1)
    dfs(graph, V, visited1)
    print('')
    bfs(graph, V, visited2)
