import sys
import heapq
INF = int(1e9)


def solution(n, m, c, array):
    distance = [INF] * (n+1)
    distance[c] = 0
    q = []
    heapq.heappush(q, (0, c))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, value in array[now]:
            cost = dist + value
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    number_of_cities, max_distance = 0, 0
    for i in range(n+1):
        if distance[i] != INF:
            number_of_cities += 1
            max_distance = max(max_distance, distance[i])
    return number_of_cities - 1, max_distance


if __name__ == "__main__":
    read = sys.stdin.readline
    # N: 도시의 개수, M: 통로의 개수, C: 메시지를 보내고자 하는 도시
    N, M, C = map(int, read().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, read().split())
        graph[a].append([b, c])
    cities, time = solution(N, M, C, graph)
    print(cities, time)
