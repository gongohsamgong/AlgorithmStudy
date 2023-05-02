import sys
from collections import deque


def bfs(graph, n):
    visited = [-1 for _ in range(n+1)]
    queue = deque()
    queue.append((1, 0))
    visited[1] = 0
    while queue:
        node, time = queue.popleft()
        for near in graph[node]:
            if visited[near] == -1:
                visited[near] = time + 1
                queue.append((near, visited[near]))
    return visited[1:]


def solution(plans, graph, n):
    for plan in plans:
        a, i, j = plan
        if a == 1:
            graph[i].append(j)
            graph[j].append(i)
            print(*bfs(graph, n))
        else:
            graph[i].remove(j)
            graph[j].remove(i)
            print(*bfs(graph, n))


if __name__ == "__main__":
    read = sys.stdin.readline
    n, m = map(int, read().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)
    q = int(read())
    plans = [list(map(int, read().split())) for _ in range(q)]
    solution(plans, graph, n)
