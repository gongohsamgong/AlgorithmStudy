import sys


read = sys.stdin.readline
N, M = map(int, read().split())
print(N,M)
graph = []
for i in range(N):
    graph.append(list(map(int, read().rstrip())))
# graph[list(map(int, read().rstrip())) for _ in range(N)]
def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)
