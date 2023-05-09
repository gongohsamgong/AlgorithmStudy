import sys
from collections import deque


def bfs(n, m, array):
    queue = deque()
    cnt = 1
    queue.append((0, 0))
    dx, dy = [1, 0], [0, 1]
    while queue:
        y, x = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < m and ny < n and array[ny][nx] == 1:
                queue.append((ny, nx))
                cnt += 1
    return cnt


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    maze = [list(map(int, read().rstrip())) for _ in range(N)]
    ans = bfs(N, M, maze)
    print(ans)
