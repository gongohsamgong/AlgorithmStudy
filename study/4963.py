import sys
sys.setrecursionlimit(100000)


def dfs(field, x, y):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    field[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny]:
            dfs(field, nx, ny)


if __name__ == "__main__":
    read = sys.stdin.readline
    while True:
        w, h = map(int, read().split())
        if w == 0 and h == 0:
            break
        count = 0
        field = [list(map(int, read().split())) for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if field[i][j] == 1:
                    dfs(field, i, j)
                    count += 1
        print(count)
