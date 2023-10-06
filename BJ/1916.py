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
    N = int(read()) # 도시 개수
    M = int(read()) # 간선 개수
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int,read().split())
        graph[a].append((b, c)) # a 도시 출발, b 도시까지 c 값 든다는 뜻
    start, end = map(int, read().split())   # 출발 도시, 목적 도시
    distance = [INF] * (N+1)
    dijkstra(graph,start,distance)
    print(distance[end])