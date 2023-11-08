import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(node, v, cnt):
    global answer
    if cnt > answer:
        answer = cnt
    v[node] = 1
    for i in graph[node]:
        if not v[i]:
            dfs(i, v, cnt+1)
            v[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    for i in range(N+1):
        dfs(i, visited, 1)
        visited[i] = 0
    print("#%d %d" % (test_case, answer))
