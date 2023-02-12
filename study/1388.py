import sys


def dfs(graph, x, y):
    if graph[x][y] == '-':
        graph[x][y] = 1 # visitied
        for _y in [1, -1]:
            new_y = y + _y
            if (new_y > 0 and new_y < m) and graph[x][new_y] == '-':
                dfs(graph, x, new_y)
    elif graph[x][y] == '|':
        graph[x][y] = 1
        for _x in [1, -1]:
            new_x = x + _x
            if (new_x > 0 and new_x < n) and graph[new_x][y] == '|':
                dfs(graph, new_x, y)

g
if __name__ == '__main__':
    read = sys.stdin.readline
    n, m = map(int, read().split())
    array = []
    for i in range(n):
        array.append(list(map(str, read().rstrip())))
    count = 0
    for i in range(n):
        for j in range(m):
            dfs(array, i, j)
            count += 1
    print(count)