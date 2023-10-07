import sys
INF = int(1e9)

read = sys.stdin.readline
n, m = map(int, read().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    # a노드에서 b노드까지 c 값이 든다
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
visited = [False] * (n + 1)
distance = [INF] * (n + 1)


# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            # 최단 거리도 업데이트
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작노드는 0으로 초기화
    distance[start] = 0
    visited[start] = True
    # 시작 노드에 대한 거리 정보도 초기화
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드 제외한 n-1개에 대해서 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리 및 최단 거리 업데이트
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            # cost: j[0]을 j를 거쳐서 가느냐 / distance[j[0]]: 그냥 j[0]의 기존 거리 값
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                # 거리 업데이트
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
