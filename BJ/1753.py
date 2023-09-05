import sys
import heapq
INF = int(1e9)


def dijkstra(graph, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


if __name__ == '__main__':
    read = sys.stdin.readline
    V, E = map(int, read().split())
    start = int(read())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, read().split())
        graph[u].append((v, w))
    distance = [INF] * (V+1)
    dijkstra(graph, start, distance)
    for i in range(1, V+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])