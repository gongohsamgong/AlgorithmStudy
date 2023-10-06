import sys

# def dfs(graph, v, visited, result):
#     visited[v] = 1
#     for i in range(1, len(graph[v])):
#         if visited[i] == 0 and graph[v][i] == 1:
#             result += 1
#             print(result)
#             dfs(graph, i, visited, result)
#     print(result)

def dfs(graph, v, visited, result):
    visited[v] = 1
    for i in range(1, len(graph[v])):
        if visited[i] == 0 and graph[v][i] == 1:
            result = dfs(graph, i, visited, result+1)
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    e = int(read())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(e):
        a, b = map(int, read().split())
        graph[a][b] = graph[b][a] = 1
    visited = [0]*(n+1)
    print(dfs(graph, 1, visited, 0))