import sys
from collections import deque

def solution(n, m, array):
    # 0은 괴물있는 부분. 0 피해야댐
    cnt = 0
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                queue.append((i, j))
                array[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    cnt += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx == n and ny == m:
                            return cnt
                        if 0 <= nx < m and 0 <= ny < n and array[nx][ny] == 1:
                            queue.append((nx, ny))


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    maze = [list(map(int, read().rstrip())) for _ in range(N)]
    ans = solution(N, M, maze)
    print(ans)
