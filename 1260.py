from collections import deque

def dfs(graph, v, visited1):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited1[i]==0 and graph[v][i]==1:
            dfs(graph, i, visited1)

def bfs(graph, v, visited2):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited2[i] = 1

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[0] *(n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
    visited1 = [False] * (n+1)
    visited2 = [False] * (n+1)
    dfs(graph, v, visited1)
    print('')
    bfs(graph, v, visited2)