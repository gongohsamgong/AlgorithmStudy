import heapq
import sys
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ =='__main__':
    read = sys.stdin.readline
    # 노드 개수, 간선 개수
    n, m = map(int, read().split())
    start = int(read())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, read().split())
        graph[a].append((b, c))
    distance = [INF] * (n + 1)
    dijkstra(start)
    for i in range(start, n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
