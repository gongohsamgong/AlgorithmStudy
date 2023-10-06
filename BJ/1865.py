import sys

INF = int(1e9)


def bf(start, n):
    dis = [INF] * (n + 1)
    dis[start] = 0
    for i in range(n):
        for edge in edges:
            current = edge[0]
            next_node = edge[1]
            cost = edge[2]

            if dis[next_node] > cost + dis[current]:
                dis[next_node] = cost + dis[current]
                if i == n - 1:
                    return True
    return False


def remove_negative_cycles(n):
    dis = [0] * (n + 1)
    for i in range(n):
        for edge in edges:
            current = edge[0]
            next_node = edge[1]
            cost = edge[2]

            if dis[next_node] > dis[current] + cost:
                dis[next_node] = dis[current] + cost
                if i == n - 1:
                    return True
    return False


if __name__ == "__main__":
    read = sys.stdin.readline
    TC = int(read())
    for _ in range(TC):
        N, M, W = map(int, read().split())
        edges = []
        for _ in range(M):
            S, E, T = map(int, read().split())
            edges.append((S, E, T))
            edges.append((E, S, T))

        for _ in range(W):
            S, E, T = map(int, read().split())
            edges.append((S, E, -T))

        if remove_negative_cycles(N):
            print("YES")
        else:
            shorten_time = bf(1, N)

            if shorten_time:
                print("YES")
            else:
                print("NO")
