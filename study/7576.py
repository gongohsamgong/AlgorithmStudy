import sys
from collections import deque


def solution(m, n, arr):
    ans = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])
    for row in arr:
        for tomato in row:
            if tomato == 0:
                ans = -1
                return ans
        # 토마토가 익은 상태인 1이 ans의 기본 값으로 들어가게 되므로, return할 때 1을 빼야함.
        ans = max(ans, max(row))
    return ans - 1


if __name__ == '__main__':
    read = sys.stdin.readline
    M, N = map(int, read().split())
    box = []
    for _ in range(N):
        box.append(list(map(int, read().split())))
    answer = solution(M, N, box)
    print(answer)
    