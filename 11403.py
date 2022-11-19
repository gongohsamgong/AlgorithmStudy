import sys
INF = int(1e9)


def floyd(n, g):
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if g[a][b] == 1 or (g[a][k] == 1 and g[k][b] == 1):
                    g[a][b] = 1
    return g


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    G = []
    for _ in range(N):
        G.append(list(map(int, read().split())))
    res = floyd(N, G)
    for i in range(N):
        for j in range(N):
            print(res[i][j], end =' ')
        print()