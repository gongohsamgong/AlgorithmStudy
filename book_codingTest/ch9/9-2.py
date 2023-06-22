import heapq
import sys

read = sys.stdin.readline
INF = int(1e9)

n, m = map(int, read().split())
start = int(read())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드는 패스
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            # 인접 노드까지의 거리
            cost = dist + i[1]
            # 현재 노드를 거쳐서 i[0]으로 가는게 더 짧다면, 거리 정보 업데이트
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
