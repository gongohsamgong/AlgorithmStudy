import sys


def solution(graph, x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        solution(graph, x-1, y)
        solution(graph, x, y-1)
        solution(graph, x+1, y)
        solution(graph, x, y+1)
        return True
    return False



if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    tray = [list(map(int, read().rstrip())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if solution(tray, i, j):
                cnt += 1
    print(cnt)
