import sys
# import heapq
from collections import deque
INF = int(1e9)

'''
# 최단경로 방법. 시간은 훨씬 오래 걸림.
def solution2(n, m, k, x, graph):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        for node, value in graph[now]:
            cost = dist + value
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    if k not in distance:
        print(-1)
        return

    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
    return
'''


def solution(n, m, k, x, array):
    distance = [-1] * (n+1)
    distance[x] = 0
    q = deque()
    q.append(x)
    while q:
        now = q.popleft()
        for next_node in array[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    if k not in distance:
        print(-1)
        return

    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
    return


if __name__ == "__main__":
    read = sys.stdin.readline
    # N: 도시 개수, M: 도로 개수, K: 거리 정보, X: 출발 도시 번호
    N, M, K, X = map(int, read().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, read().split())
        graph[a].append(b)
    solution(N, M, K, X, graph)
