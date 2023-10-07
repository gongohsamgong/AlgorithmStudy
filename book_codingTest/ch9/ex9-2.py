import sys
import heapq
INF = int(1e9)


def dijkstra(start, graph, distance):
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
    return distance


if __name__ == "__main__":
    read = sys.stdin.readline
    # 노드 수, 간선 수
    n, m = map(int, read().split())
    start = int(read())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for _ in range(m):
        a, b, c = map(int, read().split())
        graph[a].append((b, c))
    answer = dijkstra(start, graph, distance)
    for i in range(1, n+1):
        if answer[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
