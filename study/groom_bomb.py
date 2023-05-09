import sys


def solution(n, bombs):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    _sum = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    for bomb in bombs:
        y, x = bomb
        graph[y][x] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < n+1 and 0 < ny < n+1:
                graph[ny][nx] += 1
            else:
                continue
    for i in range(n+1):
        _sum += sum(graph[i])
    return _sum


if __name__ == "__main__":
    read = sys.stdin.readline
    N, K = map(int, read().split())
    bombs = [list(map(int, read().split())) for _ in range(K)]
    ans = solution(N, bombs)
    print(ans)
