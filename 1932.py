import sys


def dynamic(g):
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                g[i][j] = g[i-1][j] + g[i][j]
            elif j == i:
                g[i][j] = g[i-1][j-1] + g[i][j]
            else:
                g[i][j] = max(g[i-1][j-1], g[i-1][j]) + g[i][j]
        # if i==n-1, result = max(g[n-1])로 했더니 에러뜸... UnboundLocalError...읭...?
    return max(g[n-1])


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    graph = []
    for i in range(n):
        graph.append(list(map(int, read().split())))
    print(dynamic(graph))
